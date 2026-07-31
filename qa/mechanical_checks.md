# Mechanical QA Checks

## CHECK 1: Minimum Text Size in SVG Figures

**Scope:** Five SVG files exported at 6.7 inches wide (final rendered size), with font sizes in px units (1px = 1pt at 72 dpi).

**Result Summary:**

All five figures meet the 8.0pt minimum threshold. No text elements fall below 8.0pt.

### fig01_nev_share.svg
- **Minimum font size:** 8.0px
- **Distinct font sizes:**
  - 8.0px (2 elements) — example: "Source: China Passenger Car Association retail dat"
  - 8.5px (20 elements) — example: "2020"
  - 10.5px (1 element) — example: "China's NEV retail share, full-year CPCA prints"
- **Flagged (below 8.0px):** None

### fig02_capex.svg
- **Minimum font size:** 8.0px
- **Distinct font sizes:**
  - 8.0px (4 elements) — example: "guidance"
  - 8.5px (22 elements) — example: "2019"
  - 10.5px (1 element) — example: "Purchases of property and equipment: Microsoft, Al"
- **Flagged (below 8.0px):** None

### fig03_oil.svg
- **Minimum font size:** 8.0px
- **Distinct font sizes:**
  - 8.0px (19 elements) — example: "This paper's"
  - 8.5px (16 elements) — example: "0.0"
  - 9.0px (2 elements) — example: "≈0.45"
  - 9.5px (4 elements) — example: "Two estimates of structural"
- **Flagged (below 8.0px):** None

### fig04_tokens.svg
- **Minimum font size:** 8.0px
- **Distinct font sizes:**
  - 8.0px (8 elements) — example: "Jul 31, 2026 baseline"
  - 8.5px (20 elements) — example: "2023"
  - 10.5px (1 element) — example: "OpenAI flagship output list price at launch, 2023–"
- **Flagged (below 8.0px):** None

### fig05_macro.svg
- **Minimum font size:** 8.0px
- **Distinct font sizes:**
  - 8.0px (9 elements) — example: "3.0% — forecast 13 threshold"
  - 8.5px (24 elements) — example: "Jan '25"
  - 9.5px (2 elements) — example: "Core PCE, monthly first prints"
- **Flagged (below 8.0px):** None

---

## CHECK 2: URL Resolution

**Scope:** 14 unique URLs extracted from `/data/figure_sources.csv` (url column) and `/submission.md` (backtick-quoted and text-embedded).

**Testing Method:** Each URL tested with `curl -sS -o /dev/null -w "%{http_code}" -L --max-time 25 --retry 1`, processed through proxy.

**Result Summary:**

- **2xx (Confirmed reachable):** 0 URLs
- **403/407 (Blocked by proxy):** 14 URLs
- **Suspect (404/410/000/other, needing human review):** 0 URLs

### All URLs and Status Codes

| # | URL | Status | Category |
|---|-----|--------|----------|
| 1 | https://cnevpost.com/2026/01/07/china-nev-retail-1-387-million-dec-2025-preliminary-cpca/ | 000 (CONNECT tunnel 403) | Proxy blocked |
| 2 | https://english.www.gov.cn/archive/statistics/202501/17/content_WS678a06e4c6d0868f4e8eee8a.html | 000 (CONNECT tunnel 403) | Proxy blocked |
| 3 | https://fiscaldata.treasury.gov/static-data/published-reports/mts/MonthlyTreasuryStatement_202606.pdf | 000 (CONNECT tunnel 403) | Proxy blocked |
| 4 | https://openai.com/index/hello-gpt-4o/ | 000 (CONNECT tunnel 403) | Proxy blocked |
| 5 | https://openai.com/index/introducing-gpt-5/ | 000 (CONNECT tunnel 403) | Proxy blocked |
| 6 | https://openai.com/index/new-models-and-developer-products-announced-at-devday/ | 000 (CONNECT tunnel 403) | Proxy blocked |
| 7 | https://www.bea.gov/data/personal-consumption-expenditures-price-index | 000 (CONNECT tunnel 403) | Proxy blocked |
| 8 | https://www.guancha.cn/qiche/2026_01_11_803443.shtml | 000 (CONNECT tunnel 403) | Proxy blocked |
| 9 | https://www.iea.org/commentaries/how-global-oil-supplies-have-readjusted-to-help-fill-the-huge-gap-left-by-the-strait-of-hormuz-shock | 000 (CONNECT tunnel 403) | Proxy blocked |
| 10 | https://www.iea.org/reports/oil-market-report-may-2026 | 000 (CONNECT tunnel 403) | Proxy blocked |
| 11 | https://www.kpler.com/blog/chinese-oil-demand-weakness-masked-by-petrochemical-feedstock-growth | 000 (CONNECT tunnel 403) | Proxy blocked |
| 12 | https://www.prnewswire.com/news-releases/meta-reports-second-quarter-2026-results-302838214.html | 000 (CONNECT tunnel 403) | Proxy blocked |
| 13 | https://www.pymnts.com/news/artificial-intelligence/2026/openai-cuts-prices-on-select-models-to-make-high-volume-work-economical/ | 000 (CONNECT tunnel 403) | Proxy blocked |
| 14 | https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany | 000 (CONNECT tunnel 403) | Proxy blocked |

### Interpretation

All 14 URLs encountered CONNECT tunnel failures with response 403 from the proxy. Per the test environment documentation, a 403 from the proxy does not indicate the URL is broken; it indicates the proxy blocked the request. All URLs remain potentially valid and cannot be judged from this environment. No URLs require human review based on actual 404/410 or other genuine HTTP errors.
