---
type: spec
capability: economic-research
engagement: jones-act-hawaii-freight
date: 2026-09-29
status: draft          # draft | built | audited
built_with: "TBD — analysis to be built from this specification"
---
# Specification: Hawaiʻi Domestic Ocean Freight Rate Analysis

## Objective

Build a transparent Excel model that compares published Hawaiʻi ocean freight rates across direction and time and tests whether the observed directional result survives inclusion of the most directly comparable published fee.
The model must include information on both of the existing carriers as well as foreign rates where data is available. 
The model is intended to test an observable implication of the research hypothesis, not to estimate the total economic effect of the Jones Act.

# Economic Research — model specification

## Purpose

The purpose of this analysis is to determine whether available evidence supports the hypothesis that allowing foreign-flagged carriers to transport domestic containerized cargo between Honolulu and the U.S. West Coast would reduce ocean freight rates by increasing competition beyond the current Matson/Pasha market structure.

The research question is:

**Does available evidence support the hypothesis that permitting foreign-flagged carriers to transport domestic containerized cargo between Honolulu and U.S. West Coast ports would reduce ocean freight rates by increasing effective competition beyond Matson and Pasha?**

For purposes of the analysis, the counterfactual will focus specifically on allowing foreign-flagged carriers to transport domestic containerized cargo between Hawaiʻi and the U.S. West Coast rather than modeling the effect of a full Jones Act repeal.

The analysis must answer four main questions:

1. Would removing the Jones Act restriction on foreign-flagged carriers materially expand the number of carriers capable of competing for Hawaiʻi domestic cargo?
2. Are foreign carriers already serving Hawaiʻi or nearby Pacific routes positioned to enter without creating an entirely new shipping network? If so, would domestic cargo to and from Hawaii be an efficient inclusion for these carriers?
3. Is there observable evidence that increased carrier competition changes incumbent pricing or market behavior?
4. Are there other explanations, such as cargo imbalance, operating costs, economies of scale, or service differences, that could explain current rates without relying on market power?

The model is intended to test the proposed economic mechanism. It is not required to estimate an exact percentage "Jones Act premium" unless the available evidence can support such a calculation.

## Inputs — the evidence contract

| Name | Evidence / Value | Unit | Source / Purpose |
|---|---|---|---|
| `Coastwise_Restriction` | Requirement limiting domestic movement between U.S. ports to qualifying coastwise vessels | Legal rule | 46 U.S.C. §55102 |
| `Domestic_Competitor_Matson` | Matson operates domestic Hawaiʻi container service | Carrier | Matson SEC filings |
| `Domestic_Competitor_Pasha` | Pasha is identified by Matson as its primary Jones Act container competitor in Hawaiʻi | Carrier | Matson SEC filings |
| `Foreign_Carriers_Hawaii` | Foreign carriers including ONE and CMA CGM serve Hawaiʻi with international cargo | Carrier/network evidence | Carrier schedules / Matson filings |
| `MAT_WB_2025` | 7,276 | USD per 40' container | Matson 2025 household-goods tariff, West Coast → Honolulu |
| `MAT_EB_2025` | 4,254 | USD per 40' container | Matson 2025 household-goods tariff, Honolulu → West Coast |
| `MAT_WB_2026` | 7,476 | USD per 40' container | Matson 2026 household-goods tariff, West Coast → Honolulu |
| `MAT_EB_2026` | 4,354 | USD per 40' container | Matson 2026 household-goods tariff, Honolulu → West Coast |
| `MAT_WHARF_2025` | 349.41 | USD per 40' container | Matson 2025 tariff |
| `MAT_WHARF_2026` | 363.74 | USD per 40' container | Matson 2026 tariff |
| `Pasha_40_CargoNOS_2026` | 11,017 | USD per 40' container | Pasha tariff 980000-006, Cargo NOS, West Coast → Hawaiʻi |
| `Hawaii_Competition_Discount_2016` | 15% | percent discount | APL v. Matson factual record; Matson response to Pasha competition |
| `Hawaii_Competition_Discount_2018` | 20% / 25% | percent discount | APL v. Matson factual record |
| `Guam_Matson_Share_2016` | 94% | market share | APL v. Matson factual record |
| `Guam_Matson_Share_2017` | 82% | market share | APL v. Matson factual record |
| `Guam_Matson_Share_2018` | 74% | market share | APL v. Matson factual record |
| `Guam_APL_Rate_Difference` | approximately 40% lower in documented Home Depot comparison | percent | APL v. Matson factual record |
| `Guam_APL_Transit_Difference` | approximately 7 days slower in documented Home Depot comparison | days | APL v. Matson factual record |
| `GAO_Counterevidence` | Domestic carriers and industry participants reported relatively stable rates / adequate number of carriers in some noncontiguous markets | qualitative | GAO-22-105391 |
| `Directional_Cargo_Data` | TBD if reliable data can be located | TEU / containers | Port, government, or carrier data |

Any additional input added to the analysis must include a source and must identify whether it is a primary source, government analysis, court record, carrier statement, or secondary source.

## Structure

The analytical workbook should contain the following sheets:

- **Sources** — one row for each source, including source name, URL, date, type, primary use, and major limitation.
- **Market Structure** — current domestic carriers, relevant foreign carriers, service information, and evidence regarding whether additional carriers could plausibly enter the market.
- **Rates** — published rate observations, equipment type, commodity, direction, effective date, mandatory charges, and comparability status.
- **Competition Evidence** — observable competitive events including Matson/Pasha Hawaiʻi pricing behavior and APL/Matson Guam market behavior.
- **Analysis** — calculations used to test directional pricing, market-share changes, and other quantitative claims.
- **Figures** — only the figures ultimately needed to support the four-page paper.
- **Evidence Matrix** — summary of which evidence supports or challenges each part of the hypothesis.

The workbook should be simple enough that each important result can be traced back to a source and reproduced manually.

## Calculation logic

### Directional rate analysis

For each comparable Matson tariff year:

`RATE_GAP = WESTBOUND_RATE - EASTBOUND_RATE`

`WESTBOUND_PREMIUM = (WESTBOUND_RATE / EASTBOUND_RATE) - 1`

For 2025:

`RATE_GAP = 7,276 - 4,254 = 3,022`

`WESTBOUND_PREMIUM = (7,276 / 4,254) - 1 ≈ 71.0%`

For 2026:

`RATE_GAP = 7,476 - 4,354 = 3,122`

`WESTBOUND_PREMIUM = (7,476 / 4,354) - 1 ≈ 71.7%`

If wharfage is included:

`TOTAL_RATE = BASE_OCEAN_RATE + WHARFAGE`

The analysis must clearly distinguish the published base ocean rate from any all-in rate calculation.

### Market-share change

For the Guam comparison:

`MARKET_SHARE_CHANGE = CURRENT_YEAR_SHARE - PRIOR_YEAR_SHARE`

Example:

2016 to 2018:

`74% - 94% = -20 percentage points`

The Guam market-share analysis is intended to show whether a new entrant can win meaningful business in a Pacific island freight market. It does not estimate what Hawaiʻi market share would become under a policy change.

### Price / service tradeoff

Where the Home Depot Guam evidence is used, the analysis should report both:

- documented rate difference; and
- documented transit-time difference.

The lower rate must not be presented without the slower service because the customer decision involved both price and service quality.

### Rate comparability

A cross-carrier rate comparison is considered directly comparable only if the observations have:

- the same or reasonably equivalent commodity;
- the same equipment size/type;
- the same move type;
- comparable origin and destination;
- similar effective periods;
- equivalent treatment of mandatory fuel, wharfage, and terminal charges.

If those conditions are not met, the observation may still be reported as descriptive evidence but must not be used to calculate a carrier-to-carrier price premium.

For example:

Pasha's 2026 `Cargo, NOS` 40-foot rate must **not** be directly compared with Matson's 40-foot household-goods rate because the commodity categories differ.

## Analytical logic

The hypothesis will be evaluated as a three-step mechanism.

### Step 1 — Restriction to potential entry

Determine whether the current coastwise restriction excludes carriers that could otherwise plausibly participate in domestic Honolulu–West Coast transportation.

Evidence should include:

- the legal restriction;
- current foreign carrier service to Hawaiʻi;
- relevant transpacific / West Coast networks;
- operational barriers that would remain even if the legal barrier were removed.

The analysis should distinguish between:

- a carrier being legally eligible; and
- a carrier actually having an economic reason to enter.

### Step 2 — Entry to increased competition

Determine whether additional carrier entry has previously changed market behavior.

Primary evidence:

- Matson's Hawaiʻi household-goods discounts introduced in response to Pasha competition;
- APL entry into Guam;
- resulting changes in Matson market share;
- documented incumbent pricing responses.

The analysis should answer:

**When another credible carrier becomes available, do customers shift volume and does the incumbent respond?**

### Step 3 — Competition to freight rates

Determine whether observable competitive pressure is associated with lower offered or realized prices.

Evidence may include:

- loyalty discounts;
- price responses to new entrants;
- customer switching;
- foreign-carrier cost differences;
- published tariffs where genuinely comparable.

The analysis should not assume that all cost savings pass through to customers.

## Conventions

- "Westbound" means U.S. West Coast → Hawaiʻi.
- "Eastbound" means Hawaiʻi → U.S. West Coast.
- The primary market examined is containerized ocean freight between Honolulu and the U.S. West Coast.
- Published tariffs are observable standardized prices but are not assumed to equal average realized customer prices.
- Negotiated contracts, loyalty discounts, and other commercial arrangements may cause realized prices to differ from published tariffs.
- A directional freight-rate gap is **not** described as a Jones Act premium.
- A lower foreign-carrier cost structure does not automatically imply an equal reduction in customer freight rates.
- Hawaiʻi market concentration is not by itself proof of market power.
- The presence of two main domestic carriers is treated as evidence of market structure, not as proof that prices are supracompetitive.
- Guam is a comparator used to test the competitive mechanism; it is not treated as a controlled experiment for Hawaiʻi.
- Puerto Rico evidence, if used, is secondary comparator evidence and must be described with GAO's limitations.
- Carrier statements in SEC filings are treated as management disclosures or risk assessments, not independent proof of the predicted outcome.
- Court records must distinguish established factual evidence from allegations or disputed legal claims.
- Service quality matters. Price comparisons should consider differences in transit time, frequency, reliability, and network coverage where data are available.
- No missing value may be silently estimated.
- No rate should be normalized using an assumed surcharge unless that assumption is explicitly stated and sourced.

## Validation rules

- Every numerical value used in the analysis must trace to a listed source.
- All calculations must use source values rather than rounded values where exact values are available.
- The Matson 2025 directional analysis must calculate a $3,022 base-rate gap and approximately 71.0% westbound premium.
- The Matson 2026 directional analysis must calculate a $3,122 base-rate gap and approximately 71.7% westbound premium.
- Including the same Honolulu wharfage in both directions must leave the dollar gap unchanged.
- No Pasha Cargo NOS rate may be directly compared against a Matson household-goods rate as an equivalent commodity.
- Any Guam market-share calculation must clearly state that Guam is a comparator rather than a Hawaiʻi causal estimate.
- Any use of the approximately 40% APL/Matson Guam price difference must also disclose the approximately seven-day transit-time difference from the same customer comparison.
- The APL v. Matson court outcome must not be represented as finding the competitive practices unlawful.
- At least one credible piece of evidence that challenges the initial hypothesis must be included.
- The analysis must distinguish between evidence supporting the proposed mechanism and evidence estimating the magnitude of the effect.

### Acceptance gates

**Gate 1 — Entry plausibility**

The research must identify at least one credible foreign-carrier network or existing Hawaiʻi service that demonstrates that the set of potential suppliers would expand under the counterfactual.

Failure condition:

If no economically plausible carrier can be identified, the hypothesis that legal eligibility would materially increase competition must be weakened.

**Gate 2 — Competitive response**

At least one sourced observation must demonstrate that increased carrier competition resulted in an observable incumbent response, such as a discount, rate adjustment, or market-share change.

Current expected evidence:

Matson's response to Pasha competition in Hawaiʻi and/or APL entry into Guam.

Failure condition:

If additional competition produces no meaningful pricing or volume response, the proposed competitive mechanism is weakened.

**Gate 3 — Alternative explanation**

The analysis must test at least one non-market-power explanation for current freight rates.

Possible alternatives include:

- directional cargo imbalance;
- equipment repositioning;
- high fixed costs;
- economies of scale;
- differences in service frequency;
- transit time;
- reliability.

Failure condition:

If an alternative explanation fully explains the observed evidence, the competition hypothesis must be qualified or rejected.

**Gate 4 — Comparability**

No major quantitative conclusion may depend on a rate comparison that fails the commodity, equipment, route, time-period, or mandatory-charge comparability tests.

Failure condition:

Remove the comparison rather than force a normalization that the underlying data cannot support.

**Gate 5 — Causality**

The analysis must not calculate or label a "Jones Act premium" unless the research design can isolate the law's causal price effect.

Current expectation:

The available evidence may support the direction of the competition mechanism without supporting a precise causal magnitude.

**Gate 6 — Counterevidence**

At least one serious finding that could weaken the hypothesis must survive into the final evidence matrix and paper.

The analysis fails this gate if all evidence is selected only because it supports the initial hypothesis.

## Planned figures

### Figure 1 — Directional Hawaiʻi Container Rates

Compare Matson's published 40-foot household-goods rates:

- 2025 West Coast → Honolulu
- 2025 Honolulu → West Coast
- 2026 West Coast → Honolulu
- 2026 Honolulu → West Coast

Units:

USD per 40-foot container.

Purpose:

Show that the existing market has a large and persistent directional pricing difference consistent with asymmetric demand, capacity, or other directional economics.

The figure must **not** be labeled or interpreted as showing the size of a Jones Act premium.

### Figure 2 — Competitive Entry Evidence

Preferred figure if the data are sufficiently reliable:

Matson Guam market share:

- 2016: 94%
- 2017: 82%
- 2018: 74%

Purpose:

Show that entry by APL coincided with a meaningful change in incumbent market share.

The figure may be supplemented in the paper with the documented price-versus-transit-time tradeoff.

If the Guam figure does not materially add to the final four-page argument, it may be omitted. The project should prioritize clarity over number of figures.

## Evidence matrix

The finished analysis should include a table with the following columns:

| Evidence | Mechanism tested | Supports hypothesis? | Challenges hypothesis? | Direct or comparator | Major limitation |
|---|---|---|---|---|---|

Expected evidence categories:

- coastwise legal restriction;
- Matson/Pasha market structure;
- foreign carriers already serving Hawaiʻi;
- Matson directional tariffs;
- Matson discount response to Pasha;
- APL entry into Guam;
- Guam market-share changes;
- Guam customer price/service comparison;
- Matson SEC disclosure regarding lower-cost foreign competition;
- GAO counterevidence.

The evidence matrix is intended to help determine which evidence actually belongs in the four-page paper.

## Outputs

The analysis should produce:

- a sourced description of the current Hawaiʻi container-market structure;
- a list of plausible foreign-carrier entrants or relevant existing networks;
- the 2025 and 2026 Matson directional-rate calculations;
- one directional-rate figure;
- one competition/entry figure if it materially improves the argument;
- an evidence matrix identifying the strongest supporting and opposing evidence;
- a short table of the quantitative findings that may be cited in the paper.

The analytical model should not produce the final conclusion or recommendation automatically.

The final paper should use only the subset of findings necessary to answer the research question within the four-page limit.

One figure to include: Westbound, foreign carriers add limited capacity at the low marginal cost of an otherwise-empty slot, shifting supply right (P₀ to P₁). Eastbound, no foreign service sails Honolulu to the West Coast and the leg already has spare capacity, so price is unchanged. With a duopoly, entry would also narrow incumbents' markup over cost.

## Out of scope

Unless the research question is later expanded, the model will not attempt to calculate:

- the total economic cost or benefit of the Jones Act to Hawaiʻi;
- the exact impact of ocean freight on Hawaiʻi's overall cost of living;
- the exact effect of freight rates on retail shelf prices;
- total U.S. maritime employment effects;
- shipbuilding-industry effects;
- national-security or military-sealift value;
- the nationwide effect of full Jones Act repeal;
- a precise percentage reduction in Hawaiʻi freight rates without sufficient causal evidence.

These issues may be acknowledged in the paper where relevant but will not be primary outputs of the analysis.

## Audit findings

Added **after** the analysis is built.

For each acceptance gate and validation check document:

- what was checked;
- what was found;
- whether the check passed;
- any error discovered;
- any correction made;
- whether the specification itself needed to change;
- any remaining limitation that could affect the paper's conclusion.

