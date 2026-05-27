# Derivations

Scanned handwritten derivations + their transcriptions. The point of keeping these is twofold: (1) you'll forget how you reasoned three months from now and want to look back, (2) the public record of "here's what an actual cold-start self-study looks like at the working-paper level" has value.

## Convention

- Subfolder per month: `2026-05/`, `2026-06/`, etc.
- Filename: `YYYY-MM-DD-short-slug.{md,pdf,png}`
- The `.md` is the index/transcription; the `.pdf` or `.png` is the scan.
- One topic per file. If a scan covers multiple derivations, split them.

## Frontmatter spec

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

- Worked problems whose derivation is long enough to be worth preserving
- Hand-worked proofs (especially the reprove-from-memory ones)
- Computations where the path matters (not just the answer)
- Anything you'd want to show a future self / future study partner

## What not to scan

- Trivial arithmetic
- Tao Ch. 2 sketches that take 4 lines
- Anything where the typed version is just as good

## Recommended scanner app

Adobe Scan, Genius Scan, or Apple Notes' built-in document scanner all produce clean PDFs from phone photos. Save into the `vault/05-derivations/YYYY-MM/` folder, then write the index `.md` next to it.
