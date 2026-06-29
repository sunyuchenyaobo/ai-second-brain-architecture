"""
自动更新研究索引

扫描 research/ 目录，按日期分组生成索引文件。
"""

from pathlib import Path
import argparse


def extract_frontmatter(file_path: Path) -> dict:
    """从 markdown 文件提取 YAML frontmatter"""
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


def update_index(vault_root: Path):
    research_dir = vault_root / "research"
    index_file = research_dir / "00-Research索引.md"

    if not research_dir.exists():
        print(f"research/ directory not found in {vault_root}")
        return

    notes = []
    for path in research_dir.glob("*.md"):
        if path.name.startswith("00-"):
            continue
        fm = extract_frontmatter(path)
        date = fm.get("date", "0000-00-00")
        notes.append((date, path.stem))

    notes.sort(reverse=True)

    lines = ["# Research 索引\n\n"]
    current_group = None
    for date_str, stem in notes:
        group = date_str[:7]  # 按年月分组，例如 2026-06
        if group != current_group:
            lines.append(f"## {group}\n\n")
            current_group = group
        lines.append(f"- [[{stem}]] ({date_str})\n")

    index_file.write_text("".join(lines), encoding="utf-8")
    print(f"Updated {index_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Update research index")
    parser.add_argument("--vault", default=".", help="Path to vault root")
    args = parser.parse_args()

    update_index(Path(args.vault).resolve())
