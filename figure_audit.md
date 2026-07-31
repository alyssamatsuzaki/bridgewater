# Figure Audit — Phase 0

Audit of the ten figures in the 18-page draft, read against `submission.md`, `figures.py`, and the rendered PDF. Figure numbers below are the **rendered** numbers (build_pdf.py renumbers by order of appearance); the source filename follows in parentheses, since the two disagree for four figures.

A note that applies to every entry: **the draft records almost no URLs.** The only URL anywhere in the manuscript or code is `metro.net/28x28`. Every other source is named as an organisation and publication only. "URL: none recorded" below means exactly that; establishing a resolving URL per plotted series is Phase 2/6 work (`data/figure_sources.csv`), and any series whose primary print cannot be located will be flagged, not papered over. Values dated after January 2026 cannot be checked against model knowledge and are marked "verify live."

Second global note: `figures.py` saves 200-DPI PNGs only (spec: 300 DPI + SVG), to a hard-coded absolute path, in DejaVu Sans (the PDF body is Times), with several sub-8pt annotations (7.2–7.8pt source notes throughout; 7.2–7.6pt annotations in Figure 9). Every survivor gets rebuilt regardless of verdict, so "keep" below means "the evidence and design concept survive," not "the file survives."

---

## Figure 1 (fig01_portfolio.png) — "One claim, priced eighteen ways"

- **Claim supported:** none. It restates the 18 assigned probabilities grouped by framework claim — metadata, not evidence.
- **Forecasts served:** all 18, none evidentially.
- **Plotted series:** assigned probabilities (%, dimensionless) for 18 forecasts; two hollow "reference prior" markers — "sell-side-implied ≈ 10%" (forecast 9) and "unconditional base rate ≈ 15%" (forecast 14).
- **Source / date / vintage / URL:** internal (Part 1 text). The 10% "sell-side-implied" prior is attributed to no named estimate anywhere in the draft; the 15% base rate for the FX move is asserted in forecast 14's text without derivation. URL: n/a.
- **Transformations:** none.
- **Comparability problems / gaps:** consumes a full page; color-encodes the structural/leaning/contest taxonomy being deleted; legend-dependent; the two "priors" are unsourced numbers plotted as if they were data.
- **Verdict: DELETE** (explicit ruling). Replaced by the Part 1 forecast table. Archive PNG + code block.

## Figure 2 (fig02_nev_share.png) — "The subsidy is gone; the share keeps compounding"

- **Claim supported:** China's NEV share of passenger-vehicle retail reached 54.1% in full-year 2025 and 60.4% in the December 2025 month, against the forecast's >60% full-year-2027 threshold.
- **Forecasts served:** 1 (also framework §1).
- **Plotted series:** annual NEV (BEV+PHEV) share of passenger-vehicle retail units, % — 2020: 5.8, 2021: 14.8, 2022: 27.6, 2023: 35.7, 2024: 47.6, 2025: 54.1; single monthly point Dec 2025: 60.4; threshold line at 60.
- **Source / date / vintage / URL:** China Passenger Car Association, full-year prints 2020–2025 plus one monthly print. Vintage handling not stated (first print vs revised — the forecast's resolution requires first print). URL: none recorded. The 2020–2024 values match CPCA retail penetration as published (checkable pre-cutoff); 2025 annual and Dec-2025 monthly: verify live. The draft's own page-18 note lists all of these as unverified.
- **Transformations:** none (shares as published).
- **Comparability problems / gaps:** (a) the title is the one the ruling explicitly overturns — the purchase-tax exemption and trade-in programs mean "the subsidy is gone" overclaims; (b) annual bars and one monthly point share one panel — same source and definition, different frequency, so acceptable only if labeled; (c) bar color encodes the old taxonomy; (d) retail-vs-wholesale definition must be verified consistent across all six years (CPCA publishes both; the fallback source CAAM is wholesale).
- **Verdict: KEEP — REBUILD** on one consistent CPCA retail definition, first-print vintages, factual title, new palette, data to `data/fig_nev_share.csv`.

## Figure 3 (fig03_income_scatter.png) — "Income predicts the opposite of what happened"

- **Claim supported:** national income does not predict 2025 plug-in adoption; policy-priced access to Chinese models does.
- **Forecasts served:** none directly; framework §1 color.
- **Plotted series:** 14 country points — x: GDP per capita, 2025 IMF estimates, $ thousands, log scale, "rounded"; y: plug-in (BEV+PHEV) share of new-car sales 2025, %.
- **Source / date / vintage / URL:** Ember EV analyses (Dec 2025, Apr 2026), CPCA (China), IEA Global EV Outlook (Norway), US point marked "≈" in the figure's own source note, IMF per-capita estimates. URLs: none recorded. All 2025 shares: verify live.
- **Transformations:** rounding throughout; unit conversion to $k.
- **Comparability problems / gaps:** the figure's own source note concedes the two worst: the manuscript cites Thailand at 19.4% **BEV-only** while the chart plots 21% **BEV+PHEV**, and Japan "near 2%" prose against a plotted ~3%; the US point is an approximation; "EU" is an aggregate plotted beside its own member states' peers; sources with different vehicle-scope definitions (new-car vs passenger-car) are mixed across points; and the explanatory variable of the title — policy-priced access — is never plotted, so the chart infers a cause it does not show. Norway's basis (BEV-only vs plug-in) unverified.
- **Verdict: DELETE** (ruling allows delete or rebuild-from-scratch; recommend delete). The Thailand/Japan contrast survives in framework prose with clean single-source attribution, and the figure cap has no slot for it. Archive.

## Figure 4 (fig06_lametro.png) — "Eleven years, dedicated funding, a hard deadline: 11 of 28 open"

- **Claim supported:** 11 of 28 projects open as of May 2026; resolution NO requires 20 by July 14, 2028, i.e. nine more openings in ~26 months.
- **Forecasts served:** 3.
- **Plotted series:** cumulative projects in passenger revenue service (count) — Dec 2025: 9, May 2026: 11; required path to 20 by 2028.54 (dashed); run-rate extrapolation (2 openings / 5 months → ≈21, dotted); context lines at 28 and at the Games date.
- **Source / date / vintage / URL:** LA Metro Twenty-eight by '28 program tracker, metro.net/28x28, accessed Dec 2025 and May–Jul 2026; Metro board action March 2024 (revised list). The only recorded URL in the draft. Verify live.
- **Transformations:** linear extrapolation of a two-observation run rate (labeled as such).
- **Comparability problems / gaps:** two observed points carry the whole chart; Part 2 prose says eleven "complete" while the forecast's criterion is "open for passenger revenue service" — complete-vs-open slippage between prose and resolution language; the extrapolation manufactures a trend from n=2.
- **Verdict: DELETE, conditional on the forecast-3 cut proposed in plan.md** (the per-figure ruling: "cut if its forecast is cut"). Archive with the tracker observations preserved in a CSV note.

## Figure 5 (fig05_capex.png) — "$700B draws on the same transformers and trades as everything else"

- **Claim supported:** big-four combined capex roughly tripled from 2024 to 2026 guidance; consensus has 2027–28 still growing; forecast 9 prices the down year consensus doesn't model.
- **Forecasts served:** 9 (context for 8 and 12).
- **Plotted series:** combined Microsoft + Alphabet + Amazon + Meta "purchases of property and equipment," $B, calendar years — 2019: 70, 2020: 96, 2021: 127, 2022: 152, 2023: 148, 2024: 230 (rounded actuals); 2025: 410 ("reported ≈$410B"); 2026: 710 (guidance, hatched); 2027: 1,000 ("sell-side > $1.0T", hollow); 2028: 1,060 ("UBS ≈ +6%", hollow); orange dot at 860 labeled "forecast 9's contrarian branch, not a point estimate."
- **Source / date / vintage / URL:** company cash-flow statements 2019–2024, calendar-quarter sums; 2026 guidance "as of the April–July 2026 calls"; unnamed sell-side projections plus one named house (UBS). URLs: none recorded. 2019–2024 are checkable against 10-K/10-Q cash-flow lines; 2025 actual, 2026 guidance, and both consensus markers: verify live. The page-18 note lists the series as unverified.
- **Transformations:** Microsoft's June fiscal year re-cut to calendar quarters; rounding to $B (unstated precision); four companies summed.
- **Comparability problems / gaps:** the accounting boundary is the audit's biggest issue — the forecast defines its measure as cash-flow purchases of P&E **excluding finance leases**, but company guidance quotes routinely include finance leases (Meta explicitly guides including principal payments on finance leases), so the hatched 2026 bar and the consensus markers are probably not on the forecast's own definition; actuals/guidance/consensus are only partially distinguished (one hatch, shared hollow markers for two different kinds of estimate); the orange dot plots a probability statement as if it were a data point at a specific level, which is invented precision.
- **Verdict: KEEP — REBUILD.** Actuals, guidance, and consensus visually distinct and aligned to one stated boundary (per ruling); forecast 9 becomes a threshold annotation, not a marker; every bar traced to a filing row in `data/figure_sources.csv`.

## Figure 6 (fig09_tokens.png) — "The models' own product is the most codified good in the economy"

- **Claim supported:** OpenAI's flagship output list price fell 83% in 29 months ($60 → $10), the reference class for forecast 2's 50%-in-17-months at 90%.
- **Forecasts served:** 2 (also framework §4).
- **Plotted series:** OpenAI flagship output API list price at launch, $ per 1M tokens, log scale — GPT-4 $60 (Mar 2023), GPT-4 Turbo $30 (Nov 2023), GPT-4o $15 (May 2024), GPT-5 $10 (Aug 2025); baseline-snapshot marker Jul 31, 2026; annotation arrow to ~$5 for the forecast.
- **Source / date / vintage / URL:** OpenAI published on-demand API list prices, 2023–2025, "reasoning-tier prices excluded." URLs: none recorded (pricing pages + Wayback snapshots are the forecast's own resolution source and should be the citation). All four price points match the published list prices as of my knowledge; the Jul-2026 baseline: verify and **archive the snapshot ourselves** (Phase 3 requirement).
- **Transformations:** none (nominal list prices; step plot between launches).
- **Comparability problems / gaps:** a single-provider series supports a three-provider forecast (usable as reference class, must be labeled as one provider); "reasoning-tier prices excluded" collides with the forecast's own selection rule — if a provider's pricing page designates a reasoning model as its top tier, the figure's exclusion contradicts the resolution criterion (this is exactly Phase 3's forecast-2 ambiguity); no quality adjustment, which is fine per ruling but must be stated; the arrow to $5 draws the forecast's target as if it were data.
- **Verdict: KEEP — REBUILD** as a nominal published-list-price series, provider labeled, selection rule stated, forecast as threshold annotation. Conditional on the figure-cap resolution in plan.md.

## Figure 7 (fig08_robots.png) — "The diffusion scoreboard China is winning"

- **Claim supported:** China has installed the majority of the world's industrial robots since 2021 and reached 54.4% in 2024, against forecast 6's >54% threshold for 2027.
- **Forecasts served:** 6 (paired with 11 in the argument).
- **Plotted series:** China share of global industrial robot installations, % — 2015: 27.0, 2019: 37.6, 2020: 43.9, 2021: 51.8, 2022: 52.5, 2023: 51.0, 2024: 54.4; threshold line at 54; reference line at 50.
- **Source / date / vintage / URL:** IFR World Robotics, successive editions; the manuscript sources 2023 (276,288 / 541,302 = 51.0%, WR 2024 edition) and 2024 (295,000 / 542,076 = 54.4%, WR 2025 edition) explicitly; earlier years "from the editions covering them, and subject to IFR revision" — i.e., the draft itself concedes mixed vintages. URLs: none recorded. Pre-2023 points: the draft's page-18 note flags 2015 and 2020 as unverified.
- **Transformations:** China units ÷ world units per year; percentage.
- **Comparability problems / gaps:** each point potentially from a different edition, and the IFR revises back-years, so the series can mix vintages without saying so (the ruling: check every observation against the correct edition); label precision inconsistent (integers before 2023, one decimal after); the 2024 world figure (542,076) carries suspicious precision for what the IFR published as a preliminary round number — verify.
- **Verdict: KEEP — REBUILD** after per-edition verification, one edition-per-observation rule stated in the source line. Conditional on the figure-cap resolution in plan.md (this is the figure whose content compresses best into two sentences of prose if a slot must be freed).

## Figure 8 (fig04_oil.png) — "Demand elasticity is a form of storage"

- **Claim supported:** China's EV fleet displaces ≈1.0 mb/d of oil demand structurally (≈0.45 from passenger cars), and during the 2026 Hormuz disruption that structural floor let China pull ≈4 mb/d out of normal purchasing against a 10–13.6 mb/d world supply shortfall.
- **Forecasts served:** 4 (also framework §1; Thread 1).
- **Plotted series:** Panel A, stacked bar, mb/d — BEV passenger cars 0.38, PHEV passenger cars 0.07, buses/two-and-three-wheelers/LNG trucking 0.55; marker at cars ≈ 0.45. Panel B, horizontal bars, mb/d — world supply shortfall 10–13.6 (range bar), China crude-import pull ≈4, "of which structural EV/fleet displacement" ≈1; Brent annotation >$113 (late Mar) → <$70 (mid-Jun).
- **Source / date / vintage / URL:** Panel A: Thread 1's own arithmetic from Ministry of Public Security registrations (31.4M NEVs end-2024, Jan 2025 publication) plus assumptions (70.3% BEV split, 13,000 km/yr blended, 7.5 L/100km counterfactual); Kpler estimates (≈540 kb/d gasoline, ≈500 kb/d diesel, 2026). Panel B: IEA Oil Market Report monthly accounting, Mar–May 2026. URLs: none recorded. All 2026 observations: verify live.
- **Transformations:** fleet-stock × utilisation × fuel-economy derivation (documented in Thread 1); barrel conversion; the 0.38/0.07/0.55 split is a derived allocation.
- **Comparability problems / gaps:** the derived split is drawn with two-decimal precision and no estimate marking — these are model outputs, not observations; Panel A silently blends the draft's own derivation (~0.45 cars) with Kpler's independent estimate (1.04 total) without showing which carries which bar; Panel B's "of which structural" label makes it read as a decomposition while the text argues the opposite (the fleet did **not** supply the swing volume — refinery runs and export cuts did), which is the double-count the ruling flags; the three Panel B bars are three different kinds of quantity (a supply shortfall range, an import-flow change, a demand-stock level) presented in one frame — it is a scale comparison and must be labeled as one; Brent figures unverified.
- **Verdict: REBUILD** (likely the strongest figure, per ruling): estimate hatching/markers on all derived values, derivation vs Kpler separated, right panel relabeled as a scale comparison with the "of which" construction removed, structural vs temporary vs global-shock quantities visually distinct.

## Figure 9 (fig10_macro.png) — "Forecasts 15–17: the chain read off the gauges"

- **Claim supported:** every 2026 core-PCE print ≥3.0%; the funds-rate upper bound held at 3.75% for five meetings; customs duties running far above the $250B threshold with the May 2026 refund wave as the failure mode.
- **Forecasts served:** 15, 16, 17.
- **Plotted series:** Panel A: core PCE % y/y, monthly first prints, Jan 2025–Jun 2026 (2.6, 2.8, 2.6, 2.5, 2.7, 2.8, 2.9, 2.9, 2.8, gap, 2.8, 3.0, 3.1, 3.1, 3.2, 3.3, 3.4, 3.3), Oct 2025 missing (shutdown-delayed), thresholds at 3.0 and 2.0. Panel B: FOMC target-range upper bound, %, step — 5.50 (Jul 2023) → 5.00/4.75/4.50 (Sep–Dec 2024) → 4.25/4.00/3.75 (Sep–Dec 2025) → held to Jul 2026. Panel C: net customs duties, $B by fiscal year — FY2018–FY2025: 41.3, 70.8, 68.6, 80.0, 99.9, 80.3, 77.0, 194.9; FY2026: 353 (first-four-months pace, annualized, hatched).
- **Source / date / vintage / URL:** BEA Personal Income and Outlays monthly first prints; FOMC implementation notes / FRED DFEDTARU; Treasury Monthly Treasury Statements. URLs: none recorded (all three have canonical public homes — Phase 2). Pre-2026 values match published data where checkable; all 2026 values: verify live. The page-18 note flags the FY2018–24 duties and the PCE path as unverified.
- **Transformations:** Panel C's FY2026 bar is $117.7B (Oct–Jan) × 3 — an annualization the source note itself half-disowns ("the May refund event is why the pace is not a forecast").
- **Comparability problems / gaps:** the ruling's core complaint — three panels are unreadable at final size (annotations run 7.2–7.6pt, below the 8pt floor); the Oct-2025 gap is honestly broken, not interpolated (good — preserve); the annualized FY2026 bar sits beside actuals and is contradicted by a known later event (the May refund month is outside the annualization window), so it is closer to a talking point than an estimate; Panel B dies with forecast 16 if the cut list in plan.md is approved; first-print convention must be verified month by month against BEA's release archive, which is exactly Phase 2 lead #4.
- **Verdict: MERGE — REBUILD** as one legible small-multiple (two panels — core PCE and customs duties — under the proposed cut list), first-print vintages throughout, ≥8pt everywhere, FY2026 pace either dropped or explicitly marked as an estimate with the refund caveat in the annotation.

## Figure 10 (fig07_depreciation.png) — "Depreciation schedules are where the optimism is stored"

- **Claim supported:** stated server useful lives were extended industry-wide 2020–2024 and Amazon's January 2025 reduction is the first reversal, the behavior forecast 12 prices for two more companies.
- **Forecasts served:** 12.
- **Plotted series:** stated server useful life, years, step lines — Microsoft 4 → 6 (2022), Alphabet 4 → 6 (Jan 2023), Amazon 5 → 6 (Jan 2024) → reduced for a subset (Jan 2025, $920M accelerated-depreciation charge), Meta 4.5 → 5.5 (Jan 2025).
- **Source / date / vintage / URL:** accounting-policy notes and disclosed changes in estimate, SEC filings and earnings communications 2022–2025. URLs: none recorded (these are 10-K/10-Q citations — findable). Amazon's charge and dates checkable.
- **Transformations:** "simplified" by its own source note — Meta's pre-2025 life is drawn at the **midpoint of its 4–5-year range**, i.e., an invented 4.5 that violates the no-interpolation rule; Amazon's post-Jan-2025 line collapses a subset-only reduction into a single company-wide value; ranges collapsed to points throughout.
- **Comparability problems / gaps:** four companies' disclosures differ in equipment class (servers vs network equipment) and in form (policy range vs change in estimate), which a four-line step chart cannot carry honestly; the $8B-per-$100B sensitivity in the source note is an illustration, not data.
- **Verdict: MERGE INTO APPENDIX AS A TABLE** (ruling: move to appendix, annotated with filing date, equipment class, and old/new life ranges — those annotations are table columns; a table carries exact ranges without the midpoint fabrication, and frees a figure slot). Chart archived.

---

## Cross-cutting findings

1. **No figure has a URL trail.** One URL exists in the entire project. `data/figure_sources.csv` is being built from zero.
2. **Six figures plot at least one value the draft itself lists as unverified** (page-18 note): figs 2, 3, 5, 6 (rendered), 7, 9.
3. **Three figures draw invented or estimate-unmarked points as data:** the portfolio priors (fig 1), the forecast-9 dot (fig 5), the Meta midpoint (fig 10). Fig 8's derived split is unmarked estimate.
4. **Estimate types are conflated** wherever projections appear: guidance, sell-side consensus, annualized pace, and the draft's own contrarian branch share marker styles.
5. **Rendered vs file numbering diverges** (fig04↔Figure 8, fig06↔Figure 4, fig07↔Figure 10, fig08/09↔Figures 7/6) — an error waiting to happen; the rebuild will renumber files to match final placement.
6. **Build spec violations everywhere:** 200 DPI, no SVG, sub-8pt text, absolute paths, figure font ≠ document font.
