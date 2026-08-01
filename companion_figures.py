"""Figures for the research companion (research_companion.md).

Separate from figures.py so the submission build is untouched. Same palette
semantics and the same discipline: every plotted value is read from a CSV under
data/companion/, estimates and partial periods are drawn distinctly from
observed full-period data, and nothing is interpolated.

Palette semantics (inherited from figures.py):
  NAVY   observed primary data
  SLATE  baseline / comparison series
  ORANGE projection, estimate, or partial period
  RED    forecast threshold (dashed only)

Run: python3 companion_figures.py   ->   figs/companion/*.png|svg
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data" / "companion"
OUT = ROOT / "figs" / "companion"
FONTS = ROOT / "fonts"
OUT.mkdir(parents=True, exist_ok=True)

for fname in ("DejaVuSans.ttf", "DejaVuSans-Bold.ttf", "DejaVuSans-Oblique.ttf"):
    path = FONTS / fname
    if not path.is_file():
        raise RuntimeError(f"Bundled font missing: {path}")
    fm.fontManager.addfont(str(path))

NAVY = "#00204E"
SLATE = "#707B7C"
ORANGE = "#E65F00"
RED = "#C0392B"
INK = "#1a1d21"
GRID = "#d8dbe0"
W = 6.9

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.0,
    "axes.edgecolor": "#b0b5bc",
    "axes.linewidth": 0.8,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.labelsize": 8.5,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "figure.dpi": 200,
    "savefig.dpi": 200,
})


def rows(name):
    with open(DATA / name, newline="", encoding="utf-8") as fh:
        return list(csv.DictReader(fh))


def style_ax(ax):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(axis="y", color=GRID, lw=0.7, zorder=0)
    ax.set_axisbelow(True)


def src(fig, text, y=-0.05):
    fig.text(0.012, y, text, fontsize=7.1, color=SLATE, va="top", linespacing=1.5)


def save(fig, stem):
    fig.savefig(OUT / f"{stem}.png", bbox_inches="tight", facecolor="white")
    fig.savefig(OUT / f"{stem}.svg", bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  wrote figs/companion/{stem}.png|svg")


# =====================================================================
# C1: the tariff line breaks. FY customs duties, with FY2026 partial.
# =====================================================================
def c1_customs():
    data = rows("c1_customs_fy.csv")
    june = {r["component"]: float(r["value_usd_b"]) for r in rows("c1_june_split.csv")}

    fig, (ax, ax2) = plt.subplots(
        1, 2, figsize=(W, 2.95), gridspec_kw={"width_ratios": [2.15, 1]})

    for r in data:
        fy, v, kind = int(r["fiscal_year"]), float(r["value_usd_b"]), r["kind"]
        if kind == "actual":
            ax.bar([fy], [v], color=NAVY, width=0.64, zorder=3)
            ax.text(fy, v + 6, f"{v:.0f}", ha="center", fontsize=7.8, color=INK)
        else:
            ax.bar([fy], [v], color="white", edgecolor=ORANGE, hatch="///",
                   lw=1.2, width=0.64, zorder=3)
            ax.text(fy, v + 6, f"{v:.0f}", ha="center", fontsize=7.8,
                    color=ORANGE, fontweight="bold")
            ax.text(fy, v * 0.45, "9 mo\nonly", ha="center", va="center",
                    fontsize=7.4, color=ORANGE, fontweight="bold",
                    linespacing=1.25,
                    bbox=dict(boxstyle="round,pad=0.22", fc="white",
                              ec="none", alpha=0.92))

    ax.axhline(250, color=RED, ls="--", lw=1.2, zorder=4)
    ax.text(2018.0, 255, "$250B: forecast 14 threshold (FY2027)",
            fontsize=7.8, color=RED)
    ax.annotate("SCOTUS voids IEEPA\nFeb 20, 2026", ha="right",
                xy=(2026, 178), xytext=(2026.4, 296),
                fontsize=7.6, color=INK, linespacing=1.35,
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=0.9,
                                connectionstyle="arc3,rad=0.12"))
    ax.set_ylim(0, 320)
    ax.set_xticks([int(r["fiscal_year"]) for r in data])
    ax.set_xticklabels([str(r["fiscal_year"])[-2:] for r in data])
    ax.set_xlabel("US fiscal year")
    ax.set_ylabel("Net customs duties, $B")
    style_ax(ax)
    ax.set_title("Net customs duties by fiscal year", loc="left", pad=8)

    labels = ["Gross\nduties", "Refunds\npaid", "Net"]
    vals = [june["gross_duties_collected"], june["refunds_paid"], june["net"]]
    cols = [NAVY, RED, SLATE]
    ax2.bar(labels, vals, color=cols, width=0.6, zorder=3)
    for i, v in enumerate(vals):
        ax2.text(i, v + (2.2 if v >= 0 else -5.5), f"{v:+.1f}", ha="center",
                 fontsize=7.8, color=INK)
    ax2.axhline(0, color=INK, lw=0.9, zorder=4)
    ax2.set_ylim(-60, 40)
    ax2.set_ylabel("$B")
    style_ax(ax2)
    ax2.set_title("June 2026 alone", loc="left", pad=8)

    src(fig,
        "Sources: Treasury Monthly Treasury Statements, customs duties net of refunds (FY2018–FY2025 full years). FY2026 bar is a NINE-MONTH\n"
        "partial (Oct 2025–Jun 2026, $163B) drawn hatched; it is NOT annualized, because annualizing a series being reduced by an active refund\n"
        "programme would fabricate the very quantity in question. FY2023 and FY2024 are triangulated, not directly quoted (see V08). Right panel\n"
        "decomposes June 2026. Figures reported via secondary channels citing Treasury; primary MTS PDFs not fetchable this session (proxy 403).\n"
        "Data: data/companion/c1_customs_fy.csv, c1_june_split.csv.", y=-0.055)
    save(fig, "c1_customs_break")


# =====================================================================
# C2: penetration rose while the numerator shrank
# =====================================================================
def c2_nev():
    data = rows("c2_nev_2026.csv")
    yoy = rows("c2_yoy.csv")
    months = [r["month"][-2:] for r in data]
    pen = [float(r["penetration_pct"]) for r in data]

    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.85),
                                 gridspec_kw={"width_ratios": [1.15, 1]})

    a1.plot(months, pen, color=NAVY, marker="o", ms=5, lw=1.8, zorder=3)
    for i, (m, p) in enumerate(zip(months, pen)):
        a1.text(m, p + 1.7, f"{p:.1f}", fontsize=7.8, color=INK,
                ha="left" if i == 0 else "center")
    a1.axhline(60, color=RED, ls="--", lw=1.2, zorder=4)
    a1.text(-0.35, 57.0, "60.0%: forecast 1 threshold",
            fontsize=7.6, color=RED)
    a1.set_ylim(38, 70)
    a1.set_xlim(-0.45, 3.45)
    a1.set_ylabel("NEV share of PV retail units, %")
    a1.set_xlabel("2026 month (Feb, Mar not retrieved)")
    style_ax(a1)
    a1.set_title("Penetration rose", loc="left", pad=8)

    labels = [f"{r['series'].split()[0]}\n{r['month'][-2:]}" for r in yoy]
    vals = [float(r["yoy_pct"]) for r in yoy]
    cols = [NAVY if r["series"].startswith("NEV") else SLATE for r in yoy]
    a2.bar(labels, vals, color=cols, width=0.6, zorder=3)
    for i, v in enumerate(vals):
        a2.text(i, v - 1.4, f"{v:.0f}%", ha="center", va="top", fontsize=8.2,
                color=INK, fontweight="bold")
    a2.axhline(0, color=INK, lw=0.9, zorder=4)
    a2.set_ylim(-26, 4)
    a2.set_ylabel("Change vs same month 2025, %")
    a2.set_xlabel("navy = NEV units  ·  grey = total passenger vehicles")
    style_ax(a2)
    a2.set_title("as both NEV and the market contracted", loc="left", pad=8)

    src(fig,
        "Sources: CPCA monthly retail prints reported via CnEVPost, Gasgoo and BitAuto. Penetration = NEV (BEV+PHEV) retail units ÷ total\n"
        "passenger-vehicle retail units; April shown at the revised 61.4% (preliminary 60.6%). Feb and Mar prints were not retrieved and are\n"
        "omitted, so the left panel is a set of points and not a continuous monthly series. RIGHT PANEL MIXES MONTHS: NEV y/y was retrieved\n"
        "only for May and June, total-PV y/y only for April. They are shown together because the comparison is the point, but they are not the\n"
        "same month and the gap is not a like-for-like decomposition. Missing months are left out rather than estimated. Penetration rising while\n"
        "NEV units fall y/y is arithmetically possible only if the denominator fell faster. Data: data/companion/c2_nev_2026.csv, c2_yoy.csv.",
        y=-0.055)
    save(fig, "c2_nev_denominator")


# =====================================================================
# C3: what got repriced, and by how much
# =====================================================================
def c3_reprice():
    data = rows("c3_reprice.csv")
    labels = [f"{r['forecast']}. {r['label']}" for r in data]
    prior = [float(r["prior_pct"]) for r in data]
    curr = [float(r["current_pct"]) for r in data]
    y = range(len(data))

    fig, ax = plt.subplots(figsize=(W, 2.7))
    for i, (p, c) in enumerate(zip(prior, curr)):
        ax.plot([p, c], [i, i], color=GRID, lw=2.4, zorder=2,
                solid_capstyle="round")
        ax.scatter([p], [i], s=52, facecolors="white", edgecolors=SLATE,
                   lw=1.5, zorder=3)
        ax.scatter([c], [i], s=58, color=NAVY, zorder=4)
        ax.annotate("", xy=(c, i), xytext=(p, i),
                    arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.1))
        ax.text(p, i + 0.30, f"{p:.0f}", ha="center", fontsize=7.6, color=SLATE)
        ax.text(c, i - 0.40, f"{c:.0f}", ha="center", fontsize=8.0,
                color=NAVY, fontweight="bold")

    ax.set_yticks(list(y))
    ax.set_yticklabels(labels, fontsize=8.0)
    ax.invert_yaxis()
    ax.set_ylim(len(data) - 0.45, -0.85)
    ax.set_xlim(0, 100)
    ax.set_xlabel("Probability, % (hollow = prior draft, solid = current)")
    style_ax(ax)
    ax.grid(axis="y", visible=False)
    ax.grid(axis="x", color=GRID, lw=0.7)
    ax.set_title("Every downward reprice, with its named cause", loc="left", pad=8)
    src(fig,
        "Each move is recorded in CHANGELOG.md §3 and derived in calibration.md. Drivers, in order: premiumization observed at the top tier;\n"
        "the AI Act high-risk trigger absent from the window's first sixteen months; disclosure separated from cancellation as distinct events;\n"
        "and the Supreme Court voiding IEEPA on 20 Feb 2026, after which refunds net directly against the line forecast 14 resolves on.\n"
        "All four moved down. No forecast in the set was revised upward on the August 2026 sweep. Data: data/companion/c3_reprice.csv.",
        y=-0.075)
    save(fig, "c3_repricing")


if __name__ == "__main__":
    print("building companion figures")
    c1_customs()
    c2_nev()
    c3_reprice()
    print("done")
