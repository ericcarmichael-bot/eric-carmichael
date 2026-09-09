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
| 'Mesclun_Dim_Return' | 0.0125 | percent of compounding diminishing returns per bed 
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

## Conventions
 - Beds must be whole numbers; no partial beds planted
 - The farmer's hours 'Farmer_Hours' must be consumed first before hiring additional temp labor
 - The P&L allocates labor at the blended rate. Total labor dollars/total hours. The permanent vs temporary split is farm level and not per crop
 - Diminishing returns compound on the labor hours and not on the price
 - Fertilizer costs are linear with no compounding effects or diminishing returns
 - One planting per season with no mid-season course corrections available

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
