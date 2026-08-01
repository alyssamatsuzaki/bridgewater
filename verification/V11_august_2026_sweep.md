# V11 — August 2026 research sweep

**Date of session:** 2026-08-01
**Scope:** Re-examination of every major claim and forecast against evidence published since the July 30–31, 2026 anchors. Conducted after the second revision (CHANGELOG §8b) and the third (§8c).

---

## Verifier note on method and tooling constraints (read first)

This session hit the same wall as V01–V10, and the reader should discount accordingly.

| Channel | Result |
|---|---|
| `curl` direct egress | **403 at CONNECT**, every host tested |
| `WebFetch` | **403 Forbidden**, every URL tested |
| `WebSearch` | **Worked** |

Controls: `https://en.wikipedia.org` and `https://www.bea.gov` both failed at the CONNECT step, which establishes a session-level proxy policy rather than a site-specific block. `$HTTPS_PROXY/__agentproxy/status` returned `enabled: true` with an empty `recentRelayFailures` array, so the rejection is policy, not transport failure.

**Consequence for every finding below.** WebSearch returns result titles, URLs, and server-side syntheses of the underlying pages. It does not return raw documents to this session. No figure in this record was read out of a primary PDF, dataset, or filing by this session. Where a number is attributed to BEA, Treasury, IFR, IEA, USTR, or a company filing, that attribution is what the search channel reported the primary source to say. It has not been re-derived from the primary source here.

This is the same limitation V01–V10 carry, and it is why every new row added to `data/figure_sources.csv` from this sweep is marked `search_confirmed` rather than `primary_confirmed`. Two or more independent search results agreeing is the strongest evidence tier available in this environment, and it is weaker than opening the document.

**Evidence tiers used below**, aligned to the ledger's existing `status` vocabulary:

- **DIRECTLY ESTABLISHED** — multiple independent sources report the same figure; ledger status `search_confirmed`
- **MULTI-SOURCE INTERPRETATION** — sources agree on the reading but the figure is derived or characterized rather than printed
- **CAUSAL CLAIM** — a mechanism is asserted; the proposed mechanism and its rivals are stated explicitly
- **PROJECTION** — a forward estimate by a named party, not an observation
- **MY INFERENCE** — reasoning by this verifier from the above, labeled as such
- **COULD NOT VERIFY** — the channel could not settle it

---

## 1. The Supreme Court struck down the IEEPA tariffs (February 20, 2026)

**DIRECTLY ESTABLISHED.** The Supreme Court held 6–3 that the International Emergency Economic Powers Act does not authorize the President to impose tariffs, reasoning that the power to tariff is "a branch of the taxing power" reserved to Congress under Article I. The holding invalidated both the "reciprocal" tariffs applied to most trading partners and the China/Canada/Mexico tariffs framed around immigration and opioids. The tariffs are invalid from inception, not prospectively.

Sources (independent, consistent):
- Holland & Knight, "Supreme Court Strikes Down IEEPA Tariffs: What Importers Need to Know Now," 2026-02. https://www.hklaw.com/en/insights/publications/2026/02/supreme-court-strikes-down-ieepa-tariffs
- WilmerHale client alert, 2026-02-20. https://www.wilmerhale.com/en/insights/client-alerts/20260220-supreme-court-strikes-down-ieepa-tariffs-what-now
- White & Case, "United States terminates IEEPA-based tariffs following supreme court decision." https://www.whitecase.com/insight-alert/united-states-terminates-ieepa-based-tariffs-following-supreme-court-decision
- Norton Rose Fulbright, "Potential refunds: US Supreme Court overturns IEEPA tariffs." https://www.nortonrosefulbright.com/en/knowledge/publications/20f2de87/potential-refunds-us-supreme-court-overturns-ieepa-tariffs

**Refund magnitude — DIRECTLY ESTABLISHED, two figures in circulation.** The Court of International Trade ordered CBP to refund approximately **$165 billion**. The Penn Wharton Budget Model separately estimated revenue at risk above **$175 billion**, and put cumulative IEEPA receipts at **$179 billion** since February 2025, modeled at roughly **$500 million per day** across ~11,000 eight-digit HTS categories and 233 countries.

The $165B and $175B figures are not in conflict: the first is what a court ordered refunded, the second is what a model estimates was collected and is therefore exposed. Both should be quoted with their basis attached.

- Penn Wharton Budget Model, 2026-02-20. https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/
- Holland & Knight, "Court of International Trade Orders Nationwide Tariff Refunds," 2026-03. https://www.hklaw.com/en/insights/publications/2026/03/court-of-international-trade-orders-nationwide-tariff-refunds
- Skadden, "Tariff Refund Mechanism Takes Shape After Supreme Court's IEEPA Ruling," 2026-04. https://www.skadden.com/insights/publications/2026/04/insights-april-2026/tariff-refund-mechanism-takes-shape

**Refund mechanics — DIRECTLY ESTABLISHED.** CBP activated phase one of the refund process on **April 20, 2026**, limited to certain unliquidated entries and entries within 80 days of liquidation. Refunds carry interest and are staged.

**Bearing on the manuscript.** The submission at the pre-revision line 128 referred only to "litigation-driven refunds" pushing May 2026 net collections below zero. It never named the ruling, the Court, the date, or the invalidation. This is the largest single evidentiary gap found in the sweep. It is also directly on-thesis: an institution external to the executive forced a correction the political system had not made, which is relationship 1 (information quality drives institutional performance) operating through the judiciary rather than through prices.

---

## 2. Replacement tariff authorities recover well under half the lost revenue

**DIRECTLY ESTABLISHED.** After the ruling the administration moved to Section 122 of the Trade Act of 1974 as a temporary bridge and launched country-specific Section 301 investigations, with Section 338 also invoked.

**MULTI-SOURCE INTERPRETATION — the replacement is partial.** The Committee for a Responsible Federal Budget, in a piece dated **2026-07-23**, concluded that Section 301 and Section 338 tariffs together "replace less than 60%" of the revenue lost to the IEEPA ruling. CRFB further reports that tariffs enacted and proposed since January 2025 will generate about **$825 billion less** revenue through FY2036 than CBO's February 2026 baseline assumed.

- CRFB, "Section 301 & 338 Tariffs Replace Less Than 60% of Lost IEEPA Revenue," 2026-07-23. https://www.crfb.org/blogs/section-301-338-tariffs-replace-less-60-lost-ieepa-revenue

**DIRECTLY ESTABLISHED — the replacement is itself contested.** The Section 122 tariffs enacted in February were ruled illegal by the Court of International Trade, pending appeal. Challenges to the Section 301 and 338 actions are anticipated.

- Council on Foreign Relations, "How Trump's Tariffs Could Survive the Supreme Court Ruling." https://www.cfr.org/articles/how-trumps-tariffs-could-survive-the-supreme-court-ruling
- PwC Canada, "US Court of International Trade order affects IEEPA tariff refunds." https://www.pwc.com/ca/en/services/tax/publications/tax-insights/us-court-ieepa-tariff-refunds-2026.html

**Rates and coverage — DIRECTLY ESTABLISHED.** Vietnam, Cambodia and Thailand sat at a flat **10% Section 122** rate expiring **July 24, 2026**, with USTR proposing **12.5% Section 301** duties on 46 countries as the replacement; Vietnam falls in the higher 12.5% group. USTR initiated Section 301 investigations on **March 11, 2026** covering structural excess capacity, and released findings of 60 forced-labor investigations on **June 2, 2026**. Section 301 tariffs apply to roughly **$949 billion** of 2026 imports.

- Vietnam Briefing, "US Section 301 Forced-Labor Investigation." https://www.vietnam-briefing.com/news/us-section-301-forced-labor-investigation-new-trade-compliance-risks-for-vietnam-exporters.html/
- Tax Foundation tariff tracker. https://taxfoundation.org/research/all/federal/trump-tariffs-trade-war/

**Discrepancy flagged.** The manuscript states the July 23 Section 301 action "places sixty economies at 10% or 12.5%, with Vietnam and Thailand at the higher tier." Search confirms Vietnam in the 12.5% group. **Thailand's tier could not be independently confirmed** in this session. Treat the Thailand half of that sentence as `carried_unverified` until checked.

---

## 3. Forecast 14 (net customs duties above $250B in FY2027) — repricing warranted

**DIRECTLY ESTABLISHED.** Cumulative FY2026 customs collections through June 2026 (nine months) were approximately **$163 billion**. **June 2026 net customs duties were negative $25.6 billion**: $23.6B collected in gross duties against $49.2B paid out in refunds.

- Quartz, "U.S. pays more in tariff refunds in June than it makes in tariff revenue," 2026-07-14. https://qz.com/us-tariff-refunds-june-customs-deficit-071426
- Treasury Monthly Treasury Statement, June 2026. https://fiscaldata.treasury.gov/static-data/published-reports/mts/MonthlyTreasuryStatement_202606.pdf (URL recorded; **not fetched this session**, proxy blocked)
- CBO Monthly Budget Review, March 2026. https://www.cbo.gov/system/files/2026-04/61979-MBR.pdf (same caveat)

**MY INFERENCE — the 70% probability is too high.** The forecast requires FY2027 net customs duties above $250.0B in the September 2027 MTS first print. Against that:

1. The FY2025 base was $194.9B, and the forecast needed a $55B gain from there. That framing assumed the FY2025 regime persisted.
2. The legal authority generating the bulk of that revenue was struck down, retroactively.
3. Replacement authorities recover under 60% of the lost revenue on CRFB's estimate, and the principal bridge authority has itself been ruled illegal at first instance.
4. Refunds are being paid out of the same net line the forecast resolves on, and have already driven one month negative.

The forecast resolves on **net** duties, so refunds subtract directly. A **$250B net** print in FY2027 requires the Section 301/338 regime to exceed the FY2025 IEEPA-era gross run-rate while the refund tail is still being paid. Nothing in the evidence supports 70%.

**Recommended reprice: 70% → 25%.** Retained above a floor because Section 301 coverage of $949B of imports at 10–12.5% is a large base, the refund tail should substantially clear during FY2027, and Congress could ratify tariffs by statute. This is an inference by this verifier, not a source's estimate, and the manuscript should mark it as a revision forced by the ruling rather than a routine recalibration.

---

## 4. Forecast 13 (core PCE) and the macro anchors — largely intact

**DIRECTLY ESTABLISHED.** Core PCE was **3.3% y/y in June 2026**, down from **3.4% in May 2026**. The next release, covering July, was scheduled for **August 26, 2026**, so no July print existed as of this sweep.

- Trading Economics, US Core PCE Price Index Annual Change. https://tradingeconomics.com/united-states/core-pce-price-index-annual-change
- Qz, "June 2026 PCE inflation falls 0.1%," 2026-07-30. https://qz.com/june-2026-pce-consumer-spending-personal-income-073026
- BEA, Personal Income and Outlays. https://www.bea.gov/data/personal-consumption-expenditures-price-index-excluding-food-and-energy (URL recorded; **not fetched**, 403)

This **confirms** the manuscript's stated anchor of 3.3% in June and its "seventh consecutive reading at or above 3.0%." The Figure 4 core PCE panel does not require correction.

**CAUSAL CLAIM affected, though.** The manuscript derives its inflation floor from a tariff wedge. If the IEEPA tariffs were invalidated in February 2026 and refunds are flowing, the wedge shrank part-way through the very period the paper cites as evidence for it, yet core PCE stayed at or above 3.0% throughout. Two readings compete:

- **Reading A (weakens the paper):** inflation persisted while the tariff wedge shrank, so tariffs were not the binding driver. The paper's transmission channel is overstated.
- **Reading B (preserves it):** tariff pass-through is slow and partly irreversible, refunds accrue to importers rather than to consumer prices, and replacement tariffs kept much of the wedge in place. Persistence is consistent with the mechanism.

**Better supported: Reading B, weakly.** Refunds go to importers of record, and there is no evidence in this sweep of consumer-price pass-back. But the manuscript already concedes that forecast 13 "establishes co-movement with the framework rather than causal attribution," and this episode makes that concession load-bearing rather than decorative. The paper should say so.

---

## 5. Forecast 1 (China NEV share) — supported, but the mechanism is misattributed

**DIRECTLY ESTABLISHED — penetration.** CPCA monthly NEV retail penetration in 2026: January **44.4%**, April **60.6%** preliminary revised to **61.4%**, May **63%** (record), June **62.8%**.

**DIRECTLY ESTABLISHED — units and direction.** Monthly NEV retail units: January 800,000; April 883,000; May 974,000; June 1,037,000. Year-over-year, **NEV retail sales fell 5% in May and 7% in June**. Total passenger-car sales fell **20% year-over-year in April**.

- CnEVPost, April 2026 retail. https://cnevpost.com/2026/05/11/china-apr-2026-nev-retail-sales/
- CnEVPost, May preliminary. https://cnevpost.com/2026/06/03/china-may-nev-retail-cpca-preliminary/
- CnEVPost, June preliminary. https://cnevpost.com/2026/07/03/chinas-nev-retail-jun-cpca-preliminary-data/
- BitAuto, "CPCA April Data: China Passenger Car Sales Fall 20% YoY, NEV Penetration Hits Record 62.8%." https://www.bitauto.hk/en/news/10011000968.html
- Gasgoo, NEV penetration nears 60% in first half of April. https://autonews.gasgoo.com/articles/news/passenger-car-sales-declined-year-on-year-and-month-on-month-in-first-two-weeks-of-april-nev-penetration-rate-nears-60-2044726602527580161

**CAUSAL CLAIM requiring correction.** The manuscript treats rising penetration as adoption: the transition "continues" and prints "have remained above 60% since April 2026." The penetration figures support that sentence as written. The mechanism behind them does not match the manuscript's account.

A share is a ratio. Penetration rose through H1 2026 while the numerator itself contracted year-over-year (−5% May, −7% June). That is arithmetically possible only if the denominator contracted faster. The April print makes it explicit: total passenger-vehicle sales fell 20% y/y.

**Proposed mechanism:** the internal-combustion segment is collapsing faster than the NEV segment is, in a total market that is itself shrinking. **Rival explanation:** NEV demand was pulled forward into 2025 by the full purchase-tax exemption, and the 2026 halving (RMB 15,000 cap) depressed the numerator temporarily while ICE fell for unrelated reasons. Both are consistent with the data available here; this session cannot separate them.

**Bearing on forecast 1.** Directionally the forecast looks *better* supported than the manuscript claims, since monthly prints are running 61–63% against a >60.0% full-year 2027 threshold. But the reason matters for the framework: a share driven by denominator collapse is weaker evidence for the "optionality of strategic control" thesis than a share driven by adoption, because it partly reflects a demand shock rather than a policy-built capability. The manuscript should state the denominator effect and stop reading the share as pure adoption.

**Note on Figure 1.** The figure plots full-year first prints and the December 2025 single-month print. Nothing in it is falsified. The 2026 monthly series is new information the figure does not yet carry.

---

## 6. Forecast 3 (China gasoline) — supported, with a named rival mechanism

**DIRECTLY ESTABLISHED.** Chinese seaborne crude imports fell **3.6 mb/d** from February to April 2026 (IEA May 2026 OMR). China imported **8.1 mb/d** in Q2 2026, **32% below** the prior quarter, with May and June below **8.0 mb/d** for the first time since **2016**. Chinese oil demand growth for 2026 is set at **+50 kb/d y/y**, down from **+220 kb/d** in 2025. The expected **5.5%** gasoline decline would be the **second-steepest on record**, after the 2022 COVID-lockdown year.

- IEA Oil Market Report, May 2026. https://www.iea.org/reports/oil-market-report-may-2026
- IEA Oil Market Report, July 2026. https://www.iea.org/reports/oil-market-report-july-2026
- EIA, "China's crude oil imports fell in the second quarter." https://www.eia.gov/todayinenergy/detail.php?id=67905
- OilPrice, "China's Gasoline Consumption Could Plunge 5.5% in 2026." https://oilprice.com/Latest-Energy-News/World-News/Chinas-Gasoline-Consumption-Could-Plunge-55-in-2026-as-Oil-Prices-Surge.html

**CAUSAL CLAIM — the IEA names a mechanism the manuscript does not.** The IEA attributes part of the gasoline decline to **higher pump prices discouraging ICE driving**, with EV convenience and running cost as a compounding factor. The manuscript attributes the decline to structural fleet displacement plus refinery-run cuts and halted product exports.

These are not mutually exclusive, and the manuscript's forecast 3 is explicitly designed as the discriminating test: a price-induced decline should partly reverse when prices normalize, a fleet-induced decline should not. **The manuscript should name the IEA's price attribution as the rival mechanism rather than leaving it implicit**, because a reader who knows the OMR will otherwise notice the omission. Naming it strengthens the ratchet-test framing rather than weakening it.

**MY INFERENCE.** The 2Q26 import collapse (−32% q/q, lowest since 2016) is larger than structural displacement can account for on the manuscript's own arithmetic (~0.45 mb/d cars-only, ~1.0 mb/d all-segments per Kpler). This is consistent with the manuscript's existing position that refinery cuts and export curtailment supplied most of the volume, and Figure 3 already says the right-hand panel is a scale comparison rather than a decomposition. No correction needed to Figure 3.

---

## 7. Hyperscaler capex — the manuscript's figures are stale

**DIRECTLY ESTABLISHED.** Combined 2026 capital expenditure guidance for Microsoft, Alphabet, Amazon and Meta is now approximately **$725 billion**, up **77%** from 2025's **$410 billion**.

Company-level 2026 guidance as reported:

| Company | 2026 guidance (search-reported) | Manuscript / V06 value |
|---|---|---|
| Alphabet | $195–205B | $195–205B (agrees) |
| Amazon | ~$200B | ~$220B |
| Microsoft | ~$190B calendar | ~$175B (FY2027, fiscal basis) |
| Meta | $115–135B | $130–145B (incl. finance leases) |

- Statista, "Big Tech's AI Spending to Reach $725 Billion in 2026." https://www.statista.com/chart/35046/capital-expenditure-of-meta-alphabet-amazon-and-microsoft/
- Futurum, "AI Capex 2026." https://futurumgroup.com/insights/ai-capex-2026-the-690b-infrastructure-sprint/
- CNBC, "Amazon, Meta and Microsoft face skeptical investors," 2026-07-28. https://www.cnbc.com/2026/07/28/hyperscalers-face-higher-capex-scrutiny-after-alphabet-report-panned.html

**COULD NOT VERIFY — the company-level discrepancies.** The differences above are not necessarily errors. V06 documented that these figures are not comparable across companies without adjustment: Microsoft guides on a June fiscal year, Meta's guidance includes finance-lease principal while the forecast-8 criterion excludes finance leases, and a finance-to-operating lease reclassification depressed one Microsoft figure. This session could not obtain the filings needed to re-cut them onto a common calendar-quarter, finance-lease-excluded basis. **The $725B aggregate should be used as an aggregate only, and the manuscript should not adopt the company-level numbers above without the boundary work V06 specifies.**

**PROJECTION, not observation.** Analyst consensus now sees combined 2027 capex **above $1 trillion**. This is a projection by named analysts, not guidance and not an actual. Any chart carrying it must mark it distinctly from both actuals and guidance.

**Bearing on Figure 2 and forecast 8.** Figure 2's 2026 guidance bar reads ≈$700B; the current figure is ≈$725B. That is a defensible refresh. Forecast 8 asks whether calendar-2028 prints below calendar-2027. If 2027 lands above $1T, the required contraction is off a far larger base than the manuscript's plotted history contemplates. The forecast's 30% was already called the manuscript's weakest position; the larger base does not obviously change the probability, but the manuscript should not leave a stale $700B in the figure while claiming precision elsewhere.

---

## 8. Forecast 7 (1 GW cancellation disclosed) — mechanism confirmed, criterion not yet met

**MULTI-SOURCE INTERPRETATION.** SemiAnalysis reports Microsoft **freezing 1.5 GW** of near-term self-build datacenter projects previously scheduled for 2025 and 2026, letting **more than a gigawatt** of agreements expire, and withdrawing from multiple 100 MW deals.

- SemiAnalysis, "Microsoft's Datacenter Freeze." https://newsletter.semianalysis.com/p/microsofts-datacenter-freeze
- Data Center Frontier, "Does It Matter If Microsoft Is Cancelling AI Data Center Leases?" https://www.datacenterfrontier.com/hyperscale/article/55270517/does-it-matter-if-microsoft-is-cancelling-ai-data-center-leases
- SemiAnalysis, "Stop Saying Half of 2026 US Datacenter Capacity Is Canceled." https://newsletter.semianalysis.com/p/stop-saying-half-of-2026-us-datacenter

**This does not resolve forecast 7 YES.** The criterion requires the company's own SEC filing, official transcript, or press release quantifying ≥1 GW. SemiAnalysis is third-party analysis, which Table 2 explicitly excludes. The capacity threshold appears to have been crossed in reality while the disclosure requirement has not been met.

**MY INFERENCE — this is the strongest available confirmation of the manuscript's two-stage split.** The 0.80 × 0.70 derivation separates the decision from the admission. Here the decision is reported at 1.5 GW by a well-regarded analyst shop, and the company has not put a number on it. That is precisely the withheld 0.30.

**Rival explanation, stated fairly.** Several sources read the same events as **reallocation rather than retreat**: Microsoft spent **$11.1 billion** leasing datacenter space in Q1 2026 while waiting for self-builds; CoreWeave's Meta agreement expanded by ~**$21 billion** in April 2026, on top of a **$14.2 billion** September 2025 deal, for a combined ~**$35 billion**. Under this reading, capacity is moving between owned and leased and between counterparties, and no aggregate retreat is occurring.

**Which is better supported:** the reallocation reading, on current evidence. Aggregate 2026 capex rose 77%, which is difficult to reconcile with retreat. The manuscript's forecast 7 does not depend on aggregate retreat, though: it asks only whether ≥1 GW gets cancelled *and disclosed*, which is compatible with rising aggregate spend. The manuscript should acknowledge the reallocation reading rather than let a reader supply it.

---

## 9. Forecast 11 (depreciation) — context strengthened, direction unchanged

**DIRECTLY ESTABLISHED.** Meta extended server and network useful life from **4 to 5.5 years**, reducing **2025 depreciation expense by $2.9 billion**. Amazon moved 3→4 years in 2020 and to 6 years by 2023; Microsoft moved 4→6 for cloud server and network equipment. Hyperscalers currently report **5 to 6 year** lives. The trend of uniform extension **diverged in 2025**, when Amazon shortened a subset while Meta extended further.

- Harvard Business School case, "Meta: Accounting for AI Data Center Depreciation." https://www.hbs.edu/faculty/Pages/item.aspx?num=68932
- SiliconANGLE, "Resetting GPU depreciation." https://siliconangle.com/2025/11/22/resetting-gpu-depreciation-ai-factories-bend-dont-break-useful-life-assumptions/
- National Law Review, "Deep Quarry: Useful Lives of GPUs." https://natlawreview.com/article/deep-quarry-useful-lives-gpus-key-considerations

**PROJECTION by a named skeptic.** Michael Burry argues AI hardware economically lives 2–3 years against 5–6 year book lives, and estimates depreciation understated by roughly **$176 billion** across 2026–2028, overstating hyperscaler profits by more than 20%. This is one investor's estimate, contested, and should be labeled as such if used.

This is consistent with the manuscript's Table 1 and its 30% probability. The $2.9B Meta figure is a useful quantification of the incentive to delay that the manuscript asserts. No repricing indicated.

---

## 10. Forecast 9 (workflow data) and claim 3 — direct confirmation found

**DIRECTLY ESTABLISHED.** Reuters revealed on **April 21, 2026** that Meta had deployed monitoring software on US employees' work laptops capturing keystrokes, mouse movement, clicks, and periodic screenshots across hundreds of sites and apps. CTO **Andrew Bosworth confirmed there is no opt-out**. More than **1,600 employees** signed an internal petition demanding cancellation. Meta **paused rather than cancelled** the program and stated there is "currently no evidence" of improper internal access.

**The finding that matters most: European employees are exempt because GDPR does not permit the collection.**

- Gizmodo, "Meta Plans to Turn Its Employees' Clicks and Keystrokes into AI Training Data." https://gizmodo.com/meta-plans-to-turn-its-employees-clicks-and-keystrokes-into-ai-training-data-2000749176
- The HR Digest, "Meta Updates Employee Tracking Capabilities." https://www.thehrdigest.com/meta-updates-employee-tracking-capabilities-putting-ai-training-front-and-center/
- State of Surveillance, "Meta Is Recording Every Keystroke Its Employees Make." https://stateofsurveillance.org/news/meta-employee-keystroke-surveillance-mci-ai-training-2026/

**Bearing on framework claim 3.** The manuscript argues that employment and privacy law set the accumulation rate of workflow data, and that Europe may protect workers while excluding its firms from the input market. A single company running the same program in one jurisdiction and being unable to run it in another, within one corporate policy, is the cleanest natural experiment the claim could ask for. The manuscript currently argues this from statute (GDPR minimization, Article 4 of Italy's Workers' Statute, works councils). It should argue it from the observed carve-out, which is far stronger.

**Caveat.** All of the above is press reporting of an internal program. Meta has confirmed the program, the absence of an opt-out, and the pause. The corpus-exposure figures remain press-sourced, as the manuscript already states.

---

## 11. Forecast 6 (EU enforcement) — base rate may be thickening

**DIRECTLY ESTABLISHED.** The EDPB adopted **Guidelines 03/2026 on Web Scraping in the Context of Generative AI on July 8, 2026**. Italian, Irish, Dutch and French authorities have each taken enforcement action against AI companies. DPAs have begun citing GDPR and AI Act violations in the same action, beginning with a **€535M TikTok decision in November 2025**.

- EDPB guidance coverage. https://www.techtimes.com/articles/320024/20260709/gdpr-applies-ai-training-data-eu-ends-web-scraping-free-pass-every-lab.htm
- Oxford *International Data Privacy Law*, "Should data protection authorities enforce the AI Act? Lessons from EU-wide enforcement data." https://academic.oup.com/idpl/article/16/1/ipaf033/8382692
- Compliance Stack GDPR enforcement tracker. https://compliancestack.ai/penalties/gdpr/dpa-enforcement-trends

**SOURCE DISAGREEMENT — flagged, not resolved.** One source states full AI Act enforcement for high-risk systems applies from **August 2, 2026**. The manuscript states the Digital Omnibus (Regulation (EU) 2026/1744) **deferred** high-risk obligations for workplace AI from August 2026 to **December 2, 2027**.

These cannot both be right about workplace AI. The likeliest reconciliation is that August 2, 2026 is the general high-risk date under the original AI Act timeline while the Omnibus carved out a deferral for specific Annex III categories including employment. **This session could not obtain the Omnibus text to confirm**, and the distinction is load-bearing for forecast 6, whose probability was cut from 62% to 35% specifically because the AI Act trigger was absent from the first sixteen months of the window. **This is the highest-priority open item from the sweep.** If the deferral does not cover workplace AI, forecast 6 is underpriced.

**MY INFERENCE, held loosely.** The thickening of AI-training enforcement generally (EDPB guidelines, four national authorities active, joint GDPR/AI Act theories) modestly raises the probability that some authority names the employee-monitoring plus AI-training nexus before end-2028. Absent resolution of the deferral question, a move from 35% toward the low 40s would be defensible. I would not make that change without settling the Omnibus scope first.

---

## 12. Forecast 10 (LMArena) — the metric itself is fragile

**DIRECTLY ESTABLISHED.** Four labs (Anthropic, OpenAI, Google, xAI) sat within Elo noise of one another at the top of LMArena through 2026. The Elo gap from **#1 to #10 is roughly 28 points**, and differences under ~10 points are generally within noise. July 2026 saw Claude Fable 5 (July 1), Grok 4.5 (July 8), and the GPT-5.6 family including Sol (July 9). Earlier in 2026, Claude Opus 4.6 held #1 at Elo 1504 with Gemini 3.1 Pro Preview statistically tied.

- Swfte AI leaderboard, July 2026. https://www.swfte.com/ai/leaderboard
- ToolCenter LMArena leaderboard. https://www.toolcenter.ai/en/llm-leaderboard

**MY INFERENCE — supports the 20%, possibly lower.** The forecast requires a China-headquartered lab at **#1 for 30 consecutive days**. When the top four are within confidence-interval overlap and releases arrive roughly monthly, holding an uninterrupted 30-day #1 is hard for *any* lab, which cuts the probability for a Chinese entrant independently of capability. DeepSeek V4.1 Pro is reported as strong on math and reasoning without holding overall #1.

This is a **criterion-fragility** point the manuscript does not make: the threshold is sensitive to leaderboard noise in a way that is not about Chinese model quality. Worth a sentence, since the manuscript stakes the forecast on the frontier-versus-diffusion contrast.

**Note.** These leaderboard aggregators are secondary and mutually inconsistent on model naming. Treat the Elo values as indicative.

---

## 13. Forecast 2 (token prices) — NO CHANGE, sources unreliable

**COULD NOT VERIFY.** Third-party LLM pricing trackers returned mutually inconsistent and visibly stale figures, including one listing Anthropic's current flagship as "Claude Opus 4.8 as of May 28, 2026" alongside another source reporting Claude Fable 5 shipping July 1, 2026. Reported OpenAI figures included GPT-5.5-pro at $180/M output, a GA flagship at $30/M, and GPT-5.4 at $15/M, which do not cleanly map onto the manuscript's designated baseline of GPT-5.6 Sol at $30/M.

**Recommendation: change nothing.** These aggregators are exactly the class of source that repeats a primary without tracing it, and they disagree with each other. The manuscript's existing position (baseline carried, direct pricing-page capture blocked, `snapshot_secondary_only` recorded in `data/snapshots/`) remains the honest one. The forecast-2 baseline should be captured directly before submission if any session regains egress.

---

## 14. Forecast 16 (LA28 delivery) — supported

**MULTI-SOURCE INTERPRETATION.** Of the original 28 projects, **18 are reported still on course** to complete before the Games, with **10 anticipated to open after 2028**. A phased breakdown in circulation reads: 5 complete, 3 by end-2024, 5 in 2025, 3 in 2026, 8 in 2027, 4 in 2028. The LAX/Metro Transit Center opened **June 2025**. The program is valued at roughly **$20 billion**.

- LA Metro 28x28 program page. https://www.metro.net/28x28/
- LAist, LA28 transit status. https://laist.com/news/transportation/la28-olympics-transportation
- Wikipedia, Twenty-eight by '28. https://en.wikipedia.org/wiki/Twenty-eight_by_%2728

**Bearing on the forecast.** The threshold is fewer than 20 open for fare-paying service on July 14, 2028. An 18-on-course count sits just below it, which is consistent with the manuscript's 70% and leaves little margin: two projects slipping the other way would flip it.

**Caveat, important.** Several of these counts appear to date from 2024 reporting, and it is unclear whether they are measured against the **original** 28 or the **March 2024 revised list** that governs resolution under Table 2. This session could not obtain current LA Metro board reports. Treat the 18 figure as indicative of direction only, status `carried_unverified`.

---

## 15. Forecast 15 (world models) — asymmetry confirmed

**DIRECTLY ESTABLISHED.** NVIDIA spent 2026 enrolling industrial robotics vendors onto Cosmos: **ABB Robotics, KUKA, Universal Robots, Doosan Robotics, Boston Dynamics and Figure AI** announced stack integration since January 2026, and a **July 17, 2026** Japan announcement added 22 more manufacturers including **FANUC, Kawasaki and Yaskawa**. Named adopters include 1X, Agility Robotics, Figure AI, Boston Dynamics, Uber and XPENG. Cosmos 3 shipped **June 22, 2026** as an omnimodal world model for physical AI.

- NVIDIA Cosmos 3 technical report, 2026-06-22. https://research.nvidia.com/labs/cosmos-lab/cosmos3/technical-report.pdf
- NVIDIA newsroom, robotics leaders. https://nvidianews.nvidia.com/news/nvidia-and-global-robotics-leaders-take-physical-ai-to-the-real-world
- TechTimes, Japan manufacturers join Cosmos coalition, 2026-07-17. https://www.techtimes.com/articles/320801/20260717/nvidia-brings-robot-ai-device-japans-top-manufacturers-join-cosmos-coalition.htm

**MY INFERENCE — this confirms the manuscript's stated asymmetry precisely.** Every named adopter is a robot maker, an AI company, or a technology/automotive firm. The forecast requires a **Fortune 500 company outside the Technology sector** disclosing world-model synthetic data used to train robots **in its own production or logistics facilities**. Vendor-side adoption is now broad and well documented; end-user disclosure remains absent. The manuscript predicted exactly this ordering ("Vendor adoption is already visible; end-user disclosure is the lagging indicator"), and the 2026 record supports it. No repricing indicated; the evidentiary basis is much stronger than the manuscript currently shows.

---

## 16. Forecast 5 (robots) — no new data

**DIRECTLY ESTABLISHED, unchanged.** World Robotics 2025 (published September 2025, covering 2024) reports **295,000** Chinese installations of **542,076** worldwide, a computed **54.4%** that IFR's prose rounds to 54%. Chinese robot makers' domestic share rose to **57%** in 2024 from 47% in 2023. China's operational stock reached **2,027,000** units.

**PROJECTION.** IFR expected global installations to grow **6% to 575,000 units in 2025**.

- IFR press release, World Robotics 2025. https://ifr.org/ifr-press-releases/news/global-robot-demand-in-factories-doubles-over-10-years
- IFR China press release. https://ifr.org/downloads/press_docs/2025-09-25-IFR_press_release_China_in_English.pdf

**World Robotics 2026 was not available in this sweep**, consistent with IFR's September publication cadence. This also **resolves V07's concern** about the manuscript citing "World Robotics 2028": the 2025 edition covers 2024, so the 2028 edition covers 2027, which is the forecast's reference year. The citation is correct.

The domestic-share finding (57%, up from 47%) is new supporting evidence for the diffusion half of the frontier-versus-diffusion contrast and is not currently in the manuscript.

---

## Summary of recommended manuscript changes

| # | Change | Basis | Priority |
|---|---|---|---|
| 1 | Name the Feb 20, 2026 SCOTUS IEEPA ruling and the refund mechanics | §1 | **Required** |
| 2 | Reprice forecast 14 from 70% to 25% | §2, §3 | **Required** |
| 3 | State the NEV denominator effect; stop reading share as pure adoption | §5 | **Required** |
| 4 | Name the IEA's price attribution as the rival mechanism for forecast 3 | §6 | High |
| 5 | Refresh Figure 2's 2026 guidance bar to ≈$725B; mark 2027 >$1T as analyst projection | §7 | High |
| 6 | Add Meta's EU carve-out as direct evidence for claim 3 | §10 | High |
| 7 | Close forecast 17's admitted gap: USD/JPY 159.41, BoJ 1.0% | §17 below | High |
| 8 | Acknowledge the reallocation reading against forecast 7 | §8 | Medium |
| 9 | Note LMArena criterion fragility for forecast 10 | §12 | Medium |
| 10 | Add IFR domestic-share 57% to the diffusion argument | §16 | Low |
| 11 | Resolve the Digital Omnibus scope question before touching forecast 6 | §11 | **Open** |
| 12 | Confirm Thailand's Section 301 tier | §2 | **Open** |

---

## 17. Forecast 17 (USD/JPY) — the manuscript's acknowledged gap, now closable

**DIRECTLY ESTABLISHED.** USD/JPY was **159.41 on July 31, 2026**, down 0.07% on the session. The yen strengthened **1.95% over the prior month** and weakened **8.25% over twelve months**. The Bank of Japan held its short-term policy rate at **1.0%** at its July 2026 meeting, the highest since **September 1995**, after a **25bp hike in June 2026**. The July decision passed **8–1**, with Hajime Takata dissenting for 1.25%.

- Trading Economics, Japanese Yen. https://tradingeconomics.com/japan/currency
- Trading Economics, Japan Interest Rate. https://tradingeconomics.com/japan/interest-rate
- FXStreet, Japanese Yen mid-year outlook, 2026-07-31. https://www.fxstreet.com/analysis/japanese-yen-mid-year-outlook-why-boj-rate-hikes-arent-saving-the-yen-and-what-actually-would-202607310737
- Investing.com, "Yen Carry Trade Back in Focus as BoJ Rate Hike Looms." https://www.investing.com/analysis/usdjpy-yen-carry-trade-back-in-focus-as-boj-rate-hike-looms-200671786

**CAUSAL CLAIM, refined.** The carry trade now faces compression from both ends: the BoJ is raising funding costs while the Fed is expected to reduce the return. One analysis nonetheless puts the differential at **250–275bp by Q4 2026**, which still pays in a leveraged position. A narrowing-but-still-positive carry is the configuration in which unwinds have historically been most violent, because positioning persists while the cushion thins.

**Bearing on the manuscript.** The paper explicitly concedes that the USD/JPY level and BoJ path "are carried from our prior draft and were not re-verified in this revision," and rests the 30% on the reference-class event and funding-channel argument alone. That concession can now be replaced with verified values. The 30% itself needs no change; the reasoning behind it can stop apologizing.
