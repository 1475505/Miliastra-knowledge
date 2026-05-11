#!/usr/bin/env python3
"""
lint.py - 验证 BBS FAQ 条目是否与官方文档相悖

流程：
1. 加载 .env 配置
2. 解析 bbs/ 下的 FAQ md 文件，按块分割
3. 索引 official/ 和 derived/ 下的参考文档
4. 对每个块：关键词检索相关文档 → LLM 验证 → 输出判定
5. 生成报告，可选删除矛盾条目

用法：
  python lint.py                          # 验证所有 FAQ 文件
  python lint.py --file bbs/bbs-faq.md   # 只验证指定文件
  python lint.py --auto-delete             # 自动删除矛盾条目（跳过确认）
  python lint.py --concurrency 5           # 设置并发数
  python lint.py --top-k 3                # 每个 FAQ 块检索的参考文档数
"""

import argparse
import json
import os
import re
import shutil
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pathlib import Path
from typing import Optional

from dotenv import load_dotenv
from openai import OpenAI


ROOT_DIR = Path(__file__).resolve().parent
BBS_DIR = ROOT_DIR / "bbs"
OFFICIAL_DIR = ROOT_DIR / "official"
DERIVED_DIR = ROOT_DIR / "derived"
BACKUP_DIR = ROOT_DIR / "lint_backup"
REPORTS_DIR = ROOT_DIR / "lint_reports"

BLOCK_SEPARATOR = re.compile(r"^-{5,}$", re.MULTILINE)


def load_env_config():
    load_dotenv(ROOT_DIR / ".env")
    api_key = os.getenv("LINT_OPENAI_API_KEY", "")
    base_url = os.getenv("LINT_OPENAI_BASE_URL", "")
    model = os.getenv("MODEL", "deepseek-v4-flash")
    if not api_key:
        print("错误：LINT_OPENAI_API_KEY 未配置，请检查 .env 文件")
        sys.exit(1)
    if not base_url:
        print("错误：LINT_OPENAI_BASE_URL 未配置，请检查 .env 文件")
        sys.exit(1)
    return api_key, base_url, model


def parse_faq_blocks(content: str) -> list[dict]:
    blocks = []
    parts = BLOCK_SEPARATOR.split(content)
    for part in parts:
        text = part.strip()
        if not text:
            continue
        if text.startswith("---"):
            lines = text.split("\n")
            non_fm_lines = []
            in_fm = False
            fm_count = 0
            for line in lines:
                if line.strip() == "---":
                    fm_count += 1
                    if fm_count == 1:
                        in_fm = True
                        continue
                    elif fm_count == 2:
                        in_fm = False
                        continue
                if not in_fm:
                    non_fm_lines.append(line)
            text = "\n".join(non_fm_lines).strip()
        q_match = re.search(r"#\s*Q\.\s*(.+?)(?:\n|$)", text)
        question = q_match.group(1).strip() if q_match else ""
        lines = text.split("\n")
        answers = []
        current_answer = []
        for line in lines:
            if re.match(r"^A\.\s*", line):
                if current_answer:
                    answers.append("\n".join(current_answer).strip())
                    current_answer = []
                answer_text = re.sub(r"^A\.\s*", "", line)
                current_answer.append(answer_text)
            elif line.startswith("回答者：") or line.startswith("来自："):
                if current_answer:
                    answers.append("\n".join(current_answer).strip())
                    current_answer = []
            elif current_answer:
                current_answer.append(line)
        if current_answer:
            answers.append("\n".join(current_answer).strip())
        answers = [a for a in answers if a]
        if question or answers:
            blocks.append({
                "raw": text,
                "question": question,
                "answers": answers,
                "full_text": text,
            })
    return blocks


def parse_frontmatter(content: str):
    fm = {}
    m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if m:
        for line in m.group(1).split("\n"):
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip().strip('"').strip("'")
    return fm


def rebuild_file(frontmatter: dict, blocks: list[dict]) -> str:
    lines = []
    if frontmatter:
        lines.append("---")
        for k, v in frontmatter.items():
            lines.append(f"{k}: {v}")
        lines.append("---")
        lines.append("")
    for i, block in enumerate(blocks):
        lines.append(block["full_text"])
        if i < len(blocks) - 1:
            lines.append("")
            lines.append("-----------------------")
            lines.append("")
    return "\n".join(lines) + "\n"


class DocIndex:
    def __init__(self):
        self.docs: list[dict] = []

    @staticmethod
    def _extract_chunks(text: str) -> list[str]:
        tokens = re.findall(r'[\u4e00-\u9fff]+|[a-zA-Z0-9]+', text)
        chunks = []
        for token in tokens:
            if re.match(r'[\u4e00-\u9fff]+', token):
                chunks.append(token)
                if len(token) >= 2:
                    for i in range(len(token) - 1):
                        chunks.append(token[i:i + 2])
                if len(token) >= 3:
                    for i in range(len(token) - 2):
                        chunks.append(token[i:i + 3])
                if len(token) >= 4:
                    for i in range(len(token) - 3):
                        chunks.append(token[i:i + 4])
            else:
                chunks.append(token)
        return chunks

    def add_doc(self, path: Path, content: str, source_type: str):
        fm = parse_frontmatter(content)
        title = fm.get("title", path.stem)
        body = content
        fm_match = re.match(r"^---\s*\n.*?\n---\s*\n", content, re.DOTALL)
        if fm_match:
            body = content[fm_match.end():]
        body_clean = re.sub(r"[#*\[\]()（）【】{}\-]", " ", body)
        body_clean = re.sub(r"\s+", " ", body_clean)
        chunks = self._extract_chunks(body_clean)
        self.docs.append({
            "path": str(path),
            "title": title,
            "source_type": source_type,
            "chunk_freq": Counter(chunks),
            "body": body,
            "chunk_count": len(chunks),
        })

    def build(self):
        for dir_path, source_type in [
            (OFFICIAL_DIR / "faq", "official_faq"),
            (OFFICIAL_DIR / "guide", "official_guide"),
            (OFFICIAL_DIR / "tutorial", "official_tutorial"),
            (DERIVED_DIR / "faq", "derived_faq"),
            (DERIVED_DIR / "node", "derived_node"),
        ]:
            if not dir_path.exists():
                continue
            for f in sorted(dir_path.glob("*.md")):
                if f.name in ("category.md", "README.md"):
                    continue
                try:
                    content = f.read_text(encoding="utf-8")
                    self.add_doc(f, content, source_type)
                except Exception as e:
                    print(f"  警告：读取 {f} 失败: {e}")

    def search(self, query: str, top_k: int = 5) -> list[dict]:
        query_chunks = self._extract_chunks(query)
        query_filtered = [c for c in query_chunks if len(c) >= 2]
        bigrams = set()
        for i in range(len(query_filtered) - 1):
            bigrams.add(query_filtered[i] + query_filtered[i + 1])
        scored = []
        for doc in self.docs:
            score = 0
            for c in query_filtered:
                tf = doc["chunk_freq"].get(c, 0)
                if tf > 0:
                    weight = 3 if len(c) >= 4 else (2 if len(c) >= 3 else 1)
                    score += tf * weight
            for bg in bigrams:
                if bg in doc["body"]:
                    score += 3
            for c in query_filtered:
                if c in doc["title"]:
                    score += 20
                if len(c) >= 3:
                    sub_hits = doc["body"].count(c)
                    if sub_hits > 0:
                        score += min(sub_hits, 10)
            if score > 0:
                scored.append((score, doc))
        scored.sort(key=lambda x: x[0], reverse=True)
        results = []
        seen_titles = set()
        for score, doc in scored:
            if doc["title"] not in seen_titles:
                seen_titles.add(doc["title"])
                results.append(doc)
                if len(results) >= top_k:
                    break
        return results


VERIFICATION_PROMPT = """你是一个千星奇域（原神UGC编辑器）官方文档审核专家。你的任务是验证社区FAQ中的回答是否与官方文档相悖。

请严格根据以下官方文档内容进行判断，不要凭自己的知识做出判断。

【官方文档参考】
{ref_docs}

【社区FAQ待验证条目】
问题：{question}
回答：{answers}

请判断：
1. 该回答是否与官方文档**明确相悖**（官方文档有明确说明且与回答的核心结论冲突）
2. 该回答是否**存疑**（官方文档中可能暗示不同结论，或回答的表述不够准确但并非完全错误）
3. 该回答与官方文档**一致或无明显冲突**

注意：
- 社区FAQ回答可能是基于社区经验的游戏攻略，官方文档可能没有直接涉及该问题。如果官方文档没有涉及该问题的内容，应判定为"ok"而非"存疑"。
- 社区FAQ中的回答方式（如用节点图实现某功能）是在官方文档基础上的实践指导，不应仅因官方文档描述方式不同就判定相悖。
- 只有当回答的核心结论与官方文档的明确说明存在不可调和的矛盾时，才判定为"contradict"。

请以JSON格式输出（不要输出其他内容）：
```json
{{
  "verdict": "contradict" | "doubtful" | "ok",
  "reason": "判断理由",
  "conflict_source": "冲突的官方文档标题（如有），无冲突则为空字符串"
}}
```"""


def verify_block(client: OpenAI, model: str, block: dict, ref_docs: list[dict]) -> dict:
    ref_text_parts = []
    total_chars = 0
    max_chars = 30000
    for doc in ref_docs:
        doc_text = f"=== {doc['title']} ({doc['source_type']}) ===\n{doc['body']}\n"
        if total_chars + len(doc_text) > max_chars:
            remaining = max_chars - total_chars - 500
            if remaining > 0:
                truncated = doc["body"][:remaining]
                doc_text = f"=== {doc['title']} ({doc['source_type']}) ===\n{truncated}\n...(内容过长已截断)\n"
                ref_text_parts.append(doc_text)
            break
        ref_text_parts.append(doc_text)
        total_chars += len(doc_text)
    ref_docs_text = "\n".join(ref_text_parts) if ref_text_parts else "（未找到相关官方文档）"
    answers_text = "\n".join(block["answers"]) if block["answers"] else "（无回答）"
    prompt = VERIFICATION_PROMPT.format(
        ref_docs=ref_docs_text,
        question=block["question"],
        answers=answers_text,
    )
    max_retries = 3
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=0.1,
                max_tokens=1024,
            )
            text = response.choices[0].message.content.strip()
            json_match = re.search(r"```json\s*(.*?)\s*```", text, re.DOTALL)
            if json_match:
                text = json_match.group(1)
            result = json.loads(text)
            verdict = result.get("verdict", "ok").lower()
            if verdict not in ("contradict", "doubtful", "ok"):
                verdict = "ok"
            return {
                "verdict": verdict,
                "reason": result.get("reason", ""),
                "conflict_source": result.get("conflict_source", ""),
            }
        except json.JSONDecodeError:
            if attempt < max_retries - 1:
                time.sleep(2)
                continue
            return {
                "verdict": "error",
                "reason": f"LLM 返回内容无法解析: {text[:200]}",
                "conflict_source": "",
            }
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(3)
                continue
            return {
                "verdict": "error",
                "reason": f"API 调用失败: {str(e)}",
                "conflict_source": "",
            }


VERDICT_EMOJI = {"contradict": "❌", "doubtful": "⚠️", "ok": "✅", "error": "💥"}


def process_file(
    file_path: Path,
    client: OpenAI,
    model: str,
    doc_index: DocIndex,
    top_k: int,
    concurrency: int,
) -> tuple:
    print(f"\n{'='*60}")
    print(f"处理文件: {file_path.name}")
    print(f"{'='*60}")
    content = file_path.read_text(encoding="utf-8")
    frontmatter = parse_frontmatter(content)
    blocks = parse_faq_blocks(content)
    print(f"  共解析到 {len(blocks)} 个 FAQ 块")

    def verify_one(idx_block):
        idx, block = idx_block
        q_preview = block["question"][:40] + "..." if len(block["question"]) > 40 else block["question"]
        query = block["question"] + " " + " ".join(block["answers"][:1][:100])
        ref_docs = doc_index.search(query, top_k=top_k)
        result = verify_block(client, model, block, ref_docs)
        result["block_index"] = idx
        result["question"] = block["question"]
        result["file"] = str(file_path)
        emoji = VERDICT_EMOJI.get(result["verdict"], "?")
        print(f"  [{idx+1}/{len(blocks)}] {emoji} {result['verdict'].upper()} | {q_preview}")
        if result["verdict"] in ("contradict", "doubtful"):
            print(f"         理由: {result['reason']}")
        return result

    results = []
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = []
        for item in enumerate(blocks):
            futures.append(executor.submit(verify_one, item))
        for future in as_completed(futures):
            results.append(future.result())

    results.sort(key=lambda x: x["block_index"])
    return results, blocks, frontmatter


def delete_blocks_from_file(file_path: Path, blocks: list[dict], results: list[dict], frontmatter: dict):
    indices_to_remove = set()
    for r in results:
        if r["verdict"] == "contradict":
            indices_to_remove.add(r["block_index"])
    if not indices_to_remove:
        print(f"  {file_path.name}: 无需删除的条目")
        return 0
    backup_dir = BACKUP_DIR / datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_dir.mkdir(parents=True, exist_ok=True)
    backup_path = backup_dir / file_path.name
    shutil.copy2(file_path, backup_path)
    print(f"  已备份原文件到: {backup_path}")
    remaining_blocks = [b for i, b in enumerate(blocks) if i not in indices_to_remove]
    new_content = rebuild_file(frontmatter, remaining_blocks)
    file_path.write_text(new_content, encoding="utf-8")
    print(f"  已删除 {len(indices_to_remove)} 个矛盾条目，剩余 {len(remaining_blocks)} 个条目")
    return len(indices_to_remove)


def generate_report(all_results: list[dict], file_path: str) -> str:
    REPORTS_DIR.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_file = REPORTS_DIR / f"lint_report_{timestamp}.json"
    contradict_count = sum(1 for r in all_results if r["verdict"] == "contradict")
    doubtful_count = sum(1 for r in all_results if r["verdict"] == "doubtful")
    ok_count = sum(1 for r in all_results if r["verdict"] == "ok")
    error_count = sum(1 for r in all_results if r["verdict"] == "error")
    report = {
        "timestamp": timestamp,
        "file": file_path,
        "summary": {
            "total": len(all_results),
            "contradict": contradict_count,
            "doubtful": doubtful_count,
            "ok": ok_count,
            "error": error_count,
        },
        "results": all_results,
    }
    report_file.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n报告已保存到: {report_file}")
    print(f"\n{'='*60}")
    print(f"验证摘要: {file_path}")
    print(f"  总计: {len(all_results)} 条")
    print(f"  ❌ 矛盾: {contradict_count} 条")
    print(f"  ⚠️  存疑: {doubtful_count} 条")
    print(f"  ✅ 通过: {ok_count} 条")
    print(f"  💥 错误: {error_count} 条")
    if contradict_count > 0:
        print(f"\n  矛盾条目列表:")
        for r in all_results:
            if r["verdict"] == "contradict":
                q = r["question"][:60] + "..." if len(r["question"]) > 60 else r["question"]
                print(f"    - {q}")
                print(f"      理由: {r['reason']}")
    if doubtful_count > 0:
        print(f"\n  存疑条目列表:")
        for r in all_results:
            if r["verdict"] == "doubtful":
                q = r["question"][:60] + "..." if len(r["question"]) > 60 else r["question"]
                print(f"    - {q}")
                print(f"      理由: {r['reason']}")
    return str(report_file)


def main():
    parser = argparse.ArgumentParser(description="验证 BBS FAQ 条目是否与官方文档相悖")
    parser.add_argument("--file", type=str, help="只验证指定的 FAQ 文件（相对于项目根目录）")
    parser.add_argument("--auto-delete", action="store_true", help="自动删除矛盾条目（跳过确认）")
    parser.add_argument("--concurrency", type=int, default=3, help="并发调用 LLM 的数量（默认3）")
    parser.add_argument("--top-k", type=int, default=5, help="每个 FAQ 块检索的参考文档数（默认5）")
    parser.add_argument("--dry-run", action="store_true", help="仅验证并生成报告，不删除任何条目")
    args = parser.parse_args()

    api_key, base_url, model = load_env_config()
    client = OpenAI(api_key=api_key, base_url=base_url)

    print("=" * 60)
    print("BBS FAQ 验证工具")
    print(f"模型: {model}")
    print(f"API: {base_url}")
    print(f"并发数: {args.concurrency}")
    print(f"参考文档数: {args.top_k}")
    print("=" * 60)

    print("\n[1/4] 构建参考文档索引...")
    doc_index = DocIndex()
    doc_index.build()
    print(f"  已索引 {len(doc_index.docs)} 篇参考文档")

    print("\n[2/4] 解析 FAQ 文件...")
    if args.file:
        faq_files = [ROOT_DIR / args.file]
    else:
        faq_files = sorted(BBS_DIR.glob("*.md"))
        faq_files = [f for f in faq_files if f.name != "example.md"]
    print(f"  找到 {len(faq_files)} 个 FAQ 文件: {[f.name for f in faq_files]}")

    all_results = []
    file_results_map = {}

    for faq_file in faq_files:
        print(f"\n[3/4] 验证文件: {faq_file.name}")
        results, blocks, frontmatter = process_file(
            faq_file, client, model, doc_index, args.top_k, args.concurrency
        )
        all_results.extend(results)
        file_results_map[faq_file] = (results, blocks, frontmatter)

    print(f"\n[4/4] 生成报告...")
    for faq_file, (results, blocks, frontmatter) in file_results_map.items():
        report_path = generate_report(results, str(faq_file))
        has_contradict = any(r["verdict"] == "contradict" for r in results)
        if has_contradict and not args.dry_run:
            if args.auto_delete:
                delete_blocks_from_file(faq_file, blocks, results, frontmatter)
            else:
                answer = input(f"\n  文件 {faq_file.name} 中有矛盾条目，是否删除？(y/N): ").strip().lower()
                if answer == "y":
                    delete_blocks_from_file(faq_file, blocks, results, frontmatter)
        elif has_contradict and args.dry_run:
            print(f"  (dry-run 模式，跳过删除)")

    print(f"\n完成！报告保存在 lint_reports/ 目录下。")


if __name__ == "__main__":
    main()