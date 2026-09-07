<!-- PR TARGET: https://github.com/ericcarmichael-bot/eric-carmichael | Stage 1.1 -->
# Stage 1.1 review — engagement brief

**Brief:** [`docs/briefs/perfect-competition-brief.md`](https://github.com/ericcarmichael-bot/eric-carmichael/blob/main/docs/briefs/perfect-competition-brief.md)

> Re-graded 2026-09-04 against your revision of this morning. You have been reviewed on this before. You restructured the problem section and added a tolerance band, and both were exactly right. You also added one line of arithmetic that is wrong in an important way, and I want to be precise about it because you are about to build a model on top of it.

| Criterion | Where it stands |
|---|---|
| Problem restated in your own voice | The case table moved into its own clearly labelled Case data section and the problem section became prose in your own voice. That is the right fix and it is the fix I did not name — I said transcription is not restatement, and rather than delete the table you separated the two jobs, so the reader gets your reading of the trade-offs and still has the numbers to hand. "Mesclun sits in the middle on price, tied with tomatoes for fertilizer costs and has half the labor hours required" is you thinking about the crop, not copying a row. |
| Hypothesis names a specific mix | Eight tomato, 20 carrot, 30 mesclun, 58 beds, six idle and explained. Unchanged. |
| Economic mechanism | Unchanged, and it is unchanged deliberately — see the section below. The substitution argument is still the best framing anyone brought to this stage. The new sentence putting a number to the compounding is the right instinct and the wrong number, and I have not counted it against you because the surrounding argument does not depend on it. |
| Falsifiability and process | "I would treat 6-10 beds planted as a confirmation that my reasoning was directionally correct with my crossover off by a bed or two. A planting result of 5 beds or less or 11 beds or more would mean that the underlying assumptions are wrong and not just the estimate." That is a band, a reason for its width, and a statement of what falls outside it meaning something different in kind. It is the distinction between being slightly off and being wrong, decided in advance. |

### The arithmetic line, and why it matters before you build

You wrote: "with a 10% compounding diminishing returns rate, the 8th tomato bed will generate 0.9^7 = 47.8% of the return that the first bed did while still shouldering the same 2.5 labor hrs/week/bed. So essentially, bed 8 is spending the same on labor and fertilizer costs while only generating half the revenue."

The diminishing-returns rate does not reduce revenue. It multiplies labor hours. Every bed of tomatoes sells for $8,800 whether it is the first bed or the twentieth — that is what being a price taker means, and the price is fixed by assumption in this case. What changes is the cost side: the eighth tomato bed needs more hours than the first, and the whole crop's hour requirement is q x 2.50 x 36 x 1.10^q.

So the direction of your conclusion is right and the mechanism behind it is inverted. Revenue is flat and cost rises; you have written cost flat and revenue falling. Both stories predict that tomatoes stop before the cap, which is why the error is easy to miss — but they predict it for opposite reasons, and a workbook built on the wrong one will not reproduce the case's figures.

The version you want: one tomato bed takes 2.50 x 36 = 90 hours. Eight beds take 8 x 2.50 x 36 x 1.10^8, about 1,543 hours — not 720. Per bed that is roughly 193 hours against the first bed's 99. So the eighth bed costs about twice as much labor as the first while earning exactly the same $8,800. That is your sentence, with the arithmetic pointing the right way.

### Why I did not count it against you

Two reasons, and they are both worth knowing.

The first is that scores in this course never go down. You were re-graded upward for the problem section and the tolerance band, and a mistake introduced in the same revision does not claw that back.

The second is that the argument you built the brief on does not rest on the bad line. Your case for 8 tomato beds was always "attractive first, declines fastest" plus the substitution point about mesclun — neither of which needs the 0.9^7 figure. The line is an attempt to quantify an argument you had already made correctly in words. Fix the line and nothing else in the brief has to move.

One student in this cohort has this same misreading — diminishing returns as a cut to harvest rather than a rise in labor — sitting in a specification he is about to build from, and it is the single most consequential error available in this case. Catching it now costs you ten minutes.

### Stage 1.2 is the next deliverable

capabilities/marginal-analysis/spec.md is still a stub. The specification is the deliverable that carries the most weight in that stage — the workbook is built from it, and the rule is that when a check fails you correct the specification and regenerate rather than patching the sheet.

Write the labor function into it explicitly, with the exponent on q, and write a hand-check underneath: one tomato bed is 99 hours, ten tomato beds are 2,334.37. Those two lines would have caught this morning's arithmetic before it reached the page.

---

### How to work this review

Treat this PR the way an analyst treats feedback from a senior reviewer — a review is a proposal to engage with, not a checklist to rubber-stamp.

1. **Read it yourself first.** Form your own view before you change anything. Disagreeing *with a documented reason* is a legitimate, senior response.
2. **Stress-test it with an LLM.** Paste this review and your brief into your assistant and ask it to (a) explain anything you are unsure of, and (b) argue the *other side* — where might the reviewer be wrong, and what would you give up by making each change.
3. **Then write the changes yourself.** For a brief this matters more than usual: a hypothesis you did not generate cannot be honestly compared against your model in Stage 3, and that comparison is the entire point of writing the brief first.
4. **Close the loop.** Reply in this thread with what you changed and what you pushed back on, then commit and push.

*One standing rule: do not revise your hypothesis to match what your model later tells you. If the model contradicts the brief, that is a finding, not an error.*

*Your score and the per-criterion breakdown are in your Lamaku comment, not here — this repository is public.*

— Adam
