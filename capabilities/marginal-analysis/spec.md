---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-09-08
status: audited          # draft | built | audited
built_with: "Claude Code, from this file"
---

# <Capability> — model specification

## Purpose
The purpose of this model is to determine the optimal ratio of planted crops for a farm to plant for a single season. The model must answer the specific number of beds to plant for Tomatoes, Carrots and Mesclun.

## Inputs — the named contract
| Name | Value | Unit | Source |
|---|---|---|---|
| 'Tomato_Bed_Cap' | 20 | number of beds | Case scenario, crop table |
| 'Tomato_Price' | 8800 | USD per bed | Case scenario, crop table |
| 'Tomato_Hours' | 2.5  | hours per week per bed | Case scenario, crop table |
| 'Tomato_Fertizer' | 880 | USD per bed | Case scenario, crop table |
| 'Tomato_Dim_Return' | 0.10 | percent of compounding diminishing returns per bed | Case scenario, crop table |
| 'Carrot_Bed_Cap' | 20 | number of beds | Case scenario, crop table |
| 'Carrot_Price'| 2094 | USD per bed | Case scenario, crop table |
| 'Carrrot_Hours'| 0.833 | hours per week per bed | Case scenario, crop table |
| 'Carrot_Fertilizer' | 440 | USD per bed | Case scenario, crop table |
| 'Carrot_Dim_Return' | 0.025 | percent of compounding diminishing returns per bed | Case scenario, crop table |
| 'Mesclun_Bed_Cap' | 30 | number of beds | Case scenario, crop table |
| 'Mesclun_Price' | 2700 | USD per bed | Case scenario, crop table |
| 'Mesclun_Hours' | 1.25 | hours per week per bed | Case scenario, crop table |
| 'Mesclun_Fertilizer' | 880 | USD per bed | Case scenario, crop table |
| 'Mesclun_Dim_Return' | 0.0125 | percent of compounding diminishing returns per bed | Case scenerio, crop table |
| 'Season' | 36 | number of weeks | Case scenario, farm table |
| 'Fixed_Costs' | 20000 | USD per season | Case scenario, farm table |
| 'Beds_Available' | 64 | Total beds available to plant this season | Case scenario, farm table |
| 'Farmer_Hours' | 720 | hours available to work per season | Case scenario, farm table |
| 'Farmer_Cost' | 34.72 | USD per hour worked | Case scenario, farm table |
| 'Temp_Worker_Count' | 4 | number of available temporary workers, cannot exceed this amount | Case scenario, farm table |
| 'Temp_Worker_Cost' | 17.36 | USD per hour worked | Case scenario, farm table |
| 'Temp_Worker_Hours_Each' | 1440 | hours available to work for EACH temp worker | Case scenario, farm table |
| 'Labor_Hours_for_q_beds_of_one_crop | Labor(q) = q x hours per week per bed x 36 x (1+dimishing return rate)^q | formula for case | Case scenerio |

## Structure
 - Create an excel workbook
 - Create a crop table on the top of the sheet that lists all of the known values above. The table must be formatted in an easy-to-read way.
 - Every cell in the file outside of the known values must contain a formula and not a constant.
 - Create a separate sheet that lists all of the constraints known to this case from the information outlined in the inputs above.
 - Create a separate output area, defined by professional formatting, that will show the optimal crop mix and the mechanisms that drive the cross-over point for each particular crop
 - User will use solver plug-in to solve for the optimal crop mix, format the file to easily input into excel's solver add-in

## Calculation logic

For each of the crops, use the following formula to determine the number of beds that is optimal.

LABOR_HRS(q) = q x HRS_PER_BED x WEEKS x (1 + DIM_PCT)^q

For example, with tomatoes, the input logic would read: Labor_Hours(q) = q x 'Tomato_Hours' x 'Season' x ( 1 + 'Tomato_Dim_Return')^q

### Marginal cost and cross-over

Marginal profit for bed q = 'Price' − 'Fertilizer' − (Marginal_Labor_Hours(q) × Marginal_Rate),
where Marginal_Labor_Hours(q) = Labor(q) − Labor(q−1) and Marginal_Rate is 'Temp_Worker_Cost'
once cumulative farm-wide hours have already passed 'Farmer_Hours', else 'Farmer_Cost'.

Hand-check (tomatoes, at the optimal mix where farmer hours are already spent elsewhere):
bed 10 → 424.43 marginal hrs × $17.36 + $880 fertilizer = $8,248.59 MC → +$551.41 marginal
profit. Bed 11 → 490.22 marginal hrs × $17.36 + $880 = $9,390.72 MC → −$590.72 marginal profit.
Cross-over falls at bed 10, matching Solver's selection.

## Conventions
 - Beds must be whole numbers; no partial beds planted
 - The farmer's hours 'Farmer_Hours' must be consumed first before hiring additional temp labor
 - The P&L allocates labor at the blended rate. Total labor dollars/total hours. The permanent vs temporary split is farm level and not per crop
 - Diminishing returns compound on the labor hours and not on the price
 - Fertilizer costs are linear with no compounding effects or diminishing returns
 - One planting per season with no mid-season course corrections available
 - Blended-rate costing applies only to P&L / profit-per-crop reporting.
 - For marginal (cross-over) analysis, determining whether one more bed is worth planting,labor must be priced at the true marginal wage of the next hour, not the average: once cumulative farm-wide labor hours exceeds 'Farmer_Hours' (720), every additional hour is temp labor at 'Temp_Worker_Cost' ($17.36/hr), not the blended rate. Using the blended average as a marginal cost understates true marginal profit near a crop's cap and can misidentify the optimal bed count.

## Validation rules
 - Every calculated cell contains a formula
 - Total number of beds planted cannot exceed 64
 - Total labor hours cannot exceed the farmers' total plus the temp labor total (720+1440*4) or 6480 hours

## Outputs
 - Total number of beds per each of the crops for optimal profit
 - Profit per each of the crops

## Audit findings
Added AFTER the build. For each check: what you checked, what you found, what
you did about it.

- **Named ranges.** Checked every input in the named contract exists as a workbook-level named
  range pointing at the `Inputs` sheet. Found all 22 present and correctly resolved, including
  the two named ranges that preserve exact spec spelling/typos (`Tomato_Fertizer`,
  `Carrrot_Hours`) — kept as-is rather than "corrected," since the spec calls these out as the
  literal named contract. Also named the three decision cells (`Tomato_Beds`, `Carrot_Beds`,
  `Mesclun_Beds`) and five key computed cells (`Total_Beds`, `Total_Labor_Hours`,
  `Total_Labor_Cost`, `Blended_Labor_Rate`, `Total_Farm_Profit`) for auditability and for
  Solver's constraint/objective references. 31 named ranges total.

- **"Every cell a formula" rule.** Checked every cell outside the named inputs. Found it holds
  everywhere except the three beds-per-crop cells (`Output!B5:B7`), which are plain values by
  design — they're Solver's changeable cells, and Excel Solver requires its variable cells to
  hold values, not formulas. Documented this on the Output sheet itself (labeled "Decision
  Variables — Solver-Adjustable Cells").

- **`Labor_Hours_for_q_beds_of_one_crop` input row.** This row in the spec's contract is a
  formula pattern (`Labor(q) = q × hrs/bed/wk × Season × (1+dim)^q`), not a single value, so it
  can't be one named range — q differs per crop and per row of the marginal-analysis table.
  Implemented it directly, per crop, wherever labor hours are calculated (Output P&L and the
  Marginal Analysis bed-by-bed tables), referencing the named crop inputs each time.

- **Fixed_Costs / blended labor rate allocation.** The 756ab47 spec update confirms labor is
  costed to each crop at the farm-wide blended rate (Total Labor $ ÷ Total Labor Hours), with the
  farmer/temp split applied at the farm level, not per crop. The spec doesn't say whether
  `Fixed_Costs` should also be split across crops — assumed **no**: Fixed_Costs is subtracted
  once at the farm level only, and "Profit per crop" (Output!G11:G13) is a contribution margin
  (Revenue − Fertilizer − blended-rate Labor Cost). This ties out exactly: `Total_Farm_Profit` =
  Σ(contribution margins) − `Fixed_Costs`, with no arbitrary allocation key needed. Flagging this
  assumption for review — if crop-level P&L should absorb a fixed-cost allocation instead, that's
  a one-line formula change in Output!G11:G13.

- **Recalculation / formula errors.** Ran LibreOffice recalculation (868 formulas). Found 0
  errors. (Environment note: this sandbox's LibreOffice install was missing the `libreoffice-calc`
  component entirely, which made every load attempt fail or hang regardless of file content —
  installed it via `apt-get install libreoffice-calc` before recalculating; unrelated to the model
  itself.)

- **Independent cross-check of the optimum.** Brute-forced the full integer bed-count search
  space (21 × 21 × 31 ≈ 13,671 combinations) in a standalone Python script, applying the same
  formulas as the workbook. Found the optimum at Tomatoes=10, Carrots=20, Mesclun=30 beds,
  Total Farm Profit = $42,775.16 — matching the workbook's `Total_Farm_Profit` cell exactly.
  Used this to pre-populate the three Solver-changeable cells so the workbook opens already at
  the answer (Solver is still fully wired up on the Output sheet to re-run or audit it).

- **Cross-over mechanism.** Checked that each crop's bed-by-bed marginal-profit table in
  `Marginal Analysis` is internally consistent with the chosen mix. Found an error: the table
  priced every incremental bed's labor hours at the farm-wide blended rate ($19.73/hr), which
  produced a tomato crossover between bed 9 (+$688.37) and bed 10 (−$453.46) — directly
  contradicting the sheet's own cumulative-profit column (which peaks at bed 9, not bed 10) and
  the "Solver-selected" label sitting on bed 10. The blended rate is the correct convention for
  P&L cost *allocation* (see Conventions), but it is an average cost, not a marginal one — and at
  the optimal mix the farmer's 720 hours are already fully committed elsewhere, so the true cost
  of one more hour is the temp-worker rate ($17.36/hr). Re-priced at the marginal rate: bed 10
  marginal profit = +$551.41 (MC $8,248.59), bed 11 marginal profit = −$590.72 (MC $9,390.72) —
  the crossover now lands correctly at bed 10, agreeing with both Solver's answer and the
  brute-force total-profit search. Corrected the `Marginal Analysis` sheet's labor-cost formula
  to price incremental hours at the marginal wage (temp rate, once cumulative farm-wide hours
  exceed `Farmer_Hours`) rather than the blended average. Carrots and mesclun use the same
  formula and were re-checked under the correction — both remain marginally profitable at their
  bed caps (the lower marginal rate only raises their marginal profit further), so their
  conclusion is unchanged.
