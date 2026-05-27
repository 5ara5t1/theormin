# Scans and derivations

Handwritten work scanned to PDF at the end of each week. The PDFs are the actual record; the markdown indices describe what's in them.

## Convention

- One folder per week: `week-01/`, `week-02/`, etc.
- One or more PDFs per week. Names can be topical (`tao-ch2.pdf`, `demidovich-1.pdf`) or just `scans.pdf` for the whole week.
- One `index.md` per week describing what's in each PDF.

```
05-derivations/
  week-01/
    index.md
    scans.pdf
    (or split: tao.pdf, demidovich.pdf, strang.pdf, theorem-reproofs.pdf)
```

## Index file frontmatter

```yaml
---
type: derivation_index
week: 1
date: 2026-06-01
tags: [phase-1, scans]
---
```

Body: short list of what's in each PDF.

```markdown
# Week 1 scans

- `tao-ch2.pdf` — Tao Ch. 2 §2.1–2.3 exercises, problems 2.2.1 through 2.3.5
- `strang.pdf` — Strang Ch. 2 problems 1–12
- `demidovich.pdf` — Demidovich §1 problems, first batch
- `theorem-reproof.pdf` — "Addition is commutative on N", reproved from memory
```

## Linking from the week file

Reference the scans folder from `vault/01-weeks/week-XX.md` under `## Scans`.

## Scanner apps

Adobe Scan, Genius Scan, or Apple Notes' built-in scanner produce clean PDFs from phone photos. Page-rectify before saving.
