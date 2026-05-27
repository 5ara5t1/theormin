#!/usr/bin/env python3
"""Render SVG charts to images/ from data/sessions.csv and data/problems.csv.

Outputs:
  - images/heatmap.svg     (year-long calendar heatmap of hours/day)
  - images/sparklines.svg  (weekly hours + problems, last 12 weeks)
"""
from __future__ import annotations

import csv
import datetime as dt
import sys
from collections import defaultdict
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import yaml
from matplotlib.patches import Rectangle

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
IMAGES = ROOT / "images"
IMAGES.mkdir(exist_ok=True)


def load_config() -> dict:
    return yaml.safe_load((DATA / "config.yaml").read_text())


def load_csv(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open() as f:
        return list(csv.DictReader(f))


def heatmap_year(sessions, start_date: dt.date, today: dt.date, out: Path):
    """GitHub-style heatmap of hours/day spanning the past 53 weeks."""
    hours_by_day = defaultdict(float)
    for s in sessions:
        try:
            d = dt.date.fromisoformat(s["date"])
            hours_by_day[d] += float(s["hours"])
        except (ValueError, KeyError):
            continue

    # Align to weeks: 53 columns x 7 rows
    end = today
    start = end - dt.timedelta(days=53 * 7 - 1)
    # Start from a Sunday for visual alignment
    start -= dt.timedelta(days=(start.weekday() + 1) % 7)

    fig, ax = plt.subplots(figsize=(11, 2.0))
    cell = 0.9
    gap = 0.1

    max_hours = max(hours_by_day.values(), default=0) or 1.0

    days = []
    d = start
    while d <= end:
        days.append(d)
        d += dt.timedelta(days=1)

    for i, d in enumerate(days):
        week_col = i // 7
        day_row = 6 - (i % 7)  # invert so Sunday at top
        h = hours_by_day.get(d, 0.0)
        if h <= 0:
            color = "#ebedf0"
        else:
            intensity = min(1.0, h / max(max_hours, 4.0))
            # green scale a la GitHub
            r = int(155 - intensity * 100)
            g = int(233 - intensity * 100)
            b = int(168 - intensity * 80)
            color = f"#{r:02x}{g:02x}{b:02x}"
        ax.add_patch(Rectangle(
            (week_col, day_row), cell, cell,
            facecolor=color, edgecolor="none",
        ))

    ax.set_xlim(-0.5, (len(days) // 7) + 1)
    ax.set_ylim(-0.5, 7.5)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title(f"Hours per day, last 53 weeks (max {max_hours:.1f}h)",
                 fontsize=10, loc="left", pad=8)
    fig.tight_layout()
    fig.savefig(out, format="svg", bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close(fig)


def sparklines(sessions, problems, today: dt.date, out: Path):
    """Last 12 weeks: hours and problems per week."""
    weeks = [today - dt.timedelta(days=(today.weekday() + 1) + 7 * w) for w in range(12)][::-1]
    week_starts = [(w - dt.timedelta(days=(w.weekday() + 1) % 7)) for w in weeks]

    hours_per_week = []
    problems_per_week = []

    for ws in week_starts:
        we = ws + dt.timedelta(days=6)
        hours = sum(
            float(s["hours"]) for s in sessions
            if s.get("date") and ws <= dt.date.fromisoformat(s["date"]) <= we
        )
        probs = sum(
            1 for p in problems
            if p.get("date") and ws <= dt.date.fromisoformat(p["date"]) <= we
        )
        hours_per_week.append(hours)
        problems_per_week.append(probs)

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(11, 3.5), sharex=True)

    ax1.bar(range(12), hours_per_week, color="#3b82f6", width=0.7)
    ax1.set_ylabel("hours / week", fontsize=9)
    ax1.set_title("Last 12 weeks", fontsize=10, loc="left", pad=4)
    ax1.spines[["top", "right"]].set_visible(False)
    ax1.grid(axis="y", linestyle=":", alpha=0.4)

    ax2.bar(range(12), problems_per_week, color="#10b981", width=0.7)
    ax2.set_ylabel("problems / week", fontsize=9)
    ax2.set_xticks(range(12))
    ax2.set_xticklabels([ws.strftime("%-m/%-d") for ws in week_starts],
                        fontsize=8, rotation=0)
    ax2.spines[["top", "right"]].set_visible(False)
    ax2.grid(axis="y", linestyle=":", alpha=0.4)

    fig.tight_layout()
    fig.savefig(out, format="svg", bbox_inches="tight",
                facecolor="white", transparent=False)
    plt.close(fig)


def main() -> int:
    cfg = load_config()
    sessions = load_csv(DATA / "sessions.csv")
    problems = load_csv(DATA / "problems.csv")
    today = dt.date.today()
    start = dt.date.fromisoformat(str(cfg["start_date"]))

    heatmap_year(sessions, start, today, IMAGES / "heatmap.svg")
    sparklines(sessions, problems, today, IMAGES / "sparklines.svg")
    print(f"Charts regenerated at {today.isoformat()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
