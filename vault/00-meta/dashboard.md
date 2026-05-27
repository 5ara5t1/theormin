---
title: Dashboard
description: Internal Obsidian dashboard — live Dataview queries over the vault. The public-facing dashboard is README.md at repo root.
---

# Dashboard

This is the internal view. For the polished public dashboard see [README.md](../../README.md) at the repo root.

> [!note] Dataview required
> The queries below use the [Dataview](https://github.com/blacksmithgu/obsidian-dataview) community plugin. Install it from Settings → Community plugins → Browse → "Dataview".

## Current week plan

![[week-01]]

## Recent sessions

```dataview
TABLE WITHOUT ID
  date as Date,
  subject as Subject,
  hours as Hours,
  activity as Activity
FROM ""
WHERE type = "session"
SORT date DESC
LIMIT 10
```

## Problems worked, by subject

```dataview
TABLE WITHOUT ID
  subject as Subject,
  length(rows) as Problems,
  sum(rows.minutes) as "Total minutes"
FROM ""
WHERE type = "problem"
GROUP BY subject
SORT length(rows) DESC
```

## Last 7 days

```dataview
TABLE WITHOUT ID
  date as Date,
  problem_ref as Problem,
  book as Book,
  status as Status,
  minutes as Min
FROM ""
WHERE type = "problem"
  AND date >= date(today) - dur(7 days)
SORT date DESC
```

## Theorems reproduced from memory

```dataview
TABLE WITHOUT ID
  date as Date,
  theorem as Theorem,
  result as Result,
  time_minutes as "Time (min)"
FROM ""
WHERE type = "theorem"
SORT date DESC
```

## Chapter summaries (recent)

```dataview
TABLE WITHOUT ID
  file.link as Note,
  book as Book,
  chapter as Ch,
  date_completed as Completed,
  hours as Hrs
FROM "02-summaries"
WHERE date_completed
SORT date_completed DESC
LIMIT 10
```

## In progress

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
