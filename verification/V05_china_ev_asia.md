# V05 — China EV/NEV and Asia EV Verification

**Verifier note on method/tooling constraints (read first):** In this session, `WebFetch` returned `HTTP 403 Forbidden` for every URL tested — including cpcaauto.com, CnEVPost, Gasgoo, Global Times, Steelorbis, China Briefing, ChinaEVHome, carnewschina, Bloomberg, electrive, JATO, and even en.wikipedia.org — and a direct `curl` through the environment's outbound proxy to the same hosts also failed at the CONNECT step (`403`). This points to a session-level network/proxy restriction rather than a site-specific block (confirmed via `$HTTPS_PROXY/__agentproxy/status`, which showed unrelated CONNECT rejections). `WebSearch` worked and was used for all findings below, but this session's WebSearch budget (200 calls) was exhausted before every sub-question could be run to exhaustion (noted per item). All figures below are therefore drawn from WebSearch result snippets/AI-synthesized summaries of the underlying pages (the tool fetches and summarizes source pages server-side) rather than from independently re-fetched raw HTML. URLs are exactly as returned by the tool. Where a snippet's numeric attribution looked shaky, that is flagged explicitly rather than silently smoothed over. cpcaauto.com itself was never reachable (as expected/pre-warned); all China data below comes via secondary channels that cite CPCA (乘联会) prints, or via Chinese-language outlets reproducing 乘联会's own monthly report text.

Access date for all sources: **2026-07-31**.

---

## 1. CPCA NEV retail (BEV+PHEV) share of passenger-vehicle retail sales, full calendar years 2020–2025

**Status: CONFIRMED for 2022–2024; CONFIRMED WITHIN ROUNDING for 2020, 2021, 2025; denominator confusion flagged where found.**

| Year | Draft figure | Verified figure | Retail units (NEV) | Match |
|---|---|---|---|---|
| 2020 | 5.8% | **5.8%** | — (not separately re-derived) | Match |
| 2021 | 14.8% | **14.8%** | 2.989 million | Match |
| 2022 | 27.6% | **27.6%** | (PV retail total 20.543 million) | Match |
| 2023 | 35.7% | **35.7%** | 7.736 million | Match |
| 2024 | 47.6% | **47.6%** (also seen as 47.9–47.97%) | 10.899 million | Match (small variant reported elsewhere) |
| 2025 | 54.1% | **53.9%–54.1%** (source-dependent) | 12.809 million | Match within ~0.2pp |

All figures are attributed by the citing outlets to 乘联会 (CPCA, China Passenger Car Association) **retail (零售)** data for the **passenger-vehicle** market specifically (not CAAM/中汽协 wholesale, and not all-vehicle-type data that includes commercial vehicles) — i.e., the definition the manuscript is using is the correct one to cite, and the figures line up.

**Detail and sourcing:**

- **2021 = 14.8%, retail 2.989 million units.** Source: article titled "2021年新能源乘用车零售298.9万辆 渗透率增至14.8%" ("2021 NEV passenger-vehicle retail 2.989M units, penetration rises to 14.8%"), attributing the number to 乘联会/CPCA and explicitly using "2020年的5.8%" (2020's 5.8%) as the prior-year comparison baseline in the same piece — this is the source for the 2020 figure too. Org: 乘联会 (CPCA), via 亚讯车网 (aqsiqauto.com). URL: https://www.aqsiqauto.com/newcars/info/9553.html. Date: ~Jan 2022. Channel: secondary Chinese auto-trade press citing CPCA/乘联会.
  - **Denominator flag:** A different, higher figure for 2021 — "17.8%" — appeared in a 21世纪经济报道 (21jingji.com) headline ("新能源汽车这一年：从5.8%到17.8%的改变"), and separately CAAM (中汽协) reported ~13.4% wholesale, all-NEV-type (including commercial vehicles) penetration for 2021, with December 2021 alone at ~19.1–20.6%. These non-matching numbers are **not** CPCA retail passenger-vehicle figures — they are wholesale and/or all-vehicle-type denominators from a different trade body (CAAM) or a different in-year snapshot (December alone, not full-year). This is exactly the kind of denominator confusion the check asked to watch for; the manuscript's 14.8% for full-year 2021 retail passenger NEV is the CPCA-correct one.

- **2022 = 27.6%, PV retail total 20.543 million.** Source: "乘联会：2022年乘用车零售2054.3万辆，新能源渗透率达27.6%" via OFweek NEV channel. Org: 乘联会 (CPCA). URL: https://nev.ofweek.com/2023-01/ART-71008-8420-30584498.html. Date: ~Jan 2023. Channel: secondary Chinese industry trade press citing CPCA.
  - Note: one WebSearch synthesis surfaced a stray "25.6%" or "13%" for 2022 that appears to be either a misread/garbled AI summary artifact or a citation of a different (non-CPCA, non-retail) series; it is not corroborated by any specific dated CPCA-attributed article and is disregarded in favor of the OFweek-sourced 27.6%, which is directly attributed to 乘联会 with a matching total-market figure (20.543M) that is independently well known for 2022.

- **2023 = 35.7%, retail 7.736 million units (+36.2% YoY).** Source: "乘联会：2023年新能源乘用车国内零售销量773.6万辆，同比增长36.2%" plus companion coverage stating "全年渗透率35.7%，提升8.1个百分点" (full-year penetration 35.7%, up 8.1 points YoY). Org: 乘联会 (CPCA). URLs: https://www.ithome.com/0/744/214.htm ; https://www.yicai.com/news/101951212.html. Date: Jan 2024. Channel: secondary Chinese tech/business press (IT之家, 第一财经/Yicai) citing CPCA.

- **2024 = 47.6%, retail 10.899 million units (+40.7% YoY).** Source: "乘联会：2024年中国新能源汽车零售渗透率达到47.6% 同比增长12%" (percentage points YoY, not growth rate). Org: 乘联会 (CPCA). URL: https://www.199it.com/archives/1743685.html. Date: ~Jan 2025. Channel: secondary Chinese data-aggregator (199IT) citing CPCA. A companion 2024 wrap noted August 2024 as an interim peak at 53.9% before a second-half pullback, and December 2024 alone falling back near 49.4% — useful context that the annual 47.6% is a full-year average, not a year-end run-rate.

- **2025 = 53.9%–54.1% (small variance across outlets), retail 12.809 million units (+17.6% YoY), full-year PV retail total ≈23.7–23.8 million.** Two independently sourced figures:
  - 53.9%: "2025年1-12月，新能源乘用车市场累计零售1280.9万辆，同比增长17.6%，占全年乘用车零售总量的53.9%" — Org: 乘联会 (CPCA), via Guancha (观察者网) / Sina Finance. URLs: https://www.guancha.cn/qiche/2026_01_11_803443.shtml ; https://finance.sina.com.cn/stock/t/2026-01-11/doc-inhfwypt4021253.shtml. Date: 2026-01-11.
  - 54.07%: CnEVPost's synthesis of CPCA's preliminary December/full-year data. Org: CPCA (via CnEVPost). URL: https://cnevpost.com/2026/01/07/china-nev-retail-1-387-million-dec-2025-preliminary-cpca/. Date: 2026-01-07. Channel: secondary (CnEVPost), citing CPCA preliminary release.
  - Both are within ~0.2 percentage points of the manuscript's 54.1% and of each other — consistent with the normal CPCA preliminary-vs-final revision gap. **Verdict: CONFIRMED, treat as ≈54%, cite as approximate ("54.1%" is a defensible rounding of CPCA's own prints).**

---

## 2. December 2025 CPCA NEV retail share: draft says 60.4%, first month above 60%

**Status: CONFIRMED (with one unresolved minor discrepancy noted).**

- China's December 2025 passenger NEV retail sales reached **1.387 million units**, up 7% YoY and up 5% MoM (preliminary CPCA data). Total passenger-vehicle retail in December 2025 was **2.296 million units**, down 13% YoY. **NEV retail penetration reached 60.4% in December — surpassing 60% for the first time.** Math check: 1.387M / 2.296M = 60.4% — internally consistent with the two headline unit figures reported alongside the percentage.
  - Org: CPCA (China Passenger Car Association), preliminary data.
  - Sources/channels (all secondary, citing CPCA):
    - CnEVPost, "China NEV retail sales rise 7% to 1.387 million units in Dec, preliminary CPCA data shows," 2026-01-07. URL: https://cnevpost.com/2026/01/07/china-nev-retail-1-387-million-dec-2025-preliminary-cpca/
    - Steelorbis, "CPCA: China's passenger vehicle retail sales down 13.0% in December 2025" (explicitly states "the market penetration rate of NEVs stood at 60.4 percent in December... first time"). URL: https://www.steelorbis.com/steel-news/latest-news/cpca-chinas-passenger-vehicle-retail-sales-down-130-in-december-2025-1428147.htm
    - ChinaEVHome, "China NEV Retail Sales Reach 1.387 Million Units in Dec 2025, Up 7% YoY," 2026-01-07. URL: https://chinaevhome.com/2026/01/07/china-nev-retail-sales-reach-1-387-million-units-in-dec-2025-up-7-yoy/
  - Cross-check against November 2025: NEV retail 1.32 million units, penetration 59.3% (ChinaEVHome, 2025-12-08, citing CPCA — URL: https://chinaevhome.com/2025/12/08/chinas-nev-retail-sales-hit-1-32-million-units-penetration-climbs-to-59-3/). A rise from 59.3% (Nov) to 60.4% (Dec) is a coherent, plausible monthly progression, reinforcing the December figure.

- **Flag / minor discrepancy:** one WebSearch synthesis surfaced a lower figure — "12月新能源车国内零售渗透率59.1%" — attributed to 乘联会's official December monthly market-analysis report via a 199IT.com aggregation. I could not independently pin this to a specific, clearly-titled source page (the URL that AI-search associated with it was actually titled around "first week of December, 62.2%," so the 59.1% attribution may be a synthesis artifact mixing content from multiple scraped pages, or it could reflect 乘联会's own report using a slightly different, narrower denominator than the "preliminary CPCA" headline number CnEVPost/Steelorbis used). Given (a) three independent secondary channels all state 60.4% with a mutually consistent "first time above 60%" framing, and (b) the underlying unit figures they report (1.387M / 2.296M) arithmetically produce exactly 60.4%, I am treating **60.4% as the well-supported figure** and flagging 59.1% as an unresolved, lower-confidence outlier that the author should sanity-check against a primary 乘联会 release if the distinction matters for the manuscript's argument.

---

## 3. First-half / latest 2026 CPCA NEV retail share (context for the 2027 >60% forecast)

**Status: PARTLY SUPPORTED / CONFIRMED — monthly penetration has been running above 60% for several months in 2026, but the H1 cumulative average is lower due to a weak Jan–Mar (post-incentive-cliff) start.**

Monthly/period prints found (all preliminary CPCA data via CnEVPost/Sina-cited 乘联分会 reports; access date 2026-07-31 for all):

| Period | NEV retail | Penetration | Source | URL |
|---|---|---|---|---|
| Jan 2026 | ~800,000 units, +7.5% YoY, −40% MoM (post tax-change slump) | not stated in snippet | CnEVPost, 2026-01-22 | https://cnevpost.com/2026/01/22/cpca-estimates-china-jan-nev-retail-800000/ |
| Mar 2026 | retail sales −21% YoY | not stated in snippet | CnEVPost, 2026-04-03 | https://cnevpost.com/2026/04/03/china-mar-nev-retail-sales-cpca-preliminary/ |
| Apr 2026 | 1.406 million units (乘联分会 figure) | **62.8%** (per Sina/乘联分会); headline elsewhere says "tops 60% for the first time" | Sina Finance (乘联分会), 2026-05-08; CnEVPost, 2026-05-11 | https://finance.sina.com.cn/tech/digi/2026-05-08/doc-inhxemqm4292534.shtml ; https://cnevpost.com/2026/05/11/china-apr-2026-nev-retail-sales/ |
| May 2026 | 950,000 units retail | **62.9%** | 电池网 (itdcw.com), citing CPCA | https://www.itdcw.com/news/hangyeshuju/0609155a62026.html |
| Jun 2026 | ~1.037 million units, −7% YoY, +9% MoM | **62.8%**, "exceeding 60% for the third consecutive month" | CnEVPost, 2026-07-08 / 2026-07-03 | https://cnevpost.com/2026/07/08/china-nev-retail-sales-jun-2026/ ; https://cnevpost.com/2026/07/03/chinas-nev-retail-jun-cpca-preliminary-data/ |
| **H1 2026 cumulative** | PV retail 8.701M total; NEV retail 4.704M (−14.0% YoY) | **≈54.1%** (4.704/8.701) | via WebSearch synthesis (exact originating article not independently re-confirmed — candidate: techtimes.com "China EV Sales Slide 13% in H1 2026," 2026-07-08) | https://www.techtimes.com/articles/319909/20260708/china-ev-sales-slide-13-h1-2026-only-3-brands-profitable-export-push-soars.htm |
| Jul 2026 (forecast/partial) | first 3 weeks −4% YoY; full-month CPCA forecast ~980,000 units | forecast **≈64.5%** | CnEVPost, 2026-07-22 / 2026-07-23; Sina (乘联分会), 2026-07-23 | https://cnevpost.com/2026/07/22/china-nev-retail-sales-first-three-weeks-jul/ ; https://cnevpost.com/2026/07/23/cpca-forecasts-china-jul-nev-retail-980000/ ; https://finance.sina.com.cn/tech/digi/2026-07-23/doc-iniivihz5223378.shtml |

**Read for the manuscript's 2027 >60% forecast:** the data is directionally supportive — CPCA monthly NEV retail penetration crossed 60% for the first time in December 2025, dipped in Jan–Mar 2026 (tax-exemption-cliff-driven front-loading in late 2025 followed by a post-cliff air pocket), then has run at **~60–65% every month from April through July 2026**, even as YoY unit volumes have been declining (high base effects, not falling demand share). The H1 2026 cumulative average of ~54% reflects the weak Jan–Mar months dragging down the six-month blend; it should not be read as a reversal of the >60% trend — the monthly run-rate is consistently mid-60s% by mid-2026. This is good context for judging a "full-year >60% by 2027" forecast: it is plausible on current trend but not yet mechanically guaranteed, since full-year 2026 will still include the weak Jan–Mar months.

---

## 4. Chinese NEV purchase incentives status 2026 ("the subsidy is gone" — needs correction)

**Status: CONFIRMED — the manuscript's "gone" framing is factually wrong on both fronts; here is the corrected policy picture.**

**(a) Purchase-tax exemption schedule:**
- **2024–2025:** NEVs purchased received a **full exemption** from vehicle purchase tax, capped at a maximum exemption of **RMB 30,000 (~USD 4,200)** per passenger vehicle.
- **2026–2027 (effective January 1, 2026 through December 31, 2027):** the exemption is **halved, not eliminated** — qualifying NEVs (per the official "Catalog of New Energy Vehicle Models Eligible for Vehicle Purchase Tax Reduction and Exemption") now get a **50% tax reduction**, capped at a maximum reduction of **RMB 15,000 (~USD 2,100)** per vehicle, rather than full exemption.
- This triggered a documented year-end 2025 sales rush (dealers reporting record order volumes to lock in the old full exemption before the Jan 1, 2026 cutover; some automakers ran "tax-difference guarantee" programs for orders placed before end-Nov 2025 but delivered in 2026).
- Separately, eligibility itself was tightened via new technical standards effective 2026 (e.g., plug-in hybrids/EREVs need a minimum all-electric range, ~100km, to keep qualifying) — a second, independent tightening on top of the halved cap.
- Sources (secondary, both corroborating the same schedule):
  - "China to reduce tax exemption for NEV purchases in 2026," Steelorbis. URL: https://www.steelorbis.com/steel-news/latest-news/purchase-of-nevs-to-implement-50-percent-reduction-in-taxation-since-jan-1-2026-1426630.htm
  - "China Extends NEV Tax Reduction and Exemption Policy to 2027," China Briefing (Dezan Shira & Associates — tax/regulatory advisory, generally reliable on PRC policy specifics). URL: https://www.china-briefing.com/news/china-extends-nev-tax-reduction-and-exemption-policy-to-2027/
  - "China ends full EV tax exemption in 2026, dealerships report year-end sales rush," carnewschina.com, 2025-11-09. URL: https://carnewschina.com/2025/11/09/china-ends-full-ev-tax-exemption-in-2026-dealerships-report-year-end-sales-rush/
  - Note (adjacent but distinct policy, not to be conflated with purchase tax): "BREAKING: China scraps annual vehicle tax exemption for some NEVs, spares battery electric passenger cars," CnEVPost, 2026-07-03 (URL: https://cnevpost.com/2026/07/03/china-scraps-annual-vehicle-tax-exemption-for-some-nevs/) — this concerns the separate annual 车船税 (vehicle & vessel tax), where BEV passenger cars reportedly keep their exemption but some other NEV categories may not; flagged for completeness, not verified in depth here (out of scope of the purchase-tax question but the manuscript should not conflate the two taxes).

**(b) 2024–25 trade-in subsidy program in 2026:**
- The program **continues into 2026**, it is not "gone." China released detailed 2026 guidelines in late December 2025, shifting from flat/fixed subsidy amounts to a **percentage-of-price model with caps**:
  - Scrapping (报废更新) a vehicle for a new NEV passenger vehicle: subsidy = **12% of purchase price, capped at RMB 20,000**.
  - Trading in (置换更新) for a new NEV passenger vehicle: subsidy = **8% of purchase price, capped at RMB 15,000**.
  - Eligibility was also tightened: e.g., to access the full RMB 20,000 rebate the new vehicle must be priced at a minimum threshold (~RMB 166,700 cited in one source), which squeezes support for cheaper/budget EVs relative to 2024–25's flatter subsidy — a real change in *who benefits*, but not a cancellation of the program.
- Sources (mix of official PRC government channel and secondary trade press):
  - "China renews auto trade-in subsidy program for 2026," english.scio.gov.cn (State Council Information Office — **primary/official PRC government channel**), 2025-12-31. URL: http://english.scio.gov.cn/pressroom/2025-12/31/content_118255826.html
  - Same story mirrored at english.www.gov.cn (also official). URL: https://english.www.gov.cn/news/202512/31/content_WS6954b901c6d00ca5f9a08596.html
  - "China to continue trade-in subsidies in 2026 to stimulate auto consumption," CnEVPost, 2025-12-30. URL: https://cnevpost.com/2025/12/30/china-to-continue-trade-in-subsidies-2026-auto-consumption/
  - "China Limits Trade-In Subsidy for 2026 in Hit to Some Carmakers," Bloomberg, 2025-12-31. URL: https://www.bloomberg.com/news/articles/2025-12-31/china-limits-trade-in-subsidy-for-2026-in-hit-to-some-carmakers
  - "New Chinese vehicle subsidy policy for 2026: budget cars to see smaller subsidies under percentage formula," carnewschina.com, 2025-12-31. URL: https://carnewschina.com/2025/12/31/new-chinese-vehicle-subsidy-policy-for-2026-budget-cars-to-see-smaller-subsidies-under-percentage-formula/

**Suggested replacement language for the manuscript:** instead of "the subsidy is gone," something like: *"China's full NEV purchase-tax exemption ended on Dec 31, 2025; from 2026–2027 NEVs get a 50%-reduced purchase tax capped at RMB 15,000 (down from full exemption capped at RMB 30,000), and eligibility criteria were tightened. Separately, the 2024–25 cash-for-clunkers-style trade-in subsidy program was renewed for 2026, but reworked from flat payments to a price-percentage formula with caps (up to RMB 20,000 for scrapping, RMB 15,000 for trade-in) that reduces support for cheaper EVs."*

---

## 5. Thailand 2025: BEV share of new-car sales; Chinese-brand share of Thai BEV sales

**Status: BEV share CONFIRMED. Chinese-brand share PARTLY SUPPORTED (range found, not a single pinned FTI figure).**

- **BEV share of new-car sales 2025: CONFIRMED at ≈19.4%.** 120,301 BEV units were sold in Thailand in 2025 (a jump from 66,732 in 2024), out of 621,166 total vehicles sold domestically (excluding motorcycles), for a **19.37% BEV share** — matches the manuscript's "≈19.4%." Separately, plug-in hybrids grew 260.6% YoY to 8,621 units, and extended-range EVs (EREVs) appeared in the data for the first time (971 passenger cars + 19 pickups). BEV domestic production also surged, up 631.98% YoY to 70,914 units.
  - Org: **FTI — Federation of Thai Industries** (Automotive Industry Club), the standard primary source for Thai vehicle statistics.
  - Channel: secondary (FTI data reproduced/cited by trade press) — I could not directly reach fti.or.th this session (WebFetch blocked), so this is via outlets that explicitly attribute the numbers to FTI:
    - "Thailand: EV sales jump 80% in 2025, lifting auto market," electrive.com, 2026-01-29. URL: https://www.electrive.com/2026/01/29/thailand-ev-sales-jump-80-in-2025-lifting-auto-market/
    - "Thai Auto Industry Pins 2026 Hopes on Exports as Uncertainty Clouds 2025," Khaosod English, 2025-12-23. URL: https://www.khaosodenglish.com/news/business/2025/12/23/thai-auto-industry-pins-2026-hopes-on-exports-as-uncertainty-clouds-2025/
    - "Thailand's EV Production Soars: BEV and PHEV Output Jump Over 300%," Khaosod English, 2025-10-22 (production-side corroboration). URL: https://www.khaosodenglish.com/news/business/2025/10/22/thailands-ev-production-soars-bev-and-phev-output-jump-over-300/

- **Chinese brands' share of Thai BEV sales: PARTLY SUPPORTED — figures found range 70–85%, not a single clean "three-quarters" citation.** Multiple secondary sources give different (but broadly consonant) numbers:
  - "Chinese EV brands, including BYD, hold over 70% of Thailand's BEV market in 2025" (one synthesis, source page: MarkLines, "Chinese OEMs Dominate BEV Market in Thailand with Over 20% Share," URL: https://www.marklines.com/en/report/rep2968_202602 — note the MarkLines *headline* figure, ~20%, actually refers to Chinese brands' share of the *overall* Thai new-car market, not the BEV-specific segment; the 70%+ BEV-specific figure is a separate number pulled from within that source by the search synthesis and could not be independently re-verified against the raw MarkLines text this session).
  - A separate search pass returned "Chinese brands account for 85% of EV sales in Thailand, with BYD alone holding 38.5% of the BEV market" (source page not cleanly pinned down in that snippet).
  - Gasgoo, "Chinese Electric Vehicles Reshape Thailand's Auto Market," is a relevant secondary piece on the theme but its exact percentage was not extracted this session. URL: https://autonews.gasgoo.com/articles/ev/chinese-electric-vehicles-reshape-thailands-auto-market-2042241592943878145
  - **Verdict:** the manuscript's "roughly three-quarters (~75%)" sits within the 70–85% range found across sources, so it is plausible and directionally well-supported, but I could not confirm a single, clearly-dated, FTI-attributed figure of exactly "75%" or "three-quarters." Recommend the author cite this as "roughly 70–85% depending on source, e.g., BYD alone ~38.5% of Thai BEV sales in 2025" rather than a precise three-quarters point estimate, unless a cleaner primary FTI breakdown can be located (FTI's own site, fti.or.th / the Automotive Industry Club's monthly releases, was not reachable this session).

---

## 6. Japan 2025: EV share of new passenger-car sales; early-2026 jump

**Status: PARTLY SUPPORTED — order of magnitude confirmed, exact point estimates are denominator-sensitive and vary meaningfully by source; early-2026 subsidy-driven jump CONFIRMED.**

- **BEV-only share, 2025: PARTLY SUPPORTED, likely ~1.3–1.7% on an all-vehicle-including-kei-cars denominator, or ~2%+ on a registered-cars-only (excluding kei) denominator — not a single clean "≈2%" figure.**
  - JATO Dynamics data (via search synthesis of JATO's own H1 2025 Japan electrification report): "BEV market share dropped from 2.2% in 2023 to 1.3% in H1 2025." Org: JATO Dynamics (independent auto-market data/analytics firm — primary-ish for its own analysis, but I could not re-fetch the report directly, WebFetch blocked). URL: https://www.jato.com/resources/news-and-insights/japans-automotive-electrification-trends-2025-h1. Channel: secondary (WebSearch synthesis of JATO's page).
  - statbase.org: "BEV sales in Japan in 2025 amounted to 61,000 units, 1.67% more than in 2024 (60,000)." This is a raw unit count, not itself a percentage-share statement. URL: https://statbase.org/data/jpn-bev-sales/. Channel: secondary data aggregator, ultimate primary source unclear (likely JADA/日本自動車販売協会連合会).
  - A separate 2024 figure (different search pass): "new EVs accounted for only 1.35 percent of new vehicles sold in Japan [in 2024], with 59,736 new EVs sold" — broadly consistent with the ~60,000-unit count above, but again ambiguous on whether "EV" here means BEV-only or BEV+PHEV.
  - **Why this doesn't cleanly hit "≈2%":** Japan's total new passenger-vehicle market (~4.5–4.6 million units/year per JADA) includes a very large kei-car (minivehicle) segment (~33% of the market per JATO), which is sold mostly as gasoline/hybrid kei cars, diluting the BEV share when kei cars are included in the denominator. If the denominator instead excludes kei cars (i.e., "registered cars" only, ~2.4–2.6 million/year per Jan–Nov 2025 JADA data found), BEV share arithmetically rises toward ~2.3–2.5%. **The manuscript's "≈2%" is plausible but denominator-dependent; I could not pin down which convention its 2% figure is using, and I could not independently fetch a JADA/JAMA primary release this session to settle it (WebFetch blocked; WebSearch budget exhausted before a cleaner query could be run).**

- **BEV+PHEV combined share, 2025: PARTLY SUPPORTED at ≈2.66% (close to, but under, the manuscript's "≈3%").**
  - Source: carconnect.jp (Japanese consumer/EV-info site, secondary, citing JADA and 全国軽自動車協会連合会 [National Kei-Jidosha Association] data): "2025年通年では2.66%にとどまり" (full-year 2025 stayed at 2.66%), compared against a ~25% world-average penetration figure in the same piece. URL surfaced in search results as one of: https://carconnect.jp/column/ev/ev_penetration_rate/ or https://ev-charge-enechange.jp/articles/033/ (both returned by the same query; exact attribution of the 2.66% figure to one specific URL vs. the other was not disambiguated this session). Channel: secondary Japanese consumer/industry blog.
  - A separate figure for March 2026 alone ("new energy cars reached 4.15% [combined BEV+PHEV]" per a WebSearch synthesis, source page unclear) is consistent with a rising trend from ~2.66% (full-year 2025) into 2026, in line with the subsidy story below.
  - **Verdict:** ≈3% is a reasonable rounding of ≈2.66% but overstates it by ~0.3–0.4 points; recommend the manuscript say "just under 3%" or cite 2.7% rather than "≈3%" if precision matters, and flag that the underlying primary-source page (JADA/JAMA) was not independently reached this session to confirm the 2.66% figure at its root.

- **Early-2026 jump attributed to a subsidy program: CONFIRMED.**
  - Japan revised its Clean Energy Vehicle (CEV) subsidy framework effective January 2026: EV purchase subsidies **increased from JPY 900,000 to JPY 1,300,000** per vehicle; fuel-cell-vehicle (FCV) subsidies were **cut from JPY 2,550,000 to JPY 1,500,000** (i.e., funds reallocated toward BEVs and away from FCVs). Org: METI/経済産業省 (via 資源エネルギー庁/ANRE — the "GX" clean-energy-vehicle subsidy scheme). Corroborating URL (secondary, English-language): https://www.enecho.meti.go.jp/en/category/special/article/detail_199.html
  - Result: **Q1 2026 Japan domestic EV sales surged ~80% YoY to a record 26,959 units.** Toyota's EV sales specifically went from ~212 units in Q1 2025 to over 7,000 units in Q1 2026 (a ~3,300% jump), a result press coverage attributes directly to the subsidy redesign favoring mass-market BEV models. Sources: Autoblog, "Toyota's EV Sales Jump 3,300% In Japan As Subsidies Hit BYD." URL: https://www.autoblog.com/news/toyotas-ev-sales-jump-3300-in-japan-as-subsidies-hit-byd ; mirrored at Yahoo Finance, https://finance.yahoo.com/economy/policy/articles/toyota-ev-sales-jump-3-211500851.html ; and caradvisers.com, https://caradvisers.com/blogs/toyota-ev-sales-jump-3300percent-in-japan-after-new-subsidies. Channel: secondary auto-trade press.
  - Further into 2026: "New models, upgrades double EV sales in Japan," The Star (Malaysia, wire-sourced), 2026-07-09 — reports Japan's H1 of fiscal-year-2026 EV sales at 59,337 units, **2.1× the year-earlier H1**, and states this is "a record-high share of about 3% of total passenger car sales," again attributed to the new subsidies plus new model launches (this WebFetch could not be independently re-confirmed this session — 403 — so treat the exact "~3%" figure as a search-snippet-level citation, consistent with though not independently re-verified beyond, the full-year-2025 ≈2.66% BEV+PHEV figure above). URL: https://www.thestar.com.my/business/business-news/2026/07/09/new-models-upgrades-double-ev-sales-in-japan

---

## Compact summary

1. **CPCA NEV retail share by year (2020–2025):** CONFIRMED. 5.8% / 14.8% / 27.6% / 35.7% / 47.6% / ~53.9–54.1% — all match the draft, all genuinely CPCA (乘联会) **retail, passenger-vehicle** figures; watch for CAAM/wholesale/all-vehicle-type numbers (13.4–17.8% for 2021) that look similar but use a different denominator. Best URL: https://www.199it.com/archives/1743685.html (2024, 47.6%) and https://www.guancha.cn/qiche/2026_01_11_803443.shtml (2025, 53.9%).

2. **December 2025 = 60.4%, first month above 60%:** CONFIRMED (arithmetically consistent: 1.387M/2.296M = 60.4%; corroborated by 3 secondary outlets), with one unresolved lower outlier (59.1%) flagged. Best URL: https://cnevpost.com/2026/01/07/china-nev-retail-1-387-million-dec-2025-preliminary-cpca/

3. **H1/2026 latest prints:** PARTLY SUPPORTED/CONFIRMED — monthly penetration ~60–65% every month April–July 2026; H1 cumulative average ~54.1% (dragged down by weak Jan–Mar post-tax-cliff months). Supports plausibility of the 2027 >60% forecast but not conclusively. Best URL: https://cnevpost.com/2026/07/08/china-nev-retail-sales-jun-2026/

4. **China NEV incentives 2026:** CONFIRMED — purchase-tax exemption is halved (not gone): 50% reduction capped at RMB 15,000 for 2026–2027 (was full exemption capped at RMB 30,000 in 2024–25); trade-in subsidy program renewed for 2026 (not gone), reworked to a percentage-of-price model (up to RMB 20,000 scrapping / RMB 15,000 trade-in) with a higher price threshold squeezing cheap EVs. Best URLs: http://english.scio.gov.cn/pressroom/2025-12/31/content_118255826.html (official) and https://www.china-briefing.com/news/china-extends-nev-tax-reduction-and-exemption-policy-to-2027/

5. **Thailand 2025:** BEV share CONFIRMED at 19.37% (≈19.4%), FTI data, 120,301 units of 621,166 total. Chinese-brand share of Thai BEV sales PARTLY SUPPORTED — sources range 70–85% (not a clean "75%" citation); BYD alone ~38.5%. Best URL: https://www.electrive.com/2026/01/29/thailand-ev-sales-jump-80-in-2025-lifting-auto-market/

6. **Japan 2025/2026:** PARTLY SUPPORTED — BEV-only share likely ~1.3–1.7% (all-vehicle denominator, JATO) to ~2%+ (registered-cars-only denominator), not a single clean "2%"; BEV+PHEV combined ≈2.66% for full-year 2025 (just under the "≈3%" claim). Early-2026 subsidy-driven jump CONFIRMED: CEV subsidy raised from ¥900,000 to ¥1,300,000 (Jan 2026), Q1 2026 EV sales +80% YoY (record 26,959 units), Toyota's EV sales +3,300% YoY. Best URLs: https://www.jato.com/resources/news-and-insights/japans-automotive-electrification-trends-2025-h1 and https://www.autoblog.com/news/toyotas-ev-sales-jump-3300-in-japan-as-subsidies-hit-byd
