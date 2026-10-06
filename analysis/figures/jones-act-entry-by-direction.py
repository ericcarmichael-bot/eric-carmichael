"""Figure: conceptual effect of foreign-flag entry, by direction.

Built from capabilities/economic-research/spec.md ("One figure to include"):
  Westbound, foreign carriers add limited capacity at the low marginal cost of
  an otherwise-empty slot, shifting supply right (P0 to P1). Eastbound, no
  foreign service sails Honolulu to the West Coast and the leg already has
  spare capacity, so price is unchanged.

Conceptual only: curves are stylized, not estimated, and the axes carry no
values. Both panels share one price scale so westbound sits above eastbound.
Demand is drawn steep (freight demand for imported staples is fairly
inelastic), so the westbound effect shows up mostly as price, not volume.

Run: python analysis/figures/jones-act-entry-by-direction.py
Writes: analysis/figures/jones-act-entry-by-direction.png
"""
from pathlib import Path

import matplotlib.pyplot as plt

S_COLOR = "#2a78d6"   # supply today
F_COLOR = "#eb6834"   # supply with foreign slots
D_COLOR = "#3d3d3a"   # demand
INK = "#0b0b0b"
INK_2 = "#52514e"
GUIDE = "#8a8984"

# Stylized inputs (axis units are arbitrary)
WB_D_INTERCEPT, WB_D_SLOPE = 11.5, -1.3     # westbound demand (steep)
WB_S_INTERCEPT, WB_S_SLOPE = 2.6, 0.35      # westbound supply today
FOREIGN_SLOTS = 1.6                          # limited foreign capacity (containers/week, stylized)
FOREIGN_MC = 1.4                             # low marginal cost of an otherwise-empty slot
EB_D_INTERCEPT, EB_D_SLOPE = 5.0, -0.75     # eastbound demand
EB_S_INTERCEPT, EB_S_SLOPE = 2.1, 0.12      # eastbound supply: spare capacity, nearly flat
X_MAX, Y_MAX = 10.0, 10.0


def cross(d0, d1, s0, s1):
    """Intersection of y = d0 + d1*x and y = s0 + s1*x."""
    q = (s0 - d0) / (d1 - s1)
    return q, d0 + d1 * q


# Westbound equilibria
q0, p0 = cross(WB_D_INTERCEPT, WB_D_SLOPE, WB_S_INTERCEPT, WB_S_SLOPE)
# With foreign slots, incumbents' supply sits to the right of the foreign block
shifted_intercept = WB_S_INTERCEPT - WB_S_SLOPE * FOREIGN_SLOTS
q1, p1 = cross(WB_D_INTERCEPT, WB_D_SLOPE, shifted_intercept, WB_S_SLOPE)
assert FOREIGN_MC < p1 < p0 and q1 > q0

# Eastbound equilibrium (no foreign eastbound service, so one supply curve)
qe, pe = cross(EB_D_INTERCEPT, EB_D_SLOPE, EB_S_INTERCEPT, EB_S_SLOPE)
assert pe < p1

fig, (ax_w, ax_e) = plt.subplots(1, 2, figsize=(12, 5.6), dpi=200, sharey=True)


def line(ax, b0, b1, x_from, x_to, **kw):
    xs = [x_from, x_to]
    ax.plot(xs, [b0 + b1 * x for x in xs], **kw)


def guides(ax, q, p, label_p, label_q=None, q_align="center"):
    ax.plot([0, q], [p, p], color=GUIDE, linewidth=1, linestyle=":", zorder=1)
    ax.plot([q, q], [0, p], color=GUIDE, linewidth=1, linestyle=":", zorder=1)
    ax.scatter([q], [p], s=70, color=INK, zorder=5, edgecolors="white", linewidths=1.5)
    ax.text(-0.15, p, label_p, ha="right", va="center", fontsize=15, color=INK)
    if label_q:
        nudge = {"right": -0.08, "left": 0.08, "center": 0.0}[q_align]
        ax.text(q + nudge, -0.25, label_q, ha=q_align, va="top", fontsize=15, color=INK)


# Westbound panel
d_start = (Y_MAX - WB_D_INTERCEPT) / WB_D_SLOPE  # where demand enters the top edge
line(ax_w, WB_D_INTERCEPT, WB_D_SLOPE, d_start, 8.6, color=D_COLOR, linewidth=2.6, zorder=3)
line(ax_w, WB_S_INTERCEPT, WB_S_SLOPE, 0, X_MAX, color=S_COLOR, linewidth=2.6, zorder=3)
ax_w.plot([0, FOREIGN_SLOTS, FOREIGN_SLOTS], [FOREIGN_MC, FOREIGN_MC, WB_S_INTERCEPT],
          color=F_COLOR, linewidth=2.6, linestyle="--", zorder=4)
line(ax_w, shifted_intercept, WB_S_SLOPE, FOREIGN_SLOTS, X_MAX,
     color=F_COLOR, linewidth=2.6, linestyle="--", zorder=4)
guides(ax_w, q0, p0, "$P_0$", "$Q_0$", q_align="right")
guides(ax_w, q1, p1, "$P_1$", "$Q_1$", q_align="left")
ax_w.text(8.7, WB_D_INTERCEPT + WB_D_SLOPE * 8.6 - 0.1, "D", fontsize=15, color=INK, va="top")
ax_w.text(X_MAX - 0.1, WB_S_INTERCEPT + WB_S_SLOPE * X_MAX + 0.25, "S (today)",
          ha="right", va="bottom", fontsize=14, color=INK)
ax_w.text(X_MAX - 0.1, shifted_intercept + WB_S_SLOPE * X_MAX - 0.45, "S (with\nforeign slots)",
          ha="right", va="top", fontsize=14, color=INK)
ax_w.annotate("Foreign slots at low\nmarginal cost (limited)", xy=(FOREIGN_SLOTS / 2, FOREIGN_MC),
              xytext=(0.3, 0.35), fontsize=12.5, color=INK_2, va="bottom")
ax_w.set_title("West Coast → Honolulu (westbound)", fontsize=16, color=INK, pad=10)

# Eastbound panel
line(ax_e, EB_D_INTERCEPT, EB_D_SLOPE, 0, 6.0, color=D_COLOR, linewidth=2.6, zorder=3)
line(ax_e, EB_S_INTERCEPT, EB_S_SLOPE, 0, X_MAX, color=S_COLOR, linewidth=2.6, zorder=3)
guides(ax_e, qe, pe, "")
ax_e.text(qe + 0.3, pe + 0.3, "P unchanged", fontsize=14, color=INK, va="bottom")
ax_e.text(6.15, EB_D_INTERCEPT + EB_D_SLOPE * 6.0 + 0.1, "D", fontsize=15, color=INK, va="center")
ax_e.text(X_MAX - 0.1, EB_S_INTERCEPT + EB_S_SLOPE * X_MAX + 0.25,
          "S (same with or without exemption)", ha="right", va="bottom", fontsize=14, color=INK)
ax_e.text(X_MAX - 0.1, 8.6, "No foreign service sails Honolulu → West Coast;\nthe leg already has spare capacity",
          ha="right", va="top", fontsize=12.5, color=INK_2)
ax_e.set_title("Honolulu → West Coast (eastbound)", fontsize=16, color=INK, pad=10)

for ax in (ax_w, ax_e):
    ax.set_xlim(0, X_MAX)
    ax.set_ylim(0, Y_MAX)
    ax.set_xticks([])
    ax.set_yticks([])
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    for side in ("left", "bottom"):
        ax.spines[side].set_color(INK_2)
        ax.spines[side].set_linewidth(1.2)
    ax.set_xlabel("Containers per week", fontsize=15, color=INK, labelpad=26)
ax_w.set_ylabel("Freight rate per container", fontsize=15, color=INK, labelpad=34)

fig.text(0.5, 0.01, "Conceptual illustration; not to scale. Does not show the size of any rate change.",
         ha="center", fontsize=12.5, color=INK_2, style="italic")
fig.tight_layout(rect=(0, 0.04, 1, 1), w_pad=4)
out = Path(__file__).with_suffix(".png")
fig.savefig(out, facecolor="white")
print(f"wrote {out}  (P0={p0:.2f}, P1={p1:.2f}, Q0={q0:.2f}, Q1={q1:.2f}, eastbound P={pe:.2f})")
