# 09 - 模板设计

## 设计原则

1. **统一 frontmatter**：每篇笔记都有标准化的元数据
2. **统一区块结构**：相同类型的笔记使用相同的结构
3. **保留原文**：为后续核查和再加工留底
4. **区分 AI 输出与个人思考**：避免把 AI 总结当成自己的观点

## 研究笔记模板

```markdown
---
type: research
date: YYYY-MM-DD
tags: [research, 标签1, 标签2]
source: "来源说明"
notebook_id: "可选：NotebookLM 笔记本 ID"
---

## 原文

（完整保留原始素材，不做删减）

## 核心观点

- 核心观点 1
- 核心观点 2

## 我的思考

（个人思考、反思、觉察）

## 关联发现

- **源标题 1**：相关原文摘要...
- **源标题 2**：相关原文摘要...

## 关联笔记

- [[笔记名 1]]
- [[笔记名 2]]
```

## 日报模板

```markdown
---
type: daily
date: YYYY-MM-DD
tags: [daily]
---

## 今日输入

## 今日沉淀

## 关键发现

## 明日待办
```

## 项目笔记模板

```markdown
---
type: project
date: YYYY-MM-DD
tags: [project, 标签]
status: active
---

## 目标

## 当前进展

## 阻塞点

## 下一步动作

## 关键决策
```

## 模板使用方式

1. 在 Obsidian 中安装 Templater 插件
2. 将模板文件放入 `templates/` 目录
3. 配置 Templater 的模板文件夹路径
4. 使用快捷键插入模板

## 下一步

了解 [10 - 技术栈](10-tech-stack.md)，看如何选择和配置工具。
