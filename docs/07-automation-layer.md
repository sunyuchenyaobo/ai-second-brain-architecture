# 07 - 自动化层

## 目标

用脚本和工具承担重复劳动，让人把精力放在输入、思考和判断上。

## 自动化范围

| 任务 | 工具 | 频率 |
|---|---|---|
| 更新研究索引 | Python 脚本 | 每次新增研究笔记 |
| 归档日报 | Python 脚本 | 每日 |
| 格式化笔记 | Python 脚本 | 按需 |
| 检查 frontmatter 完整性 | Python 脚本 | 按需 |

## 示例脚本：`update_research_index.py`

功能：扫描 `research/` 目录下的笔记，自动生成 `research/00-Research索引.md`。

```python
"""
自动更新研究索引
扫描 research/ 目录，按日期分组生成索引文件
"""

from pathlib import Path
from datetime import datetime
import re

VAULT_ROOT = Path(".")
RESEARCH_DIR = VAULT_ROOT / "research"
INDEX_FILE = RESEARCH_DIR / "00-Research索引.md"

def extract_frontmatter(file_path: Path) -> dict:
    """从 markdown 文件提取 frontmatter"""
    content = file_path.read_text(encoding="utf-8")
    fm = {}
    if content.startswith("---"):
        parts = content.split("---", 2)
        if len(parts) >= 3:
            for line in parts[1].strip().split("\n"):
                if ":" in line:
                    k, v = line.split(":", 1)
                    fm[k.strip()] = v.strip()
    return fm

def update_index():
    notes = []
    for path in RESEARCH_DIR.glob("*.md"):
        if path.name.startswith("00-"):
            continue
        fm = extract_frontmatter(path)
        if "date" in fm:
            notes.append((fm["date"], path.stem, path.name))

    notes.sort(reverse=True)

    lines = ["# Research 索引\n\n"]
    current_group = None
    for date_str, stem, filename in notes:
        group = date_str[:7]  # 按年月分组
        if group != current_group:
            lines.append(f"## {group}\n\n")
            current_group = group
        lines.append(f"- [[{stem}]] ({date_str})\n")

    INDEX_FILE.write_text("".join(lines), encoding="utf-8")

if __name__ == "__main__":
    update_index()
```

## 自动化原则

1. **脚本只处理机械任务**
   - 不替代人的思考
   - 只处理格式化、索引、归档等重复劳动

2. **保留人工确认节点**
   - 自动生成后，人检查一遍
   - 特别是涉及内容修改的脚本

3. **脚本路径可配置**
   - 不要硬编码个人路径
   - 使用相对路径或配置文件

## 下一步

了解 [08 - 目录结构](08-directory-structure.md)，看如何在 vault 中组织这些内容。
