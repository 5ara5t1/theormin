---
title: Problem log
description: Pointer to where the problem log lives.
---

# Problem log

Problems are recorded in the `## Problems worked` table inside each week's file in [`01-weeks/`](../01-weeks/). The current week is [[week-01]].

The aggregate count and per-subject breakdown live on the public dashboard ([README.md](../../README.md)) and are regenerated each push from `data/problems.csv` (which `scripts/extract_from_vault.py` builds by parsing the weekly tables).

This page is intentionally short. The data has one home: the week file. Dataview can't query arbitrary markdown tables, so the per-problem view is the week file itself.

## Notable problem write-ups

For the rare problems that warrant a dedicated note (technique-introducing, got stuck, want to remember), see [`04-problems/`](../04-problems/):

```dataview
TABLE WITHOUT ID
  file.link as Problem,
  book as Book,
  problem_ref as Ref,
  subject as Subject,
  date as Date,
  status as Status
FROM "04-problems"
WHERE type = "problem"
SORT date DESC
```
