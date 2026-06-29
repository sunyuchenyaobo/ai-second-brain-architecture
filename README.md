# AI Second Brain Architecture

> 一套 AI 驱动的个人知识管理系统架构，打通 **Claude Code + NotebookLM + Obsidian**，实现从信息输入到结构化知识沉淀的完整闭环。

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

---

## 为什么需要这套系统？

信息过载时代，收藏 ≠ 学会，记录 ≠ 掌握。

本架构将个人知识管理（PKM）拆分为清晰的五层：

- **输入层**：统一接收文本、链接、视频、语音、PDF、想法
- **处理层**：用 Claude Code 完成采集、清洗、结构化
- **关联层**：用 NotebookLM 做跨源语义关联
- **沉淀层**：用 Obsidian 做模板化、可检索、可双链的笔记沉淀
- **复盘层**：用自动化脚本维护索引、日报、项目上下文

核心目标：**让信息从“被消费”走向“被关联、被沉淀、被复用”**。

---

## 系统架构

```mermaid
graph TD
    A[输入层<br/>文本 / 链接 / 视频 / 语音 / PDF / 想法] --> B[处理层<br/>Claude Code]
    B --> C[关联层<br/>NotebookLM]
    C --> D[沉淀层<br/>Obsidian]
    D --> E[复盘层<br/>索引 / 日报 / 上下文]
    E --> A
```

---

## 核心流程

```mermaid
graph LR
    A[用户输入] --> B[Claude Code 采集]
    B --> C[NotebookLM 关联分析]
    C --> D[生成结构化笔记]
    D --> E[写入 Obsidian]
    E --> F[更新索引 / context]
    F --> A
```

---

## 目录结构

```text
ai-second-brain-architecture/        # 本身就是一个 Obsidian vault
├── .obsidian/                       # Obsidian 核心配置
│   ├── app.json
│   ├── appearance.json
│   ├── community-plugins.json
│   ├── core-plugins.json
│   └── daily-notes.json
├── inbox/                           # 临时捕获，定期清空
├── raw/                             # 原始素材存档
├── research/                        # 研究笔记
│   └── 00-Research索引.md          # 自动索引脚本生成
├── projects/                        # 项目笔记
├── daily-notes/                     # 日记/日报
├── people/                          # 人物笔记
├── templates/                       # 笔记模板
│   ├── research-note.md
│   ├── daily-note.md
│   └── project-note.md
├── assets/                          # 图片等附件
├── context.md                       # 流水线上下文
├── scripts/                         # 自动化脚本
├── starter-config/                  # 备用配置副本
├── examples/                        # 脱敏示例
├── architecture/                  # Mermaid 图源文件
├── docs/                            # 架构文档
├── README.md
└── LICENSE
```

---

## 快速开始

### 方式一：作为新 vault 打开（推荐）

1. **Clone 本仓库**
   ```bash
   git clone https://github.com/sunyuchenyaobo/ai-second-brain-architecture.git
   ```

2. **在 Obsidian 中打开**
   - 打开 Obsidian
   - 点击 "Open folder as vault"
   - 选择 `ai-second-brain-architecture` 目录

3. **安装推荐插件**
   - 进入 **Settings → Community plugins → Browse**
   - 安装并启用以下插件：
     - **Templater**：模板自动化
     - **Dataview**：动态查询笔记
     - **Periodic Notes**：日报/周报

4. **开始使用模板**
   - 新建笔记时选择 `templates/research-note.md`
   - 或配置 Templater 快捷键自动插入模板

5. **（可选）配置自动化脚本**
   ```bash
   cd ai-second-brain-architecture
   python scripts/update_research_index.py --vault .
   ```

### 方式二：复制配置到已有 vault

如果你已有自己的 vault，可以只复制以下文件：

- `templates/*.md` → 你的 vault 根目录
- `.obsidian/*.json` → 你的 vault `.obsidian/` 目录
- `scripts/` → 你的 vault 根目录

---

## 技术栈

| 层级 | 工具 | 作用 |
|---|---|---|
| 处理层 | Claude Code / Claude API | 采集、清洗、结构化 |
| 关联层 | NotebookLM (MCP) | 跨源语义检索与关联 |
| 沉淀层 | Obsidian | 笔记存储、双链、图谱 |
| 自动化层 | Python + MCP | 索引更新、日报归档 |
| 格式 | Markdown + YAML frontmatter | 统一笔记格式 |

---

## 设计原则

1. **隐私优先**：本仓库不包含任何私人笔记，只提供架构、模板和脚本
2. **AI 原生**：每个环节都考虑如何与 LLM 协作，而不是让 AI 替代思考
3. **可复制**：任何人都能 fork 后，用自己的内容跑通整个流程
4. **渐进式**：从最小配置开始，按需扩展自动化脚本

---

## 文档导航

- [01 - 系统总览](docs/01-system-overview.md)
- [02 - 输入层](docs/02-input-layer.md)
- [03 - 处理层](docs/03-processing-layer.md)
- [04 - 关联层](docs/04-association-layer.md)
- [05 - 沉淀层](docs/05-sedimentation-layer.md)
- [06 - 复盘层](docs/06-review-layer.md)
- [07 - 自动化层](docs/07-automation-layer.md)
- [08 - 目录结构](docs/08-directory-structure.md)
- [09 - 模板设计](docs/09-templates.md)
- [10 - 技术栈](docs/10-tech-stack.md)

---

## 授权

[MIT](LICENSE)
