---
title: Dashboard
description: Internal Obsidian dashboard. The public dashboard is README.md at the repo root.
---

# Dashboard

The public dashboard is [README.md](../../README.md) at the repo root. It's regenerated from the vault on every push.

For the live view inside Obsidian, the canonical place to look is **this week's file** in [01-weeks/](../01-weeks/). The Sessions and Problems tables there are the day-to-day record.

## This week

![[week-01]]

## Chapter summaries in progress

```dataview
TABLE WITHOUT ID
  file.link as Chapter,
  book as Book,
  date_started as Started,
  hours as "Hrs so far"
FROM "02-summaries"
WHERE status = "in_progress"
SORT date_started DESC
```

## Chapter summaries completed

```dataview
TABLE WITHOUT ID
  file.link as Chapter,
  book as Book,
  date_completed as Completed,
  hours as Hrs
FROM "02-summaries"
WHERE status = "completed"
SORT date_completed DESC
LIMIT 15
```

## Theorems reproved

```dataview
TABLE WITHOUT ID
  date as Date,
  theorem as Theorem,
  result as Result,
  time_minutes as "Time (min)"
FROM "03-theorems"
WHERE type = "theorem"
SORT date DESC
```

## Checkpoints

```dataview
TABLE WITHOUT ID
  id as "#",
  domain as Domain,
  status as Status,
  attempt_date as "Last attempt"
FROM "06-checkpoints"
WHERE type = "checkpoint"
SORT id ASC
```

> [!note] Sessions and problems are in week files
> Sessions and problems are recorded as markdown tables inside each week's file in `01-weeks/`. They aren't surfaced here as Dataview queries — Dataview doesn't parse arbitrary tables. For the live counts, run `./scripts/refresh.sh` at the repo root and look at the README, or just scroll the current week file.
