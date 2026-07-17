# Miliastra-knowledge

Miliastra-knowledge 是千星奇域工具箱的文档资产仓库，仅保存文档内容，不包含文档生产流程、爬虫、配置或 RAG 运行时代码。

## 目录结构

- official/guide: 官方综合指南文档
- official/tutorial: 官方教程文档
- official/faq: 官方常见问题文档
- bbs: 从问答楼整理出的社区问答文档
- user: 预留给后续用户投稿或人工整理文档
- derived: 由 process_docs.py 生成的聚合文档和索引

## 约定

- 本仓库只存放 Markdown 文档资产
- 不存放 spider、bbs_spider、rag_v1、rag_v2 等代码
- 不存放 .env、数据库、缓存或索引产物

## 派生逻辑（derived/ 的生成与维护）

`derived/` 下的内容均由 `official/` 源文档派生而来，分为两类维护方式：

### 1. 全自动派生（node / faq / index）

由仓库外的 `mcp/process_docs.py` 生成，源文档变化后重新运行该脚本即可，**不要手工编辑这些产物**：

- `derived/node/<分组>.md`：扫描 `official/guide/` 下文件名包含 6 类节点分组名（执行节点、事件节点、流程控制节点、查询节点、运算节点、其它节点）的文档，按 `#` 一级标题作为所属大类、`##` 二级标题作为单个节点切分，跨文档去重后合并到对应分组文件。
- `derived/node/<分组>.md` 的端归属：每个节点块标注【服务端/客户端/双端】（`**归属端**` 行），服务端=实体节点图，客户端=角色技能/造物技能/造物状态/造物状态决策/过滤器节点图，双端=通用节点（同时出现在服务端与客户端节点图文档中，去重时取端并集）。端归属映射维护在仓库外的 `mcp/node_side_map.json`（按文档 id 索引），新增无法靠章节判定的节点文档时在该文件补一行即可。
- `derived/faq/faq.md`：扫描 `official/faq/` 下所有文档，仅提取以 `## Q：`/`## Q:` 开头的问答块，去重后合并。
- `derived/index.json`：记录每个 chunk 的标题、所属大类、端归属（`side`）、来源文档、本地路径与输出文件，供 RAG/MCP 检索使用。

### 2. 半自动派生（svg 一图流）

由 AI 依据源指南文档、遵循生成技能规范手工产出：

- `derived/svg_skill.md`：「一图流」SVG 生成技能规范（配色、排版、来源链接、页脚版本号等）。
- `derived/svg/*.svg`：按主题生成的单页可视化信息图，文件名为「序号-中文主题名.svg」。
- `derived/svg_index.md`：SVG 内容清单，并按版本（如「月之X」版本更新）分组标注本次新增/更新的主题。
- 维护方式：新增或更新主题时，依据对应源文档、遵循 `svg_skill.md` 生成 SVG，并同步 `svg_index.md`；随官方版本推进更新页脚与索引中的版本号（只对新变更的svg更新版本号，未变更的原有svg版本号不变）。

### 3. 文档目录索引（AGENTS.md）

本目录下的 `AGENTS.md` 是手工维护的文档目录索引，供 `backend/agent/prompt.py` 读取并注入 Agent 提示词。新增源文档时需在 `AGENTS.md` 补充对应条目（标题：摘要 | 关键词）。