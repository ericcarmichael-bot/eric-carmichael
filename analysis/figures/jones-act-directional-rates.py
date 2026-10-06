"""Figure: Matson Hawaiʻi household-goods base ocean rates by direction.

Built from capabilities/economic-research/spec.md, "Planned figures — Figure 1".
Inputs use the spec's evidence-contract names. Gaps and premiums are computed
from those inputs, not typed in.

Sources (USD per 40-ft container, base ocean rate, excludes wharfage):
  Matson Navigation Company. Hawaiʻi household goods tariff, effective June 1, 2025.
  Matson Navigation Company. Hawaiʻi household goods tariff, effective June 1, 2026.

Run: python analysis/figures/jones-act-directional-rates.py
Writes: analysis/figures/jones-act-directional-rates.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

# Inputs — USD per 40-ft container
MAT_WB_2025 = 7276  # West Coast -> Honolulu
MAT_EB_2025 = 4254  # Honolulu -> West Coast
MAT_WB_2026 = 7476
MAT_EB_2026 = 4354

years = ["2025", "2026"]
westbound = [MAT_WB_2025, MAT_WB_2026]
eastbound = [MAT_EB_2025, MAT_EB_2026]

# Spec calculation logic
gaps = [wb - eb for wb, eb in zip(westbound, eastbound)]  # RATE_GAP
premiums = [wb / eb - 1 for wb, eb in zip(westbound, eastbound)]  # WESTBOUND_PREMIUM

# Validation rules from the spec
assert gaps == [3022, 3122]
assert round(premiums[0], 3) == 0.710 and round(premiums[1], 3) == 0.717

WB_COLOR = "#2a78d6"
EB_COLOR = "#eb6834"
INK = "#0b0b0b"
INK_2 = "#52514e"
GRID = "#e4e3df"

fig, ax = plt.subplots(figsize=(10.3, 6.0), dpi=150)
width = 0.26
gap = 0.02
x = range(len(years))
wb_x = [i - (width + gap) / 2 for i in x]
eb_x = [i + (width + gap) / 2 for i in x]

ax.bar(wb_x, westbound, width, color=WB_COLOR, label="West Coast → Honolulu (westbound)", zorder=3)
ax.bar(eb_x, eastbound, width, color=EB_COLOR, label="Honolulu → West Coast (eastbound)", zorder=3)

for xs, vals in ((wb_x, westbound), (eb_x, eastbound)):
    for xi, v in zip(xs, vals):
        ax.text(xi, v + 120, f"${v:,}", ha="center", va="bottom", fontsize=12, color=INK)

# Bracket over each year showing the computed gap
for i, (wb, eb, g, p) in enumerate(zip(westbound, eastbound, gaps, premiums)):
    top = wb + 1150
    ax.plot([wb_x[i], wb_x[i], eb_x[i], eb_x[i]], [wb + 700, top, top, eb + 700],
            color=INK_2, linewidth=1.2, zorder=2)
    ax.text(i, top + 120, f"Gap ${g:,} · westbound {p:.1%} higher",
            ha="center", va="bottom", fontsize=11.5, color=INK)

ax.set_xticks(list(x))
ax.set_xticklabels(years, fontsize=12)
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(0, 10000)
ax.set_yticks(range(0, 10001, 2000))
ax.set_yticklabels([f"${t:,}" for t in range(0, 10001, 2000)], fontsize=11, color=INK_2)
ax.set_ylabel("Base ocean rate (USD per 40-ft container)", fontsize=12, color=INK)
ax.set_xlabel("Tariff year", fontsize=12, color=INK)
ax.set_title("Matson Hawaiʻi Household-Goods Rates by Direction", fontsize=18, color=INK, pad=12)

ax.grid(axis="y", color=GRID, linewidth=0.8, zorder=0)
for side in ("top", "right"):
    ax.spines[side].set_visible(False)
for side in ("left", "bottom"):
    ax.spines[side].set_color(INK_2)
ax.tick_params(colors=INK_2)

ax.legend(loc="upper left", bbox_to_anchor=(0.0, -0.13), ncol=2, frameon=False, fontsize=11)
fig.text(0.01, 0.01,
         "Source: Matson Navigation Company Hawaiʻi household-goods tariffs, effective June 1, 2025 and June 1, 2026. "
         "Base ocean rate only; excludes wharfage.",
         fontsize=9, color=INK_2)

fig.tight_layout(rect=(0, 0.03, 1, 1))
out = Path(__file__).with_suffix(".png")
fig.savefig(out, facecolor="white")
print(f"wrote {out}")
