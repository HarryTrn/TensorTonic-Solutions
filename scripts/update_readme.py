#!/usr/bin/env python3
"""
Regenerate README.md from README.template.md.

- Scans the repo for solution folders (any folder that directly contains files).
- Looks up title / category / key idea in scripts/problems.json.
- Unknown (newly solved) problems are auto-titled from the folder name and
  auto-categorized with keyword rules, so nothing has to be typed by hand.
- Computes stats (total, per topic, last 7 / 30 days, recent problems,
  cumulative growth) from git history and fills the template placeholders.

Standard library only. Run from the repo root:  python scripts/update_readme.py
"""
from __future__ import annotations

import json
import re
import subprocess
from collections import Counter, OrderedDict
from datetime import date, datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
META_FILE = ROOT / "scripts" / "problems.json"
TEMPLATE_FILE = ROOT / "README.template.md"
OUTPUT_FILE = ROOT / "README.md"

# Folders that are never solutions.
IGNORED_DIRS = {".git", ".github", "scripts", "assets", "images", "docs", "__pycache__", "node_modules"}
PROBLEM_URL = "https://www.tensortonic.com/problems/{slug}"
RESEARCH_URL = "https://www.tensortonic.com/research/{path}"
RECENT_COUNT = 5
GROWTH_WEEKS = 10


# --------------------------------------------------------------------------- #
# Discovery
# --------------------------------------------------------------------------- #
def has_visible_files(folder: Path) -> bool:
    return any(p.is_file() and not p.name.startswith(".") for p in folder.iterdir())


def find_solution_dirs(base: Path, depth: int = 0) -> list[Path]:
    """Return folders that directly contain files (max 2 levels deep)."""
    found: list[Path] = []
    for child in sorted(base.iterdir()):
        if not child.is_dir() or child.name.startswith(".") or child.name in IGNORED_DIRS:
            continue
        if has_visible_files(child):
            found.append(child)
        elif depth < 1:
            found.extend(find_solution_dirs(child, depth + 1))
    return found


def first_added_date(rel_path: str) -> date:
    """Date of the first commit that added something in this folder."""
    try:
        out = subprocess.run(
            ["git", "log", "--diff-filter=A", "--format=%cs", "--", rel_path],
            cwd=ROOT, capture_output=True, text=True, check=True,
        ).stdout.split()
        if out:
            return date.fromisoformat(out[-1])
    except (subprocess.CalledProcessError, FileNotFoundError, ValueError):
        pass
    return date.today()


def title_from_folder(folder: Path, slug: str) -> str:
    """Use the first markdown heading inside the folder if any, else titleize the slug."""
    for md in sorted(folder.glob("*.md")):
        for line in md.read_text(encoding="utf-8", errors="ignore").splitlines():
            m = re.match(r"^#{1,3}\s+(.+)", line.strip())
            if m:
                return m.group(1).strip()
    return " ".join(w.upper() if len(w) <= 3 and w.isalpha() and w not in {"and", "for", "the", "of"} else w.capitalize()
                    for w in slug.replace("_", "-").split("-"))


def guess_category(slug: str, rules: list[list[str]]) -> str:
    s = slug.lower()
    for keyword, cat in rules:
        if keyword in s:
            return cat
    return "new"


# --------------------------------------------------------------------------- #
# Rendering helpers
# --------------------------------------------------------------------------- #
def render_pie(counts: "OrderedDict[str, int]", cats: dict) -> str:
    lines = ["```mermaid", "pie showData", "    title Solved problems by topic"]
    for cid, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        if n:
            lines.append(f'    "{cats[cid]["short"]}" : {n}')
    lines.append("```")
    return "\n".join(lines)


def render_topic_table(counts: "OrderedDict[str, int]", cats: dict, total: int) -> str:
    cells = [f'[{cats[c]["emoji"]} {cats[c]["name"]}](#{c}) | {n}' for c, n in counts.items() if n]
    cells.append(f"**Total** | **{total}**")
    if len(cells) % 2:
        cells.append(" | ")
    half = len(cells) // 2
    rows = ["| Topic | Solved | Topic | Solved |", "|:--|:--:|:--|:--:|"]
    for left, right in zip(cells[:half], cells[half:]):
        rows.append(f"| {left} | {right} |")
    return "\n".join(rows)


def render_recent(problems: list[dict]) -> str:
    recent = sorted(problems, key=lambda p: (p["added"], p["path"]), reverse=True)[:RECENT_COUNT]
    rows = ["| Date | Problem | Topic | Code |", "|:--|:--|:--|:-:|"]
    for p in recent:
        rows.append(f'| {p["added"].isoformat()} | [{p["title"]}]({p["url"]}) | {p["cat_label"]} | [📁](./{p["path"]}) |')
    return "\n".join(rows)


def render_growth(problems: list[dict]) -> str:
    """Cumulative solved count at the end of each of the last N weeks (Mermaid xychart)."""
    today = date.today()
    week_ends = [today - timedelta(weeks=i) for i in range(GROWTH_WEEKS - 1, -1, -1)]
    values = [sum(p["weight"] for p in problems if p["added"] <= d) for d in week_ends]
    labels = ", ".join(f'"{d.strftime("%d/%m")}"' for d in week_ends)
    top = max(values + [1])
    return "\n".join([
        "```mermaid",
        "xychart-beta",
        '    title "Cumulative problems solved (weekly)"',
        f"    x-axis [{labels}]",
        f'    y-axis "Solved" 0 --> {top + max(5, top // 10)}',
        f"    bar [{', '.join(map(str, values))}]",
        f"    line [{', '.join(map(str, values))}]",
        "```",
    ])


def render_solutions(problems: list[dict], cats: dict, order: list[str]) -> str:
    blocks = []
    first = True
    for cid in order:
        items = [p for p in problems if p["category"] == cid]
        if not items:
            continue
        n = sum(p["weight"] for p in items)
        c = cats[cid]
        rows = ["| # | Problem | Key idea | Code |", "|:-:|:--|:--|:-:|"]
        for i, p in enumerate(items, 1):
            new_tag = " 🆕" if p["is_new"] else ""
            rows.append(f'| {i} | [{p["title"]}]({p["url"]}){new_tag} | {p["idea"]} | [📁](./{p["path"]}) |')
        blocks.append("\n".join([
            f'<a id="{cid}"></a>',
            f"<details{' open' if first else ''}>",
            f'<summary><b>{c["emoji"]} {c["name"]} ({n})</b></summary>',
            "<br/>",
            "",
            *rows,
            "",
            "</details>",
        ]))
        first = False
    return "\n\n".join(blocks)


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #
def main() -> None:
    meta = json.loads(META_FILE.read_text(encoding="utf-8"))
    cats = OrderedDict((c["id"], c) for c in meta["categories"])
    known = meta["problems"]
    rules = meta.get("keyword_rules", [])

    today = date.today()
    problems: list[dict] = []
    for folder in find_solution_dirs(ROOT):
        rel = folder.relative_to(ROOT).as_posix()
        slug = folder.name
        info = known.get(rel) or known.get(slug) or {}
        is_new = not info
        category = info.get("category") or ("papers" if "/" in rel else guess_category(slug, rules))
        if category not in cats:
            category = "new"
        url = info.get("url") or (RESEARCH_URL.format(path=rel) if "/" in rel else PROBLEM_URL.format(slug=slug))
        added = first_added_date(rel)
        problems.append({
            "path": rel,
            "title": info.get("title") or title_from_folder(folder, slug),
            "idea": info.get("idea", "—"),
            "category": category,
            "cat_label": f'{cats[category]["emoji"]} {cats[category]["short"]}',
            "url": url,
            "added": added,
            "weight": int(info.get("count", 1)),
            "is_new": is_new or (today - added).days <= 7,
        })

    total = sum(p["weight"] for p in problems)
    counts: "OrderedDict[str, int]" = OrderedDict((cid, 0) for cid in cats)
    for p in problems:
        counts[p["category"]] += p["weight"]
    topics = sum(1 for cid, n in counts.items() if n and cid != "new")
    last7 = sum(p["weight"] for p in problems if (today - p["added"]).days < 7)
    last30 = sum(p["weight"] for p in problems if (today - p["added"]).days < 30)

    values = {
        "TOTAL": str(total),
        "TOPICS": str(topics),
        "LAST_7_DAYS": str(last7),
        "LAST_30_DAYS": str(last30),
        "LAST_UPDATED": datetime.now(timezone.utc).strftime("%Y-%m-%d"),
        "PIE_CHART": render_pie(counts, cats),
        "TOPIC_TABLE": render_topic_table(counts, cats, total),
        "RECENT_TABLE": render_recent(problems),
        "GROWTH_CHART": render_growth(problems),
        "SOLUTIONS": render_solutions(problems, cats, list(cats)),
    }

    text = TEMPLATE_FILE.read_text(encoding="utf-8")
    for key, val in values.items():
        text = text.replace("{{" + key + "}}", val)
    leftover = re.findall(r"\{\{[A-Z_0-9]+\}\}", text)
    if leftover:
        print(f"Warning: unknown placeholders left in template: {sorted(set(leftover))}")

    OUTPUT_FILE.write_text(text, encoding="utf-8")
    uncategorized = [p["path"] for p in problems if p["category"] == "new"]
    print(f"README updated: {total} problems, {topics} topics, {last7} in the last 7 days.")
    if uncategorized:
        print("Uncategorized (add them to scripts/problems.json):", ", ".join(uncategorized))


if __name__ == "__main__":
    main()
