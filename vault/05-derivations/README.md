# Derivations

Scanned handwritten derivations and their transcriptions.

## Convention

- Subfolder per month: `2026-05/`, `2026-06/`, etc.
- Filename: `YYYY-MM-DD-short-slug.{md,pdf,png}`.
- The `.md` is the index and transcription; the `.pdf` or `.png` is the scan.
- One topic per file.

## Frontmatter

```yaml
---
type: derivation
date: 2026-05-30
topic: "Peano induction → addition is commutative"
book: tao-analysis-1
chapter: 2
related_problems: [tao-2-2-1, tao-2-2-2]
scan: 2026-05-30-peano-commutativity.pdf
tags: [phase-1, analysis]
---
```

## What to scan

- Worked problems with long derivations
- Reprove-from-memory proofs
- Computations where the path matters

## What not to scan

- Trivial arithmetic
- Short sketches (4 lines or less)
- Anything that types up just as cleanly

## Scanner apps

Adobe Scan, Genius Scan, or the Apple Notes scanner all produce clean PDFs from phone photos. Save into `vault/05-derivations/YYYY-MM/`, then write the index `.md` next to it.
