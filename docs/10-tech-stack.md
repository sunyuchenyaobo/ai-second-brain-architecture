# 10 - 技术栈

## 整体工具链

| 层级 | 工具 | 作用 |
|---|---|---|
| 输入 | 多种 | 文本、链接、视频、PDF、灵感 |
| 处理 | Claude Code / Claude API | 采集、清洗、结构化 |
| 关联 | NotebookLM (MCP) | 跨源语义检索 |
| 沉淀 | Obsidian | 笔记存储、双链、图谱 |
| 自动化 | Python + MCP | 索引、归档、格式化 |
| 格式 | Markdown + YAML frontmatter | 统一笔记格式 |

## Claude Code

Claude Code 在本系统中承担**处理层**的角色：

- 接收用户输入
- 抓取网页/视频内容
- 清洗和结构化信息
- 调用 NotebookLM MCP 进行关联
- 生成 Obsidian 笔记并写入

## NotebookLM MCP

NotebookLM 通过 MCP 与 Claude Code 集成：

- 查询历史知识库
- 添加新的 source
- 返回相关 source 列表
- 提取源内容

## Obsidian

Obsidian 是沉淀层的核心工具：

### 推荐插件

| 插件 | 作用 |
|---|---|
| Templater | 模板自动化 |
| Dataview | 动态查询笔记 |
| Periodic Notes | 日报/周报 |
| Local REST API | 外部脚本写入 |

## Python

用于自动化脚本：

- 更新索引
- 归档日报
- 格式化 frontmatter
- 检查笔记完整性

## Markdown + YAML frontmatter

统一的笔记格式：

```markdown
---
type: research
date: 2026-06-29
tags: [research, ai]
source: "来源说明"
---
```

## 选型理由

| 工具 | 理由 |
|---|---|
| Claude Code | 代码级 AI 助手，可直接操作文件系统 |
| NotebookLM | 原生支持多 source 语义关联 |
| Obsidian | 本地优先、Markdown 原生、双链 |
| Python | 自动化能力强，生态成熟 |

## 下一步

回到 [README.md](../README.md)，开始搭建你自己的系统。
