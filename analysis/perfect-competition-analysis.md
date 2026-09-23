-
type: analysis
engagement: perfect-competition
capability: marginal-analysis
date: 2026-09-23
model: capabilities/marginal-analysis/model.xlsx
---

# Stage 3: Perfect Competition

All figures come from `capabilities/marginal-analysis/model.xlsx`. T

## 0. Where each finding lives in the workbook

| Finding | Cells |
|---|---|
| Marginal cost per bed, current plan | `Marginal Analysis!J` column (J = E + F) |
| Tomato MC dip (crop grown alone) | `Marginal Analysis!K10:K11` |
| Standalone AVC and profit per bed count | `Marginal Analysis!L` and `M` columns |
| Next-bed value and shadow value of each cap | `Output!E52:H54` |
| Farm slack (beds, hours, temp workers) | `Output!B59:E61` |
| Standalone vs. in-plan AVC and profit | `Output!B65:H67` |
| Acceptance checks | `Output!A41:F48` (all OK) |

---

## 1. Why tomatoes stop at 10 (P = MC)

| Bed | Marginal hrs | Marginal labor $ (temp rate) | Fert | **MC** | Price − MC | Cells |
|---|---|---|---|---|---|---|
| 9 | 366.55 | 6,363.78 | 880 | 7,243.78 | +1,556.22 | row 14 |
| **10** | **424.43** | **7,368.59** | 880 | **8,248.59** | **+551.41** | `C15, F15, J15, G15` |
| **11** | **490.22** | **8,510.72** | 880 | **9,390.72** | **−590.72** | `C16, F16, J16, G16` |
| 12 | 564.92 | 9,807.59 | 880 | 10,687.59 | −1,887.59 | row 17 |

- Total farm profit when only tomatoes change (carrots and mesclun fixed at 20/30): 8 → $40,654.03 · 9 → $42,210.25 · **10 → $42,761.66** · 11 → $42,170.95 · 12 → $40,283.36. It peaks at 10, and the drop from 10 to 11 ($590.72) matches `G16` exactly.
- Revenue per bed is flat at $8,800, so the price never falls. What rises is **hours per bed**: bed 10 needs 424 hrs and bed 11 needs 490. That's the 10% compounding in `Labor(q)`.
- The tomato cap (20) is short by 10 (`Output!D52`). 
- Figure: `analysis/figures/tomato-mc-vs-price.png`

## 2. What binds, and what relaxing it is worth

| Constraint | Used | Limit | Slack | Binds? | Value of +1 | Cells |
|---|---|---|---|---|---|---|
| Carrot cap | 20 | 20 | 0 | **Yes** | **+$352.49** (bed 21 MC $1,741.51 vs $2,094) | `Output!F53:H53`; bed 20 MC $1,688.95 = `Marginal Analysis!J59`, `G59` = +$405.05 |
| Mesclun cap | 30 | 30 | 0 | **Yes** | **+$246.47** (bed 31 MC $2,453.53 vs $2,700) | `Output!F54:H54`; bed 30 MC $2,420.10 = `Marginal Analysis!J103`, `G103` = +$279.90 |
| Tomato cap | 10 | 20 | 10 | No | $0 | `Output!B52:H52` |
| Total beds | 60 | 64 | 4 | No | $0 | `Output!B59:E59` |
| Labor hours | 5,277.22 | 6,480 | 1,202.78 hrs | No | $0 | `Output!B60:E60` |
| Temp workers | 3.16 | 4 | 0.84 | No | $0 (a 5th worker is worth nothing) | `Output!B61:E61` |

- If the carrot cap were lifted completely, Solver plants 24 carrots (10/24/30 = 64 beds) for $43,837.51 (+$1,075.85), and then **total land becomes binding**. Lifting the mesclun cap instead gives 10/20/34 = $43,541.00 (+$779.34). Carrot ground comes first.
- Figures: `analysis/figures/carrot-mc-vs-price.png`, `analysis/figures/mesclun-mc-vs-price.png`

## 3. The tomato MC dip (tomatoes grown alone)

| Bed | Cum hrs | Marginal hrs | Farmer hrs in it | Temp hrs in it | Standalone MC | Cells |
|---|---|---|---|---|---|---|
| 4 | 527.08 | 167.71 | 167.71 | 0 | $6,703.13 | `B9, C9, K9` |
| **5** | **724.73** | 197.65 | 192.92 | 4.73 | **$7,660.86** | `B10, C10, K10` |
| **6** | 956.64 | 231.91 | 0 | 231.91 | **$4,906.28** | `B11, C11, K11` |
| 7 | 1,227.69 | 271.05 | 0 | 271.05 | $5,585.71 | `B12, C12, K12` |

- Hours per bed **keep rising** the whole way (167 → 198 → 232 → 271). Diminishing returns never paused.
- The farmer's 720 hrs (`Farmer_Hours`, `Inputs!B15`) run out during bed 5 (cum 724.73). The price of the next hour halves: $34.72 → $17.36 (`Inputs!B16`, `B18`; exactly 25,000/720 vs 25,000/1,440).
- At bed 6, 17% more hours at 50% of the wage makes MC fall by $2,754.58. From bed 7 on, the 10% compounding wins again.
- The same dip shows up in each crop's standalone schedule: tomatoes at bed 6, carrots at bed 17 ($2,552.10 → $1,670.90, `K55:K56`), mesclun at beds 14–15 ($2,988.40 → $2,522.58 → $1,983.96, `K86:K88`).
- **Why it doesn't show in the 10/20/30 plan:** with all three crops planted, farm-wide hours pass 720 before the tomato table starts, so every tomato hour is a temp hour (`J` column; blue line in the tomato figure). The dip is about *which* hours are marginal. In the plan, the farmer's hours are infra-marginal.

## 4. Why grow crops that "lose money"

| Crop | Beds | Price | Standalone AVC | In-plan AVC | Standalone profit after $20k | In-plan contribution | P > AVC? |
|---|---|---|---|---|---|---|---|
| Tomatoes | 10 | 8,800 | 6,182.72 | 5,485.66 | **+6,172.77** | 33,143.42 | Yes |
| Carrots | 20 | 2,094 | 1,918.45 | 1,409.89 | **−16,488.92** | 13,682.27 | Yes |
| Mesclun | 30 | 2,700 | 2,430.74 | 2,168.80 | **−11,922.19** | 15,935.98 | Yes |

Cells: `Output!A65:H67`

- Carrots and mesclun lose money at **every** quantity when grown alone (`Marginal Analysis!M40:M59` and `M74:M103`, all negative).
- **Correction to the page:** tomatoes alone are *not* a loss everywhere. They're profitable at 7–13 beds (`M12:M18`) and peak at +$6,172.77 at 10. "Every single crop loses money alone" is true only for carrots and mesclun.
- In the plan, contribution before fixed cost is $62,761.66 in total. Subtract the $20,000 fixed cost and you get $42,761.66 (`Output!G14`, `B23`).
- Shutdown rule: produce if P ≥ AVC, and fixed cost doesn't enter the decision. The $20k is paid either way this season. Dropping carrots would throw away $13,682 of contribution toward a cost the farm pays anyway.

## 5. Stage 1 hypothesis vs. the result

| | Predicted | Model | My own test | Verdict by my test |
|---|---|---|---|---|
| Tomatoes | 8 | 10 | 6–10 = directionally right; ≤5 or ≥11 = assumptions wrong | Right, but at the very edge of the band |
| Carrots | 20 | 20 | <20 = something constraining | Right |
| Mesclun | 30 | 30 | <30 = something constraining | Right |
| Total beds | 58 | 60 | ">58 = proven incorrect" | **Wrong by my rule** |

Points to be precise about:
1. **The mechanism was wrong even though the number was close.** The brief says "the 8th tomato bed will generate 0.9^7 = 47.8% of the return that the first bed did." In the model (and in my own spec's Conventions: "Diminishing returns compound on the labor hours and not on the price"), every bed earns $8,800. The 10% compounds on **hours**, which is why bed 10 still earns +$551. If revenue had really decayed 10% per bed, bed 8 would earn $4,208 against $6,361 of MC, and the answer would be about 6 beds.
2. **The two falsification tests contradict each other.** A 10-bed tomato result passes the 6–10 band but fails the 58-bed total.
3. **Cost of the miss:** 8 tomatoes instead of 10 = $40,654.03 vs $42,761.66, which leaves **$2,107.63** on the table (4.9%).
4. **Carrots and mesclun: right answer, partly right reason.** I said "efficient use of resources." The model says P > MC at the cap, so the cap stops them, not the economics. I didn't mention the caps binding or their shadow value.
5. **Not anticipated at all:** the MC dip, and that land (4 beds) and labor (0.84 workers) are both slack.

## 6. What would change my answer?

| Change | New optimum | Profit | Δ |
|---|---|---|---|
| Base | 10/20/30 | $42,761.66 | — |
| Tomato price −20% ($7,040) | **8/20/30** | $26,574.03 | −$16,187.63 |
| Tomato price below $8,248.59 (−6.3%) | 9 tomatoes | | bed 10 no longer pays |
| Tomato price above $9,390.72 (+6.7%) | 11 tomatoes | | bed 11 starts paying |
| Carrot cap lifted | 10/24/30 (land binds) | $43,837.51 | +$1,075.85 |
| Mesclun cap lifted | 10/20/34 (land binds) | $43,541.00 | +$779.34 |
| 5th temp worker | no change | $42,761.66 | $0 |
| More total beds (caps unchanged) | no change | $42,761.66 | $0 |

Most sensitive variable: **tomato price**. Tomatoes are 53% of contribution ($33,143 of $62,762), and a ~6–7% price move shifts the plan by a bed.

