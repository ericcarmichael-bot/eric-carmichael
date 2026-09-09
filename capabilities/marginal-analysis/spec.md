---
type: spec
capability: marginal-analysis
engagement: perfect-competition
date: 2026-09-08
status: built            # draft | built | audited
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
| 'Tomato_Dim_Return | 0.10 | percent of compounding diminishing returns per bed | Case scenario, crop table |
| 'Carrot_Bed_Cap' | 20 | number of beds | Case scenario, crop table |
| 'Carrot_Price'| 2094 | USD per bed | Case scenario, crop table |
| 'Carrrot_Hours'| 0.833 | hours per week per bed | Case scenerio, crop table |
| 'Carrot_Fertilizer' | 440 | USD per bed | Case scenario, crop table |
| 'Carrot_Dim_Return' | 0.025 | percent of compounding diminishing returns per bed | Case scenario, crop table |
| 'Mesclun_Bed_Cap' | 30 | number of beds | Case scenario, crop table |
| 'Mesclun_Price' | 2700 | USD per bed | Case scenario, crop table |
| 'Mesclun_Hours' | 1.25 | hours per week per bed | Case scenario, crop table |
| 'Mesclun_Fertilizer' | 880 | USD per bed | Case scenario, crop table |
| 'Mesclun_Dim_Return' | 0.0125 | percent of compounding diminishing returns per bed 
| 'Season' | 36 | number of weeks | Case scenerio, farm table |
| 'Fixed_Costs' | 20000 | USD per season | Case scenerio, farm table |


## Structure
Each sheet or region, and what it is for.

## Calculation logic
In named-range notation, never cell addresses:

  LABOR_HRS(q) = q x HRS_PER_BED x WEEKS x (1 + DIM_PCT)^q

"Column D times column E" is not a specification — it describes a spreadsheet
that does not exist yet.

## Conventions
The rules that are not visible in the formulas: costing order, allocation basis,
rounding, what happens at the boundaries. State all of them. A convention you
leave out is a convention the builder invents.

## Validation rules
The conditions the finished artifact must satisfy — check figures as acceptance
criteria, hand calculations, and structural rules ("every calculated cell
contains a formula", "no error cells").

## Outputs
Each result the model reports, by name.

## Audit findings
Added AFTER the build. For each check: what you checked, what you found, what
you did about it.
