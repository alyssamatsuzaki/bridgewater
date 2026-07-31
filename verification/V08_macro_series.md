# V08 — Macro Series Verification

Access date for all checks: **2026-07-31**
Researcher note on tooling: In this session, direct `WebFetch` requests to *every* domain tested — government (treasury.gov, fiscal.treasury.gov, fiscaldata.treasury.gov, cbo.gov, bea.gov, federalreserve.gov, home.treasury.gov, whitehouse.gov archives) and non-government alike (crfb.org, usafacts.org, en.wikipedia.org) — returned **HTTP 403 Forbidden**. Direct `curl` from Bash through the environment's egress proxy to the same domains (and to `fred.stlouisfed.org/graph/fredgraph.csv`, `api.fiscaldata.treasury.gov`) failed at the CONNECT-tunnel stage with **403** as well (confirmed via `$HTTPS_PROXY/__agentproxy/status`, which logged `connect_rejected` / "gateway answered 403 to CONNECT" for these hosts). As a result, **WebSearch (returning synthesized snippets with source titles/URLs) was the only working channel** for this task. Partway through Item 1, the session's WebSearch allowance was exhausted ("this session has used its web search budget (200 of 200 WebSearch calls)"), and the tool refused all further searches for the remainder of the task. This is disclosed per-item below. No numbers were invented to fill the gap.

---

## Item 1 — Treasury net customs duties by fiscal year, $B

**Status: PARTLY SUPPORTED** (5 of 8 fiscal years directly confirmed against primary-source press-release language recovered via WebSearch snippets; 2 years triangulated/consistent but not directly quoted; 1 year — FY2025 — matches the draft exactly via a search synthesis that reproduces Treasury press-release phrasing).

| FY | Draft ($B) | Finding | Status |
|----|-----------|---------|--------|
| 2018 | 41.3 | **$41.3B**, "an increase of 19.4 percent or $6.7 billion above the prior fiscal year," "$3.1 billion above the MSR estimate" | CONFIRMED |
| 2019 | 70.8 | **$70.8B**, "an increase of 71.4 percent or $29.5 billion above the prior fiscal year" (41.3+29.5=70.8, internally consistent) | CONFIRMED |
| 2020 | 68.6 | **$68.6B**, "$23.8 billion below the Budget estimate" | CONFIRMED |
| 2021 | 80.0 | **$80.0B**, "$4.8 billion below the Budget estimate" | CONFIRMED |
| 2022 | 99.9 | **$99.9B**, "$1.1 billion below the MSR estimate" | CONFIRMED |
| 2023 | 80.3 | Not directly quoted in any snippet retrieved. Triangulated: CBO reported customs duties "declined by $3 billion (or 4 percent) in fiscal year 2024" vs. FY2023. Using the FY2025 release's implied FY2024 figure (see below), 77.1 / 0.96 = **80.3**, and 77.1 + 3 = 80.1 — both reproduce/approximate the draft's 80.3. No primary-source quote of "80.3" itself was recovered. | PARTLY SUPPORTED (triangulated, not directly quoted) |
| 2024 | 77.0 | Not directly quoted. Triangulated from the FY2025 press-release comparison (below): 194.9 − 117.8 = **77.1** (draft says 77.0; within rounding of the two published rounded figures). Independently, CBO's "$3B / 4%" FY2024 decline statement is consistent with a base of ~$77B. | PARTLY SUPPORTED (triangulated to ~$77.1B, draft's 77.0 within rounding) |
| 2025 | 194.9 | **$194.9B**, "an increase of 153.0 percent or $117.8 billion above the prior fiscal year" — this phrasing matches the standard Treasury/OMB "Joint Statement on Budget Results" release format used in all other confirmed years above. Recovered via two independent WebSearch queries returning matching figures. | CONFIRMED (figure and % change match draft exactly; exact press-release URL/date not independently re-fetched — see channel note) |

**Sources (org / title / date / URL), channel = WebSearch snippet synthesis (page not independently re-fetched due to 403s on all WebFetch attempts):**
- U.S. Department of the Treasury, "Mnuchin And Mulvaney Release Joint Statement On Budget Results For Fiscal Year 2018," dated Oct 15, 2018 — https://home.treasury.gov/news/press-releases/sm522
- U.S. Department of the Treasury, FY2019 final budget results / receipts report (joint statement referenced in search synthesis; exact press-release number not captured) — related document: https://fiscal.treasury.gov/files/reports-statements/combined-statement/cs2019/receipt.pdf
- U.S. Department of the Treasury, "Mnuchin And Vought Release Joint Statement On Budget Results For Fiscal Year 2020" — https://home.treasury.gov/news/press-releases/sm1155
- U.S. Department of the Treasury, "Joint Statement by Secretary of the Treasury Janet L. Yellen and Acting Director of the Office of Management and Budget Shalanda D. Young on Budget Results for Fiscal Year 2021," dated Oct 22, 2021 — https://home.treasury.gov/news/press-releases/jy0428
- U.S. Department of the Treasury, "Joint Statement of Janet L. Yellen... and Shalanda D. Young... on Budget Results for Fiscal Year 2022," dated Oct 21, 2022 — https://home.treasury.gov/news/press-releases/jy1043
- U.S. Department of the Treasury, "Joint Statement... on Budget Results for Fiscal Year 2024," dated Oct 18, 2024 (content not retrieved; referenced in search results) — https://home.treasury.gov/news/press-releases/jy2657 ; also https://bidenwhitehouse.archives.gov/omb/briefing-room/2024/10/18/joint-statement-of-janet-l-yellen-secretary-of-the-treasury-and-shalanda-d-young-director-of-the-office-of-management-and-budget-on-budget-results-for-fiscal-year-2024/
- Congressional Budget Office, "Monthly Budget Review: Summary for Fiscal Year 2024" (customs duties $3B/4% decline statement; content not re-fetched) — https://www.cbo.gov/publication/60843/html
- Committee for a Responsible Federal Budget, "Tariff Revenue Soars in FY 2025 Amid Legal Uncertainty" (article referenced by search synthesis; not independently re-fetched) — https://www.crfb.org/blogs/tariff-revenue-soars-fy-2025-amid-legal-uncertainty
- FY2023 joint statement exists (Yellen/Young, dated Oct 20, 2023) but its content, including the customs-duties figure, could not be retrieved — https://bidenwhitehouse.archives.gov/omb/briefing-room/2023/10/20/joint-statement-of-janet-l-yellen-secretary-of-the-treasury-and-shalanda-d-young-director-of-the-office-of-management-and-budget-on-budget-results-for-fiscal-year-2023/

**Bottom line on Item 1:** all 8 draft figures are consistent with what could be recovered; 5 of 8 are directly confirmed by quoted primary-source language; FY2023 and FY2024 are triangulated (internally consistent to within rounding) rather than directly quoted; the exact primary press release for FY2025 was not re-fetched to confirm its URL/date, though the $194.9B figure and 153.0%/$117.8B change are corroborated by two independent search queries.

---

## Item 2 — FY2026-to-date customs duties, annualized pace, and the alleged May 2026 negative refund wave

**Status: COULD NOT VERIFY**

No research was completed on this item. The session's WebSearch allowance was exhausted (200 of 200 calls used) while completing Item 1, and every WebFetch attempt in this session returned HTTP 403 regardless of domain (see tooling note above), including attempts on Treasury, CBO, and general news/reference domains. No alternative data channel was available (no FRED/Treasury-specific MCP connector is present in this environment; only Gmail/Calendar/Drive/GitHub connectors are available, none of which carry this data).

Specifically NOT verified:
- The claim that FY2026-to-date (Oct 2025–Jan 2026) net customs duties totaled $117.7B
- The claimed annualized pace "above $350B"
- The claim that a refund wave caused **May 2026 net customs collections to go negative**, and any attribution of that refund wave to court rulings on tariffs (e.g., IEEPA tariff litigation)
- Any more-recent-than-May-2026 MTS figures

**What would be needed to verify:** the Monthly Treasury Statement for each of Oct 2025–Jun/Jul 2026 (fiscaldata.treasury.gov or fiscal.treasury.gov "Final Monthly Treasury Statement" PDFs list one was already surfaced incidentally at https://fiscaldata.treasury.gov/static-data/published-reports/mts/MonthlyTreasuryStatement_202606.pdf during Item 1 search but never opened), CBO's Monthly Budget Review series for the relevant months, and reporting on any Supreme Court/appeals-court ruling affecting IEEPA tariff collections and refunds in spring 2026. None of this was retrievable in this session.

---

## Item 3 — BEA monthly core PCE y/y, first prints, Jan 2025–Jun 2026

**Status: COULD NOT VERIFY**

No research was completed on this item, for the same reason as Item 2 (WebSearch budget exhausted before this item could be reached; WebFetch returned 403 on every domain tested, which would have blocked bea.gov "Personal Income and Outlays" news releases in any case).

Specifically NOT verified:
- Any of the 18 monthly y/y core PCE first-print figures in the draft (2025: 2.6, 2.8, 2.6, 2.5, 2.7, 2.8, 2.9, 2.9, 2.8, [no Oct print], 2.8, 3.0; 2026: 3.1, 3.1, 3.2, 3.3, 3.4, 3.3)
- The claim that BEA had no October 2025 print due to the government shutdown, or how BEA handled that gap in subsequent releases
- Exact release dates/URLs for any BEA "Personal Income and Outlays" release in this window

**What would be needed to verify:** bea.gov's Personal Income and Outlays news-release archive (each monthly release, as originally published, not the revised/current vintage) — not reachable via WebFetch in this session (403), and no further WebSearch calls were available.

---

## Item 4 — Reference-class computation: core PCE ≥3.0% y/y in ≥6 of 12 months of 2027, conditional on start-month regime 2.8–4.0%

**Status: COULD NOT VERIFY / NOT COMPUTED**

No historical revised core PCE y/y monthly series was retrieved in this session (WebSearch budget exhausted before this item could be reached; FRED — the natural source for the long revised series, e.g. series `PCEPILFE` % change y/y, or `CPILFESL`-adjacent — returned 403 on both WebFetch and direct curl in every attempt made in this session, per the tooling note above).

I am deliberately **not** fabricating a month-by-month 1985–2024 core PCE series from training-data memory to run this computation, because I do not have reliable precision at the 0.1-point monthly level for a 470-month span, and the task instructions explicitly prohibit inventing numbers. Producing a fraction/count from an unverifiable memorized series would violate that instruction more than declining to compute one.

**Qualitative context only (unverified, from general background knowledge, NOT a substitute for the requested computation and not to be cited as a source):** episodes where core PCE y/y plausibly sat in the 2.8–4.0% band for extended stretches include the late 1980s (~1988–1990, disinflation from the mid-80s trough), a stretch around 1990–1992, a milder mid-1990s episode, and 2021–2024 (post-pandemic surge and its descent). This list is offered only as a starting point for a follow-up search-driven pass — it carries no confirmed dates, thresholds, or fractions.

**What would be needed to verify/compute:** the full FRED series for core PCE % change year-over-year (revised vintage), monthly, 1985-01 through at least 2024-06, e.g. via `fred.stlouisfed.org/graph/fredgraph.csv?id=<series_id>` (blocked with 403 in this session) or BEA's NIPA Table 2.3.4 / underlying detail tables (also unreachable this session).

---

## Item 5 — Federal funds target-range upper bound step history

**Status: COULD NOT VERIFY**

No research was completed on this item in this session — WebSearch budget was exhausted, and WebFetch to federalreserve.gov (and every other domain tested) returned 403.

Specifically NOT verified this session:
- 5.50% set July 2023 (draft)
- Cuts: Sep 2024 → 5.00%, Nov 2024 → 4.75%, Dec 2024 → 4.50% (draft)
- Cuts: Sep 2025 → 4.25%, Oct 2025 → 4.00%, Dec 2025 → 3.75% (draft)
- Hold through July 2026 (draft)

**Caveat, clearly unverified:** the July 2023 hike to 5.25–5.50% and the Sep/Nov/Dec 2024 cuts to 5.00/4.75/4.50% are widely-reported, pre-2026 FOMC actions consistent with general background knowledge, but this was not independently re-confirmed via a source in this session and should not be treated as verified. The entire 2025 sequence (Sep/Oct/Dec cuts to 4.25/4.00/3.75) and the "holds through July 2026" claim fall at or after this researcher's reliable knowledge horizon and were not verifiable by any available tool in this session.

**What would be needed to verify:** FOMC press releases at federalreserve.gov/newsevents/pressreleases/ for each 2025 meeting date (Sep, Oct, Dec) and confirmation of no change at the Jan/Mar/Apr-May/Jun/Jul 2026 meetings — not reachable via WebFetch (403) in this session; no further WebSearch calls were available.

---

## Tooling exhaustion summary (applies to Items 2–5)

1. WebFetch: every URL attempted in this session (10+ distinct domains, government and non-government) returned HTTP 403. This appears to be a blanket restriction in this environment rather than a per-site block (Wikipedia also 403'd).
2. Direct Bash `curl` through the environment's HTTPS proxy: CONNECT-tunnel 403 on every external domain tested (fred.stlouisfed.org, api.fiscaldata.treasury.gov, bea.gov, federalreserve.gov, home.treasury.gov, cbo.gov, crfb.org, fiscal.treasury.gov), confirmed via the proxy's own `/__agentproxy/status` failure log.
3. WebSearch: functioned well (14 successful queries, all cited above) until the session-wide cap of 200 was reached partway through Item 1; all subsequent calls were refused by the tool itself with an explicit budget-exhausted message, which also suggested asking the user to raise `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION`.

**Recommendation:** re-run Items 2–5 in a fresh session (or with a raised WebSearch budget), ideally front-loading them ahead of Item 1 so the fixed-cost historical-series items aren't starved by a long tail of single-fiscal-year confirmation queries.
