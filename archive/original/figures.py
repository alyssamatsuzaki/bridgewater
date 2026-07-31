"""Figures for 'Forecasting the Future 2026' submission.
All series are first-print or as-published values; sources noted under each chart.
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import numpy as np

# ---------- shared style ----------
NAVY   = "#16324f"   # structural / primary
STEEL  = "#4878a8"   # leaning / secondary
ORANGE = "#c65d21"   # contest / accent
RED    = "#a83232"   # thresholds
GRAY   = "#8a8f98"
LGRAY  = "#c9cdd4"
INK    = "#22262b"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.5,
    "axes.edgecolor": "#b7bcc4",
    "axes.linewidth": 0.8,
    "axes.titlesize": 12,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.labelcolor": INK,
    "xtick.color": INK, "ytick.color": INK,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "svg.fonttype": "none",
})

def style_ax(ax, grid_axis="y"):
    for s in ["top", "right"]:
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color="#e8eaee", linewidth=0.8)
        ax.set_axisbelow(True)

def src(fig, text, y=0.012):
    fig.text(0.012, y, text, fontsize=7.2, color=GRAY, ha="left", va="bottom")

def save(fig, name):
    fig.savefig(f"/home/claude/ftf/figs/{name}.png", dpi=200,
                bbox_inches="tight", facecolor="white")
    plt.close(fig)

# =====================================================================
# FIGURE 1 — the portfolio at a glance
# =====================================================================
rows = [
    ("Optionality: the return on control arrives in crises", [
        (1,  "China NEV retail share >60% in 2027", 85, "S"),
        (4,  "China gasoline demand 2027 < 2026 (the ratchet)", 65, "L"),
        (5,  "MP Materials still on MOFCOM list, end-2027", 70, "L"),
        (13, "US imports from Vietnam+Thailand, 2028 < 2026", 38, "C"),
        (17, "FY2027 net customs duties > $250B", 70, "L"),
    ]),
    ("Delivery: the binding constraint is physical, not capital", [
        (3,  "Fewer than 20 of 28 LA Metro projects open by the Games", 70, "L"),
        (8,  "A hyperscaler discloses \u22651 GW of US cancellations by 2028", 65, "L"),
        (9,  "Big-four capex falls in 2028 vs 2027", 30, "C"),
        (12, "Two of four shorten server useful lives by Mar 2029", 30, "C"),
        (14, "USD/JPY moves \u226510% in 20 trading days by end-2027", 30, "C"),
    ]),
    ("Workflow data: the chokepoint employment law now governs", [
        (7,  "EU proceeding on employee-monitoring data for AI by 2028", 62, "L"),
        (10, "A non-tech Fortune 500 licenses workflow data by 2030", 30, "C"),
    ]),
    ("Migration: value moves to what stays scarce", [
        (2,  "Frontier output-token price \u221250% by end-2027", 90, "S"),
        (6,  "China >54% of global robot installs in 2027", 68, "L"),
        (11, "Chinese lab holds LMArena #1 for 30 days by end-2027", 20, "C"),
        (18, "Tech sector trails Energy/Industrials/Utilities avg in 2027", 45, "C"),
    ]),
    ("Macro: the inflation floor and the squeezed Fed", [
        (15, "Core PCE \u22653.0% in \u22656 months of 2027", 55, "C"),
        (16, "Fed funds upper bound \u22653.75% on Dec 31, 2027", 55, "C"),
    ]),
]
cls_color = {"S": NAVY, "L": STEEL, "C": ORANGE}
cls_name  = {"S": "structural", "L": "leaning", "C": "contest"}

fig, ax = plt.subplots(figsize=(8.6, 7.6))
y = 0
yt, yl = [], []
group_y = []
for gname, items in rows:
    group_y.append((y, gname))
    y -= 0.5
    for num, label, p, c in items:
        ax.hlines(y, 0, p, color=cls_color[c], lw=1.4, alpha=0.55, zorder=2)
        ax.scatter([p], [y], s=64, color=cls_color[c], zorder=3)
        ax.text(p + 2.2 if p < 88 else p - 2.2, y, f"{p}%",
                va="center", ha="left" if p < 88 else "right",
                fontsize=8.6, color=cls_color[c], fontweight="bold")
        yt.append(y)
        yl.append(f"{num}.  {label}")
        y -= 1
    y -= 0.55

# stated priors for the two forecasts where the draft quantifies one
ax.scatter([10], [yt[7]], s=60, facecolors="none", edgecolors=GRAY, lw=1.4, zorder=3)
ax.annotate("sell-side-implied \u2248 10%", (10, yt[7]), xytext=(11, yt[7] - 0.62),
            fontsize=7.6, color=GRAY)
ax.scatter([15], [yt[9]], s=60, facecolors="none", edgecolors=GRAY, lw=1.4, zorder=3)
ax.annotate("unconditional base rate \u2248 15%", (15, yt[9]), xytext=(16.5, yt[9] - 0.62),
            fontsize=7.6, color=GRAY)

for gy, gname in group_y:
    ax.text(0.5, gy, gname, fontsize=9.6, fontweight="bold", color=INK,
            ha="left", va="center")
    ax.hlines(gy - 0.42, 0, 100, color="#eef0f3", lw=0.8, zorder=1)

ax.axvline(50, color=LGRAY, lw=1.0, ls="--", zorder=1)
ax.text(50, y + 0.15, "50%", fontsize=8, color=GRAY, ha="center")
ax.set_yticks(yt)
ax.set_yticklabels(yl, fontsize=8.6)
ax.set_xlim(0, 100)
ax.set_ylim(y, 1.0)
ax.set_xlabel("Assigned probability")
ax.xaxis.set_major_formatter(mtick.PercentFormatter())
style_ax(ax, grid_axis="x")
ax.set_title("One claim, priced eighteen ways", loc="left", pad=14)
ax.text(0, 1.012, "Two structural calls anchor the set; nine genuine contests, three inside 40\u201360%, are where the framework takes risk.",
        transform=ax.transAxes, fontsize=9, color=GRAY, ha="left")

import matplotlib.lines as mlines
handles = [mlines.Line2D([], [], marker="o", ls="", color=cls_color[k],
                         markersize=8, label=cls_name[k]) for k in ["S", "L", "C"]]
handles.append(mlines.Line2D([], [], marker="o", ls="", markerfacecolor="none",
                             markeredgecolor=GRAY, markersize=8, label="named prior (forecasts 9, 14)"))
ax.legend(handles=handles, loc="upper center", bbox_to_anchor=(0.5, -0.055),
          ncol=4, frameon=False, fontsize=8.2)
src(fig, "Probabilities as assigned in Part 1. Hollow markers show the reference priors the derivations name for the two capex/FX contests.", y=-0.035)
save(fig, "fig01_portfolio")

# =====================================================================
# FIGURE 2 — China NEV retail share
# =====================================================================
years = [2020, 2021, 2022, 2023, 2024, 2025]
share = [5.8, 14.8, 27.6, 35.7, 47.6, 54.1]

fig, ax = plt.subplots(figsize=(6.9, 3.9))
ax.bar(years, share, color=[STEEL]*5 + [NAVY], width=0.62, zorder=3)
for x, v in zip(years, share):
    ax.text(x, v + 1.2, f"{v:.1f}", ha="center", fontsize=8.6, color=INK)
ax.axhline(60, color=RED, lw=1.4, ls="--", zorder=2)
ax.text(2019.6, 61.2, "Forecast 1 threshold: >60% for full-year 2027", color=RED, fontsize=8.6)
ax.annotate("Dec 2025 monthly share: 60.4%\n(first month above the line)",
            xy=(2025, 60.4), xytext=(2022.7, 68),
            fontsize=8.4, color=INK,
            arrowprops=dict(arrowstyle="-", color=GRAY, lw=0.9))
ax.scatter([2025], [60.4], s=44, color=RED, zorder=4)
ax.set_ylim(0, 78)
ax.set_xticks(years)
ax.set_ylabel("NEV share of passenger-vehicle retail (%)")
style_ax(ax)
ax.set_title("The subsidy is gone; the share keeps compounding", loc="left", pad=10)
src(fig, "Source: China Passenger Car Association retail data (BEV + PHEV share of passenger-vehicle retail units), full-year prints 2020\u20132025;\nDec 2025 monthly print. Forecast 1 resolves on the CPCA full-year 2027 print.", y=-0.05)
save(fig, "fig02_nev_share")

# =====================================================================
# FIGURE 3 — income predicts the opposite (EV share vs GDP per capita)
# =====================================================================
# EV = BEV + PHEV share of new passenger-car sales, 2025
pts = [
    # (name, gdp per capita $k (IMF 2025 est.), ev share %, emphasis)
    ("Vietnam",   4.9, 40, 1),
    ("Indonesia", 5.2, 15, 1),
    ("Thailand",  7.6, 21, 2),
    ("Colombia",  8.4, 10, 0),
    ("Brazil",   11.0, 10, 0),
    ("China",    13.7, 54, 1),
    ("Mexico",   14.0,  7, 0),
    ("T\u00fcrkiye", 16.0, 17, 0),
    ("Uruguay",  23.0, 27, 0),
    ("EU",       44.0, 27, 0),
    ("Japan",    33.0,  3, 2),
    ("US",       89.0, 11, 0),
    ("Singapore",93.0, 40, 1),
    ("Norway",   92.0, 97, 0),
]
fig, ax = plt.subplots(figsize=(6.9, 4.3))
for name, g, s, emph in pts:
    if emph == 2:
        ax.scatter([g], [s], s=120, color=RED, zorder=4)
        ax.annotate(name, (g, s), xytext=(0, 9), textcoords="offset points",
                    ha="center", fontsize=9.4, fontweight="bold", color=RED)
    elif emph == 1:
        ax.scatter([g], [s], s=64, color=NAVY, zorder=3)
        ax.annotate(name, (g, s), xytext=(0, 7), textcoords="offset points",
                    ha="center", fontsize=8.4, color=NAVY)
    else:
        ax.scatter([g], [s], s=40, color=GRAY, zorder=2)
        ax.annotate(name, (g, s), xytext=(0, 6), textcoords="offset points",
                    ha="center", fontsize=7.8, color=GRAY)
ax.set_xscale("log")
ax.set_xticks([5, 10, 20, 40, 80])
ax.get_xaxis().set_major_formatter(mtick.FormatStrFormatter("$%dk"))
ax.set_xlim(3.6, 130)
ax.set_ylim(-4, 104)
ax.set_xlabel("GDP per capita, 2025 (log scale)")
ax.set_ylabel("Plug-in (BEV+PHEV) share of new-car sales, 2025 (%)")
ax.annotate("", xy=(33, 10), xytext=(8.6, 24),
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
ax.text(15.5, 22.5, "5\u00d7 the income,\n1/7th the adoption", fontsize=8.8, color=RED,
        ha="center", style="italic")
style_ax(ax)
ax.set_title("Income predicts the opposite of what happened", loc="left", pad=10)
src(fig, "Sources: Ember, ASEAN/emerging-market EV analyses (Dec 2025, Apr 2026); CPCA (China); IEA Global EV Outlook (Norway); US \u2248.\nText cites Thailand at 19.4% on a BEV-only basis and Japan near 2%; this chart uses the broader BEV+PHEV measure throughout.\nGDP per capita: IMF estimates, rounded. Policy-priced access to Chinese models, not income, is the variable that sorts the points.", y=-0.09)
save(fig, "fig03_income_scatter")

# =====================================================================
# FIGURE 4 — oil: the fleet as stored elasticity (two panels)
# =====================================================================
fig, (a1, a2) = plt.subplots(1, 2, figsize=(8.8, 3.9),
                             gridspec_kw={"width_ratios": [1, 1.15]})

# Panel A: displacement build-up
cats = ["BEV\npassenger cars", "PHEV\npassenger cars", "Buses, 2/3-wheelers,\nLNG trucking"]
vals = [0.38, 0.07, 0.55]   # mb/d; cars ~0.45 combined per Thread 1; ~1.0 total
bottoms = np.cumsum([0] + vals[:-1])
colors = [NAVY, STEEL, GRAY]
for c, v, b, col in zip(cats, vals, bottoms, colors):
    a1.bar([0], [v], bottom=[b], color=col, width=0.5, zorder=3)
    a1.text(0.32, b + v/2, c.replace("\n", " "), va="center", fontsize=8.2, color=col)
a1.text(0, 1.06, "\u2248 1.0 mb/d", ha="center", fontsize=10.5, fontweight="bold", color=INK)
a1.axhline(0.45, xmin=0.28, xmax=0.72, color=INK, lw=0.8)
a1.text(-0.31, 0.45, "cars \u2248 0.45", fontsize=7.8, color=INK, va="center", ha="right")
a1.set_xlim(-0.6, 1.7)
a1.set_ylim(0, 1.25)
a1.set_xticks([])
a1.set_ylabel("Structural oil-demand displacement (mb/d)")
style_ax(a1)
a1.set_title("Built in advance, at subsidized cost", loc="left", fontsize=10.5, pad=8)

# Panel B: what the option allowed in the 2026 shock
labels = ["World supply shortfall\n(Mar\u2013May, IEA)", "China: crude-import pull\n(\u2248 \u221240%)", "of which structural\nEV/fleet displacement"]
lo = [10.0, 4.0, 1.0]
hi = [13.6, 4.0, 1.0]
ypos = [2, 1, 0]
a2.barh(ypos[0], hi[0]-lo[0], left=lo[0], color=LGRAY, height=0.5, zorder=3)
a2.barh(ypos[0], lo[0], color=GRAY, height=0.5, zorder=3)
a2.barh(ypos[1], 4.0, color=NAVY, height=0.5, zorder=3)
a2.barh(ypos[2], 1.0, color=STEEL, height=0.5, zorder=3)
a2.set_yticks(ypos)
a2.set_yticklabels(labels, fontsize=8.4)
a2.set_xlabel("Million barrels per day")
a2.text(13.6, 2, "  10\u201313.6", va="center", fontsize=8.6, color=INK)
a2.text(4.0, 1, "  \u2248 4", va="center", fontsize=8.6, color=INK)
a2.text(1.0, 0, "  \u2248 1", va="center", fontsize=8.6, color=INK)
a2.text(6.8, 2.62, "Brent: >$113 (late Mar) \u2192 <$70 (mid-Jun)", fontsize=8.6,
        color=RED, ha="center")
a2.set_xlim(0, 15.5)
a2.set_ylim(-0.55, 2.95)
style_ax(a2, grid_axis="x")
a2.set_title("What the option paid for in the Hormuz shock", loc="left", fontsize=10.5, pad=8)

fig.suptitle("Demand elasticity is a form of storage", x=0.012, ha="left",
             fontsize=12, fontweight="bold", y=1.02)
src(fig, "Sources: Thread 1 arithmetic from MPS fleet registrations (31.4M NEVs, end-2024) and Kpler displacement estimates (\u2248540 kb/d gasoline,\n\u2248500 kb/d diesel, 2026); IEA Oil Market Report monthly accounting, Mar\u2013May 2026. Refinery-run cuts and halted product exports supplied\nmost of the \u22484 mb/d swing; the structurally lower demand base is what made those levers safe to pull.", y=-0.11)
save(fig, "fig04_oil")

# =====================================================================
# FIGURE 5 — hyperscaler capex
# =====================================================================
yrs   = [2019, 2020, 2021, 2022, 2023, 2024, 2025, 2026]
capex = [70, 96, 127, 152, 148, 230, 410, 710]
fig, ax = plt.subplots(figsize=(6.9, 4.1))
bars = ax.bar(yrs, capex, width=0.62,
              color=[STEEL]*7 + [NAVY], zorder=3)
bars[-1].set_hatch("//")
bars[-1].set_edgecolor("white")
for x, v in zip(yrs, capex):
    ax.text(x, v + 12, f"{v}", ha="center", fontsize=8.4, color=INK)
# consensus path vs forecast 9
ax.plot([2026, 2027], [710, 1000], color=GRAY, lw=1.4, ls=":")
ax.scatter([2027], [1000], s=46, facecolors="none", edgecolors=GRAY, lw=1.4)
ax.text(2027, 1035, "sell-side 2027:\n> $1.0T", ha="center", fontsize=8.2, color=GRAY)
ax.plot([2027, 2028], [1000, 1060], color=GRAY, lw=1.4, ls=":")
ax.scatter([2028], [1060], s=46, facecolors="none", edgecolors=GRAY, lw=1.4)
ax.text(2028.04, 1100, "2028 consensus:\nstill growing\n(UBS \u2248 +6%)", ha="center", fontsize=8.2, color=GRAY)
ax.annotate("Forecast 9: 30% that the\n2028 sum prints below 2027",
            xy=(2028, 860), xytext=(2024.4, 810),
            fontsize=8.6, color=ORANGE, fontweight="bold",
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.3))
ax.scatter([2028], [860], s=60, color=ORANGE, zorder=4)
ax.set_xlim(2018.4, 2028.9)
ax.set_ylim(0, 1250)
ax.set_ylabel("Combined capex, $B (purchases of P&E)")
ax.set_xticks(yrs + [2027, 2028])
style_ax(ax)
ax.set_title("$700B draws on the same transformers and trades as everything else", loc="left", pad=10)
src(fig, "Sources: Microsoft, Alphabet, Amazon, Meta cash-flow statements, calendar-quarter sums, 2019\u20132024 (rounded); 2025 reported \u2248$410B;\n2026 = full-year guidance (\u2248$700\u2013725B as of the April\u2013July 2026 calls). 2027\u201328 markers: sell-side projections; the orange marker is\nforecast 9's contrarian branch, not a point estimate.", y=-0.10)
save(fig, "fig05_capex")

# =====================================================================
# FIGURE 6 — LA Metro burn-up
# =====================================================================
fig, ax = plt.subplots(figsize=(6.9, 4.0))
# actual checkpoints (program list as revised March 2024)
ax.plot([2024.2, 2025.95, 2026.35], [None, 9, 11], color=NAVY, lw=2.0, marker="o", ms=6, zorder=4)
ax.plot([2025.95, 2026.35], [9, 11], color=NAVY, lw=2.0, marker="o", ms=6, zorder=4)
ax.text(2025.95, 8.0, "Dec 2025: 9 open", fontsize=8.4, color=NAVY, ha="center")
ax.text(2026.42, 11.9, "May 2026: 11 open", fontsize=8.4, color=NAVY, ha="left")
# required path to 20
ax.plot([2026.35, 2028.54], [11, 20], color=RED, lw=1.6, ls="--", zorder=3)
ax.scatter([2028.54], [20], s=54, color=RED, zorder=4)
ax.text(2028.0, 21.0, "20 needed by Jul 14, 2028\nfor forecast 3 to resolve NO", fontsize=8.4,
        color=RED, ha="right")
# run-rate extrapolation
ax.plot([2026.35, 2028.54], [11, 11 + 0.4*26.3], color=GRAY, lw=1.4, ls=":", zorder=2)
ax.text(2027.32, 18.6, "recent run rate\n(2 in 5 months) \u2192 \u224821", fontsize=8.0, color=GRAY,
        ha="center")
# context lines
ax.axhline(28, color=LGRAY, lw=1.0)
ax.text(2024.28, 28.5, "28 projects (list as revised Mar 2024; 11 originals already swapped out as undeliverable)",
        fontsize=7.8, color=GRAY)
ax.axvline(2028.54, color=LGRAY, lw=1.0)
ax.text(2028.50, 1.2, "Games open", fontsize=8, color=GRAY, rotation=90, va="bottom", ha="right")
ax.set_xlim(2024.2, 2028.95)
ax.set_ylim(0, 31)
ax.set_ylabel("Projects in passenger revenue service")
ax.set_xticks([2024.5, 2025.5, 2026.5, 2027.5, 2028.5])
ax.set_xticklabels(["2024", "2025", "2026", "2027", "2028"])
style_ax(ax)
ax.set_title("Eleven years, dedicated funding, a hard deadline: 11 of 28 open", loc="left", pad=10)
src(fig, "Source: LA Metro Twenty-eight by '28 program tracker (metro.net/28x28), accessed Dec 2025 and May\u2013Jul 2026; board action of\nMarch 2024. The dashed red line is the pace resolution NO requires; the dotted gray line extrapolates the recent five-month run rate.\nMetro rail openings have historically slipped 2\u20133 years, and roughly a quarter of the list was still in planning in late 2025.", y=-0.10)
save(fig, "fig06_lametro")

# =====================================================================
# FIGURE 7 — server useful lives
# =====================================================================
fig, ax = plt.subplots(figsize=(6.9, 3.7))
def steps(ax, xs, ys, color, label, yoff=0.0, ls="-"):
    ax.step(xs, ys, where="post", color=color, lw=2.0, zorder=3, linestyle=ls)
    ax.text(xs[-1] + 0.06, ys[-1] + yoff, label, fontsize=8.6, color=color,
            va="center", fontweight="bold")
steps(ax, [2020, 2022.5, 2026.6], [4, 6, 6], NAVY, "Microsoft", yoff=0.32)
steps(ax, [2020, 2023.05, 2026.6], [4, 6, 6], STEEL, "Alphabet", yoff=-0.30, ls=(0, (4, 2)))
steps(ax, [2020, 2024.05, 2025.05, 2026.6], [5, 6, 5, 5], ORANGE, "Amazon*")
steps(ax, [2020, 2025.05, 2026.6], [4.5, 5.5, 5.5], GRAY, "Meta", yoff=0.0)
ax.annotate("Jan 2025: Amazon shortens lives for a\nsubset of servers; $920M accelerated\ndepreciation charge",
            xy=(2025.08, 5.02), xytext=(2020.3, 3.35),
            fontsize=8.2, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.2))
ax.set_ylim(2.8, 7.0)
ax.set_xlim(2020, 2027.7)
ax.set_ylabel("Stated server useful life (years)")
ax.set_yticks([3, 4, 5, 6])
ax.set_xticks([2020, 2021, 2022, 2023, 2024, 2025, 2026])
style_ax(ax)
ax.set_title("Depreciation schedules are where the optimism is stored", loc="left", pad=10)
src(fig, "Source: accounting-policy notes and disclosed changes in estimate, company SEC filings and earnings communications, 2022\u20132025\n(simplified; Meta's pre-2025 lives shown at the midpoint of its 4\u20135-year range). On $100B of gross server assets, moving straight-line\ndepreciation from six years back to four adds roughly $8B of annual expense \u2014 the incentive to delay recognition (forecast 12).", y=-0.11)
save(fig, "fig07_depreciation")

# =====================================================================
# FIGURE 8 — China share of global robot installations
# =====================================================================
yrs_r  = [2015, 2019, 2020, 2021, 2022, 2023, 2024]
share_r = [27.0, 37.6, 43.9, 51.8, 52.5, 51.0, 54.4]
fig, ax = plt.subplots(figsize=(6.9, 3.9))
ax.plot(yrs_r, share_r, color=NAVY, lw=2.2, marker="o", ms=6, zorder=3)
for x, v in zip(yrs_r, share_r):
    ax.text(x, v + 1.6, f"{v:.0f}" if x < 2023 else f"{v:.1f}", ha="center",
            fontsize=8.4, color=INK)
ax.axhline(54, color=RED, lw=1.4, ls="--", zorder=2)
ax.text(2015.0, 55.2, "Forecast 6 threshold: >54% in 2027", color=RED, fontsize=8.6)
ax.axhline(50, color=LGRAY, lw=1.0)
ax.text(2024.35, 47.6, "50%: China installs more than\nthe rest of the world combined", fontsize=7.8,
        color=GRAY, ha="right")
ax.set_ylim(20, 66)
ax.set_ylabel("China share of global installations (%)")
ax.set_xticks(yrs_r)
style_ax(ax)
ax.set_title("The diffusion scoreboard China is winning", loc="left", pad=10)
src(fig, "Source: IFR World Robotics, successive editions (2023 and 2024 unit counts as cited in Part 3; earlier years from the editions covering\nthem, and subject to IFR revision). Compute export controls target the frontier scoreboard (forecast 11, 20%); nothing in them touches\nthis one, which is gated by deployment friction instead.", y=-0.10)
save(fig, "fig08_robots")

# =====================================================================
# FIGURE 9 — the price of the most codified good
# =====================================================================
fig, ax = plt.subplots(figsize=(6.9, 3.9))
xs = [2023.2, 2023.87, 2024.37, 2025.6, 2026.58]
ys = [60, 30, 15, 10, 10]
labels = ["GPT-4\n$60", "GPT-4 Turbo\n$30", "GPT-4o\n$15", "GPT-5\n$10", ""]
ax.step(xs, ys, where="post", color=NAVY, lw=2.2, zorder=3)
ax.scatter(xs[:-1], ys[:-1], s=48, color=NAVY, zorder=4)
for x, v, l in zip(xs[:-1], ys[:-1], labels[:-1]):
    ax.text(x + 0.04, v * 1.14, l, fontsize=8.4, color=NAVY)
ax.set_yscale("log")
ax.set_yticks([5, 10, 20, 40, 60])
ax.get_yaxis().set_major_formatter(mtick.FormatStrFormatter("$%d"))
ax.axvline(2026.58, color=GRAY, lw=1.0, ls=":")
ax.text(2026.55, 4.35, "Jul 31, 2026:\nbaseline snapshot", fontsize=8, color=GRAY, ha="right")
ax.annotate("", xy=(2027.6, 5.0), xytext=(2026.62, 10),
            arrowprops=dict(arrowstyle="->", color=RED, lw=1.6))
ax.text(2027.62, 5.0, "Forecast 2: any one of\nOpenAI / Anthropic / Google\n\u221250% by Dec 31, 2027 (90%)",
        fontsize=8.4, color=RED, va="center")
ax.set_xlim(2023.0, 2028.6)
ax.set_ylim(3.4, 90)
ax.set_ylabel("Flagship output price, $ per 1M tokens (log)")
ax.set_xticks([2023, 2024, 2025, 2026, 2027, 2028])
style_ax(ax)
ax.set_title("The models' own product is the most codified good in the economy", loc="left", pad=10)
src(fig, "Source: OpenAI published on-demand API list prices at launch for the top general-purpose tier (reasoning-tier prices excluded), 2023\u20132025,\nshown as the cleanest public series; an 83% decline in 29 months. The forecast needs one of three providers to cut 50% in 17 months.", y=-0.07)
save(fig, "fig09_tokens")

# =====================================================================
# FIGURE 10 — macro dashboard (3 panels)
# =====================================================================
fig, (a1, a2, a3) = plt.subplots(1, 3, figsize=(10.6, 3.8))

# Panel A: core PCE, monthly YoY first prints
m = np.array([1,2,3,4,5,6,7,8,9,10,11,12, 13,14,15,16,17,18])  # Jan25..Jun26
pce = [2.6, 2.8, 2.6, 2.5, 2.7, 2.8, 2.9, 2.9, 2.8, np.nan, 2.8, 3.0,
       3.1, 3.1, 3.2, 3.3, 3.4, 3.3]
a1.plot(m, pce, color=NAVY, lw=2.0, marker="o", ms=3.6, zorder=3)
a1.axhline(3.0, color=RED, lw=1.3, ls="--")
a1.text(0.7, 3.05, "3.0% \u2014 forecast 15 threshold", fontsize=7.6, color=RED)
a1.axhline(2.0, color=LGRAY, lw=1.0)
a1.text(0.7, 2.04, "2% target", fontsize=7.4, color=GRAY)
a1.axvspan(12.5, 18.4, color="#f3e9e2", zorder=0)
a1.text(15.4, 2.20, "2026:\nevery print\n\u2265 3.0%", fontsize=7.6, color=ORANGE, ha="center")
a1.set_xticks([1, 4, 7, 10, 13, 16])
a1.set_xticklabels(["Jan'25", "Apr", "Jul", "Oct", "Jan'26", "Apr"], fontsize=7.6)
a1.set_ylim(1.8, 3.8)
a1.set_ylabel("Core PCE, % y/y (first prints)")
style_ax(a1)
a1.set_title("The floor is already in", loc="left", fontsize=10.5, pad=7)

# Panel B: fed funds target upper bound
dates = [2023.55, 2024.72, 2024.86, 2024.96, 2025.72, 2025.83, 2025.96, 2026.58]
ub    = [5.50,   5.00,    4.75,    4.50,    4.25,    4.00,    3.75,    3.75]
a2.step(dates, ub, where="post", color=NAVY, lw=2.0, zorder=3)
a2.axhline(3.75, color=RED, lw=1.3, ls="--")
a2.text(2023.62, 3.62, "3.75% \u2014 forecast 16 line", fontsize=7.6, color=RED)
a2.annotate("five straight holds;\n9\u20133, dissents for a hike", xy=(2026.3, 3.75),
            xytext=(2025.15, 4.62), fontsize=7.6, color=INK,
            arrowprops=dict(arrowstyle="->", color=GRAY, lw=1.0))
a2.axvline(2027.99, color=LGRAY, lw=1.0)
a2.text(2027.93, 5.28, "Dec 31, 2027", fontsize=7.4, color=GRAY, rotation=90, va="top", ha="right")
a2.set_xlim(2023.5, 2028.15)
a2.set_ylim(3.0, 5.75)
a2.set_xticks([2024, 2025, 2026, 2027])
a2.set_ylabel("Target-range upper bound (%)")
style_ax(a2)
a2.set_title("The squeezed reaction function", loc="left", fontsize=10.5, pad=7)

# Panel C: customs duties
fys  = [2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025]
duty = [41.3, 70.8, 68.6, 80.0, 99.9, 80.3, 77.0, 194.9]
a3.bar(fys, duty, color=[STEEL]*7 + [NAVY], width=0.62, zorder=3)
b26 = a3.bar([2026], [353], color=NAVY, width=0.62, zorder=3, hatch="//", edgecolor="white")
a3.axhline(250, color=RED, lw=1.3, ls="--")
a3.text(2017.6, 259, "$250B \u2014 forecast 17 threshold (FY2027)", fontsize=7.6, color=RED)
a3.text(2026, 363, "FY26 pace\n(4-mo ann.)", ha="center", fontsize=7.2, color=NAVY)
a3.annotate("May 2026: refund wave turns\nnet collections negative", xy=(2026, 250),
            xytext=(2021.1, 322), fontsize=7.4, color=ORANGE,
            arrowprops=dict(arrowstyle="->", color=ORANGE, lw=1.0))
a3.set_ylim(0, 420)
a3.set_xticks([2018, 2020, 2022, 2024, 2026])
a3.set_ylabel("Net customs duties, $B (fiscal year)")
style_ax(a3)
a3.set_title("The wall's own revenue line", loc="left", fontsize=10.5, pad=7)

fig.suptitle("Forecasts 15\u201317: the chain read off the gauges", x=0.012, ha="left",
             fontsize=12, fontweight="bold", y=1.04)
fig.tight_layout(w_pad=2.4)
src(fig, "Sources: BEA Personal Income and Outlays, monthly first prints (Oct 2025 gap: shutdown-delayed reporting); FOMC implementation notes /\nFRED DFEDTARU; US Treasury Monthly Treasury Statements (FY2018\u2013FY2025 net customs duties; FY2026 = first-four-months pace of\n$117.7B, annualized, shown hatched \u2014 the May refund event is why the pace is not a forecast).", y=-0.08)
save(fig, "fig10_macro")

print("done")
