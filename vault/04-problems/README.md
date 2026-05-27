# Problems

One note per worked problem. Frontmatter feeds the running count.

## Convention

- Subfolder per book: `demidovich/`, `irodov/`, `galitski/`, `tao/`, `strang/`, etc.
- Filename: book-id + reference (`demidovich/d-0001.md`, `tao/t-2-2-3.md`).
- Use the template at [`../templates/problem.md`](../templates/problem.md).

## Frontmatter

```yaml
---
type: problem
id: tao-2-2-3                # globally unique
book: tao-analysis-1          # matches data/books.yaml id
chapter: 2
problem_ref: "2.2.3"
subject: real_analysis        # one of the keys in data/config.yaml
phase: 1
date: 2026-05-28
minutes: 18
status: solved                # solved | partial | stuck | revisit
tags: [phase-1, analysis, induction]
---
```

## Body

- Statement (paraphrased)
- Approach
- Solution
- What was hard
- Connections (wikilinks to chapter summaries, related problems, theorems used)

## Status values

- `solved` — correct answer, understood
- `partial` — got something, missed the cleanest path
- `stuck` — couldn't solve, come back
- `revisit` — solved but flagged for a second pass
