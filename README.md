# theormin

A self-study traversal of [Landau's theoretical minimum](vault/00-meta/curriculum.md) — nine domains of classical and quantum theoretical physics, the foundation of the Soviet theoretical-physics tradition, taken seriously by one person in 2026.

Curriculum generated with Claude Opus 4.7.

The curriculum is a work in progress and shall be adjusted and adapted as time goes on. Let's see where this goes :) .

<!-- BEGIN auto:headline -->**Phase 1 · Week 1 · 0 / 9,000 problems · 1 hrs logged · started 2026-05-26**<!-- END auto:headline -->

## Where I am

<!-- BEGIN auto:status -->
| | |
|---|---|
| Active phase | Phase 1 |
| Current week | Week 1 (2026-05-27) |
| Books in progress | Tao *Analysis I*, Zorich *Mathematical Analysis vol 1*, Demidovich *Problems in Mathematical Analysis*, Strang *Introduction to Linear Algebra* |
| Last theorem reproved | — |
| Last derivation logged | — |
| Estimated baseline completion | computing… (needs ≥4 weeks of data) |
<!-- END auto:status -->

## Progress

### Phases (baseline + Phase 6)

<!-- BEGIN auto:phases -->
```
Phase 1 — Mathematical foundation         ░░░░░░░░░░░░░░░░░░░░   0.0%
Phase 2 — Classical mechanics + fields    ░░░░░░░░░░░░░░░░░░░░   0.0%
Phase 3 — Quantum mechanics               ░░░░░░░░░░░░░░░░░░░░   0.0%
Phase 4 — QED + stat phys + fluids        ░░░░░░░░░░░░░░░░░░░░   0.0%
Phase 5 — Continuous media + kinetics     ░░░░░░░░░░░░░░░░░░░░   0.0%
Phase 6 — Modern QFT + GR + EFT + CMT     ░░░░░░░░░░░░░░░░░░░░   0.0%
```
<!-- END auto:phases -->

### The Nine Checkpoints

<!-- BEGIN auto:checkpoints -->
| # | Domain | Status |
|---|--------|--------|
| 1 | Math I — real analysis, ODE | 🟡 in progress |
| 2 | Math II — complex, tensor, PDE, special functions | ⬜ not started |
| 3 | Mechanics (L1) | ⬜ not started |
| 4 | Field Theory (L2) — SR, GR intro, classical E&M | ⬜ not started |
| 5 | Quantum Mechanics (L3) | ⬜ not started |
| 6 | Statistical Physics (L5) | ⬜ not started |
| 7 | Continuous Media (L6, L7) | ⬜ not started |
| 8 | Electrodynamics of Continuous Media (L8) | ⬜ not started |
| 9 | Quantum Electrodynamics (L4) | ⬜ not started |
<!-- END auto:checkpoints -->

### Subject progress (problems worked / target)

<!-- BEGIN auto:subjects -->
```
Real analysis               0 / 500   ░░░░░░░░░░░░░░░░░░░░
Linear algebra              0 / 300   ░░░░░░░░░░░░░░░░░░░░
ODE                         0 / 400   ░░░░░░░░░░░░░░░░░░░░
Complex analysis            0 / 200   ░░░░░░░░░░░░░░░░░░░░
Calc of variations          0 / 100   ░░░░░░░░░░░░░░░░░░░░
PDE / math methods          0 / 200   ░░░░░░░░░░░░░░░░░░░░
Functional analysis         0 / 200   ░░░░░░░░░░░░░░░░░░░░
General physics             0 / 2,000 ░░░░░░░░░░░░░░░░░░░░
Mechanics (L1)              0 / 400   ░░░░░░░░░░░░░░░░░░░░
Classical fields (L2)       0 / 300   ░░░░░░░░░░░░░░░░░░░░
Quantum mechanics (L3)      0 / 1,000 ░░░░░░░░░░░░░░░░░░░░
QED / QFT                   0 / 600   ░░░░░░░░░░░░░░░░░░░░
```
<!-- END auto:subjects -->

### Activity

<!-- BEGIN auto:heatmap -->
![hours per day](images/heatmap.svg)
<!-- END auto:heatmap -->

<!-- BEGIN auto:sparklines -->
![weekly hours & problems](images/sparklines.svg)
<!-- END auto:sparklines -->

## Recent activity

<!-- BEGIN auto:recent -->_Nothing logged yet. Activity will appear here after Week 1 entries land._<!-- END auto:recent -->

## Reading shelf

<!-- BEGIN auto:shelf -->
| Book | Status | Progress |
|------|--------|----------|
| Tao, *Analysis I* | in progress | 0 / 13 chapters |
| Zorich, *Mathematical Analysis vol 1* | in progress | 0 / 8 chapters |
| Demidovich, *Problems in Mathematical Analysis* | in progress | 0 / 10 chapters |
| Strang, *Introduction to Linear Algebra* | in progress | 0 / 11 chapters |
| Shilov, *Linear Algebra* | not started | — |
| Axler, *Linear Algebra Done Right* | not started | — |
| Arnold, *Ordinary Differential Equations* | not started | — |
| Hirsch-Smale-Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* | not started | — |
| Krasnov, Kiselev, Makarenko, *Problems in ODEs* | not started | — |
| Markushevich, *Theory of Functions of a Complex Variable vol 1* | not started | — |
<!-- END auto:shelf -->

## How this repo works

- **`vault/`** is an [Obsidian](https://obsidian.md) vault. Clone, open `vault/` in Obsidian, install the recommended plugins (Dataview, Templater), and you're set up. Notes use YAML frontmatter as the structured data source.
- **`data/`** holds machine-readable progress: `problems.csv`, `sessions.csv`, `books.yaml`, `theorems.csv`. These drive the README dashboards.
- **`scripts/`** has the Python that regenerates this README and the chart SVGs from `data/`. Run `python scripts/gen_readme.py && python scripts/gen_charts.py`.
- **`.github/workflows/update-dashboard.yml`** runs the scripts on push and on a weekly cron.
- **`images/`** holds the generated charts.

## The curriculum

The full plan, with phase-by-phase book lists, problem targets, and verification protocols: [`vault/00-meta/curriculum.md`](vault/00-meta/curriculum.md).

The honest target is reading-level competence across the nine domains plus research-level depth in one chosen subfield, in roughly 13–18 years at ~30 hrs/week including modern QFT/GR/EFT/CMT (Phase 6). Not a sprint.

## Why public

Two reasons. First, accountability: a public log makes the work harder to abandon. Second, signal to the rare person doing or considering the same thing — there are extremely few public logs of serious adult self-study at this depth, and the genre needs more honest examples.

## License

Notes, summaries, derivations: [CC BY 4.0](LICENSE-notes). Code: [MIT](LICENSE-code).

---

_Started 2026-05-26. Last dashboard refresh: <!-- BEGIN auto:timestamp -->2026-05-27<!-- END auto:timestamp -->._
