---
title: Problem log
description: Live list of every problem worked, pulled from frontmatter across the vault.
---

# Problem log

Every problem with `type: problem` frontmatter shows up here.

```dataview
TABLE WITHOUT ID
  date as Date,
  file.link as Note,
  book as Book,
  chapter as Ch,
  problem_ref as Ref,
  subject as Subject,
  minutes as Min,
  status as Status
FROM ""
WHERE type = "problem"
SORT date DESC, problem_ref DESC
```

## Running totals

```dataview
TABLE WITHOUT ID
  length(rows) as "Problems",
  sum(rows.minutes) as "Total min",
  round(sum(rows.minutes) / length(rows), 1) as "Avg min/problem"
FROM ""
WHERE type = "problem"
GROUP BY true
```

## By book

```dataview
TABLE WITHOUT ID
  book as Book,
  length(rows) as Problems
FROM ""
WHERE type = "problem"
GROUP BY book
SORT length(rows) DESC
```
