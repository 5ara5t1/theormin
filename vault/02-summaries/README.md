# Chapter summaries

Your personal compressed Landau-Lifshitz. One folder per book, one note per chapter, each starting with frontmatter so the scripts pick them up.

## Convention

- Folder per book: `tao-analysis-1/`, `zorich-vol-1/`, `strang/`, `arnold-ode/`, etc.
- One note per chapter: `tao-analysis-1/ch02-naturals.md`
- Start each note with the template at [`../templates/chapter-summary.md`](../templates/chapter-summary.md). Templater plugin will fill this automatically.

## Frontmatter spec

```yaml
---
type: session                    # if you logged hours here directly
book: tao-analysis-1             # matches an id in data/books.yaml
chapter: 2
sections: [2.1, 2.2, 2.3]
status: in_progress              # in_progress | completed
date_started: 2026-05-27
date_completed:                  # empty until done
hours: 4.5
problems_worked: 12
tags: [phase-1, analysis]
---
```

## Body convention

Write in your own words. Aim for 2–3 pages compressed.
- **What this chapter establishes** (1–2 sentences)
- **Key definitions** (terse, no padding)
- **Major theorems** with proof sketches (not full proofs — the point is your compressed mental version)
- **Where this connects** — wikilink to prior chapters/books with `[[ch01-intro]]`
- **What was hard / felt important** (write to yourself, frankly)
- **Open questions** — list of things you didn't fully understand. Revisit on second pass.
