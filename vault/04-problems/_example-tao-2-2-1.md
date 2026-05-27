---
type: problem
id: tao-2-2-1
book: tao-analysis-1
chapter: 2
problem_ref: "2.2.1"
subject: real_analysis
phase: 1
date: 2026-05-26
minutes: 15
status: solved
tags: [example, phase-1, analysis, induction]
---

# Example: Tao 2.2.1 — addition is associative on N

> Example entry. Delete or replace once you have real ones.

## Statement (paraphrased)

For natural numbers $a, b, c$, show $(a + b) + c = a + (b + c)$, using only the Peano axioms and Tao's definition of addition $n + 0 := n$, $n + S(m) := S(n+m)$.

## Approach

Induct on $c$ with $a, b$ fixed.

## Solution

**Base $c = 0$:** $(a+b) + 0 = a+b$ (by definition), and $a + (b + 0) = a + b$ (also by definition). ✓

**Inductive step:** Assume $(a+b) + c = a + (b+c)$. Show $(a+b) + S(c) = a + (b + S(c))$.

LHS: $(a+b) + S(c) = S((a+b) + c)$ by definition of addition.
By inductive hypothesis: $= S(a + (b+c))$.
By definition of addition (working in reverse): $= a + S(b+c) = a + (b + S(c))$. ✓

By induction, holds for all $c \in \mathbb{N}$. $\blacksquare$

## What was hard

Resisting the urge to use commutativity (which Tao hasn't proved yet at this point). Discipline of "only what's been built so far."

## Connections

- Theorem reproved separately: [[addition-commutativity-on-N]]
- Chapter context: [[ch02-naturals]]
