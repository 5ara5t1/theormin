#!/usr/bin/env python3
"""Walk the Obsidian vault, parse YAML frontmatter and weekly tables, write
data/problems.csv, data/sessions.csv, data/theorems.csv.

Two sources of data:

1. **Per-note frontmatter** (kept for theorems and chapter summaries; optional for
   notable problem write-ups under 04-problems/).

2. **Weekly tables** inside files with `type: week` frontmatter. Sessions and
   problems are rows in markdown tables under `## Sessions` and `## Problems
   worked` headings. This is the primary data source for the day-to-day flow.

Files starting with `_` are skipped (examples / scratch).

Markdown-table conventions:

  ## Sessions
  | Date       | Hours | Subject       | Activity                   |
  |------------|-------|---------------|----------------------------|
  | 2026-05-26 | 0.5   | meta          | Repo + vault setup         |

  ## Problems worked
  | Date       | Book           | Ref   | Subject       | Min | Status | Note |
  |------------|----------------|-------|---------------|-----|--------|------|
  | 2026-05-27 | tao-analysis-1 | 2.2.1 | real_analysis | 8   | solved |      |

Header rows are detected by the literal column names "Date", "Hours", etc.
Separator rows (|---|---|) are detected and skipped.
"""
from __future__ import annotations

import csv
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
VAULT = ROOT / "vault"
DATA = ROOT / "data"


def parse_frontmatter(text: str) -> dict | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end < 0:
        return None
    raw = text[4:end]
    try:
        return yaml.safe_load(raw) or {}
    except yaml.YAMLError:
        return None


def split_row(line: str) -> list[str]:
    line = line.strip()
    if not line.startswith("|"):
        return []
    return [c.strip() for c in line.strip("|").split("|")]


def is_separator(cells: list[str]) -> bool:
    return bool(cells) and all(re.fullmatch(r":?-+:?", c or "") for c in cells if c != "")


def is_header(cells: list[str], expected_first: str) -> bool:
    return bool(cells) and cells[0].lower() == expected_first.lower()


def parse_week_tables(text: str, source_path: str) -> tuple[list[dict], list[dict]]:
    """Return (sessions, problems) parsed from ## Sessions and ## Problems worked tables."""
    sessions: list[dict] = []
    problems: list[dict] = []
    in_sessions = False
    in_problems = False
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^##\s+Sessions\b", stripped, re.IGNORECASE):
            in_sessions, in_problems = True, False
            continue
        if re.match(r"^##\s+Problems(\s+worked)?\b", stripped, re.IGNORECASE):
            in_sessions, in_problems = False, True
            continue
        if stripped.startswith("##"):
            in_sessions, in_problems = False, False
            continue
        if not (in_sessions or in_problems):
            continue
        if not stripped.startswith("|"):
            continue
        cells = split_row(stripped)
        if is_separator(cells):
            continue
        if in_sessions:
            if is_header(cells, "Date"):
                continue
            if len(cells) < 4:
                continue
            date, hours, subject, activity = cells[:4]
            if not date:
                continue
            sessions.append({
                "date": date,
                "hours": hours,
                "subject": subject,
                "activity": activity,
                "notes": source_path,
            })
        elif in_problems:
            if is_header(cells, "Date"):
                continue
            if len(cells) < 6:
                continue
            date, book, ref, subject, minutes, status = cells[:6]
            if not date:
                continue
            problems.append({
                "id": f"{book}-{ref.replace('.', '-')}".strip("-"),
                "date": date,
                "book": book,
                "chapter": ref.split(".")[0] if ref else "",
                "problem_ref": ref,
                "subject": subject,
                "phase": "",
                "minutes": minutes,
                "status": status,
                "notes_path": source_path,
            })
    return sessions, problems


def walk_vault() -> tuple[list[dict], list[dict], list[dict], list[dict]]:
    problems: list[dict] = []
    sessions: list[dict] = []
    theorems: list[dict] = []
    summaries: list[dict] = []
    if not VAULT.exists():
        return problems, sessions, theorems, summaries

    for md in VAULT.rglob("*.md"):
        if md.name.startswith("_"):
            continue
        try:
            text = md.read_text()
        except Exception:
            continue
        fm = parse_frontmatter(text)
        rel_path = str(md.relative_to(ROOT))
        if not fm:
            continue
        kind = fm.get("type")

        if kind == "week":
            w_sessions, w_problems = parse_week_tables(text, rel_path)
            sessions.extend(w_sessions)
            problems.extend(w_problems)
            continue

        if kind == "problem":
            problems.append({
                "id": fm.get("id", md.stem),
                "date": fm.get("date", ""),
                "book": fm.get("book", ""),
                "chapter": fm.get("chapter", ""),
                "problem_ref": fm.get("problem_ref", ""),
                "subject": fm.get("subject", ""),
                "phase": fm.get("phase", ""),
                "minutes": fm.get("minutes", ""),
                "status": fm.get("status", ""),
                "notes_path": rel_path,
            })
            continue

        if kind == "session":
            sessions.append({
                "date": fm.get("date", ""),
                "hours": fm.get("hours", ""),
                "subject": fm.get("subject", ""),
                "activity": fm.get("activity", ""),
                "notes": rel_path,
            })
            continue

        if kind == "theorem":
            theorems.append({
                "date": fm.get("date", ""),
                "theorem": fm.get("theorem", ""),
                "book": fm.get("book", ""),
                "result": fm.get("result", ""),
                "time_minutes": fm.get("time_minutes", ""),
                "notes_path": rel_path,
            })
            continue

        if kind == "summary":
            summaries.append({
                "book": fm.get("book", ""),
                "chapter": fm.get("chapter", ""),
                "status": fm.get("status", ""),
                "date_started": fm.get("date_started", ""),
                "date_completed": fm.get("date_completed", ""),
                "hours": fm.get("hours", ""),
                "problems_worked": fm.get("problems_worked", ""),
                "notes_path": rel_path,
            })
            continue

    return problems, sessions, theorems, summaries


def write_csv(path: Path, rows: list[dict], cols: list[str]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for r in rows:
            writer.writerow({c: r.get(c, "") for c in cols})


def main() -> int:
    problems, sessions, theorems, summaries = walk_vault()
    problems.sort(key=lambda r: (r.get("date") or "", r.get("id") or ""))
    sessions.sort(key=lambda r: (r.get("date") or "", r.get("activity") or ""))
    theorems.sort(key=lambda r: r.get("date") or "")
    summaries.sort(key=lambda r: (r.get("book") or "", str(r.get("chapter") or "")))
    write_csv(
        DATA / "problems.csv", problems,
        ["id", "date", "book", "chapter", "problem_ref", "subject",
         "phase", "minutes", "status", "notes_path"],
    )
    write_csv(
        DATA / "sessions.csv", sessions,
        ["date", "hours", "subject", "activity", "notes"],
    )
    write_csv(
        DATA / "theorems.csv", theorems,
        ["date", "theorem", "book", "result", "time_minutes", "notes_path"],
    )
    write_csv(
        DATA / "summaries.csv", summaries,
        ["book", "chapter", "status", "date_started", "date_completed",
         "hours", "problems_worked", "notes_path"],
    )
    print(f"Vault extracted: "
          f"{len(problems)} problems, {len(sessions)} sessions, "
          f"{len(theorems)} theorems, {len(summaries)} summaries")
    return 0


if __name__ == "__main__":
    sys.exit(main())
