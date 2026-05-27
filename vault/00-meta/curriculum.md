# Theoretical Physics Curriculum

Self-study targeting Landau's theoretical minimum: the nine domains of classical and quantum theoretical physics. Built from the surviving Soviet texts plus Western complements. Phase 6 extends past the 1960 Landau baseline into modern QFT, GR, EFT, and condensed matter field theory.

---

## What this aims for

The Landau theoretical minimum (теорминимум) was nine oral exams covering all of theoretical physics, administered by Landau personally and, after his accident, by his colleagues at the Kapitza Institute. About 43 people passed it during his lifetime. The Phystech (MIPT) curriculum was a separate institutional program with overlapping content. Together they produced theoretical physicists at unusual density.

Realistic outcomes from disciplined self-study:

- Reading-level competence across all nine domains: follow modern research papers in any subfield, work through textbook problems, understand the mathematical machinery.
- Research-level competence in one subfield: requires actual research apprenticeship; the curriculum can't substitute.

Differences from doing this at Phystech in 1980: no selection filter, no six-year full-time focus, no in-person mentorship, no seminar culture. Compensating advantages in 2026: access to both Soviet and Western texts, modern numerical computing, dynamical-systems and mathematical-physics texts written after 1970, and bounded use of AI (rephrasing, references, dimensional checks; not derivations).

---

## Structure

Five phases for the baseline, plus Phase 6 for modern theoretical physics. Math and physics run partially in parallel. Each phase is 12–24 months at serious part-time effort.

| Phase | Math                                                                | Physics                                                                 |
| ----- | ------------------------------------------------------------------- | ----------------------------------------------------------------------- |
| 1     | Analysis, linear algebra, ODE, complex analysis, calc of variations | (general physics review with Irodov)                                    |
| 2     | PDE, tensor calc + intro diff geom, math methods reference          | Mechanics (L1), Classical Fields (L2)                                   |
| 3     | Functional analysis, group theory + Lie algebras                    | QM (L3)                                                                 |
| 4     | Probability, asymptotics, numerical methods                         | QED (L4), Stat Phys 1 (L5), Fluid (L6)                                  |
| 5     | Algebraic topology (optional), gap-filling                          | Elasticity (L7), Cont. media E&M (L8), Stat Phys 2 (L9), Kinetics (L10) |
| 6     | —                                                                   | Modern QFT, GR, EFT, CMT                                                |

---

## Phase 1: Mathematical foundation (12–24 months)

### Real analysis

- Zorich, *Mathematical Analysis* vols 1–2 — main text. Hard on first pass.
- Demidovich, *Problems in Mathematical Analysis* — problem volume; target ~500 problems.
- Tao, *Analysis I & II* — gentler on-ramp for proof technique. Read before or alongside Zorich.
- Alternative main: Apostol vols 1–2.

### Linear algebra

- Strang, *Introduction to Linear Algebra* — first pass, geometric and computational. Pair with MIT 18.06 video lectures.
- Shilov, *Linear Algebra* — classical Soviet sequence: systems of equations → determinants via the permutation/Leibniz formula → vector spaces and linear maps. Computational depth via determinants.
- Axler, *Linear Algebra Done Right* — modern axiomatic. Deliberately defers determinants to the last chapter; the contrast with Shilov is pedagogical.
- Halmos, *Finite-Dimensional Vector Spaces* — short, rigorous.

### Ordinary differential equations

- Arnold, *Ordinary Differential Equations* — main text, geometric and rigorous.
- Hirsch, Smale & Devaney, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* — scaffolding for Arnold.
- Strogatz, *Nonlinear Dynamics and Chaos* — applied complement.
- Krasnov, Kiselev, Makarenko, *Problems in ODEs* — problem volume.

### Complex analysis

- Markushevich, *Theory of Functions of a Complex Variable* vol 1 — main text. Vols 2–3 are reference.
- Needham, *Visual Complex Analysis* — geometric complement.
- Alternative main: Ahlfors, *Complex Analysis*.

### Calculus of variations

- Gelfand & Fomin, *Calculus of Variations*.

Phase 1 problem target: **~1,950**

- Real analysis ~1,000 (Demidovich 500, Zorich 300, Tao 200)
- Linear algebra ~350 (Strang 150, Shilov 100, Axler 100)
- ODE ~400 (Krasnov 200, HSD 100, Strogatz 50, Arnold 40)
- Complex analysis ~150 (Markushevich 100, Needham 50)
- Calc of variations ~50 (Gelfand-Fomin)

---

## Phase 2: Mechanics + fields (12–18 months)

### Math

- PDE: Vladimirov, *Equations of Mathematical Physics*, or Evans, *Partial Differential Equations*.
- Tensor calculus + intro differential geometry: Frankel, *The Geometry of Physics*, or Dubrovin-Fomenko-Novikov, *Modern Geometry* vol 1.
- Math methods reference: Hassani, *Mathematical Physics*. Alternative: Arfken-Weber.

### Physics: general physics review (parallel with math)

- Sivukhin, *General Course of Physics* (5 vols).
- Irodov, *Problems in General Physics* — ~2,000 problem target.
- Krotov, *Aptitude Test Problems in Physics* — olympiad-style mechanics.

### Physics: theoretical minimum begins

- Mechanics (L1) — Landau-Lifshitz vol 1. Prereqs: calc of variations, ODE.
- Classical Theory of Fields (L2) — Landau-Lifshitz vol 2. Prereqs: tensor calc, SR.
- Companion for L1: Goldstein, *Classical Mechanics*.
- Companion for L1 (modern geometric): José & Saletan, *Classical Dynamics: A Contemporary Approach*.
- Companion for L2's electrodynamics: Jackson, *Classical Electrodynamics* — Western graduate canonical. Dense, problem-heavy.
- Gentler alternative E&M reference: Griffiths, *Introduction to Electrodynamics* — undergraduate-level if Jackson is too compressed early.

Phase 2 problem target: **~3,000**

- Math ~150 (PDE 100, math methods 50)
- General physics ~2,300 (Irodov 2,000, Sivukhin 200, Krotov 100)
- Theormin physics ~500 (Jackson 200, Goldstein 150, José-Saletan 50, L1 50, L2 50)

---

## Phase 3: Quantum mechanics (18–24 months)

This phase is commonly underestimated. L3 + Sakurai + Shankar + Galitski + functional analysis + Lie algebras is 18–24 months, not 12.

### Math

- Hall, *Quantum Theory for Mathematicians* — bridge from functional analysis to QM. Unbounded operators, spectral theorem.
- Kolmogorov-Fomin, *Elements of the Theory of Functions and Functional Analysis* — Soviet first pass.
- Reed-Simon vol 1 — reference for specific theorems.
- Georgi, *Lie Algebras in Particle Physics* — first pass on group theory.
- Kirillov **Jr.**, *An Introduction to Lie Groups and Lie Algebras* — mathematical depth. (This is A. Kirillov Jr. at Stony Brook, not his father A. A. Kirillov of orbit-method fame, whose *Elements of the Theory of Representations* is a different and harder book.)
- Vinberg, *A Course in Algebra* — for abstract algebra gaps.

### Physics

- QM (L3) — Landau-Lifshitz vol 3.
- Shankar, *Principles of Quantum Mechanics* — clearest first contact.
- Sakurai, *Modern Quantum Mechanics* — Western complement.
- Galitski, Karnakov, Kogan, Galitski, *Exploring Quantum Mechanics* — ~700 problem target.
- Flügge, *Practical Quantum Mechanics* — solved-problems companion.

Phase 3 problem target: **~1,300**

- Math ~320 (Hall 100, Kolmogorov-Fomin 100, group theory + Lie 120)
- Physics ~950 (Galitski 500, Shankar 200, Sakurai 100, Flügge 100, L3 50)

---

## Phase 4: Advanced theoretical physics (15–24 months)

### Math

- Probability + SDEs: Shiryaev, *Probability*; Øksendal, *Stochastic Differential Equations*.
- Differential geometry: Dubrovin-Fomenko-Novikov vols 2–3.
- Asymptotic analysis: Bender & Orszag, *Advanced Mathematical Methods for Scientists and Engineers*.
- Numerical methods: Trefethen & Bau, *Numerical Linear Algebra*; LeVeque, *Finite Difference Methods for ODE and PDE*.

### Physics

- QED (L4) — Landau-Lifshitz vol 4. Read for the scattering material; the framework predates path integrals.
- Stat Phys 1 (L5) — Landau-Lifshitz vol 5.
- Fluid Mechanics (L6) — Landau-Lifshitz vol 6.
- Peskin & Schroeder, *An Introduction to Quantum Field Theory* — Western QFT companion to L4.
- Kardar, *Statistical Physics of Particles* and *of Fields* — modern stat mech (MIT lectures freely available).
- Zinn-Justin, *Quantum Field Theory and Critical Phenomena* — bridge between stat mech and QFT.

Phase 4 problem target: **~850**

- Math ~560 (Shiryaev 200, Bender-Orszag 150, Trefethen-Bau 80, LeVeque 80, Øksendal 50)
- Physics ~280 (Kardar 200, Peskin 100 partial, L5 50, L4 50, Zinn-Justin 50, L6 30 — Peskin's bulk shifts to Phase 6)

Earlier versions overstated Phase 4 by spreading too thin across L4 + L5 + L6, all of which are theory-heavy with sparse embedded problems.

---

## Phase 5: Continuous media + remainder (12–18 months)

### Physics

- Elasticity (L7) — Landau-Lifshitz vol 7.
- Electrodynamics of Continuous Media (L8) — Landau-Lifshitz vol 8.
- Stat Phys 2 (L9) — Landau-Lifshitz vol 9.
- Physical Kinetics (L10) — Landau-Lifshitz vol 10.

### Math

- Gap-filling and consolidation.
- Algebraic topology (optional, for field theory / condensed matter trajectories): Hatcher, *Algebraic Topology* (free at hatcher.cornell.edu) or Fomenko-Fuks-Gutenmacher, *Homotopic Topology*.
- Category theory (optional, for mathematical physics / TQFT): Riehl, *Category Theory in Context*.

Phase 5 problem target: **~450**

- L7 ~50, L8 ~80, L9 ~80, L10 ~50 (~260 from L-L embedded)
- Supplementary problems (olympiad continuous-media, Galitski-Kogan-Karnakov *Selected Problems in Physical Kinetics and Hydrodynamics*): ~150

The earlier ~1,500 target was wishful. L7–L10 are short volumes with sparse problem sets; the substance is in working through derivations and physical examples rather than crank-the-handle problems.

---

## The nine checkpoints

After each phase's relevant block, sit a self-administered exam in the corresponding domain. The nine domains Landau examined:

1. Math I — real analysis, ODE
2. Math II — complex analysis, vector and tensor calculus, PDE basics, special functions
3. Mechanics — L1
4. Field Theory — L2 (SR, GR, classical electrodynamics)
5. Quantum Mechanics — L3
6. Statistical Physics — L5
7. Mechanics of Continuous Media — L6, L7
8. Electrodynamics of Continuous Media — L8
9. Quantum Electrodynamics — L4

### Verification protocol

Self-administered exams need concrete failure conditions to be meaningful. For each checkpoint, pre-commit to:

- Three results from the block (e.g., for Mechanics: Noether's theorem, the Hamilton-Jacobi equation, the action-angle reduction). Reproduce each proof from a blank page in ≤30 minutes.
- Five problems unseen, solved in four hours total. Source from olympiad archives (Phystech entrance, Russian Physics Olympiad), the listed problem books, and unworked L-L embedded problems.
- Oral component with a study partner if possible. The oral was the original Landau format and reveals understanding vs. recognition.

Failing any of the three means the block isn't done. Sit it again later.

---

## Phase 6: Modern QFT, GR, and EFT (3–5 years)

The Landau theoretical minimum covers physics through roughly 1960. Modern theoretical work requires three more pillars: path-integral QFT and gauge theory, modern GR, and Effective Field Theory as the unifying framework. These bring you to ~1990, the foundation underlying currently active research in particle physics, cosmology, condensed matter field theory, mathematical physics, and the theory of deep learning.

After 1990 the field splits into specialties (string theory, quantum information, modern condensed matter, TQFT). The QFT + GR + EFT triad is the common foundation.

### QFT (1.5–2.5 years)

Prereqs: Phase 3 (L3 + Galitski), Phase 4 (L4), group theory + Lie algebras, complex analysis, intro functional analysis.

Entry point:

- Tong, *Lectures on Quantum Field Theory* — Cambridge, free. Read first.

Primary text (pick one):

- Schwartz, *Quantum Field Theory and the Standard Model* — first full text. Integrates Standard Model content.
- Peskin & Schroeder, *An Introduction to QFT* — Western graduate canonical.
- Srednicki, *Quantum Field Theory* — free; clean exposition.

Supplementary:

- Zee, *Quantum Field Theory in a Nutshell* — intuition-building.
- Weinberg, *The Quantum Theory of Fields* (3 vols) — reference for depth.
- Coleman, *Lectures on Quantum Field Theory* — book plus Harvard recordings on YouTube.

Problems: Radovanović, *Problem Book in QFT*, plus end-of-chapter problems in the primary text.

Bogoliubov & Shirkov predates the path-integral revolution; useful as a supplement for operator formalism and renormalization, not as a first text.

### GR (1–1.5 years)

Prereqs: Phase 2 (L2, tensor calc, intro differential geometry).

Entry point (optional, if differential geometry is shaky):

- Hartle, *Gravity: An Introduction to Einstein's General Relativity* — physics-first, accessible.
- Schutz, *A First Course in General Relativity* — gentler than Carroll.

Primary texts (read two):

- Carroll, *Spacetime and Geometry: An Introduction to General Relativity*.
- Wald, *General Relativity* — more rigorous, natural follow-on after Carroll.

Supplementary:

- MTW, *Gravitation* — 1973 encyclopedic reference.
- Weinberg, *Gravitation and Cosmology* — gravity as a field theory.

Problems: Lightman, Press, Price, Teukolsky, *Problem Book in Relativity and Gravitation*.

Cosmology (if interested):

- Dodelson, *Modern Cosmology*.
- Weinberg, *Cosmology*.
- Mukhanov, *Physical Foundations of Cosmology*.

### EFT (6–9 months focused, on top of QFT)

EFT covers Wilson's RG plus systematic integration of heavy degrees of freedom. Threaded through Schwartz and Peskin-Schroeder but deserves dedicated study.

- Manohar, *Effective Field Theories* — lecture notes, free.
- Cohen, "Effective Field Theory" lecture notes (TASI 2018) — free.
- Penco, "An Introduction to Effective Field Theories" — review article.
- Burgess, *Introduction to Effective Field Theory*.
- Petrov & Blechman, *Effective Field Theories*.

Relevant chapters: Schwartz 22–25, Peskin-Schroeder 12 and others, Weinberg vol 1 ch. 12.

### Condensed matter field theory

Strictly post-1990 and a specialization, but adjacent to the QFT + EFT core and large in current research output.

- Altland & Simons, *Condensed Matter Field Theory* — modern standard.
- Coleman, *Introduction to Many-Body Physics* — operator-flavored alternative.
- Fradkin, *Field Theories of Condensed Matter Physics* — topological phases and gauge theories.

### Soviet supplements for Phase 6

QFT:

- Bogoliubov & Shirkov, *Introduction to the Theory of Quantized Fields* — operator formalism, Bogoliubov-Parasiuk renormalization.
- Bogoliubov, Logunov, Oksak, Todorov, *General Principles of Quantum Field Theory* — axiomatic.
- Faddeev & Slavnov, *Gauge Fields: Introduction to Quantum Theory* — Soviet gauge theory.
- Polyakov, *Gauge Fields and Strings* — monopoles, Polyakov path integral, early conformal symmetry.
- Akhiezer & Berestetskii, *Quantum Electrodynamics*.
- Vasiliev, *The Field Theoretic Renormalization Group in Critical Behavior Theory* — RG, bridges QFT and stat mech.

Western analog with comparable rigor: Itzykson & Zuber, *Quantum Field Theory*.

GR:

- Fock, *The Theory of Space, Time and Gravitation* — non-Landau Soviet perspective.
- Zeldovich & Novikov, *Relativistic Astrophysics* (2 vols) — stars + cosmology.
- Mukhanov, *Physical Foundations of Cosmology*.
- Mukhanov, Feldman & Brandenberger, "Theory of Cosmological Perturbations" (Phys. Rep. 1992) — canonical paper.

EFT (limited Soviet coverage):

- Vasiliev (as above).
- Polyakov, *Gauge Fields and Strings* — CFT and RG fixed points.
- Migdal, *Qualitative Methods in Quantum Theory* — scaling, dimensional analysis, estimation.

### Methodology

The choice of text matters less than how it's worked. Apply the same standard to any text:

- Heavy problem volume.
- Derive every result from foundations; don't accept a formula until you've worked it.
- Tight integration of computation with applications.
- Mathematical depth without unnecessary abstraction.
- Geometric and physical intuition before formalism.

Schwartz worked thoroughly is equivalent to Bogoliubov-Shirkov worked thoroughly.

### Order

Tong → primary QFT text → GR in parallel or after → EFT after QFT → CMT if relevant. Cosmology after GR.

If only one of the three: QFT. Modern theoretical physics is largely QFT-flavored thinking applied across domains.

Phase 6 problem target: **~1,400**

- QFT ~700 (Schwartz 300, Radovanović 200, Peskin 100, Srednicki 70, Tong 30)
- GR ~500 (Carroll 150, LPPT 200, Hartle 100, Wald 50)
- EFT ~50 (lecture notes)
- CMT ~150 (Altland-Simons 100, Coleman 50)

---

## Operational principles

1. **Problem volume.** Target ~7,600 problems for Phases 1–5 (general physics dominates the count via Irodov's ~2,000), ~9,000 with Phase 6. Don't shortcut.

2. **Math and physics in parallel.** Each L-L volume has specific math prerequisites. Learn them adjacently rather than preemptively.

3. **Two texts per subject minimum, three when stuck.** Soviet text for depth, Western for clarity, problem book for fluency.

4. **Reprove from memory weekly.** Pick one major theorem each week, reproduce its proof on paper, closed-book.

5. **Write chapter summaries.** 2–3 pages in your own words after each chapter. Reread before starting the next volume.

6. **Computational reinforcement.** Implement key results numerically when possible. Numerical experiments expose hand-waving and build a parallel skill that working physicists use.

7. **Study partner.** A co-learner reading the same texts on a similar schedule replicates the seminar component of Soviet pedagogy. The oral component of the checkpoint exam needs another person.

8. **AI tooling, bounded.** Use for: rephrasing dense passages, dimensional checks, locating where a result is treated, debugging numerical code. Don't use for: producing or verifying non-trivial derivations, signs and factors, problem-solving where you can't independently check the answer.

9. **No skipping.** The chapters that look elementary often contain the ideas that matter most later.

10. **Concrete checkpoint conditions.** A solo four-hour exam without falsifiable pass/fail criteria reduces to self-grading. Pre-commit to reproducing three theorems from blank pages in 30 minutes each and solving five unseen problems.

---

## Realistic timeline

Baseline (Phases 1–5):

| Effort                          | Completion |
| ------------------------------- | ---------- |
| Full-time, no other obligations | 5–6 years  |
| Serious part-time, 20 hrs/week  | 9–13 years |
| Steady part-time, 10–15 hrs/week| 13–18 years|
| Casual, 5 hrs/week              | Probably never reaches theormin — pick a smaller goal |

With Phase 6:

| Effort                          | Completion |
| ------------------------------- | ---------- |
| Full-time                       | 8–11 years |
| Serious part-time, 20 hrs/week  | 13–18 years|
| Steady part-time, 10–15 hrs/week| 17–24 years|

These ranges assume no peer cohort and normal life obligations. Adjust downward for prior rigorous physics or math training; adjust further downward if embedded in a research environment. Adjust upward for non-mathematical background.

---

## Minimum-viable bookshelf

The high-leverage subset:

**Math:**

- Analysis: Zorich vol 1 + Demidovich (Tao as on-ramp if needed)
- Linear algebra: Shilov + Axler
- ODE: Arnold + Hirsch-Smale-Devaney + Krasnov
- Complex analysis: Markushevich vol 1 + Needham
- Calc of variations: Gelfand-Fomin
- PDE: Vladimirov or Evans
- Functional analysis: Kolmogorov-Fomin + Hall
- Tensor calc + diff geom: Frankel
- Group theory: Georgi
- Math methods: Hassani
- Probability: Shiryaev
- Asymptotics: Bender-Orszag
- Numerical: Trefethen-Bau

**Physics:**

- General physics: Sivukhin (5 vols), Irodov for problems
- Theoretical baseline: Landau-Lifshitz (10 vols)
- QM problems: Galitski et al.
- Western complements: Shankar, Sakurai, Peskin-Schroeder, Kardar
- Phase 6: Tong (free), Schwartz, Carroll + Wald, Altland-Simons, Zinn-Justin

~30 core books. The full Soviet curriculum was longer; this is what does the most work.

---

Curriculum scoped with Claude Opus 4.7.
