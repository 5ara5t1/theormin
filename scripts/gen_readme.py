#!/usr/bin/env python3
"""Regenerate README.md dashboards from data/*.csv and data/*.yaml.

Replaces content between marker comments of the form:
    <!-- BEGIN auto:KEY -->
    ...anything...
    <!-- END auto:KEY -->

so the hand-written narrative outside the markers is preserved.
"""
from __future__ import annotations

import csv
import datetime as dt
import re
import sys
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
VAULT = ROOT / "vault"
README = ROOT / "README.md"
BAR_WIDTH = 20


# ---------- data loading ----------


def load_config() -> dict:
    return yaml.safe_load((DATA / "config.yaml").read_text())


def load_books() -> list[dict]:
    return yaml.safe_load((DATA / "books.yaml").read_text())["books"]


def load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def apply_auto_chapters_done(books: list[dict], summaries: list[dict]) -> list[dict]:
    """Override chapters_done in books from the count of completed chapter summaries.

    The number in data/books.yaml becomes a fallback for books without any
    summary entries yet. Anything with at least one summary row whose status
    is 'completed' gets its chapters_done recomputed from the vault.
    """
    counts: dict[str, int] = defaultdict(int)
    seen_books: set[str] = set()
    for s in summaries:
        book = (s.get("book") or "").strip()
        if not book:
            continue
        seen_books.add(book)
        status = (s.get("status") or "").strip().lower()
        if status == "completed":
            counts[book] += 1
    for b in books:
        if b["id"] in seen_books:
            b["chapters_done"] = counts.get(b["id"], 0)
            # If the book had no chapters done before but has at least one summary
            # in progress, flip status to in_progress.
            if b["chapters_done"] > 0 and b.get("status") == "not_started":
                b["status"] = "in_progress"
    return books


# ---------- formatting helpers ----------


def bar(value: float, total: float, width: int = BAR_WIDTH) -> str:
    if total <= 0:
        return "░" * width
    frac = max(0.0, min(1.0, value / total))
    filled = round(frac * width)
    return "▓" * filled + "░" * (width - filled)


def pct(value: float, total: float) -> str:
    if total <= 0:
        return "0.0%"
    return f"{100.0 * value / total:.1f}%"


# ---------- sections ----------


def status_phase(books: list[dict]) -> tuple[int, list[str]]:
    """Identify the active phase (the lowest phase with any in_progress book)."""
    by_phase = defaultdict(list)
    for b in books:
        by_phase[b["phase"]].append(b)
    for phase in sorted(by_phase):
        if any(b["status"] == "in_progress" for b in by_phase[phase]):
            in_prog = [
                f"{b['author']} *{b['title']}*"
                for b in by_phase[phase]
                if b["status"] == "in_progress"
            ]
            return phase, in_prog
    return 1, []


def week_number(start_date: dt.date, today: dt.date) -> int:
    delta_days = (today - start_date).days
    return max(1, delta_days // 7 + 1)


def section_headline(cfg, books, problems, sessions, today) -> str:
    total_problems = len(problems)
    target = sum(cfg["problem_targets"].values())
    total_hours = sum(float(s["hours"]) for s in sessions if s.get("hours"))
    phase, _ = status_phase(books)
    start = dt.date.fromisoformat(str(cfg["start_date"]))
    week = week_number(start, today)
    return (
        f"**Phase {phase} · Week {week} · "
        f"{total_problems:,} / {target:,} problems · "
        f"{total_hours:,.0f} hrs logged · "
        f"started {start.isoformat()}**"
    )


def section_status(cfg, books, problems, sessions, theorems, today) -> str:
    phase, in_prog = status_phase(books)
    start = dt.date.fromisoformat(str(cfg["start_date"]))
    week = week_number(start, today)
    last_theorem = theorems[-1]["theorem"] if theorems else "—"
    last_derivation = "—"  # populated later when derivations get logged
    weeks_done = max(0, (today - start).days // 7)
    if weeks_done < 4:
        eta = "computing… (needs ≥4 weeks of data)"
    else:
        total_problems = len(problems)
        target = sum(cfg["problem_targets"].values())
        rate_per_week = total_problems / weeks_done if weeks_done else 0
        if rate_per_week > 0:
            weeks_left = (target - total_problems) / rate_per_week
            done_date = today + dt.timedelta(days=int(weeks_left * 7))
            eta = f"~{done_date.year} (at current pace of {rate_per_week:.1f} problems/week)"
        else:
            eta = "indeterminate — no recent problems"
    rows = [
        ("Active phase", f"Phase {phase}"),
        ("Current week", f"Week {week} ({today.isoformat()})"),
        ("Books in progress", ", ".join(in_prog) or "—"),
        ("Last theorem reproved", last_theorem),
        ("Last derivation logged", last_derivation),
        ("Estimated baseline completion", eta),
    ]
    out = ["| | |", "|---|---|"]
    for k, v in rows:
        out.append(f"| {k} | {v} |")
    return "\n".join(out)


def section_phases(cfg, books) -> str:
    by_phase = defaultdict(lambda: [0, 0])  # done, total
    for b in books:
        by_phase[b["phase"]][1] += b.get("chapters_total", 0) or 0
        by_phase[b["phase"]][0] += b.get("chapters_done", 0) or 0
    labels = {
        1: "Mathematical foundation",
        2: "Classical mechanics + fields",
        3: "Quantum mechanics",
        4: "QED + stat phys + fluids",
        5: "Continuous media + kinetics",
        6: "Modern QFT + GR + EFT + CMT",
    }
    lines = ["```"]
    for phase in sorted(labels):
        done, total = by_phase.get(phase, [0, 0])
        # Use cfg phase_chapter_totals as fallback to avoid 0/0
        ptot = cfg.get("phase_chapter_totals", {}).get(phase, total) or total or 1
        b = bar(done, ptot)
        label = f"Phase {phase} — {labels[phase]}"
        lines.append(f"{label:<42}{b}  {pct(done, ptot):>5}")
    lines.append("```")
    return "\n".join(lines)


def section_checkpoints(cfg, books, problems) -> str:
    problems_by_subject = defaultdict(int)
    for p in problems:
        if p.get("subject"):
            problems_by_subject[p["subject"]] += 1
    book_status = {b["id"]: b["status"] for b in books}
    lines = ["| # | Domain | Status |", "|---|--------|--------|"]
    for cp in cfg["checkpoints"]:
        statuses = [book_status.get(bid, "not_started") for bid in cp["requires_books"]]
        if all(s == "completed" for s in statuses):
            mark = "✅ passed"
        elif any(s in ("in_progress", "completed") for s in statuses):
            mark = "🟡 in progress"
        else:
            mark = "⬜ not started"
        lines.append(f"| {cp['id']} | {cp['name']} | {mark} |")
    return "\n".join(lines)


def section_subjects(cfg, problems) -> str:
    counts = defaultdict(int)
    for p in problems:
        if p.get("subject"):
            counts[p["subject"]] += 1
    display = [
        ("Real analysis", "real_analysis"),
        ("Linear algebra", "linear_algebra"),
        ("ODE", "ode"),
        ("Complex analysis", "complex_analysis"),
        ("Calc of variations", "calc_of_variations"),
        ("PDE / math methods", "pde"),
        ("Functional analysis", "functional_analysis"),
        ("General physics", "general_physics"),
        ("Mechanics (L1)", "mechanics"),
        ("Classical fields (L2)", "classical_fields"),
        ("Quantum mechanics (L3)", "quantum_mechanics"),
        ("QED / QFT", "qft"),
    ]
    lines = ["```"]
    for label, key in display:
        c = counts.get(key, 0)
        tgt = cfg["problem_targets"].get(key, 0)
        b = bar(c, tgt)
        lines.append(f"{label:<24}{c:>5,} / {tgt:<5,} {b}")
    lines.append("```")
    return "\n".join(lines)


def section_daily_log(sessions: list[dict], today: dt.date, limit: int = 10) -> str:
    """Render the most recent `limit` calendar days with sessions, grouped by date.

    Days with no sessions are skipped. The activity heatmap is the place to see
    silent gaps — this section is the chronological diary of what got worked on.
    """
    by_date = defaultdict(list)
    for s in sessions:
        try:
            d = dt.date.fromisoformat(s["date"])
        except (ValueError, KeyError, TypeError):
            continue
        by_date[d].append(s)
    if not by_date:
        return "_No sessions logged yet. Add rows to `## Sessions` in `vault/01-weeks/week-XX.md`._"
    dates = sorted(by_date.keys(), reverse=True)[:limit]
    lines = []
    for d in dates:
        day_sessions = by_date[d]
        total = sum(float(s.get("hours") or 0) for s in day_sessions)
        lines.append(f"**{d.strftime('%a')} {d.isoformat()} — {total:g}h**")
        for s in day_sessions:
            subj = s.get("subject") or "—"
            act = s.get("activity") or "—"
            hrs = s.get("hours") or "0"
            lines.append(f"- {hrs}h *{subj}* — {act}")
        lines.append("")
    return "\n".join(lines).strip()


def section_recent(books, problems, theorems) -> str:
    items = []
    for t in theorems[-5:][::-1]:
        items.append(f"- **Theorem:** {t['theorem']} — *{t['result']}* ({t['date']})")
    if not items:
        return "_Nothing logged yet. Activity will appear here after Week 1 entries land._"
    return "\n".join(items)


def section_todo() -> str:
    """Pull unchecked items from vault/00-meta/todo.md, grouped by ## subheading."""
    path = VAULT / "00-meta" / "todo.md"
    if not path.exists():
        return "_No todo file yet. Create `vault/00-meta/todo.md` with `- [ ]` items._"
    text = path.read_text()
    # Skip frontmatter
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end > 0:
            text = text[end + 4:]
    sections: list[tuple[str, list[str]]] = []
    current = None
    items: list[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        # ## subheading marks a new section. Skip h1 (#) and h3+ (###).
        if re.match(r"^##\s+", stripped) and not stripped.startswith("###"):
            if current is not None and items:
                sections.append((current, items))
            current = stripped.lstrip("#").strip()
            items = []
            continue
        m = re.match(r"^\s*-\s*\[\s*\]\s*(.+)$", line)
        if m and current is not None:
            items.append(m.group(1).strip())
    if current is not None and items:
        sections.append((current, items))
    # Drop a "Done" section if it somehow has unchecked items (shouldn't happen).
    sections = [(h, it) for h, it in sections if h.lower() != "done"]
    if not sections:
        return "_No open items. Add some to `vault/00-meta/todo.md`._"
    out = []
    for heading, todos in sections:
        out.append(f"**{heading}**\n")
        for t in todos:
            out.append(f"- [ ] {t}")
        out.append("")
    return "\n".join(out).strip()


def section_shelf(books) -> str:
    lines = ["| Book | Status | Progress |", "|------|--------|----------|"]
    # Only show in_progress and completed; cap at 12 rows for legibility
    relevant = [b for b in books if b["status"] in ("in_progress", "completed")]
    not_started = [b for b in books if b["status"] == "not_started"][:6]
    for b in relevant + not_started:
        title = f"{b['author']}, *{b['title']}*"
        if b["status"] == "in_progress":
            status = "in progress"
            if b.get("chapters_total"):
                prog = f"{b.get('chapters_done', 0)} / {b['chapters_total']} chapters"
            elif b.get("problems_target"):
                prog = f"0 / {b['problems_target']} target problems"
            else:
                prog = "—"
        elif b["status"] == "completed":
            status = "completed"
            prog = "✅"
        else:
            status = "not started"
            prog = "—"
        lines.append(f"| {title} | {status} | {prog} |")
    return "\n".join(lines)


# ---------- marker replacement ----------


def replace_marker(content: str, key: str, new_body: str) -> str:
    """Replace content between <!-- BEGIN auto:KEY --> and <!-- END auto:KEY -->.

    Handles both inline and block forms. If new_body has no newlines, output stays
    inline; otherwise it's reflowed as a block.
    """
    pattern = re.compile(
        rf"<!-- BEGIN auto:{re.escape(key)} -->(.*?)<!-- END auto:{re.escape(key)} -->",
        re.DOTALL,
    )
    if not pattern.search(content):
        sys.stderr.write(f"warning: marker auto:{key} not found in README\n")
        return content
    if "\n" in new_body:
        replacement = (
            f"<!-- BEGIN auto:{key} -->\n{new_body}\n<!-- END auto:{key} -->"
        )
    else:
        replacement = f"<!-- BEGIN auto:{key} -->{new_body}<!-- END auto:{key} -->"
    return pattern.sub(lambda _m: replacement, content, count=1)


def main() -> int:
    cfg = load_config()
    books = load_books()
    problems = load_csv(DATA / "problems.csv")
    sessions = load_csv(DATA / "sessions.csv")
    theorems = load_csv(DATA / "theorems.csv")
    summaries = load_csv(DATA / "summaries.csv")
    books = apply_auto_chapters_done(books, summaries)
    today = dt.date.today()

    content = README.read_text()
    replacements = {
        "headline": section_headline(cfg, books, problems, sessions, today),
        "status": section_status(cfg, books, problems, sessions, theorems, today),
        "todo": section_todo(),
        "phases": section_phases(cfg, books),
        "checkpoints": section_checkpoints(cfg, books, problems),
        "subjects": section_subjects(cfg, problems),
        "daily_log": section_daily_log(sessions, today),
        "recent": section_recent(books, problems, theorems),
        "shelf": section_shelf(books),
        "timestamp": today.isoformat(),
    }
    for key, body in replacements.items():
        content = replace_marker(content, key, body)
    README.write_text(content)
    print(f"README regenerated at {today.isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
