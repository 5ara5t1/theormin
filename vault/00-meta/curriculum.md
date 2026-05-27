# Phystech-Level Theoretical Physics Curriculum

A self-study program targeting the Landau Theoretical Minimum baseline — competent across all nine domains of classical and quantum theoretical physics. Built from surviving Soviet texts plus Western complements. Optimized for theory.

---

## The goal, honestly stated

The Landau theoretical minimum (теорминимум) was nine oral exams covering all of theoretical physics, administered by Landau personally and, after his accident, by his colleagues at the Kapitza Institute. Roughly 43 people passed it during his lifetime. The Phystech (MIPT) curriculum was a separate institutional program with overlapping but distinct content — it shared Landau's standards but was not the same exam. Together they produced theoretical physicists at unmatched density.

What self-study can realistically achieve in 2026:

- **Reading-level competence across all nine domains.** You can read and follow modern research papers in any subfield, understand the mathematical machinery, and solve non-trivial textbook problems. This is already rare among working Western physicists.
- **Research-level competence in one chosen subfield.** Requires actual research apprenticeship; the curriculum can't substitute.

What you'll lack vs. a 1980 Phystech student: (1) selection effect — they were filtered by olympiad and entrance exams to be the brightest in the country; (2) full-time focus for six years; (3) direct mentorship from working researchers; (4) seminar culture.

What you'll gain over them: (1) access to both Soviet and Western literature; (2) modern numerical computing; (3) modern dynamical-systems and post-1970 mathematical physics texts they didn't have; (4) bounded use of AI tooling — useful for rephrasing, finding references, dimensional sanity checks, and concept lookup; unreliable for non-trivial derivations and not a substitute for working a problem yourself; (5) the entire historical record of theoretical physics already settled.

Aim for reading-level breadth across the nine domains, then research-level in whichever subfield you actually pursue.

---

## Structure overview

Five phases, math and physics running partially in parallel rather than sequentially. Each phase is 12–24 months at serious part-time effort. Total ~6–12 years for the baseline depending on time available.

| Phase | Math | Physics |
|-------|------|---------|
| 1 | Analysis, linear algebra, ODE, complex analysis, calc of variations | (general physics review with Irodov) |
| 2 | PDE, tensor calc + intro diff geom, math methods reference | Mechanics (L1), Classical Fields (L2) |
| 3 | Functional analysis (physics-flavored), group theory + Lie algebras | QM (L3) |
| 4 | Probability, asymptotics, numerical methods | QED (L4), Stat Phys 1 (L5), Fluid (L6) |
| 5 | Algebraic topology (optional), gap-filling | Elasticity (L7), Cont. media E&M (L8), Stat Phys 2 (L9), Kinetics (L10) |

---

## Phase 1: Mathematical foundation (12–24 months)

### Real analysis

- **Zorich**, *Mathematical Analysis* vols 1–2 — main text, bridges Soviet rigor and modern perspective. Brutal on a first pass; rewards rereading.
- **Demidovich**, *Problems in Mathematical Analysis* — problem volume (target: work ~500 problems)
- **Tao**, *Analysis I & II* — gentler on-ramp if Zorich is too steep on first contact. Builds proof technique deliberately. Use as scaffolding, not replacement.
- Alternative main text: Apostol vols 1–2 (similar difficulty to Zorich, less Soviet flavor)

### Linear algebra

- **Shilov**, *Linear Algebra* — Soviet combinatorial-determinant approach
- **Axler**, *Linear Algebra Done Right* — modern axiomatic view
- **Halmos**, *Finite-Dimensional Vector Spaces* — short, beautiful, Soviet-flavored rigor
- **Strang**, *Introduction to Linear Algebra* — geometric/computational intuition for first contact
- (Defer Trefethen-Bau to Phase 4 unless needed sooner)

### Ordinary differential equations

- **Arnold**, *Ordinary Differential Equations* — main text, geometric and rigorous. Notoriously hard to read cold.
- **Hirsch, Smale & Devaney**, *Differential Equations, Dynamical Systems, and an Introduction to Chaos* — scaffolding for Arnold. Read in parallel.
- **Strogatz**, *Nonlinear Dynamics and Chaos* — applied/qualitative complement
- **Krasnov, Kiselev, Makarenko**, *Problems in ODEs* — problem volume

### Complex analysis

- **Markushevich**, *Theory of Functions of a Complex Variable* vol 1 — Soviet canonical, vol 1 is the curriculum. Vols 2–3 are reference, consult as needed.
- **Needham**, *Visual Complex Analysis* — geometric intuition, ideal complement
- Alternative main text: Ahlfors, *Complex Analysis*

### Calculus of variations

- **Gelfand & Fomin**, *Calculus of Variations* — Dover classic, short and beautiful

**Phase 1 problem volume target:** ~1,500 problems total.

---

## Phase 2: Begin physics + advanced math (12–18 months)

### Math

- **PDE:** Vladimirov, *Equations of Mathematical Physics* (Soviet) or Evans, *Partial Differential Equations* (Western)
- **Tensor calculus + intro differential geometry:** Frankel, *The Geometry of Physics* or Dubrovin-Fomenko-Novikov, *Modern Geometry* vol 1
- **Math methods reference:** Hassani, *Mathematical Physics: A Modern Introduction to Its Foundations* — keep on the shelf for adjacent techniques (Green's functions, special functions, integral transforms) as they come up in L2 and later. Arfken-Weber is the alternative; less rigorous but more compendious.

### Physics: General physics review (parallel with math)

- **Sivukhin**, *General Course of Physics* (5 vols) — Soviet general physics
- **Irodov**, *Problems in General Physics* — the canonical problem book, ~2,000 problems
- **Krotov**, *Aptitude Test Problems in Physics* — olympiad-style mechanics

### Physics: Theoretical minimum begins

- **Mechanics (L1)** — Landau-Lifshitz vol 1
  - Prerequisites: calc of variations, ODE
- **Classical Theory of Fields (L2)** — Landau-Lifshitz vol 2
  - Prerequisites: tensor calc, SR
- Companion: Goldstein, *Classical Mechanics* (Western analog of L1, more verbose, more problems)
- Companion for L1: José & Saletan, *Classical Dynamics: A Contemporary Approach* — modern geometric mechanics

**Phase 2 problem volume target:** ~2,000 problems (Irodov heavy, plus L1/L2 embedded problems — these are notoriously hard).

---

## Phase 3: Quantum mechanics block (18–24 months)

This phase is the most commonly underestimated. L3 + Sakurai + Shankar + Galitski problems + functional analysis + Lie algebras is genuinely 18–24 months of serious work, not 12.

### Math

- **Functional analysis (physics-flavored):** Hall, *Quantum Theory for Mathematicians* — the right bridge text between functional analysis and QM. Treats unbounded operators, spectral theorem, and the mathematical structure of QM without the encyclopedic detour of Reed-Simon.
- **Functional analysis (Soviet first pass):** Kolmogorov-Fomin, *Elements of the Theory of Functions and Functional Analysis* — Dover, concise, rigorous, useful before Hall.
- **Reference only:** Reed-Simon vol 1 — encyclopedic and excellent, but used as reference when a specific theorem matters, not read cover-to-cover.
- **Group theory + Lie algebras:** Georgi, *Lie Algebras in Particle Physics* (physicist-friendly first pass), then Kirillov, *An Introduction to Lie Groups and Lie Algebras* (mathematical depth). Vinberg's *Course in Algebra* covers earlier abstract algebra if missing.

### Physics

- **QM (L3)** — Landau-Lifshitz vol 3 — the canonical Soviet QM
- **Shankar**, *Principles of Quantum Mechanics* — pedagogically the clearest of the major Western texts; best first contact
- **Sakurai**, *Modern Quantum Mechanics* — Western complement, sharper on spin and symmetry
- **Galitski, Karnakov, Kogan, Galitski**, *Exploring Quantum Mechanics* — problem book, ~700 problems. Famously hard; pace yourself.
- **Flügge**, *Practical Quantum Mechanics* — solved-problems companion, lighter than Galitski, useful when Galitski stalls you

**Phase 3 problem volume target:** ~1,000 problems, QM-focused.

---

## Phase 4: Advanced theoretical physics (15–24 months)

### Math

- **Probability + stochastic processes:** Shiryaev, *Probability*; Øksendal, *Stochastic Differential Equations*
- **Differential geometry advanced:** Dubrovin-Fomenko-Novikov vols 2–3
- **Asymptotic analysis:** Bender & Orszag, *Advanced Mathematical Methods for Scientists and Engineers* — the classic
- **Numerical methods:** Trefethen & Bau, *Numerical Linear Algebra*; LeVeque, *Finite Difference Methods for ODE and PDE*

### Physics

- **QED (L4)** — Landau-Lifshitz vol 4 — read for the relativistic-scattering material; the QFT framework here predates the path-integral revolution
- **Stat Phys 1 (L5)** — Landau-Lifshitz vol 5
- **Fluid Mechanics (L6)** — Landau-Lifshitz vol 6
- Companion: Peskin & Schroeder, *An Introduction to Quantum Field Theory* — Western QFT, pedagogically clearer than L4
- Companion: Kardar, *Statistical Physics of Particles* and *of Fields* — modern stat mech, MIT lectures freely available
- Bridge text: **Zinn-Justin**, *Quantum Field Theory and Critical Phenomena* — the canonical bridge between statistical mechanics and QFT. Belongs alongside Kardar + Peskin-Schroeder; load-bearing for understanding why these subjects are the same subject.

**Phase 4 problem volume target:** ~1,500 problems.

---

## Phase 5: Continuous media + remainder (12–18 months)

### Physics

- **Elasticity (L7)** — Landau-Lifshitz vol 7
- **Electrodynamics of Continuous Media (L8)** — Landau-Lifshitz vol 8
- **Stat Phys 2 (L9)** — Landau-Lifshitz vol 9
- **Physical Kinetics (L10)** — Landau-Lifshitz vol 10

### Math

- Gap-filling and consolidation.
- If trajectory is modern field theory / condensed matter: **algebraic topology** via Hatcher, *Algebraic Topology* (free at hatcher.cornell.edu) or Fomenko-Fuks-Gutenmacher, *Homotopic Topology*.
- If trajectory is mathematical physics / TQFT: introductory **category theory** via Riehl, *Category Theory in Context*.

**Phase 5 problem volume target:** ~1,500 problems.

---

## The Theoretical Minimum — nine self-assessment checkpoints

After each phase's relevant block is complete, sit a self-administered exam: write competent solutions to five non-trivial problems in four hours, closed-book. These are the actual nine domains Landau examined:

1. **Math I** — real analysis, ODE
2. **Math II** — complex analysis, vector and tensor calculus, PDE basics, special functions
3. **Mechanics** — L1
4. **Field Theory** — L2 (SR, GR, classical electrodynamics)
5. **Quantum Mechanics** — L3
6. **Statistical Physics** — L5
7. **Mechanics of Continuous Media** — L6, L7
8. **Electrodynamics of Continuous Media** — L8
9. **Quantum Electrodynamics** — L4

### Verification protocol

A self-administered four-hour exam is mostly a self-flattery machine unless you bind it to concrete, falsifiable failure conditions. For each checkpoint, pre-commit to specific re-derivation tests, scored honestly:

- Pick three load-bearing results from the block (e.g., for Mechanics: Noether's theorem, the Hamilton-Jacobi equation, the action-angle reduction of an integrable system). Reproduce each proof from a blank page in ≤30 minutes.
- Solve five non-trivial problems unseen — sourced from olympiad archives (Phystech entrance, Russian Physics Olympiad), the problem books listed, and L-L embedded problems you haven't worked yet.
- If possible, have a study partner administer the exam orally — the original Landau format. The oral component is what reveals whether you actually understand or merely recognize.

Failing any of the three components means the block isn't done. The Soviet system was harsh because the standard was real. Self-grade as if your instructor would notice the difference.

---

## Phase 6: Beyond baseline — Modern QFT, GR, and EFT (~3–5 years)

The Landau theoretical minimum gets you to roughly 1960 physics. Modern theoretical physics as actually practiced requires three additional pillars: modern Quantum Field Theory (path-integral formulation, gauge theory, renormalization), modern General Relativity, and Effective Field Theory as the unifying conceptual framework. Together these bring you to ~1990 — the foundation underlying currently-active research in particle physics, cosmology, condensed matter field theory, mathematical physics, and increasingly the theory of deep learning.

After 1990 the field fragments into specialties (string theory, quantum information, modern condensed matter, TQFT). The QFT + GR + EFT triad is the common foundation that unlocks all of them.

### QFT track (~1.5–2.5 years)

Prerequisites from prior phases: Phase 3 (L3 QM + Galitski problems), Phase 4 (L4 QED), group theory + Lie algebras (especially Lorentz, Poincaré, SU(N)), complex analysis, intro functional analysis.

Entry point (read first, in parallel with your primary text):

- **Tong**, *Lectures on Quantum Field Theory* — Cambridge, freely available. Widely regarded as the cleanest entry point in 2026: short, focused, geometrically motivated, no detours. Read these first; they make Schwartz/Peskin readable.

Primary text — pick one:

- **Schwartz**, *Quantum Field Theory and the Standard Model* — best first full text. Modern, pedagogically careful, integrates Standard Model content.
- **Peskin & Schroeder**, *An Introduction to QFT* — canonical Western graduate text. Slightly older flavor, still excellent.
- **Srednicki**, *Quantum Field Theory* — free PDF at srednicki.physics.ucsb.edu. Very clean exposition; often preferred for self-study.

Supplementary:

- **Zee**, *Quantum Field Theory in a Nutshell* — opinionated, intuition-building. Read alongside the primary text.
- **Weinberg**, *The Quantum Theory of Fields* (3 vols) — the deep reference. Vol 1 (foundations, S-matrix), Vol 2 (gauge theory, RG), Vol 3 (supersymmetry). Not a first text; consult for depth on specific topics.
- **Coleman**, *Lectures on Quantum Field Theory* — book plus Harvard recordings on YouTube. Sidney Coleman was legendary; the lectures alone are worth watching.

Problems: **Radovanović**, *Problem Book in QFT*, plus end-of-chapter problems in your primary text.

Soviet note: Bogoliubov & Shirkov's *Introduction to the Theory of Quantized Fields* is the classical Soviet treatment but predates the path-integral revolution and is less effective as a first text now. For modern path-integral QFT, lean Western for the primary track; the Soviet QFT texts enter as supplements (below).

### GR track (~1–1.5 years)

Prerequisites: Phase 2 (L2 Classical Theory of Fields, tensor calc, intro differential geometry). L2 covers SR + a basic GR introduction; modern GR is much more.

Entry point:

- **Hartle**, *Gravity: An Introduction to Einstein's General Relativity* — physics-first approach, very accessible. Optional but useful if your differential geometry is shaky.
- **Schutz**, *A First Course in General Relativity* — easier introduction if you want scaffolding before Carroll.

Primary texts — read two:

- **Carroll**, *Spacetime and Geometry: An Introduction to General Relativity* — modern pedagogical standard. Free lecture notes online predate the book.
- **Wald**, *General Relativity* — more mathematical and rigorous than Carroll. Standard graduate text for theorists. Natural follow-on after Carroll.

Supplementary:

- **MTW** (Misner-Thorne-Wheeler), *Gravitation* — encyclopedic 1973 classic. Eccentric two-track presentation; still the best reference for sheer breadth.
- **Weinberg**, *Gravitation and Cosmology* — particle physicist's GR, treats gravity as a field theory. Distinctive perspective worth knowing.

Problems: **Lightman, Press, Price, Teukolsky**, *Problem Book in Relativity and Gravitation* — canonical GR problem book.

Cosmology (natural follow-on):

- **Dodelson**, *Modern Cosmology* — graduate standard
- **Weinberg**, *Cosmology* — Weinberg's perspective
- **Mukhanov**, *Physical Foundations of Cosmology* — modern, treats inflation rigorously

### EFT track (~6–9 months focused, on top of QFT)

EFT is the modern unifying conceptual framework: Wilson's RG plus systematic integration of heavy degrees of freedom. Woven through Schwartz and Peskin-Schroeder but deserves dedicated focused study afterward.

Core resources (much of this is lecture notes rather than books):

- **Manohar**, *Effective Field Theories* — lecture notes, freely available
- **Cohen**, "Effective Field Theory" lecture notes (TASI 2018) — modern, free, excellent
- **Penco**, "An Introduction to Effective Field Theories" — review article
- **Burgess**, *Introduction to Effective Field Theory* — book-length treatment
- **Petrov & Blechman**, *Effective Field Theories* — alternative book

Relevant chapters in QFT texts: Schwartz Ch. 22–25, Peskin-Schroeder Ch. 12 + various, Weinberg Vol 1 Ch. 12.

### Condensed matter field theory (the missing fourth pillar)

Strictly speaking this is post-1990 and a specialization, but it sits so close to the QFT + EFT core — and produces so much of currently-active theoretical work — that it belongs in Phase 6 for anyone not committing entirely to high-energy.

- **Altland & Simons**, *Condensed Matter Field Theory* — the modern standard. Path-integral CMT done carefully.
- **Coleman**, *Introduction to Many-Body Physics* — alternative, more operator-flavored.
- **Fradkin**, *Field Theories of Condensed Matter Physics* — topological phases and gauge theories in CMT.

### Soviet-tradition supplements for Phase 6

The Soviet tradition contributed enormously to QFT and GR but is thinner on EFT specifically (which crystallized as a framework in the West post-1970). Where Soviet texts exist and add unique value:

**QFT supplements:**

- **Bogoliubov & Shirkov**, *Introduction to the Theory of Quantized Fields* — operator formalism, careful renormalization theory (Bogoliubov-Parasiuk theorem). Less path-integral focus, so use as a supplement rather than primary.
- **Bogoliubov, Logunov, Oksak, Todorov**, *General Principles of Quantum Field Theory* — axiomatic/rigorous treatment. Austere but deep.
- **Faddeev & Slavnov**, *Gauge Fields: Introduction to Quantum Theory* — Faddeev was one of the giants of 20th-century theoretical physics (Faddeev-Popov ghosts, quantum inverse scattering). The Soviet-style gauge theory text; strongly recommended.
- **Polyakov**, *Gauge Fields and Strings* — Polyakov is among the all-time greats. Idiosyncratic but profound: 't Hooft-Polyakov monopoles, Polyakov path integral, early conformal symmetry.
- **Akhiezer & Berestetskii**, *Quantum Electrodynamics* — pre-Peskin Soviet QED.
- **Vasiliev**, *The Field Theoretic Renormalization Group in Critical Behavior Theory* — modern Russian, RG-focused, bridges QFT and statistical mechanics. Useful for EFT-adjacent thinking.

Western text with the most Soviet-flavor pedagogy: **Itzykson & Zuber**, *Quantum Field Theory* — extremely thorough, problem-heavy, derives everything. Often considered the closest Western analog to Soviet rigor in QFT.

**GR supplements:**

- **Landau L2** (you'll have done this) — Soviet style at its peak. GR alongside SR and electrodynamics, no separation.
- **Fock**, *The Theory of Space, Time and Gravitation* — different perspective from Landau, more philosophical about coordinates and absolute geometry.
- **Zeldovich & Novikov**, *Relativistic Astrophysics* (2 vols) — Vol 1 stars and relativity, Vol 2 structure of the universe. Both volumes are masterworks of Soviet astrophysics.
- **Mukhanov**, *Physical Foundations of Cosmology* — modern Russian cosmology text, inflation done rigorously.
- **Mukhanov, Feldman & Brandenberger**, "Theory of Cosmological Perturbations" (1992) — canonical paper, freely available, essential for cosmology.

**EFT supplements (limited):**

- **Vasiliev** (as above) — most rigorous Russian treatment of Wilsonian RG, conceptual core of EFT.
- **Polyakov**, *Gauge Fields and Strings* — CFT and RG fixed points.
- **Migdal**, *Qualitative Methods in Quantum Theory* — closest the Soviet tradition gets to teaching the "EFT mindset" before EFT had a name. Migdal-style estimation, scaling arguments, dimensional analysis.

For EFT proper, Western lecture notes remain unavoidable — but you can apply Soviet methodology to them.

### Applying Soviet pedagogy regardless of text choice

Soviet pedagogy isn't only about which books you read — it's how you engage with them. The defining features apply to any text:

- Heavy problem volume; never accept a result without working it through
- No skipped derivations; derive everything from foundations before accepting the formula
- Tight integration with physical computation and applications
- Mathematical depth without Bourbaki-style abstraction
- Geometric and physical intuition primary, formalism secondary

You can take Schwartz QFT, work every problem, derive every formula from the path integral up, compute every Feynman diagram explicitly. That's Soviet methodology applied to a Western text — functionally equivalent to studying Bogoliubov-Shirkov with the same intensity. Methodology matters more than the cover of the book.

The realistic synthesis for Phase 6: use Soviet texts where they exist and add unique value (Faddeev-Slavnov, Polyakov, Fock, Zeldovich-Novikov, Mukhanov, Vasiliev), Western texts where the Soviet tradition is weak or absent (path-integral QFT via Tong/Schwartz, EFT proper, rigorous modern GR formalism, modern CMT via Altland-Simons), and Soviet methodology applied to all of them.

### Order and integration

Tong's notes → primary QFT text → GR in parallel or after → EFT as concentrated study on top of QFT → CMT if relevant to your trajectory. Cosmology if interested follows GR.

If you can only do one of the three: do **QFT**. Modern theoretical physics is essentially QFT-flavored thinking applied across domains. GR is necessary for gravity-specific work and cosmology; EFT is the conceptual layer that turns a QFT mechanic into a theorist who understands the framework.

### What Phase 6 enables

- Reading modern theoretical research papers in particle physics, cosmology, condensed matter field theory, mathematical physics
- Substantive engagement with theory of deep learning literature (RG flow, EFT thinking, mean-field theory, statistical field theory of neural networks)
- Original theoretical work given the right project and direction
- Entry point to all post-1990 specializations: string theory (Polchinski; Becker-Becker-Schwarz), modern condensed matter (Altland-Simons; Coleman's *Many-Body Physics*), quantum information (Nielsen-Chuang; Preskill's notes), TQFT, holography, and beyond

**Phase 6 problem volume target:** ~2,000 problems.

---

## Operational principles

1. **Problem volume is the bet.** Soviet pedagogy assumed ~5,000 worked problems across the full curriculum. Total across phases above: ~7,500 problems if you do everything listed. Don't shortcut this. Volume is what produces fluency; explanation alone doesn't.

2. **Math and physics in parallel.** You don't need all the math before physics. Mechanics needs only ODE + calc of variations. Each L-L volume has specific math prerequisites — learn them adjacently, not preemptively.

3. **Two texts per subject minimum, three when stuck.** Triangulate Soviet + Western. The Soviet text for depth, the Western for clarity, the problem book for fluency.

4. **Re-prove from memory weekly.** Pick a major theorem each week and reproduce the proof on paper, closed-book. The gold standard for "actually learned" versus "passively followed."

5. **Write your own summaries after each chapter.** 2–3 pages in your own words, kept in a notebook (digital or paper). These become your personal compressed Landau-Lifshitz. Reread before starting the next volume.

6. **Computational reinforcement.** Implement key results numerically when possible. Given a CS background this is high leverage: numerical experiments check that your understanding matches reality, expose where you're hand-waving, and build a parallel skill (scientific computing) that working physicists use daily.

7. **A serious study partner is worth a lot.** Soviet pedagogy depended on seminars and informal peer review. The closest substitute is a co-learner reading the same texts on roughly the same schedule. Worth actively seeking. The oral component of Landau's exam was non-negotiable; replicate it as best you can.

8. **AI tooling — bounded use.** Useful: rephrasing dense passages, dimensional sanity checks, looking up where a result is treated, suggesting alternative derivations to compare against your own, debugging numerical code. Unreliable: producing or verifying non-trivial derivations, getting signs and factors right, anything where the answer matters and you can't independently check. Do not let AI do problems for you. The point is to build the cognitive machinery; outsourcing the machine-building defeats the curriculum.

9. **Resist the urge to skip "easy" parts.** The Soviet curriculum's depth comes from never skipping anything. The chapters that look elementary are often where the load-bearing ideas hide.

10. **Verification protocol over self-grading.** A four-hour solo exam is mostly self-flattery. Bind each checkpoint to concrete failure conditions (re-derive three theorems from blank pages in 30 min each, solve five unseen problems, ideally oral with a partner). Either you pass or the block isn't done.

---

## Realistic timeline

Baseline only (Phases 1–5, theormin level):

| Effort level | Realistic completion |
|--------------|---------------------|
| Full-time, no other obligations | 5–6 years (matches Phystech core curriculum with Landau's filter) |
| Serious part-time, 20 hrs/week | 9–13 years |
| Steady part-time, 10–15 hrs/week | 13–18 years |
| Casual, 5 hrs/week | Probably never reaches theormin; pick a smaller goal |

With Phase 6 (modern QFT + GR + EFT + CMT) added:

| Effort level | Realistic completion |
|--------------|---------------------|
| Full-time | 8–11 years |
| Serious part-time, 20 hrs/week | 13–18 years |
| Steady part-time, 10–15 hrs/week | 17–24 years |

These estimates are deliberately bumped from the prior version. The original numbers were calibrated to optimistic Soviet pedagogy from inside the system; outside it, with normal life obligations and no peer cohort, work takes longer. Phystech students reached the baseline because they did nothing else for six years, surrounded by peers doing the same, mentored by working physicists. Self-study is harder; budget accordingly. Honest assessment up front saves frustration later.

Adjust downward if you have a recent rigorous physics or math degree, and downward further if you're working at this seriously embedded in a research environment (postdocs occasionally cover huge ground fast). Adjust upward if you're starting from a non-mathematical background.

---

## Minimum-viable bookshelf

If you needed only one or two books per subject to begin tomorrow:

**Math:**

- Analysis: **Zorich** vol 1 + **Demidovich** (or Tao as on-ramp)
- Linear algebra: **Shilov** + **Axler**
- ODE: **Arnold** + **Hirsch-Smale-Devaney** as scaffolding + **Krasnov**
- Complex analysis: **Markushevich** vol 1 + **Needham**
- Calc of variations: **Gelfand-Fomin**
- PDE: **Vladimirov** or **Evans**
- Functional analysis: **Kolmogorov-Fomin** + **Hall** (QM bridge)
- Tensor calc + diff geom: **Frankel**, *Geometry of Physics*
- Group theory: **Georgi**
- Math methods reference: **Hassani**
- Probability: **Shiryaev**
- Asymptotics: **Bender-Orszag**
- Numerical: **Trefethen-Bau**

**Physics:**

- General physics problems: **Irodov**
- General physics texts: **Sivukhin** (5 vols)
- Theoretical baseline: **Landau-Lifshitz** (10 vols)
- QM problem book: **Galitski et al.**, *Exploring QM*
- Western complements: **Shankar** (QM), **Sakurai** (QM), **Peskin-Schroeder** (QFT), **Kardar** (Stat Mech)
- Modern Phase 6: **Tong** (QFT notes, free), **Schwartz** (QFT), **Carroll** + **Wald** (GR), **Altland-Simons** (CMT), **Zinn-Justin** (bridge stat mech ↔ QFT)

That's ~30 core books. The full Soviet curriculum was longer. This is the high-leverage subset.

---

## The synthesis

The Soviet curriculum produced great physicists because of three conditions: (1) extraordinary selection of talent, (2) full-time focus for six years, (3) direct mentorship from working researchers in dense intellectual communities. You'll lack all three. The texts compensate partially.

The Soviet-vs-Western framing is a false binary in 2026. The Soviet tradition's contribution was a methodology — depth, problem volume, derivation discipline, geometric intuition, refusal to skip — and a set of texts that embody that methodology. The Western tradition contributes texts that are clearer, more modern, and often free. The synthesis is to use Western texts for first contact and modern frameworks (Tong, Schwartz, Hall, Altland-Simons, Hatcher) and Soviet texts where they remain uniquely deep (Landau-Lifshitz, Faddeev-Slavnov, Vasiliev, Polyakov, Zorich, Demidovich) — and to apply Soviet methodology to every text on your shelf regardless of where it was written. The methodology is what produces physicists. The book selection just optimizes the input.

Curriculum scoped and generated with Claude Opus 4.7. 




