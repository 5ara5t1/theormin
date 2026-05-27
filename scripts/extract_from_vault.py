#!/usr/bin/env python3
"""Walk the Obsidian vault, parse YAML frontmatter from .md files, and update
data/problems.csv, data/sessions.csv, data/theorems.csv accordingly.

This lets you log everything inside Obsidian (with templates) and have the CSV
data sources stay in sync. Idempotent — overwrites the CSVs each run from the
source of truth in the vault.

Frontmatter conventions:

  04-problems/foo.md:
    type: problem
    book: tao-analysis-1
    chapter: 2
    problem_ref: "2.2.1"
    subject: real_analysis
    phase: 1
    date: 2026-05-28
    minutes: 18
    status: solved

  03-theorems/foo.md:
    type: theorem
    theorem: "Commutativity of addition on N"
    book: tao-analysis-1
    date: 2026-05-30
    result: passed
    time_minutes: 12

  01-weeks/week-XX.md or 02-summaries/<book>/<chapter>.md:
    type: session
    date: 2026-05-26
    hours: 4.0
    subject: real_analysis
    activity: "Tao Ch. 1 read"
"""
from __future__ import annotations

import csv
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


def walk_vault() -> tuple[list[dict], list[dict], list[dict]]:
    problems, sessions, theorems = [], [], []
    if not VAULT.exists():
        return problems, sessions, theorems
    for md in VAULT.rglob("*.md"):
        # Skip files starting with underscore — these are examples / scratch / not real data.
        if md.name.startswith("_"):
            continue
        try:
            text = md.read_text()
        except Exception:
            continue
        fm = parse_frontmatter(text)
        if not fm or "type" not in fm:
            continue
        t = fm["type"]
        if t == "problem":
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
                "notes_path": str(md.relative_to(ROOT)),
            })
        elif t == "session":
            sessions.append({
                "date": fm.get("date", ""),
                "hours": fm.get("hours", ""),
                "subject": fm.get("subject", ""),
                "activity": fm.get("activity", ""),
                "notes": str(md.relative_to(ROOT)),
            })
        elif t == "theorem":
            theorems.append({
                "date": fm.get("date", ""),
                "theorem": fm.get("theorem", ""),
                "book": fm.get("book", ""),
                "result": fm.get("result", ""),
                "time_minutes": fm.get("time_minutes", ""),
                "notes_path": str(md.relative_to(ROOT)),
            })
    return problems, sessions, theorems


def write_csv(path: Path, rows: list[dict], cols: list[str]) -> None:
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=cols)
        writer.writeheader()
        for r in rows:
            writer.writerow({c: r.get(c, "") for c in cols})


def main() -> int:
    problems, sessions, theorems = walk_vault()
    problems.sort(key=lambda r: (r.get("date") or "", r.get("id") or ""))
    sessions.sort(key=lambda r: r.get("date") or "")
    theorems.sort(key=lambda r: r.get("date") or "")
    write_csv(
        DATA / "problems.csv", problems,
        ["id", "date", "book", "chapter", "problem_ref",
         "subject", "phase", "minutes", "status", "notes_path"],
    )
    write_csv(
        DATA / "sessions.csv", sessions,
        ["date", "hours", "subject", "activity", "notes"],
    )
    write_csv(
        DATA / "theorems.csv", theorems,
        ["date", "theorem", "book", "result", "time_minutes", "notes_path"],
    )
    print(f"Vault extracted: "
          f"{len(problems)} problems, {len(sessions)} sessions, {len(theorems)} theorems")
    return 0


if __name__ == "__main__":
    sys.exit(main())
