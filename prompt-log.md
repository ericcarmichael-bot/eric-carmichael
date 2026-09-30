# Prompt Log

A record of the prompts used to draft portfolio content with AI assistance, and what was kept or changed from the output.

## Bio (README.md)

- **Prompt:** "README.md Three to six sentences on who you are and what you are working toward, then an engagement index: a short list linking each piece of work to its brief, analysis, and memo. This is the by-subject view of the repository. It lives here, never in the folder paths. Help me start these."
  - **Kept/changed:** Used the draft as a starting point, then edited it before committing.

## Resume (RESUME.md)

- Written directly, no AI assistance used.

## Specifications (SPEC.md)

Here is my model specification. Do not rewrite it, and do not fill in
anything that is missing.

1. List every place a builder would have to guess, and say what they
   would probably guess.
2. Name each term I use without defining it.
3. Ask me the questions whose answers are missing from this document.

Then stop. I will make the changes.

## Stage 3 Reflection

AI assisted me in turning the case requirements into the model deliverable. AI also help advance my knowledge by acting as an additional tutor and explaining concepts, specifically why tomatoes stop being profitable and why the mix is optimal. It also helped create marginal-cost charts, and explain the results. AI also originally incorrectly guided me towards diminishing revenue instead of the labor costs that actually affected the marginal analysis. I caught multiple issues over the course of this project that AI had generated. AI was using rounded figures to calculate the model results which output an incorrect answer. It resulted in an initial value of $42,775 instead of the correct $42,762.  Additionally, I had an instance of AI outputting a completely blank workbook. I checked the recalculated revenue by hand. Also, I checked the labor cost and profit by hand. Finally, I checked the model to ensure the optimal mix was there. Updated the workbook to change the total tomato bed numbers to 9 and 11 to ensure that 10 was the optimum. There was also an instance where Claude had incorrectly calculated the crossover point for tomatoes that I had to correct. Overall, AI is a powerful "alien-brain" that helped me understand this assignment better. It also assisted greatly in understanding the basic mechanics behind GitHub. 

## Perfect competition — Stage 3 sessions

| Date | Tool | What I asked | What I got | What I did with it |
|---|---|---|---|---|
| 2026-09-23 | Claude Code | Read the Stage 3 requirements and pull the evidence from my workbook: cell references, shadow prices, standalone P&L, the MC dip. | An evidence pack with numbers and cell citations, and a finding that my workbook priced every labor hour at the temp rate, stopped each table at the crop cap, and had no standalone P&L, so the MC dip, the bed-21/31 shadow prices and the standalone losses couldn't be cited from it. | Prepared the case analysis |
| 2026-09-23 | Claude Code | Add the missing evidence cells to the workbook and commit it. | New columns `Marginal Analysis!J:M` (marginal cost, standalone MC/AVC/profit) and `Output` rows 50–68 (shadow values, slack, standalone vs. in-plan). Existing formulas and values unchanged; acceptance checks still OK. | Checked to ensure that the evidence cells were correct|
| 2026-09-23 | Claude Code | Make MC-vs-price charts for each crop. | Three PNGs in `analysis/figures/`, drawn with Python from the workbook's formulas (not exported from Excel). | Had Claude embed these into the analysis|
| 2026-09-23 | Claude Code | Check my repo against the Stage 3 checklist; fix the figures so they render. | A checklist gap review; embedded Figures 1–3 with captions in the analysis. |Made the corrections per the suggestions |
| 2026-09-23 | Claude code | Help me draft the initial analysis and memo docs that I will then rewrite in my own words | Drafts of the deliverables | Used it to prepare the analysis |

## Individual research paper — Jones Act sessions

| Date | Tool | What I asked | What I got | What I did with it |
|---|---|---|---|---|
| 2026-09-29 | ChatGPT | Help research the Jones Act / Hawaiʻi freight question, assuming the existing decision memo remained the working direction. | Source leads and counterarguments covering Matson tariffs, Matson's 10-K, GAO, Pasha tariffs, and competition evidence from APL v. Matson. | Kept the research leads; verified the material sources before using them. |
| 2026-09-29 | ChatGPT | Keep digging for evidence more directly tied to whether additional carrier competition changes prices. | Found Hawaiʻi-specific loyalty-discount evidence tied to Pasha competition, Guam entry/market-share evidence, a Home Depot price-versus-transit-time comparison, and a Puerto Rico GAO comparator. | Shifted the research emphasis away from tariff comparisons and toward competition/entry evidence. |
| 2026-09-29 | ChatGPT | Review current Pasha tariff information I supplied and decide whether more tariff hunting was necessary. | Identified a current $11,017 40-foot Cargo NOS westbound Pasha tariff but flagged that it is not commodity-comparable with Matson's household-goods tariff. | Did not use it as a direct Matson-versus-Pasha price comparison; stopped further tariff archaeology unless it becomes necessary. |
| 2026-09-29 | ChatGPT | Finalize the GitHub setup for the research paper. | Checked the course research-paper instructions and the existing repo structure. ChatGPT had earlier drafted paper-like prose before the course AI boundary was re-checked. | Did not commit the AI-written paper prose or AI-built analysis model. Kept only compliant research support, repo scaffolding, and this log entry; the brief, spec, drafts, analysis, recommendation, paper prose, and reflection remain mine. |
| 2026-09-30 | Claude Code | Build the deliverable from my research brief and spec as a draft, meet the paper format constraints (4 pages, APA/MLA/Chicago, at least one graph), and do the additional research the spec calls for. | A draft Excel model built to the spec (sources, market structure, rates, competition evidence, analysis with validation checks, figures, evidence matrix); two figures; a formatted ~1,030-word paper draft with APA references. New research leads: DBEDT directional cargo tonnage, CMA CGM EXX and ONE AHX rotations, Pasha sailings, Reeve (2020) and Dunham (2020) studies, Drewry WCI. It also found that GAO-22-105391 covers STB regulatory processes, not the "stable rates" point in the spec. Kept in the git-ignored `scratch/` folder and not committed, per my AI boundary. | [To fill in] |
