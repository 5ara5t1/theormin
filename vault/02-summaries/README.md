# Chapter summaries

One folder per book, one note per chapter. Frontmatter required for the scripts to pick the note up.

## Convention

- Folder per book: `tao-analysis-1/`, `zorich-vol-1/`, `strang/`, etc.
- One note per chapter: `tao-analysis-1/ch02-naturals.md`.
- Use the template at [`../templates/chapter-summary.md`](../templates/chapter-summary.md).

## Frontmatter

```yaml
---
type: summary
book: tao-analysis-1           # matches an id in data/books.yaml
chapter: 2
sections: [2.1, 2.2, 2.3]
status: in_progress            # in_progress | completed
date_started: 2026-05-27
date_completed:                # empty until done
hours: 4.5
problems_worked: 12
tags: [phase-1, analysis]
---
```

## Body

Write in your own words. Target 2–3 pages.

- What this chapter establishes (1–2 sentences)
- Key definitions
- Major theorems with proof sketches
- Connections to prior material — link via `[[ch01-intro]]`
- What was hard
- Open questions to revisit on a second pass
