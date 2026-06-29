# 08 - 目录结构

## 推荐目录结构

```text
second-brain-vault/
├── inbox/              # 临时捕获区，定期清空
├── raw/                # 原始素材存档
├── research/           # 研究笔记
│   └── 00-Research索引.md
├── projects/           # 项目笔记
│   └── 项目名/
├── daily-notes/        # 日记/日报
├── people/             # 人物笔记
├── templates/          # 笔记模板
├── target/             # 战略目标
├── executive/          # 执行记录
├── Clippings/          # 网页剪藏
└── context.md          # 流水线上下文
```

## 目录说明

| 目录 | 用途 | 是否必须 |
|---|---|---|
| `inbox/` | 快速捕获，临时存放 | 是 |
| `raw/` | 原始素材存档 | 是 |
| `research/` | 研究笔记，核心知识沉淀 | 是 |
| `projects/` | 项目文档 | 是 |
| `daily-notes/` | 日记、日报、复盘 | 是 |
| `people/` | 人物笔记 | 可选 |
| `templates/` | 笔记模板 | 是 |
| `target/` | 长期目标和拆解 | 可选 |
| `executive/` | 执行记录和打卡 | 可选 |
| `Clippings/` | 网页剪藏 | 可选 |
| `context.md` | 流水线上下文 | 是 |

## 目录设计原则

1. **扁平优先**
   - 避免过深的层级
   - 用标签和双链替代复杂分类

2. ** inbox 是缓冲区**
   - 不要长期堆积
   - 定期清空到 `research/` 或 `projects/`

3. **每个目录职责单一**
   - `research/` 只放研究笔记
   - `projects/` 只放项目文档

4. **用 frontmatter 补充分类**
   - 目录解决物理组织
   - frontmatter 和标签解决逻辑分类

## 下一步

查看 [09 - 模板设计](09-templates.md)，了解每类笔记的具体格式。
