# Problems

One note per worked problem, with frontmatter so it gets pulled into the running count.

## Convention

- Subfolder per book: `demidovich/`, `irodov/`, `galitski/`, `tao/`, `strang/`, etc.
- Filename: book-id + reference: `demidovich/d-0001.md`, `tao/t-2-2-3.md`, `irodov/i-1-001.md`.
- Use the template at [`../templates/problem.md`](../templates/problem.md) — Templater can drop it in for you.

## Frontmatter spec

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

## Body convention

- **Statement** (paraphrased — copyright)
- **Approach** (one paragraph, the strategy you used)
- **Solution** (the math, terse but complete)
- **What was hard** (one sentence)
- **What this is connected to** (wikilinks to chapter summaries, related problems, theorems used)

Status meaning:
- **solved** — got the right answer, full understanding
- **partial** — got something but missed the cleanest path
- **stuck** — couldn't solve; come back later
- **revisit** — solved but flagged for second pass (felt fragile)
