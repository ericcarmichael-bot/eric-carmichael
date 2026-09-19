Reviewed below, criterion by criterion. This is entered.

**CRITERION BY CRITERION**

* **Spec completeness — inputs, structure, calculation flow** — Both things I held back last time are closed. The heading names the capability instead of the template's unfilled `<Capability>`, and `## Structure` is now sheet by sheet — Inputs, Constraints, Marginal Analysis, Output, each with what it must hold, the rule that Inputs is the only sheet allowed typed constants, and the Solver wiring — where it used to say "Create an excel workbook". Someone else could build from this document now.
* **Spec validation rules** — Your `### Acceptance gates` block is exactly the fix: the 10 / 20 / 30 mix at tolerance zero, `Total_Farm_Profit` at $42,761.66 within a cent, the tomato bed-10 and bed-11 crossings at +$551.41 and −$590.72, each with a stated action when it fails. One point still held, and it is worth knowing why: the gates were written after the build rather than before it, and the typed acceptance targets you added at `Output!B41:B46` contradict your own structural rule that no constant lives outside the Inputs sheet.
* **Workbook satisfies the contract** — `Output!A39:F46` is a six-row target / computed / diff / tolerance / status block driven off named ranges, every row reading OK, with `Output!B48` counting the CHECK rows and returning zero — the error-count cell the half point was held for. 890 formulas, no error cells, 31 named ranges, and the cached values are present, so the blank-on-open regression you found and repaired yourself has not come back. Profit lands on $42,761.66 and both crossover figures are exact.
* **Audit note** — Already at maximum and unchanged this sweep. One tidy-up rather than a deduction: the brute-force entry under `## Audit findings` still quotes $42,775.16 as the optimum, and later entries in the same section correct it to $42,761.66. Leave the wrong figure in if you mark it as superseded — an audit trail that shows the correction is better than one that hides it.

**Repo:** https://github.com/ericcarmichael-bot/eric-carmichael
**Spec:** `capabilities/marginal-analysis/spec.md` (16,434 B) · **Workbook:** `model.xlsx` (30,006 B, 4 sheets, 890 formulas, 0 error cells, 31 named ranges) · `README.md` (790 B)

**WHAT I'D FIX FIRST**

* Write the gates before the build next time, not after it. That is the whole of the remaining point and it is a habit rather than a task — the acceptance figures are what the build has to earn, so they belong in the spec before there is a workbook to compare them against. On this stage you had the answer first and wrote the gate to match; on the next one, write the gate blind.
* Move the typed acceptance targets at `Output!B41:B46` onto the Inputs sheet, or mark them as an allowed exception in your own Structure rule. Five minutes. Your rule says no constant outside Inputs, and right now six of them sit on Output.
* Correct the stale $42,775.16 in the brute-force audit entry, or annotate it as superseded. Two minutes.

**LOOKING AHEAD**

The Stage 1.2 review is still open as a pull request on your repository, and your commits already answer it — reply in the thread with what you changed and close it. Then carry the gates-first order into Stage 1.3: the memo is an argument, and an argument has acceptance criteria too.

> **Grade history:** 88 (2026-09-10) → 90 (2026-09-12) → 93 (2026-09-17) → **99 (2026-09-18)**, after all three defects named in the 09-17 review were closed in one commit.

---
