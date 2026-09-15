@ericcarmichael-bot

Reviewed below, criterion by criterion. This is entered.

CRITERION BY CRITERION

* **Spec completeness — inputs, structure, calculation flow** — Named contract complete with values, units and sources; both costing conventions correct — the farmer's hours consumed first, and the P&L at the blended rate with the split treated as a farm-level fact. Three inputs are printed display values.
* **Spec validation rules** — Structural rules only, and they are the right ones. No check figures as acceptance criteria before the build, and no q = 1 hand check. The brute-force comparison in the audit came after the answer was known, which makes it a comparison rather than an acceptance criterion.
* **Workbook satisfies the contract** — 868 formulas, 31 named ranges, no error cells, live constraints sheet, mix right at 10/20/30. Profit $13.50 high.
* **Audit note** — Nine checks now, and the new one found a real conceptual defect rather than confirming a passing result — see below. Eight checks. Two are better than the assignment asks: you preserved the spec's own misspellings in the named ranges **because the spec is the contract**, and you flagged the fixed-cost allocation as an assumption you want reviewed, with the one-line change that would reverse it.

**YOU CAUGHT THE AVERAGE-VERSUS-MARGINAL ERROR, WHICH IS THE ONE THIS CASE IS ABOUT**

Your marginal-profit table had been pricing every incremental bed's labor at the farm-wide **blended**
rate of $19.73/hr. Blended is an average. A marginal decision has to be priced at the marginal wage —
once cumulative hours pass 720, the next hour costs $17.36, not $19.73, and never the average of the
two.

You found it, and you found it the right way: the table contradicted its own neighbouring column.

> which produced a tomato crossover between bed 9 (+$688.37) and bed 10 (−$453.46) — directly
> contradicting the sheet's own cumulative-profit column (which peaked at bed 9, not bed 10) and the
> "Solver-selected" label sitting on bed 10

Three things in the same workbook disagreed, and instead of trusting the one that was easiest to read
you worked out which was wrong. Then you wrote the convention down so it cannot drift back:

> Blended-rate costing applies only to P&L / profit-per-crop reporting … For marginal (cross-over)
> analysis … labor must be priced at the true marginal wage of the next hour, not the average.

That is correct, it is stated at the right level of generality, and *"using the blended average as a
marginal cost understates true marginal profit near a crop's cap and can misidentify the optimal bed
count"* is precisely the consequence.

Your hand-check reproduces exactly against my model:

| Quantity | Yours | Mine |
|---|---|---|
| Tomato bed 10 marginal hours | 424.43 | 424.4306 |
| Tomato bed 10 MC | $8,248.59 | $8,248.59 |
| Bed 10 marginal profit | +$551.41 | +$551.41 |
| Tomato bed 11 MC | $9,390.72 | $9,390.72 |
| Bed 11 marginal profit | −$590.72 | −$590.72 |

Defining "farm-wide" by holding the other two crops at their solved bed counts — and checking that any
two crops together already exceed 720 hours — is the right resolution of a genuine ambiguity, and
implementing it as a live tiered formula rather than hard-coding the temp rate is what keeps it true
if the mix moves.

**ONE DIAGNOSIS IS BACKWARDS, AND IT POINTS AT SOMETHING LARGER**

You attribute the gap between your hand-check and your workbook to hours precision:

> the ~$0.50 difference is the hand-check rounding marginal hours to 2 decimals before multiplying

It is the other way round. Your hours are fine — 424.43 against my 424.4306 is worth about a hundredth
of a cent. The gap is the **wage**:

- 424.4306 × **$17.36** + $880 = $8,248.11 ← your workbook
- 424.4306 × **$17.3611…** + $880 = $8,248.59 ← your hand check

$17.36 is a rounded display of `25,000 / 1,440`. The hand check is the accurate one.

The same root cause explains something bigger: your workbook returns **$42,775.16** where the model
returns **$42,761.66**. That $13.50 is exactly what you get from rounding all three of the case's
displayed values — carrot hours 0.833 instead of `2.5/3`, and both wage rates. I verified each variant
separately:

| Inputs | Profit |
|---|---|
| All three exact | $42,761.66 |
| Wages rounded only | $42,768.33 |
| Carrot hours rounded only | $42,768.49 |
| **All three rounded** | **$42,775.16** ← yours |

Derive all three and both discrepancies close at once.

**WHERE THIS LEAVES YOU**

The rounded inputs are the only thing standing between this and the high 90s, and they are three
cells. What you did on the marginal-rate question is the more valuable half of this stage, and it is
the half that cannot be fixed by editing three cells.

---

**How to reply to this review.** Comment on this pull request with what you changed, or push another
commit to `main` and say so here. If you disagree with something, say that too — a disagreement you
can support is worth more to me than a correction you make because I asked. This stage is still open.

