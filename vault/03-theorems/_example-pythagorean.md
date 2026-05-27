---
type: theorem
theorem: "Pythagorean theorem (Euclidean)"
book: example
date: 2026-05-26
result: passed
time_minutes: 8
tags: [example]
---

# Example: Pythagorean theorem

> This file is an example of the format. Delete or replace once you have real entries.

## Statement

For a right triangle with legs $a, b$ and hypotenuse $c$:
$$a^2 + b^2 = c^2.$$

## Proof (rearrangement)

Construct a square of side $a + b$ in two ways:

1. As four copies of the right triangle (area $\tfrac{1}{2}ab$ each, total $2ab$) plus the inner square on the hypotenuse (area $c^2$). Total: $c^2 + 2ab$.
2. As four copies of the right triangle plus two squares on the legs ($a^2$ and $b^2$). Total: $a^2 + b^2 + 2ab$.

Both equal $(a+b)^2$, so $c^2 + 2ab = a^2 + b^2 + 2ab \implies a^2 + b^2 = c^2$. $\blacksquare$

## Attempts

| Date       | Result | Time | Notes                         |
|------------|--------|------|-------------------------------|
| 2026-05-26 | passed | 8m   | First attempt, smooth         |

## Connections

- Underlies: norm of inner product spaces — [[norm-definition]]
- Generalizes via: law of cosines
