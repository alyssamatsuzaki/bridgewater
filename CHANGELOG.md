# Changelog — July 2026 revision

From an 18-page, 18-forecast, 10-figure draft to a 10-page, 14-forecast, 5-figure submission. Original text, figures, and build code are preserved in `archive/original/`. Forecast numbers below are given as **old → new** where they changed.

---

## 1. Structure

| | Before | After |
|---|---|---|
| Pages | 18 | **13** (limit 15) |
| Forecasts | 18 | **17** |
| Figures | 10 | **5** |
| Words | 8,010 | ~7,400 |
| Part 3 begins | page 12 | page 4 |

Page allocation: forecasts on 1–2, framework on 2–6, appendix on 6–12, sources/method/self-audit on 12–13.

Renumbering (old → new): 1→1, 2→2, 4→3, 5→4, 6→5, 7→6, 8→7, 9→8, 10→9, 11→10, 12→11, 13→12, 15→13, 17→14. Editing was done under original numbers and renumbered once at the end, with a scripted sweep over prose, both tables, figure captions, in-figure labels, and the sources block; every changed line was reviewed against a diff.

## 2. Forecasts removed (full text in `archive/forecasts_cut.md`)

- **Old 3 (LA Metro delivery)** — a domestic transit program reaching the thesis only by analogy to "physical delivery," which the datacenter, capex, and depreciation forecasts already test inside the AI buildout.
- **Old 14 (USD/JPY volatility)** — flagged by all four reviewers; its own resolution language conceded the trigger was "mechanism-blind," so a generic carry unwind would resolve YES with no mercantilism or AI in the chain.
- **Old 16 (federal funds rate)** — one causal link past the core-PCE forecast, with a recession unrelated to the framework as its entire NO case.
- **Old 18 (sector returns)** — the longest market chain in the set, and the draft conceded index concentration could swamp the thesis in either direction.

Held in reserve, not cut: old 11 (LMArena) and old 13 (ASEAN imports).

## 3. Probabilities changed

Every change is derived in `calibration.md`. No probability, threshold, date, or resolution criterion was changed silently.

| Forecast | Was | Now | Why |
|---|---|---|---|
| 2 — token prices | 90% | **80%** | Under the newly pre-registered selection rule, YES requires the *top-designated* tier to halve. The July 31, 2026 baseline shows top-tier prices have risen since 2025 while cuts land on lower tiers — premiumization is adverse evidence the 90% did not price. |
| 6 (was 7) — EU enforcement | 62% | **35%** | Recalculated from scratch, not adjusted. The Digital Omnibus moved Annex III high-risk obligations to December 2027, removing the August 2026 AI Act trigger from the window's first sixteen months. Base rate: one employee-monitoring proceeding against the six firms in eight years, one AI-training proceeding (annulled), zero combining both. |
| 7 (was 8) — capacity disclosure | 65% | **56%** | The criterion measures disclosure, not cancellation. Two stages now derived independently — 0.80 that a ≥1 GW pullback occurs, 0.70 that the company itself puts it on the record — and the product printed as it falls out. The 0.70 reflects that the most prominent pullback episode produced analyst figures and a corporate clarification, never a company-quantified number, which the criterion excludes. |

Unchanged and re-checked: 1 (85%), 3 (65%), 4 (70%), 5 (68%), 8 (30%), 9 (30%), 10 (20%), 11 (30%), 12 (38%), 13 (55%), 14 (70%).

## 4. Resolution criteria changed

- **Forecast 2** — selection rule pre-registered in full (top-designated general-purpose tier, successor inheritance, premium tiers only if the page designates them top, output rates only, provider against its own baseline). The draft's "most capable" was unresolvable once premium tiers existed.
- **Forecast 5 (was 6)** — fallback deleted. The draft substituted MIIT China installations over the last available IFR world total, changing source and denominator at once. Now: **unresolved** if the IFR discontinues the series. Also clarified that resolution follows the first published IFR figure for calendar-2027 installations, since the cited "World Robotics 2028" edition does not exist yet.
- **Forecast 10 (was 11)** — Artificial Analysis fallback deleted; a different benchmark can reverse the outcome. Now **unresolved** if LMArena is discontinued.
- **Forecast 7 (was 8)** — criterion kept as written (disclosure), with the two-stage structure stated explicitly in the derivation so the measured event is unambiguous.
- **Forecast 2, wording only** — "on archived pricing pages" became "on dated pricing-page readings," because the archives the earlier phrasing implied do not exist in this build. What the forecast measures is unchanged, and Table 2 now records the OpenAI baseline reading ($30 output, GPT-5.6 Sol) so the comparison is fixed in the manuscript itself rather than depending on a capture that has not happened. Anthropic's and Google's baseline readings are in the data files and are weaker: **the Anthropic case needs a decision before submission**, because it ships both a top standard model and a separately branded premium tier, and the pre-registered rule turns on which one its pricing page designates as top.

## 5. Corrections forced by the evidence

Each item was treated as a lead and re-checked against the primary record; `verification/` holds the per-claim findings.

- **MOFCOM "enforcement bounty."** The draft attributed a formalized enforcement bounty to the export-control listing. The listing instrument — Announcement No. 23 of 2026, June 22 — contains prohibitions and a licensing-exception process, no bounty. A reward mechanism for reporting export-control violations does exist, but as a **separate instrument** (Announcement No. 26 of 2026, effective July 1). The manuscript now cites the two separately and no longer rests forecast 4's linkage on a bounty.
- **EU AI Act timing.** The draft's claim that general application from August 2, 2026 put workplace AI systems in the high-risk tier from that date is wrong as of this revision: Regulation (EU) 2026/1744 defers Annex III obligations to **December 2, 2027**. Removed from Part 2 §3 and Thread 2; forecast 6 now rests on GDPR, national labour law, and data-protection authorities, and was repriced.
- **Meta MCI figures.** The 45,000-table exposure and the 1,600-signature petition are **press reporting** citing an internal security notice, not company disclosure. Now attributed as such. Company-confirmed: the program, the absence of a broad opt-out, the pause. The draft's "tax filings and medical data" characterization traced only to a single anonymous-employee account in secondary aggregators and is **cut**.
- **Garante v. OpenAI.** Verification surfaced what the draft did not know: the €15M fine was **annulled** on jurisdictional grounds in March 2026. This weakens the AI-training enforcement base rate and is stated in the derivation.
- **CNIL v. Amazon France Logistique.** The €32M fine was **reduced to €15M on appeal** in December 2025. Recorded.
- **July FOMC hold and July 23 Section 301 action.** Both confirmed and kept. Two details corrected: there was no July SEP (the cadence is quarterly; the June 2026 SEP is the relevant projection), and the Section 301 exemption is a defined product carve-out rather than the draft's "goods the US cannot source elsewhere" framing.
- **Core PCE vintage convention.** First prints hold everywhere, in prose and in figures, and the October 2025 gap is drawn as a gap. The draft's trailing note had already corrected the run to seven months at or above 3.0%; that correction is carried into the text.
- **IFR 2024 share.** 54.4% is *our* computation from 295,000 ÷ 542,076; the IFR's own prose says 54%. The manuscript now says so, which matters because the threshold is >54.0%.
- **"The subsidy is gone."** Factually wrong and now removed. China's NEV purchase-tax relief was **halved** for 2026–27 (50% reduction, capped at RMB 15,000) rather than eliminated, and the trade-in program was renewed for 2026. Figure 1's title is now descriptive.
- **Amazon depreciation.** The draft conflated two things: the $920M Q4-2024 accelerated-depreciation charge on early-retired hardware, and the separate January 2025 useful-life reduction for a subset of servers and network equipment. Table 1 separates them.
- **Korea unmanned-store count.** Unverifiable; cut.
- **Sell-side capex markers.** The ">$1.0T 2027 consensus" and "UBS ≈ +6% for 2028" could not be attributed to any citable published estimate. Deleted from the figure. The manuscript's claim is narrowed to what is defensible: we could locate no published estimate modelling a 2028 contraction.
- **Trailing verification note (draft page 18).** Deleted, and the verification it called for was performed instead. Where it could not be completed, the specific gap is listed in §8 below rather than announced to reviewers inside the manuscript.

## 6. Figures

Deleted (PNGs in `archive/figures_cut/`, code in `archive/original/figures.py`):

- **Portfolio map** — a full page of metadata with no evidence; replaced by the Part 1 forecast list. It also plotted two unsourced "reference priors" as if they were data.
- **Income vs. EV adoption scatter** — mixed BEV-only with BEV+PHEV observations, blended rounded and approximated points, plotted an aggregate ("EU") beside its own members, and inferred the effect of a policy variable it never plotted. The Thailand/Japan contrast survives in Part 2 prose with single-source attribution.
- **LA Metro burn-up** — went with its forecast; also extrapolated a trend from two observations.
- **Server useful lives** → **Table 1**. The chart required inventing a midpoint for Meta's 4–5-year range (an interpolation) and collapsed a subset-only Amazon change into a company-wide line. The table carries filing date, equipment class, and exact old→new ranges.
- **Robot share** → prose. Two edition-sourced observations and a flat-trend threshold; two sentences carry it, which holds the five-figure cap.

Rebuilt (all five): one palette with fixed semantics (navy observed, slate baseline, orange estimate, red dashed threshold only), one font family from bundled TTFs, 6.7-inch design width, 8pt minimum text verified by parsing the exported SVGs, y-gridlines only, top and right spines removed, direct labels rather than legends, SVG plus 300-dpi PNG.

Specific figure fixes: NEV chart retitled factually and put on one consistent CPCA retail definition; oil figure's right panel relabelled as **a scale comparison, not a decomposition**, with the misleading "of which structural" construction removed and all derived values hatched as estimates, and the derivation and Kpler estimates separated into distinct bars; capex chart distinguishes actuals from guidance and states that guidance boundaries differ from the forecast's own definition; token chart carries one provider labelled as a reference class with no implied quality adjustment; macro chart reduced from three unreadable panels to two legible ones, first prints throughout, with the partial FY2026 duties bar **excluded** rather than annualized.

## 7. Framework and prose

- "Error correction" is now **operationally defined**: a system keeps it if, when a delivery or demand signal moves against a standing commitment, some institution's recorded behavior adjusts in the same direction within about twenty-four months. Forecasts 3, 7, 8, and 11 are identified as direct measurements of that elasticity.
- Two-sentence plain-language definition of modern mercantilism added at the top of Part 2.
- Conviction taxonomy (structural / leaning / contest) deleted from prose, headers, and figure colours. Figure colour now encodes data status, never conviction.
- Epistemological-commitment paragraph cut.
- Part 1 is one sentence per forecast, probability leading; resolution mechanics moved to Table 2.
- Sentences over roughly 40 words broken throughout.
- Falsification block kept nearly intact, as ruled.
- Title: *Forecasts on AI and Modern Mercantilism*. An earlier working title prefixed this with a thesis phrase; that prefix was dropped, leaving the subject line to stand alone. The thesis itself is unchanged and still carries both competition themes in the epigraph.

## 8. Claims that remain unresolved — read this before submitting

Verification ran against a hard environmental limit: **every direct fetch of a primary document returned 403** through this environment's proxy (BEA, SEC EDGAR, the Federal Reserve, Treasury, IFR, provider pricing pages, and `web.archive.org`), and the session's search allowance was exhausted. Findings therefore rest on search-mediated reporting that quotes the primary sources, labelled by channel in `verification/`. Outstanding items, in priority order:

1. **Core PCE monthly first prints, Jan 2025 – Jun 2026** (`carried_unverified`). Eighteen values behind Figure 4 and the worked derivation for forecast 13. The 2025 values are consistent with the published record; the 2026 values could not be checked at all. **Largest evidence risk in the submission, and it touches a live forecast.**
2. **Forecast 2's baseline pricing snapshot** (`snapshot_secondary_only`). The value the forecast resolves against rests on secondary reporting. `data/snapshots/README.md` has the exact capture commands; this needs one unrestricted network session.
3. **Combined capex 2019–2023** (`carried_unverified`). Standard filing figures, but not re-read from the filings this pass. 2024 and 2025 are search-confirmed.
4. **FY2023 and FY2024 customs duties** (`triangulated`) — consistent across sources but not directly quoted from the MTS.
5. **IEA world-supply shortfall upper bound (13.6 mb/d).** March (10.1) and April (12.8) were confirmed; the 13.6 figure was not located in a world-supply table. The manuscript now says "roughly 10 to 13" and the figure hatches the upper segment.
6. **LMArena current state.** Could not be checked; forecast 10's 20% rests on the structural argument, not on today's leaderboard.
7. **Thailand Chinese-brand share.** Verified in a 70–85% range, not at a clean three-quarters; the manuscript now says "most of them Chinese brands."
8. **Japan EV share.** Denominator-sensitive (1.3–2% BEV-only, ~2.7% BEV+PHEV); the manuscript now says "below 3% even counting plug-in hybrids."
9. **May 2026 net customs collections turning negative.** Asserted in Part 3 and in forecast 14's derivation as the named failure mode. Carried from the prior draft; the follow-up verification pass that would have checked the monthly MTS could not run (search allowance exhausted, Treasury fetch blocked). The mechanism — tariff-refund litigation — is well attested; the specific claim that one month's *net* collections went negative is not confirmed. If it cannot be confirmed before submission, soften to "a refund wave sharply reduced spring 2026 collections."
11. **Forecast 17's structural setup.** The level of USD/JPY against its multi-decade range and the Bank of Japan's tightening path are carried from the prior draft and were not re-verified. The manuscript states this inside the derivation, and the 30% rests on the August 2024 reference event and the funding-channel argument rather than on a current rate reading.
12. **Forecast 16's project list.** That a March 2024 LA Metro board action replaced eleven projects, and the composition of the revised 28, are carried from the prior draft. The list governs resolution, so it should be confirmed against the board report before submission.
13. **Forecast 15's adoption figure.** NVIDIA's roughly two million cumulative Cosmos downloads is a vendor claim, cited as such in the manuscript, and is not independently confirmed.
10. **Japan self-checkout, 77.1% of supermarkets.** Cited to the Japan Supermarket Association's annual survey and carried from the prior draft. Not independently re-verified this pass; it was not among the six flagged leads and no brief covered it. Low stakes — it supports an illustrative claim in Part 2 §4, not a forecast — but it is unverified and should be checked or attributed more loosely.

## 8b. Second revision: page limit raised to 15, three forecasts added

The page limit moved from 10 to 15, and three subjects were requested: the Japanese yen, LA28, and world models. Two of the three had been cut earlier in this same revision, so this reverses those cuts deliberately rather than by oversight.

**Framework.** Part 2 gains a synthesis section stating the general mechanism: societies as nested feedback systems, where local conditions shape perception, perception feeds prediction, prediction drives action, and the resulting feedback becomes either learning or accumulated error that eventually forces structural change. Six recurring relationships are stated as a table, each with the forecasts that price it and the observation that would falsify it. The five existing mercantilism-and-AI claims are now framed as the domain application of that chain.

Two disciplines were applied to the synthesis so it adds testability rather than unfalsifiable scope:

- **The phase-transition claim is not forecast.** "Symmetry breaking" has no resolution criterion writable for a three-year window, so the paper says so and forecasts the accumulating mismatches that would precede one instead, naming forecasts 8, 13, and 17 as the joint signature to watch.
- **The thinnest relationship is disclosed.** Inequality feeding back into political power enters only through workflow-data ownership and employment law. No forecast prices wealth concentration, campaign finance, or regulatory capture. The manuscript states this as a real gap between the framework's breadth and the evidence at risk.

**Forecasts added.**

| # | Forecast | Prob. | Why it earns a slot now |
|---|---|---|---|
| 15 | A Fortune 500 non-technology company discloses using world-model synthetic data to train robots in its own facilities, before end-2028 | 40% | World models industrialize the prediction stage of the loop. Framework claim 4 predicts an asymmetry: fidelity gets cheap fast while interaction data and physical position stay scarce, so deployment lags capability. Grounded in the 2026 state of the art (DeepMind Genie 3; NVIDIA Cosmos 3, June 22, 2026). |
| 16 | Fewer than 20 of LA Metro's 28 projects open by the LA28 opening date, July 14, 2028 | 70% | Restores original forecast 3, cut for reaching the thesis "only by analogy." The general form of the loop is what brings it back: relationship 4 is about policy delay as such, not about datacenters. It also tests the delivery claim outside the AI buildout, where forecasts 7, 8, and 11 all share one industry. |
| 17 | USD/JPY moves ≥10% peak-to-trough in a 20-session window between Aug 3, 2026 and Dec 31, 2027 | 30% | Restores original forecast 14, cut as "mechanism-blind." The limitation is **restated rather than repaired**: the criterion still resolves YES on a generic carry unwind, so it establishes co-movement, not attribution, exactly as forecast 13 does. What changed is that relationship 2 gives fragility a named mechanism the earlier draft lacked. |

Probabilities are carried from the original drafts (70% and 30%) rather than re-derived, because the environment could not re-read the underlying series. Forecast 15's 40% is new and derived in `calibration.md`.

**Falsification logic corrected.** Low-probability forecasts cannot falsify by resolving NO, since NO is what we already expect. The manuscript now says so explicitly: forecast 17's informative direction is YES, as is forecast 15's, and only forecasts priced above even odds carry falsifying power in the NO direction. Forecast 16 at 70% is added to the falsification block on that basis.

**Correlation recounted.** Seventeen forecasts, roughly nine independent tests. Forecast 16 improves the ratio because a transit program on a fixed deadline shares almost no driver with the AI buildout.

**Attribution note.** The six-relationship synthesis is written in the paper's own voice. It was supplied to us as a named third party's cross-domain argument, but no citable published source under that name could be located, and a submission that stakes its credibility on provenance discipline cannot carry an attribution a judge is unable to check. If the source is citable, or is the author, the framing should be revisited before submission.

## 8c. Third revision: the human layer named as the first link in the chain

The framework already ran a causal chain from conditions through perception, prediction, and action to policy and market feedback. What it asserted and then dropped was the first link: the psychology and behaviour that every stage passes through. Named mechanisms sat in the six-relationship table ("emotion, imitation, and optimistic expectations"; "hierarchy, fear, and propaganda") while claims 1 through 5 ran almost entirely on subsidies, grid capacity, employment law, depreciation schedules, and tariffs. No forecasts were added and no probability, resolution criterion, or entry in Table 2 changed. 13 pages to 14.

**The private cost of correcting error, added after the six-relationship table.** A feedback loop closes only when a particular person acts on the signal, and acting early on an adverse signal is privately expensive: the executive who cancels announced capacity turns defensible optimism into a documented misjudgment, and the finance officer who shortens a depreciation life concedes in a filing that the prior estimate was wrong. The individual bears a concentrated cost so the institution captures a diffuse one. The information usually arrives on time; what arrives late is someone willing to be first to say so. This gives relationships 1, 4, and 6 a single shared mechanism and makes the lag itself the forecastable quantity, priced by forecasts 7, 11, and 16.

**Forecast 7's two-stage split identified as that mechanism.** The 0.80 × 0.70 derivation already separated cancelling from disclosing. The appendix now says what the second factor is: cancelling is an operating decision a company can take quietly, while quantifying it is a statement about the judgment behind the original commitment. The withheld 0.30 is the probability that the retreat happens and nobody attaches a number to it, which the unquantified Microsoft lease cancellations demonstrate directly.

**Automation-follows-scarcity promoted from a mid-paragraph aside to its own passage** in claim 4. The standard labor-cost account predicts the wrong geography; the installations run the other way, with China taking most of the world's industrial robots since 2021 at a fraction of US wages and with a shrinking working-age population. The argument now rests on that verified evidence (V07) rather than on the illustrative retail figures.

**Japan self-checkout 77.1% attribution loosened**, closing item 10 of §8. That figure was carried from an earlier draft and never independently re-verified. Since the surrounding passage was being promoted to load-bearing, the precise number was replaced with "the large majority" and the text now states in-line that it is carried from earlier reporting and unverified in this revision. Leaving a precise unverified figure in a structural position would have contradicted the provenance discipline the paper argues for.

**Claim 1's income inversion sharpened.** Thailand at 19.4% BEV share against a several-times-richer Japan below 3% was already stated. The paper now draws the conclusion: availability at a price point determines what people drive, availability is set upstream by trade and subsidy policy, and preference adjusts to what reaches the lot.

## 8d. August 2026 sweep: re-examination against post-anchor evidence

A full research pass over every major claim and forecast, run after the July 30–31 anchors. Evidence recorded in `verification/V11_august_2026_sweep.md`; analysis, additional figures, and per-forecast reassessment in `research_companion.md`. The submission stayed at its 15-page limit, so the sweep's quantitative build-out lives in the companion rather than the manuscript.

**Tooling constraint, unchanged.** `curl` and `WebFetch` both returned 403 at every host including controls; `WebSearch` worked. No primary document was opened this session. Every new figure is `search_confirmed` at best, never `primary_confirmed`, and the companion says so once at the top rather than repeating it per number.

**The Supreme Court voided the IEEPA tariffs, and the paper had not said so.** On February 20, 2026 the Court held 6–3 that IEEPA does not authorize tariffs, retroactive to inception. The CIT ordered ~$165B refunded; Penn Wharton put revenue at risk above $175B; CBP opened phase-one refunds on April 20. The prior draft referred only to "litigation-driven refunds" and never named the ruling. This was the largest evidentiary gap in the manuscript and is also directly on-thesis: an institution outside the executive forced a correction the political system had not, which is relationship 1 running through the judiciary rather than through prices.

**Forecast 14 repriced 70% → 25%.** Derivation in `calibration.md`. Refunds subtract from the net line the forecast resolves on and have already carried one month below zero; CRFB puts Section 301 and 338 replacement at under 60% of lost revenue; the Section 122 bridge was itself ruled illegal pending appeal. Held above a floor because Section 301 covers ~$949B of imports at 10–12.5% and Congress may still ratify by statute.

**Forecast 1's mechanism corrected.** Penetration prints support the forecast more strongly than the draft claimed (61.4% April, 63.0% May, 62.8% June). The mechanism did not: NEV retail units fell 5% y/y in May and 7% in June while total passenger-vehicle sales fell 20% y/y in April, so the share rose because the denominator fell faster. The draft read a ratio as adoption. A competing pull-forward account is stated and not resolved.

**The IEA's rival mechanism for forecast 3 named.** The IEA attributes part of China's gasoline decline to high pump prices discouraging ICE driving rather than to fleet displacement. Forecast 3 is the discriminating test between the two, so naming the rival strengthens the ratchet framing rather than weakening it.

**Forecast 17's acknowledged gap closed.** The prior draft conceded that the USD/JPY level and BoJ path were carried and unverified. Both are now read: 159.41 on July 31 2026, BoJ at 1.0% after a June hike, held 8–1 in July. Probability unchanged at 30%.

**Claim 3 now argued from behaviour rather than statute.** Meta's CTO confirmed no opt-out for the MCI program, 1,600+ employees petitioned against it, and European employees were excluded because GDPR does not permit the collection. One firm, one program, permitted in one jurisdiction and barred in another.

**Figure 2 refreshed.** 2026 guidance 700 → 725 ($B), and a 2027 analyst-consensus marker added at $1T using the figure's existing third mark, so actuals, guidance, and projection are now three visually distinct classes. Company-level splits were deliberately **not** adopted: V06's boundary work (fiscal-year and finance-lease differences) needs filings this session could not fetch.

**Three companion figures added**, built by `companion_figures.py` from `data/companion/`: the FY customs break with the June decomposition, the NEV penetration-versus-numerator pair, and the repricing history. Each carries underlying values, citation, limitations, and a reported-versus-estimated note. The FY2026 customs bar is drawn as a nine-month partial and is **not** annualized.

**Open items carried forward.** The Digital Omnibus scope question is the highest-priority unresolved item: if the deferral does not cover workplace AI, forecast 6 is underpriced. Thailand's Section 301 tier is unconfirmed. Forecast 2's baseline remains uncapturable. Nothing was changed on any of these.

## 9. Reproducibility

- All hard-coded absolute paths (`/home/claude/ftf/`, `/mnt/user-data/outputs/`) replaced with project-relative `pathlib` paths.
- One command builds everything: `python3 build_pdf.py` regenerates the five figures from `data/`, builds the PDF, and renders `qa/page_01.png`–`page_10.png`.
- The build **refuses to run** if unresolved `{{PENDING:...}}` markers remain in the manuscript, and **fails loudly** if the bundled fonts are missing rather than silently substituting DejaVu — the exact drift the figure spec warned about.
- Fonts bundled in `fonts/`. Dependencies pinned in `requirements.txt`. Every figure's inputs are a CSV under `data/`, and every plotted point has a row in `data/figure_sources.csv` carrying source, vintage, URL, access date, transformation, and verification status.
- No repository was created or published, per ruling.
