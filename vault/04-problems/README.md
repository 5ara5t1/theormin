# Problems

Problems are tracked **per-week** in the `## Problems worked` table inside each `01-weeks/week-XX.md` file. That table is the canonical record and what the dashboard reads.

This folder is for **notable problem write-ups only** — problems worth writing about because they:

- took >45 min,
- introduced a technique worth remembering,
- got you stuck and you want to capture the breakthrough,
- or felt fragile and you flagged for a second pass.

Most problems don't need a write-up. The handwritten work in the paper notebook (and the end-of-week PDF scan) is the actual record.

## When you do write one up

Use the template at [`../templates/problem.md`](../templates/problem.md).

Convention:

- Subfolder per book: `demidovich/`, `irodov/`, `galitski/`, `tao/`, etc.
- Filename: book-id + reference (`tao/t-2-2-3.md`).
- Frontmatter required so the entry shows up in addition to its row in the weekly table.

Frontmatter spec:

```yaml
---
type: problem
id: tao-2-2-3
book: tao-analysis-1
chapter: 2
problem_ref: "2.2.3"
subject: real_analysis
phase: 1
date: 2026-05-28
minutes: 48
status: solved
tags: [phase-1, analysis, notable]
---
```

Body: whatever you want to remember. Statement, approach, what the trick was, where to use it next.
