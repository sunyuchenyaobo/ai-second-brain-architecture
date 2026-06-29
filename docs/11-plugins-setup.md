# 11 - 插件安装与配置

本仓库推荐的 Obsidian 插件清单及配置方法。

## 必装插件

### 1. Templater

**作用**：模板自动化，支持在模板中使用变量和脚本。

**安装**：
1. 打开 Obsidian Settings
2. 进入 **Community plugins → Browse**
3. 搜索 "Templater"
4. 点击 Install → Enable

**配置**：
1. 进入 **Templater 设置**
2. 设置 **Template folder location** 为 `templates`
3. 设置 **Timeout** 为 5000

**使用**：
- 新建笔记后，按 `Ctrl/Cmd + P` 打开命令面板
- 搜索 "Templater: Open Insert Template modal"
- 选择 `research-note` 或其他模板

---

### 2. Dataview

**作用**：通过类 SQL 语法动态查询笔记，生成索引、看板、清单。

**安装**：
1. 进入 **Community plugins → Browse**
2. 搜索 "Dataview"
3. 点击 Install → Enable

**配置**：
1. 进入 **Dataview 设置**
2. 启用 **Enable JavaScript queries**
3. 设置 **Date format** 为 `YYYY-MM-DD`

**示例查询**（放到任意 markdown 文件中）：

```dataview
table date, tags
from "research"
sort date desc
```

---

### 3. Periodic Notes

**作用**：自动化生成日报、周报、月报。

**安装**：
1. 进入 **Community plugins → Browse**
2. 搜索 "Periodic Notes"
3. 点击 Install → Enable

**配置**：
1. 进入 **Periodic Notes 设置**
2. 启用 **Daily Notes**
3. 设置 **Date format** 为 `YYYY-MM-DD`
4. 设置 **Template** 为 `templates/daily-note.md`
5. 设置 **Folder** 为 `daily-notes`

**使用**：
- 按 `Ctrl/Cmd + P` → "Periodic Notes: Open daily note"
- 自动生成当日报报

---

## 推荐插件

### 4. Omnisearch

**作用**：增强的全文搜索，支持中文分词。

**安装**：
1. 进入 **Community plugins → Browse**
2. 搜索 "Omnisearch"
3. 点击 Install → Enable

**配置**：
1. 进入 **Omnisearch 设置**
2. 启用 **PDF indexing**（如果需要）
3. 启用 **Images OCR**（可选）

---

## 可选插件

| 插件 | 作用 | 建议 |
|---|---|---|
| Local REST API | 外部脚本写入 Obsidian | 使用脚本自动化时安装 |
| Calendar | 日历视图看日报 | 日报频繁时安装 |
| Excalidraw | 手绘风格图表 | 需要画架构图时安装 |
| Obsidian Clipper | 网页剪藏 | 剪藏网页多时安装 |
| Full Calendar | 完整日历管理 | 日程管理复杂时安装 |

---

## 插件启用清单

本仓库 `.obsidian/community-plugins.json` 已配置以下插件：

```json
{
  "templater-obsidian": true,
  "dataview": true,
  "periodic-notes": true,
  "omnisearch": true
}
```

Obsidian 会自动识别这个清单，你只需在 Community plugins 页面点击安装即可。

---

## 常见问题

### 安装插件时提示需要安全模式

1. 进入 **Settings → Community plugins**
2. 关闭 **Safe mode**
3. 重新安装插件

### Templater 模板不生效

- 检查 **Template folder location** 是否设置为 `templates`
- 检查模板文件是否在 `templates/` 目录下
- 检查是否启用了 Templater 插件

### Dataview 查询无结果

- 检查查询语法是否正确
- 确认笔记中有对应的 frontmatter
- 尝试刷新 Dataview 索引
