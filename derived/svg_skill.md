---
name: svg-1flow
description: 输入文本内容，输出千星奇域「一图流」SVG 信息图。将编辑器功能文档转化为结构化可视化教程 SVG。
---

# SVG 一图流生成技能

将千星奇域编辑器的功能/概念/教程文档内容，转化为单页可视化信息图 SVG。

## 设计风格：Apple HIG × 原神风

### 核心视觉语言
融合 Apple Human Interface Guidelines 的极简排版风格。极简、干净、留白充足，以蓝色为主色调，温暖背景衬托。扁平化、轻微阴影、柔和圆角。不使用描边/硬边框。不使用搜索框等无关装饰。不使用黄色/金色作为主体色调。

### 整体原则
- 页面背景暖白 `#F9F7F2`，卡片纯白 `#FFFFFF`
- 留白充足但不留大面积空白（viewBox 高度贴合实际内容底部）
- 不使用 emoji，以文字为主
- 卡片柔和阴影，不用描边/硬边框
- 几何感强：圆角卡片、药丸标签、圆形编号
- 主色调为蓝色系，避免黄色/金色作为视觉主体

### 色彩系统

| 用途 | 色值 | 说明 |
|------|------|------|
| 页面背景 | `#F9F7F2` | 暖白 |
| 主色 | `#2D6BE4` | 蓝色，仅用于小节标题、圆圈序号、竖条、标签背景、来源超链接。**禁止在正文内容、卡片描述、表格内容等位置使用蓝色文字，避免与底部超链接混淆** |
| 主色深 | `#1B4FC0` | 深蓝，用于步骤最终圆圈 |
| 顶部色带渐变 | `#2D6BE4` → `#4A3F6B` | 蓝到深紫，仅顶部 |
| 深色文字 | `#1A1B2E` | 深海军蓝 |
| 正文 | `#4A4B65` | 灰紫 |
| 辅助 | `#8B8DA0` | 淡灰紫 |
| 卡片背景 | `#FFFFFF` | 纯白 |
| 交替行 | `#F4F1EA` | 暖浅灰 |
| 分隔线 | `#E8E4DA` | 暖灰 |
| 重点标签蓝 | `#E8EEFB` | 蓝色淡底 |
| 重点标签橙 | `#FFF3E0` | 橙色淡底（提示/警告） |
| 重点标签红 | `#FDE8E6` | 红色淡底 |
| 重点标签绿 | `#E5F2E9` | 绿色淡底 |
| 提示条蓝 | `#E8EEFB` | 蓝色淡底（替代原金色提示） |
| 提示文字 | `#2D6BE4` | 蓝色提示文字（仅在蓝色提示框内使用） |
| 警告文字 | `#D93025` | 红色警告文字 |
| 成功 | `#34A853` | 绿色确认 |
| 错误 | `#D93025` | 红色否认 |

### 色彩使用规范

**蓝色 `#2D6BE4` 严禁过度使用**：蓝色与底部来源超链接颜色相同，正文内容中大量使用蓝色会导致读者无法区分内容与链接。遵循以下原则：

- **可以使用蓝色的地方**：小节标题（18px bold）、编号圆圈填充、标题卡片左侧竖条、药丸标签背景 `#E8EEFB` 内的文字、提示框内文字、底部来源超链接
- **禁止使用蓝色的地方**：卡片内容描述文字、表格内容文字、流程步骤文字、参数说明文字——这些一律使用 `#1A1B2E`（加粗时）或 `#4A4B65`（正文时）
- **对比表表头行**使用蓝色背景 `#2D6BE4` + 白色文字，表格内容行使用 `#1A1B2E` 或 `#4A4B65`

### 阴影与圆角

```xml
<defs>
  <linearGradient id="topGrad" x1="0" y1="0" x2="1200" y2="0" gradientUnits="userSpaceOnUse">
    <stop offset="0%" stop-color="#2D6BE4"/>
    <stop offset="100%" stop-color="#4A3F6B"/>
  </linearGradient>
  <filter id="card">
    <feDropShadow dx="0" dy="1" stdDeviation="4" flood-color="#2D6BE4" flood-opacity="0.06"/>
  </filter>
  <filter id="elevated">
    <feDropShadow dx="0" dy="4" stdDeviation="14" flood-color="#000" flood-opacity="0.07"/>
  </filter>
</defs>
```

- `card`：普通卡片，微蓝阴影
- `elevated`：标题卡片，更浮起
- 卡片圆角：`rx="14"`（大）、`rx="10"`（中）、`rx="6"`（小）
- 药丸标签：`rx="16"` ~ `rx="20"`
- 步骤圆圈：`r="12"` ~ `r="14"`，`fill="#2D6BE4"`；最终步骤用深蓝 `#1B4FC0`
- 四色标签：蓝 `#E8EEFB`、橙 `#FFF3E0`、红 `#FDE8E6`、绿 `#E5F2E9`

### 字体

```
font-family="'HYWenHei 85W','Noto Sans SC','PingFang SC','Roboto',sans-serif"
```

主字体为原神字体「汉仪文黑 85W」（CSS 名 `HYWenHei 85W`），回退为 Noto Sans SC。

| 层级 | 大小 | 字重 | 颜色 |
|------|------|------|------|
| 页大标题 | 34px | bold | `#1A1B2E` |
| 小节标题 | 18px | 400 | `#2D6BE4` |
| 卡片标题 | 16px | 500 | `#1A1B2E` |
| 正文 | 14px | normal | `#4A4B65` |
| 正文加粗 | 14px | 500 | `#1A1B2E` |
| 辅助说明 | 12px | normal | `#8B8DA0` |

### 页面结构

```
1. 顶部色带（6px，蓝→深紫渐变）
2. 标题卡片（白底阴影，左侧 4px 蓝色竖条）
3. 小节标题（18px 蓝色）+ 可选灰色副标题
4. 内容卡片（白底阴影，rx=14）
5. 来源链接（页面底部，页脚上方，蓝色可点击文字）
6. 页脚文字（8B8DA0，12px）
7. 白底结束（无底部色带）
```

### 标题卡片格式

```xml
<rect x="48" y="32" width="1104" height="80" rx="14" fill="#fff" filter="url(#elevated)"/>
<rect x="48" y="32" width="4" height="80" rx="2" fill="#2D6BE4"/>
<text x="72" y="72" fill="#1A1B2E" font-size="34" font-weight="bold">主标题</text>
<text x="X2" y="72" fill="#4A4B65" font-size="16">副标题</text>
```

### 来源链接格式

来源链接放在页面最底部，页脚文字上方：

```xml
<!-- 单链接 -->
<a xlink:href="URL" target="_blank">
  <text x="48" y="Y" fill="#2D6BE4" font-size="12" text-decoration="underline">奇匠学院文档：课程标题</text>
</a>

<!-- 多链接，横排排列，间距 24px -->
<a xlink:href="URL1" ...><text ...>课程</text></a>
<text ... fill="#8B8DA0">|</text>
<a xlink:href="URL2" ...><text ...>指南</text></a>
```

### 小节标题格式

```xml
<text x="48" y="Y" fill="#2D6BE4" font-size="18">X、小节名称</text>
<text x="X2" y="Y" fill="#8B8DA0" font-size="13">补充说明</text>
```

不使用分隔线，卡片间距自然分隔。

### 步骤流程格式

药丸按钮：
```xml
<rect x="X" y="Y" width="W" height="48" rx="24" fill="#2D6BE4"/>
<text ... fill="#fff" font-weight="500">步骤名</text>
<text ... fill="#8B8DA0" font-size="16">›</text>
```

编号圆圈：
```xml
<circle cx="CX" cy="CY" r="16" fill="#2D6BE4"/>
<text ... fill="#fff" font-size="13" text-anchor="middle" font-weight="500">N</text>
```
最终步骤用深蓝底：`fill="#1B4FC0"`

### 对比表格

```xml
<rect x="X" y="Y" width="W" height="44" rx="14" fill="#2D6BE4"/>
<rect x="X" y="Y+32" width="W" height="12" fill="#2D6BE4"/>
<text ... fill="#fff" font-size="15" text-anchor="middle" font-weight="500">列名</text>
<line ... stroke="#E8E4DA"/>
<text ... fill="#1A1B2E">内容</text>
```

### 提示框
- 蓝色提示：`fill="#E8EEFB"` 背景 + `#2D6BE4` 左侧 4px 竖条 + `#4A4B65` 文字
- 红色警告：`fill="#FDE8E6"` 背景 + `#D93025` 左侧 4px 竖条 + `#D93025` 文字

### 间距规范
- 页面宽度：1200px
- 左右边距：48px，卡片内边距 24px
- 卡片间距：12-16px
- **viewBox 高度必须紧密贴合内容，页面以白底结束，无底部色带。页面底部结构从下往上为：页脚文字 → 来源链接行 → 「相关文档：」标签行 → 最后内容卡片下方间距。页脚文字距 SVG 底部留 12-16px 间距，页脚文字与来源链接之间留 6px 间距**

## 内容提炼规则

1. 从文档提炼核心知识点，去除冗余描述。面向新手，不要丢失细节，要全面。**请尽量细致地综合所有信息，完善细节：每个参数、配置项、操作步骤、限制条件、注意事项都必须体现，宁可信息密度高也不要遗漏。对比差异要逐项列出，流程步骤要完整，参数表格要覆盖全部字段。**
2. 结构化展示：流程→步骤卡片+箭头，参数→键值对/表格，对比→对比表
3. 重要提示用提示框高亮
4. 每个 SVG 信息密度适中，不过度拥挤
5. 小节标题用中文数字序号：「一、」「二、」等
6. 不使用 emoji
7. **内容完整性原则：源文档中每个独立子专题必须有至少一行独立呈现，不可合并压缩到只留标题而丢失操作细节**
8. **FAQ/常见问题中的关键限制或注意事项，必须以提示框呈现**

## 来源链接规范

每张 SVG 页面底部（页脚文字上方）必须包含来源链接：
- **「相关文档」标签单独成行**：在链接上方先用一行灰色小字标注「相关文档」，例如 `<text x="48" y="Y" fill="#8B8DA0" font-size="12">相关文档：</text>`
- **链接文字单独另起一行**：在标签下方紧接一行或数行蓝色可点击 `<a>` 超链接，每个链接独占一行（不与标签同行）
- 链接文字格式：`奇匠学院文档：课程标题` 或 `奇匠学院文档：课程 | 综合指南`
- 多个来源时分多行排列，每行一个链接
- SVG 中使用 `xlink:href` 和 `target="_blank"`
- 链接位于页面最底部，页脚文字上方，紧跟内容卡片下方

已知文档 URL 映射（从文档 frontmatter 获取）：
- 经典模式课程：`https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhvoc3rviq32`
- 地形编辑指南：`https://act.mihoyo.com/ys/ugc/tutorial/detail/mhwe1n94b1x6`
- 地形编辑FAQ：`https://act.mihoyo.com/ys/ugc/tutorial/faq/detail/mhcqfc0h5aoo`
- 环境配置教程：`https://act.mihoyo.com/ys/ugc/tutorial/course/detail/mhw64cr51fue`
- 环境配置指南：`https://act.mihoyo.com/ys/ugc/tutorial/detail/mhdznsie9up8`
- 整体界面（快捷设置）：`https://act.mihoyo.com/ys/ugc/tutorial/detail/mhn4bsi5lb58`

## 页脚规范

每张 SVG 底部页脚文字：

```
由 AI 基于官方奇匠学院文档生成。版本：月之七
```

格式：`fill="#8B8DA0" font-size="11" text-anchor="middle"`，居中于 x=600。

来源链接紧贴页脚文字上方。页脚文字距 SVG 底部留 12-16px 间距（白底）。

**页面底部结构（从下往上）：**
1. SVG 底部（12-16px 白底间距）
2. 页脚文字（"由 AI ..."）
3. 来源链接行（蓝色可点击超链接，每行一个，与页脚文字间距 6px）
4. 「相关文档：」标签行（灰色小字 #8B8DA0，与链接间距 6px）
5. 最后内容卡片下方间距

## 输出规则

1. 输出完整 SVG 文件（`<svg` 开头，`</svg>` 结尾）
2. `viewBox` 宽度固定 1200，高度必须贴合内容，不留底部大段空白
3. 中文字符宽度 ≈ 字号 × 1.0~1.2，用于估算文字宽度防溢出
4. 文件输出到 `derived/svg/` 目录，文件名为中文主题名.svg
5. SVG 根元素必须声明 `xmlns:xlink="http://www.w3.org/1999/xlink"` 用于超链接

## 自检清单

- [ ] 页面背景 `#F9F7F2`，卡片 `#FFFFFF`
- [ ] 不使用 emoji
- [ ] 主色 `#2D6BE4`，不使用黄色/金色作为视觉主体
- [ ] 标题卡片左侧 4px 蓝色竖条
- [ ] 卡片使用阴影，无 stroke
- [ ] 来源链接在页面底部（页脚上方），蓝色可点击（`<a xlink:href>`）
- [ ] 「相关文档：」标签单独一行（灰色 #8B8DA0），链接文字另起一行（蓝色 #2D6BE4），两者不在同一行
- [ ] 底部有页脚：「由 AI 基于官方奇匠学院文档生成。版本：月之七」
- [ ] viewBox 高度贴合内容，无底部大段空白
- [ ] 顶部色带（6px，蓝→深紫渐变），无底部色带
- [ ] 源文档每个独立子专题至少一行呈现
- [ ] 字体使用 `HYWenHei 85W`（原神字体）为主字体，回退 Noto Sans SC
- [ ] 正文内容不使用蓝色文字，蓝色仅用于：小节标题、编号圆圈、标题竖条、药丸标签内文字、提示框内文字、底部超链接