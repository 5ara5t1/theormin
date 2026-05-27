# Theorems reproved from memory

The weekly verification ritual: pick a major theorem, reproduce its proof on a blank page, write up here what you wrote on paper plus any spots you stumbled on. Repeat reproofs are valuable — they get faster, and the gaps move.

## Convention

- One note per theorem.
- Filename: descriptive kebab-case: `pythagoras.md`, `addition-commutativity-on-N.md`, `noether.md`, `cauchy-residue.md`.
- Each note can be reproved multiple times — log each attempt under `## Attempts` with date and outcome.

## Frontmatter spec

```yaml
---
type: theorem
theorem: "Addition is commutative on N"
book: tao-analysis-1
date: 2026-06-01            # most recent attempt
result: passed              # passed | partial | failed
time_minutes: 12
tags: [phase-1, analysis]
---
```

Multiple attempts: bump the `date`, `result`, and `time_minutes` to the latest; preserve history in the body under `## Attempts`.

## Why this ritual

Re-proving from memory is the cleanest separator of "actually learned" from "passively followed." It also generates a measurable cadence the Soviet system relied on but is otherwise easy to drop. See [the curriculum](../00-meta/curriculum.md) Operational Principle 4.
