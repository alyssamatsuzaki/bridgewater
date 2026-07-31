"""Figures for "Control Without Feedback: Forecasts on AI and Modern Mercantilism".

Every plotted value is read from a CSV under data/ and traces to a row in
data/figure_sources.csv (source, vintage, URL, access date). Estimates are
drawn hatched or hollow; observed data solid. Rebuilding is deterministic and
offline: no network access at build time.

Palette semantics (fixed):
  NAVY   observed primary data
  SLATE  baseline / comparison series
  ORANGE projection or estimate
  RED    forecast threshold (dashed only)
"""
import csv
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
FIGS = ROOT / "figs"
FONTS = ROOT / "fonts"

# ---------- fonts: bundled TTFs only, fail loudly ----------
REQUIRED_FONTS = {
    "DejaVuSans.ttf": "DejaVu Sans",
    "DejaVuSans-Bold.ttf": "DejaVu Sans",
    "DejaVuSans-Oblique.ttf": "DejaVu Sans",
}
for fname in REQUIRED_FONTS:
    path = FONTS / fname
    if not path.is_file():
        raise RuntimeError(
            f"Bundled font missing: {path}. The figure build requires the TTFs "
            "in fonts/ so output is identical on every machine. Do not fall "
            "back to system fonts."
        )
    fm.fontManager.addfont(str(path))

NAVY = "#00204E"
SLATE = "#707B7C"
ORANGE = "#E65F00"
RED = "#C0392B"
INK = "#1a1d21"
GRID = "#d8dbe0"

plt.rcParams.update({
    "font.family": "DejaVu Sans",
    "font.size": 9.0,
    "axes.edgecolor": "#b0b5bc",
    "axes.linewidth": 0.8,
    "axes.titlesize": 10.5,
    "axes.titleweight": "bold",
    "axes.titlecolor": INK,
    "axes.labelsize": 8.5,
    "axes.labelcolor": INK,
    "xtick.labelsize": 8.5,
    "ytick.labelsize": 8.5,
    "xtick.color": INK,
    "ytick.color": INK,
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "svg.fonttype": "none",
    "hatch.linewidth": 0.7,
})

W = 6.7  # designed width, inches


def style_ax(ax, grid_axis="y"):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    if grid_axis:
        ax.grid(axis=grid_axis, color=GRID, linewidth=0.7, linestyle=(0, (3, 3)))
        ax.set_axisbelow(True)


def src(fig, text, y=0.0):
    fig.text(0.005, y, text, fontsize=8.0, color=SLATE, ha="left", va="top")


def save(fig, name):
    FIGS.mkdir(exist_ok=True)
    for ext, kw in (("png", {"dpi": 300}), ("svg", {})):
        fig.savefig(FIGS / f"{name}.{ext}", bbox_inches="tight",
                    facecolor="white", **kw)
    plt.close(fig)


def rows(csv_name):
    with open(DATA / csv_name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


# =====================================================================
# Figure 1 — China NEV share of passenger-vehicle retail sales
# =====================================================================
def fig_nev():
    data = rows("fig01_nev_share.csv")
    annual = [(int(r["period"]), float(r["value"])) for r in data
              if r["series"] == "annual"]
    monthly = [(r["period"], float(r["value"])) for r in data
               if r["series"] == "monthly"]

    fig, ax = plt.subplots(figsize=(W, 2.45))
    years = [y for y, _ in annual]
    vals = [v for _, v in annual]
    ax.bar(years, vals, color=NAVY, width=0.62, zorder=3)
    for x, v in zip(years, vals):
        ax.text(x, v + 1.6, f"{v:.1f}", ha="center", fontsize=8.5, color=INK)
    ax.axhline(60, color=RED, lw=1.3, ls="--", zorder=2)
    ax.text(years[0] - 0.42, 62.0, "Forecast 1 threshold: >60.0% for full-year 2027",
            color=RED, fontsize=8.5)
    if monthly:
        mv = monthly[0][1]
        ax.scatter([years[-1]], [mv], s=42, facecolors="white",
                   edgecolors=NAVY, lw=1.4, zorder=4)
        ax.annotate(f"Dec 2025, single month: {mv:.1f}",
                    xy=(years[-1], mv), xytext=(years[-1] - 2.6, mv + 8.5),
                    fontsize=8.5, color=INK,
                    arrowprops=dict(arrowstyle="-", color=SLATE, lw=0.9))
    ax.set_ylim(0, 80)
    ax.set_xticks(years)
    ax.set_ylabel("NEV share of passenger-vehicle retail sales (%)")
    style_ax(ax)
    ax.set_title("China's NEV retail share, full-year CPCA prints", loc="left", pad=9)
    src(fig, "Source: China Passenger Car Association retail data (BEV+PHEV units ÷ total passenger-vehicle retail units), full-year first\n"
             "prints 2020–2025 and the Dec 2025 monthly print (hollow marker). data/fig01_nev_share.csv lists each print and URL.",
        y=-0.04)
    save(fig, "fig01_nev_share")


# =====================================================================
# Figure 2 — hyperscaler purchases of property and equipment
# =====================================================================
def fig_capex():
    data = rows("fig02_capex.csv")
    fig, ax = plt.subplots(figsize=(W, 2.7))
    handles = {}
    for r in data:
        yr, v, kind = int(r["year"]), float(r["value_usd_b"]), r["kind"]
        if kind == "actual":
            b = ax.bar([yr], [v], color=NAVY, width=0.62, zorder=3)
            handles["actual"] = b
            ax.text(yr, v + 16, f"{v:.0f}", ha="center", fontsize=8.5, color=INK)
        elif kind == "guidance":
            b = ax.bar([yr], [v], color="white", edgecolor=ORANGE, hatch="///",
                       lw=1.2, width=0.62, zorder=3)
            handles["guidance"] = b
            ax.text(yr, v + 16, f"≈{v:.0f}", ha="center", fontsize=8.5,
                    color=ORANGE, fontweight="bold")
            ax.text(yr, v - 60, "guidance", ha="center", fontsize=8.0,
                    color=ORANGE)
        elif kind == "consensus":
            ax.scatter([yr], [v], s=44, facecolors="white", edgecolors=SLATE,
                       lw=1.4, zorder=3)
            ax.text(yr, v + 26, f"consensus\n≈{v:.0f}", ha="center",
                    fontsize=8.0, color=SLATE)
    years = sorted(int(r["year"]) for r in data)
    ax.set_xticks(years)
    ax.set_xlim(years[0] - 0.6, years[-1] + 0.6)
    top = max(float(r["value_usd_b"]) for r in data)
    ax.set_ylim(0, top * 1.24)
    ax.set_ylabel("Combined capex, $B per calendar year")
    style_ax(ax)
    ax.set_title("Purchases of property and equipment: Microsoft, Alphabet, Amazon, Meta",
                 loc="left", pad=9)
    ax.text(0.0, 1.005,
            "Cash-flow “purchases of property and equipment,” finance leases excluded — forecast 8 resolves YES if the 2028 sum prints below 2027.",
            transform=ax.transAxes, fontsize=8.0, color=SLATE, va="bottom")
    src(fig, "Sources: company SEC cash-flow statements, calendar-quarter sums (navy = reported actuals); 2026 = company guidance re-based to the\n"
             "same line where companies guide a different boundary (orange hatch = estimate). Per-company figures and URLs: data/fig02_capex.csv.",
        y=-0.04)
    save(fig, "fig02_capex")


# =====================================================================
# Figure 3 — oil: displacement estimates and the Hormuz scale comparison
# =====================================================================
def fig_oil():
    data = rows("fig03_oil.csv")
    A = [r for r in data if r["panel"] == "A"]
    B = [r for r in data if r["panel"] == "B"]
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.7),
                                 gridspec_kw={"width_ratios": [1, 1.25]})

    # Panel A: two independent estimates, both hatched (estimates)
    groups = {"derivation": [r for r in A if r["item"].startswith("derivation")],
              "kpler": [r for r in A if r["item"].startswith("kpler")]}
    xpos = {"derivation": 0, "kpler": 1}
    shades = {"derivation": ORANGE, "kpler": SLATE}
    for g, items in groups.items():
        bottom = 0.0
        for r in items:
            v = float(r["lo"])
            a1.bar([xpos[g]], [v], bottom=[bottom], color="white",
                   edgecolor=shades[g], hatch="///", lw=1.1, width=0.46, zorder=3)
            bottom += v
        parts = " + ".join(f"{r['label'].split()[0]} {float(r['lo']):.2f}"
                           for r in items)
        a1.text(xpos[g], bottom + 0.16, f"≈{bottom:.2f}", ha="center",
                fontsize=9.5, fontweight="bold", color=INK)
        a1.text(xpos[g], bottom + 0.05, parts, ha="center", fontsize=8.0,
                color=shades[g])
    a1.set_xticks([0, 1])
    a1.set_xticklabels(["This paper\n(cars only)", "Kpler 2026\n(all segments)"],
                       fontsize=8.5)
    a1.set_xlim(-0.80, 1.90)
    a1.set_ylim(0, 1.42)
    a1.set_ylabel("Structural displacement, mb/d (estimates)")
    style_ax(a1)
    a1.set_title("Two estimates of structural\noil-demand displacement", loc="left",
                 fontsize=9.5, pad=7)

    # Panel B: scale comparison, explicitly not a decomposition
    labels, ypos = [], []
    for i, r in enumerate(B):
        lo, hi = float(r["lo"]), float(r["hi"] or r["lo"])
        y = len(B) - 1 - i
        kind = r["kind"]
        if kind == "observed_range":
            a2.barh([y], [lo], color=SLATE, height=0.5, zorder=3)
            a2.barh([y], [hi - lo], left=[lo], color="white", edgecolor=SLATE,
                    hatch="///", lw=1.0, height=0.5, zorder=3)
            a2.text(hi + 0.25, y, f"{lo:g}–{hi:g}", va="center",
                    fontsize=8.5, color=INK)
        elif kind == "observed_approx":
            a2.barh([y], [lo], color=NAVY, height=0.5, zorder=3)
            a2.text(lo + 0.25, y, f"≈{lo:g}", va="center", fontsize=8.5, color=INK)
        else:  # estimate
            a2.barh([y], [lo], color="white", edgecolor=ORANGE, hatch="///",
                    lw=1.1, height=0.5, zorder=3)
            a2.text(lo + 0.25, y, f"≈{lo:g}", va="center", fontsize=8.5, color=INK)
        labels.append(r["label"].replace("\\n", "\n"))
        ypos.append(y)
    a2.set_yticks(ypos)
    a2.set_yticklabels(labels, fontsize=8.0)
    a2.set_xlabel("Million barrels per day")
    a2.set_xlim(0, 16.5)
    style_ax(a2, grid_axis="x")
    a2.set_title("March–May 2026: a scale comparison,\nnot a decomposition", loc="left",
                 fontsize=9.5, pad=7)

    fig.subplots_adjust(wspace=0.52)
    src(fig, "Sources: derivation — MPS fleet registrations and stated assumptions (Thread 1); Kpler displacement estimates, 2026; IEA Oil Market\n"
             "Report monthly accounting, Mar–May 2026. Hatched bars are estimates. The three right-hand quantities are different kinds of measure,\n"
             "shown together only for scale; refinery-run cuts and halted product exports, not the fleet, supplied most of the import swing.",
        y=-0.05)
    save(fig, "fig03_oil")


# =====================================================================
# Figure 5 — OpenAI flagship output list price (reference class for F2)
# =====================================================================
def fig_tokens():
    data = rows("fig05_tokens.csv")
    pts = [(r["date"], r["model"], float(r["output_usd_per_1m"]), r["kind"])
           for r in data]

    def tx(datestr):
        y, m = int(datestr[:4]), int(datestr[5:7])
        return y + (m - 0.5) / 12

    steps = [(tx(d), v, m) for d, m, v, k in pts if k == "list_price"]
    base = [(tx(d), v, m) for d, m, v, k in pts if k == "snapshot"]

    fig, ax = plt.subplots(figsize=(W, 2.55))
    xs = [x for x, _, _ in steps]
    ys = [v for _, v, _ in steps]
    # step series ends at the last launch price; the baseline is a separate,
    # separately dated observation and is not connected by a line.
    ax.step(xs + [xs[-1] + 0.9], ys + [ys[-1]], where="post", color=NAVY, lw=2.0,
            zorder=3)
    ax.scatter(xs, ys, s=40, color=NAVY, zorder=4)
    for x, v, m in steps:
        ax.text(x + 0.05, v * 1.13, f"{m}\n${v:g}", fontsize=8.5, color=NAVY)
    if base:
        bx, bv, bm = base[0]
        ax.scatter([bx], [bv], s=52, facecolors="white", edgecolors=ORANGE,
                   lw=1.6, zorder=5)
        ax.annotate(f"Jul 31, 2026 baseline\n{bm}: ${bv:g}",
                    xy=(bx, bv), xytext=(bx + 0.18, bv * 2.05),
                    fontsize=8.0, color=ORANGE, ha="left",
                    arrowprops=dict(arrowstyle="-", color=ORANGE, lw=0.9))
        ax.plot([bx, 2028.15], [bv / 2, bv / 2], color=RED, lw=1.3, ls="--", zorder=2)
        ax.text(2028.25, bv / 2, f"Forecast 2 threshold:\n−50% (${bv/2:g}) by\nDec 31, 2027",
                fontsize=8.0, color=RED, va="center")
    ax.set_yscale("log")
    ax.set_yticks([5, 10, 20, 40, 60])
    ax.set_yticklabels(["$5", "$10", "$20", "$40", "$60"])
    ax.yaxis.set_minor_formatter(mticker.NullFormatter())
    ax.yaxis.set_minor_locator(mticker.NullLocator())
    ax.set_xlim(2023.0, 2029.5)
    ax.set_ylim(4.0, 105)
    ax.set_xticks([2023, 2024, 2025, 2026, 2027, 2028])
    ax.set_ylabel("Output list price, $ per 1M tokens (log)")
    style_ax(ax)
    ax.set_title("OpenAI top-tier output list price: four launches, then the baseline",
                 loc="left", pad=9)
    src(fig, "Source: OpenAI published on-demand API list prices for the pricing page's top general-purpose tier — one provider, shown as the\n"
             "reference class; no quality adjustment. The hollow marker is the July 31, 2026 baseline the forecast resolves against, drawn as an\n"
             "estimate because direct pricing-page capture was blocked in this build (data/fig05_tokens.csv; see data/snapshots/README.md).",
        y=-0.05)
    save(fig, "fig05_tokens")


# =====================================================================
# Figure 4 — macro small-multiple: core PCE first prints; customs duties
# =====================================================================
def fig_macro():
    pce = rows("fig04a_core_pce.csv")
    dut = rows("fig04b_customs_duties.csv")
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(W, 2.5),
                                 gridspec_kw={"width_ratios": [1.15, 1]})

    # Panel A — core PCE y/y first prints; missing months drawn as gaps
    xs, ys = [], []
    for i, r in enumerate(pce):
        xs.append(i)
        ys.append(float(r["value"]) if r["value"] else None)
    segx, segy = [], []
    for x, y in zip(xs, ys):
        if y is None:
            if segx:
                a1.plot(segx, segy, color=NAVY, lw=1.8, marker="o", ms=3.2, zorder=3)
            segx, segy = [], []
        else:
            segx.append(x)
            segy.append(y)
    if segx:
        a1.plot(segx, segy, color=NAVY, lw=1.8, marker="o", ms=3.2, zorder=3)
    a1.axhline(3.0, color=RED, lw=1.2, ls="--")
    a1.text(0.2, 3.05, "3.0% threshold", fontsize=8.0, color=RED)
    a1.axhline(2.0, color=SLATE, lw=0.9, ls="--")
    a1.text(0.2, 2.05, "2% target", fontsize=8.0, color=SLATE)
    a1.text(0.2, 3.74, "forecast 13 needs 6 of 12\nmonths of 2027 at ≥3.0%",
            fontsize=8.0, color=RED, ha="left", va="top")
    gap = [i for i, r in enumerate(pce) if not r["value"]]
    if gap:
        a1.annotate("no Oct '25 print\n(shutdown)", xy=(gap[0], 2.86),
                    xytext=(gap[0] - 0.3, 2.18), fontsize=8.0, color=SLATE,
                    ha="center", arrowprops=dict(arrowstyle="-", color=SLATE, lw=0.7))
    ticks = [i for i, r in enumerate(pce) if r["month"].endswith(("-01", "-07"))]
    a1.set_xticks(ticks)
    a1.set_xticklabels([{"01": "Jan", "07": "Jul"}[pce[i]["month"][-2:]] +
                        " '" + pce[i]["month"][2:4] for i in ticks], fontsize=8.5)
    a1.set_ylim(1.8, 3.8)
    a1.set_ylabel("Core PCE, % y/y (first prints)")
    style_ax(a1)
    a1.set_title("Core PCE, monthly first prints", loc="left", fontsize=9.5, pad=7)

    # Panel B — customs duties by fiscal year
    for r in dut:
        fy, v, kind = int(r["fiscal_year"]), float(r["value_usd_b"]), r["kind"]
        if kind == "actual":
            a2.bar([fy], [v], color=NAVY, width=0.62, zorder=3)
        else:  # ytd partial year
            a2.bar([fy], [v], color="white", edgecolor=ORANGE, hatch="///",
                   lw=1.1, width=0.62, zorder=3)
            a2.text(fy, v + 12, "FY26\nYTD", ha="center", fontsize=8.0, color=ORANGE)
    a2.axhline(250, color=RED, lw=1.2, ls="--")
    a2.text(int(dut[0]["fiscal_year"]) - 0.4, 224,
            "$250B — forecast 14 threshold (FY2027)", fontsize=8.0, color=RED)
    last_actual = [r for r in dut if r["kind"] == "actual"][-1]
    a2.text(int(last_actual["fiscal_year"]), float(last_actual["value_usd_b"]) + 12,
            f"{float(last_actual['value_usd_b']):.0f}", ha="center", fontsize=8.5, color=INK)
    a2.set_xticks([int(r["fiscal_year"]) for r in dut][::2])
    a2.set_ylim(0, 300)
    a2.set_ylabel("Net customs duties, $B (fiscal year)")
    style_ax(a2)
    a2.set_title("Net customs duties by fiscal year", loc="left", fontsize=9.5, pad=7)

    fig.subplots_adjust(wspace=0.42)
    src(fig, "Sources: BEA Personal Income and Outlays, monthly first prints, Jan 2025–Jun 2026 (October 2025 has no print — shutdown-delayed\n"
             "reporting; drawn as a gap, not interpolated); US Treasury Monthly Treasury Statements, net customs duties by fiscal year, complete\n"
             "fiscal years only — the partial FY2026 total is excluded rather than annualized. Rows, statuses, and URLs: data/fig04a–b CSVs.",
        y=-0.05)
    save(fig, "fig04_macro")


# Order matches the figure numbering in submission.md.
ALL = [fig_nev, fig_capex, fig_oil, fig_macro, fig_tokens]

if __name__ == "__main__":
    for f in ALL:
        f()
    print(f"built {len(ALL)} figures → {FIGS}/ (SVG + 300-dpi PNG)")
