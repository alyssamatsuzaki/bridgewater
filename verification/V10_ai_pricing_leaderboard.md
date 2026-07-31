# V10 — AI Provider Pricing & LMArena Leaderboard Verification

**Verification date:** 2026-07-31
**Verifier:** source-verification researcher (subagent)
**Forecast under test:** By Dec 31 2027, does the published on-demand OUTPUT-token price of the most capable generally available model from at least one of OpenAI, Anthropic, or Google fall ≥50% below that provider's July 31, 2026 level?

---

## 0. Methodology and a critical tooling limitation (read first)

This verification was constrained by two tool failures that materially limit confidence in several line items below. Documenting them explicitly per instructions ("if unverifiable, write COULD NOT VERIFY and what you tried"):

1. **WebFetch was completely non-functional for the entire session.** Every single WebFetch call — to primary provider pricing pages (openai.com, platform.openai.com, anthropic.com, ai.google.dev), provider announcement/blog posts, secondary aggregator sites, Wikipedia, LMArena's own site, CNBC, Yahoo Finance, and even a control fetch of `https://example.com` — returned `HTTP 403 Forbidden`. This is a uniform, environment-wide failure, not site-specific blocking. A direct WebFetch to `web.archive.org` was refused outright by the tool itself ("Claude Code is unable to fetch from web.archive.org"). I also attempted the Wayback Machine's availability API via `curl` from Bash; the outbound proxy gateway returned `403` for `archive.org` (confirmed via `$HTTPS_PROXY/__agentproxy/status`, which logged `connect_rejected` / gateway 403 for `archive.org`, `sec.gov`, `treasury.gov`, `fred.stlouisfed.org`, and others). **Net effect: no primary-source page fetch and no Wayback Machine snapshot was obtainable for any provider, for any item in this brief.**
2. **The WebSearch budget for this session was exhausted after 10 successful queries** (the 11th and 12th calls were rejected with "this session has used its web search budget (200 of 200 WebSearch calls)"). Given only 10 queries were issued from this task, the budget was evidently shared with/depleted by other activity in this environment before or during this session. This means several planned follow-up searches — including any query at all on the LMArena leaderboard — could not be run.

**Consequence:** All pricing figures below come from WebSearch's synthesized summaries of secondary/tertiary sources (pricing-tracker sites, news aggregators, OpenRouter listings) rather than from a primary-source fetch or an archived snapshot of the provider's own pricing page. Every figure is sourced and dated as precisely as the tool output allows, and every URL below is a URL that WebSearch actually returned — none invented. Where confidence is materially weaker than a primary-source confirmation would give, I've flagged it. Item 4 (LMArena) could not be attempted at all and is marked COULD NOT VERIFY.

---

## 1. Baseline snapshot, ~2026-07-31

**Snapshot table**

| Provider | Model | Input $/1M | Output $/1M | Designated top/most-capable tier? | Page URL (attempted) | Access time | Wayback URL |
|---|---|---|---|---|---|---|---|
| OpenAI | GPT-5.6 Sol | $5.00 (per GPT-5.5's carried-forward rate; not independently re-confirmed for Sol specifically) | $30.00 | **Yes** — described as "the most powerful model in the [GPT-5.6] family"; price left unchanged in the July 30, 2026 price-cut announcement that cut the two lower tiers | openai.com/api/pricing/ (403, unreachable) | 2026-07-31, exact time not captured | Not obtainable — see §0 |
| OpenAI | GPT-5.6 Terra | $2.00 (post-cut; was $2.50) | $12.00 (post-cut; was $15.00) | No — mid tier | same, unreachable | 2026-07-31 | Not obtainable |
| OpenAI | GPT-5.6 Luna | $0.20 (post-cut; was $1.00) | $1.20 (post-cut; was $6.00) | No — fastest/cheapest tier | same, unreachable | 2026-07-31 | Not obtainable |
| OpenAI | GPT-5.5 (superseded by 5.6, still referenced) | $5.00 | $30.00 | Was flagship until GPT-5.6 launch; "frontier model," 1.05M context / 128K max output | same, unreachable | 2026-07-31 | Not obtainable |
| OpenAI | GPT-5.2 (older, referenced in trackers) | $0.875 (cut from $1.75 within the prior ~90 days as of the source's writing) | $7.00 | No — appears to be a lower/mid tier, not clearly the flagship at its Dec 10, 2025 launch relative to the historical $10 GPT-5 figure below; **could not fully reconcile this data point's tier positioning** | same, unreachable | 2026-07-31 | Not obtainable |
| Anthropic | Claude Fable 5 | $10.00 | $50.00 | **Presented as Anthropic's most capable widely released model** — a premium/reasoning-style tier distinct from the standard Opus/Sonnet/Haiku lineup | anthropic.com/pricing (403, unreachable) | 2026-07-31 | Not obtainable |
| Anthropic | Claude Opus 5 | $5.00 | $25.00 | Top of the standard GA lineup ("premium Claude option for complex reasoning, agentic coding, high-autonomy work"; "half the standard API price of Fable 5") | same, unreachable | 2026-07-31 | Not obtainable |
| Anthropic | Claude Sonnet 5 | $3.00 (intro $2.00 through 2026-08-31) | $15.00 (intro $10.00 through 2026-08-31) | No — mid tier | same, unreachable | 2026-07-31 | Not obtainable |
| Anthropic | Claude Haiku 4.5 | $1.00 | $5.00 | No — fastest/cheapest tier | same, unreachable | 2026-07-31 | Not obtainable |
| Google | Gemini 3.1 Pro | $2.00 (≤200K context); $4.00 (>200K) | $12.00 (≤200K context); $18.00 (>200K) | Reported as Google's flagship in the sources found; long-context surcharge tier above 200K tokens | ai.google.dev/gemini-api/docs/pricing (403, unreachable) | 2026-07-31 | Not obtainable |
| Google | Gemini 3.6 Flash | $1.50 | $7.50 | No, but sources note it "beats Gemini 3.1 Pro on coding at ~25% lower cost" (launched 2026-07-21) — capability-vs-price positioning is muddied; page itself would be needed to confirm Google's own top-tier designation | same, unreachable | 2026-07-31 | Not obtainable |
| Google | Gemini 3.5 Flash | $1.50 | $9.00 | No (launched 2026-05-19) | same, unreachable | 2026-07-31 | Not obtainable |
| Google | Gemini 2.5 Flash-Lite | $0.10 | $0.40 | No — cheapest tier | same, unreachable | 2026-07-31 | Not obtainable |

**Confidence notes on Section 1:**
- **OpenAI Sol figures** are corroborated across two independent WebSearch summaries (one naming "GPT-5.5" at $5/$30, a second explicitly stating "GPT-5.6, with Sol holding the $5/$30 flagship tier, which matches GPT-5.5's pricing structure") and by the July 30, 2026 price-cut news coverage, which states Sol's price was **not** touched while Luna and Terra were cut. This is the best-corroborated figure in the table. Still, no primary OpenAI page was fetched, so treat $5 input specifically as inferred-by-continuity rather than directly confirmed for Sol.
- **Anthropic figures** for Opus 5 ($5/$25) were independently returned by WebSearch from aggregator sources (finout.io, cloudzero.com, tldl.io, benchlm.ai, evolink.ai, aipricing.guru) and are also consistent with Anthropic's own `claude-api` reference material available in this environment (cached 2026-06-24), which lists Claude Fable 5 at $10/$50, Claude Opus 5 at $5/$25, Claude Sonnet 5 at $3/$15 (intro $2/$10 through 2026-08-31), and Claude Haiku 4.5 at $1/$5 — i.e., two independent sources agree. That cached reference is Anthropic's own SDK/API documentation content, not a fetch of the public pricing marketing page, so I'm treating it as strong-but-not-primary-page corroboration.
- **Google figures** rest on a single WebSearch call; I was not able to run a confirming second query before the budget was exhausted. Treat the Gemini row with lower confidence than the OpenAI/Anthropic rows.
- I could not independently determine, from a primary page, exactly how each provider visually/structurally designates "the top tier" (e.g., a "most capable" badge) — the designations above are inferred from descriptive language in the secondary sources, not observed directly on a pricing page.

---

## 2. Historical OpenAI flagship launch prices (output, per 1M tokens)

| Model | Claimed launch output price | Verification result | Sources |
|---|---|---|---|
| GPT-4 | $60 (Mar 2023) | **Consistent with search results.** Multiple sources describe GPT-4's March 2023 API pricing as $0.03/1K input and $0.06/1K output, i.e. $30/$60 per million tokens. | [cloudzero.com — GPT-4 API cost 2026 breakdown](https://www.cloudzero.com/blog/gpt-4-api-cost/), [pricepertoken.com — GPT-4 pricing](https://pricepertoken.com/pricing-page/model/openai-gpt-4), [PMC table](https://pmc.ncbi.nlm.nih.gov/articles/PMC11071574/table/T4) |
| GPT-4 Turbo | $30 (Nov 2023) | **Consistent.** Announced Nov 6, 2023 at OpenAI's first DevDay; per-search summary: "input tokens are 3x cheaper than GPT-4 at $0.01 and output tokens are 2x cheaper at $0.03" per 1K tokens — i.e., $10/$30 per million, output = $30 as claimed. | [CNBC, Nov 6 2023](https://www.cnbc.com/2023/11/06/openai-announces-more-powerful-gpt-4-turbo-and-cuts-prices.html), [TechCrunch](https://techcrunch.com/2023/11/06/openai-launches-gpt-4-turbo-and-launches-fine-tuning-program-for-gpt-4), [Forbes](https://www.forbes.com/sites/elijahclark/2023/11/09/openai-announces-gpt-4-turbo-ushering-in-a-new-era-of-ai/), [OpenAI DevDay recap](https://openai.com/index/new-models-and-developer-products-announced-at-devday/) (URL returned by search; not independently fetchable — see §0) |
| GPT-4o | $15 (May 2024) | **Consistent.** "GPT-4o launched in May 2024 at $5.00 input and $15.00 output per million tokens," later cut ~50% to $2.50/$10.00 in October 2024. | [TechTarget — GPT-4o explained](https://www.techtarget.com/whatis/feature/GPT-4o-explained-Everything-you-need-to-know), [OpenRouter — GPT-4o (2024-05-13)](https://openrouter.ai/openai/gpt-4o-2024-05-13), [Wikipedia — GPT-4o](https://en.wikipedia.org/wiki/GPT-4o) (URL returned by search; not independently fetchable) |
| GPT-5 | $10 (Aug 2025) | **Consistent, with one reconciliation caveat.** GPT-5 launched Aug 7, 2025. Search results show **two** figures depending on variant: "GPT-5 Chat" at $1.25 input / $10.00 output per million tokens (matches the $10 claim exactly), and a separate "GPT-5" (non-chat) figure at $0.625 input / $5.00 output. I could not determine from these sources which variant is the one the forecast's $10 baseline refers to, though $10 output for "GPT-5 Chat" matches the number given in the task brief precisely. | [pricepertoken.com — GPT-5 Chat](https://pricepertoken.com/pricing-page/model/openai-gpt-5-chat), [pricepertoken.com — GPT-5](https://pricepertoken.com/pricing-page/model/openai-gpt-5), [getdeploying.com — GPT-5](https://getdeploying.com/llms/gpt-5), [yourgpt.ai — GPT-5 overview](https://yourgpt.ai/blog/updates/gpt-5) |

**Status: item 2 is substantially verified** via multiple independent secondary sources per data point (2–4 corroborating sources each), with the GPT-5 variant-naming ambiguity flagged above as the one open question. None of these were confirmed against a primary OpenAI announcement page directly (all such attempts returned 403 — see §0), so this should be understood as strong secondary-source corroboration, not primary-source confirmation.

---

## 3. Price changes/successor launches, Aug 2025 → Jul 31 2026

**OpenAI — clear sequence found, well corroborated:**
Based on the sources gathered, OpenAI's flagship line moved through multiple named versions between the Aug 2025 GPT-5 launch and today: GPT-5 (Aug 7, 2025, $10 output per the "Chat" variant) → GPT-5.2 (Dec 10, 2025, tracked at a **lower** $7 output after a cut) → GPT-5.4 → **GPT-5.5** ($30 output; one source's headline explicitly frames this as "six weeks after 5.4, doubled price") → **GPT-5.6** (three-tier family: Sol/Terra/Luna, ~July 2026), which is the current flagship generation as of this snapshot.

The most concrete, best-dated event in the window is a **July 30, 2026** OpenAI price cut — one day before this snapshot:
> "OpenAI announced on July 30, 2026 that it is reducing the price of two models in its GPT-5.6 family — cutting the cost of GPT-5.6 Luna by 80% and GPT-5.6 Terra by 20% — roughly three weeks after the models launched... Luna...now priced at 20 cents per million input tokens and $1.20 per million output tokens, a reduction from its previous rates of $1 and $6. Terra...input token rate fall to $2 per million and output token rate fall to $12 per million, compared with prior $2.50 and $15. **Pricing for Sol, the most powerful model in the family, remains unchanged.**"

Sources: [CNBC, Jul 30 2026](https://www.cnbc.com/2026/07/30/open-ai-price-cut-gpt.html), [Axios, Jul 30 2026](https://www.axios.com/2026/07/30/openai-cuts-prices-gpt-terra-luna5), [Yahoo Finance](https://finance.yahoo.com/technology/ai/articles/openai-cuts-gpt-5-6-173045044.html), [Unite.AI](https://www.unite.ai/openai-cuts-api-prices-on-its-two-cheaper-gpt-5-6-tiers/), [Tech Times](https://www.techtimes.com/articles/322305/20260730/openai-cuts-luna-80-sol-rewrote-its-own-inference-stack-fund-price-drop.htm), [Seeking Alpha](https://seekingalpha.com/news/4621938-openai-slashes-prices-of-2-of-its-latest-gpt-56-ai-models), [PYMNTS](https://www.pymnts.com/news/artificial-intelligence/2026/openai-cuts-prices-on-select-models-to-make-high-volume-work-economical/) — eight independent outlets reporting the same figures, strong corroboration for this specific event.

**Important, non-obvious finding for the forecast:** taking the sources at face value, OpenAI's *flagship-tier* output price does **not** show a monotonic decline from Aug 2025 to Jul 2026 — it appears to have **risen**, from $10/M (GPT-5, Aug 2025) to $30/M (GPT-5.5 and now GPT-5.6 Sol, unchanged through the Jul 30, 2026 cut). The July 30 cuts applied only to the two *lower* tiers (Luna, Terra), not to the flagship (Sol). This is directly relevant to how the forecast's baseline should be read — if $10 (Aug 2025) is used as an anchor for "50% below," the current $30 flagship price is already 3x above that anchor, not below it. I flag this as a finding for the manuscript authors to reconcile, not as something I've resolved myself — it depends entirely on secondary sources of unconfirmed reliability (see §0) and on which model counts as "the flagship" at each point in time, which I could not fully verify from primary sources.

**Anthropic — no verification attempted.** I did not have search budget remaining to specifically query for an Anthropic price cut or successor-model launch between Aug 2025 and Jul 2026. The only Anthropic-specific data gathered is the current-state snapshot in §1. **COULD NOT VERIFY** whether Anthropic changed its flagship output price in this window — what I tried: one general "Anthropic API pricing July 2026" query (see §1), which surfaced current prices only, not a historical timeline; no dedicated query on Anthropic price-cut history was possible before the WebSearch budget was exhausted.

**Google — no verification attempted.** Same limitation. The one Gemini query returned current Gemini 3.1 Pro / 3.6 Flash / 3.5 Flash / 2.5 Flash-Lite prices with two 2026 launch dates (Gemini 3.5 Flash: May 19, 2026; Gemini 3.6 Flash: Jul 21, 2026), but nothing about whether Gemini's flagship (Pro-tier) output price itself was cut or raised since Aug 2025. **COULD NOT VERIFY** — what I tried: one general Gemini pricing query; no dedicated historical/price-cut query was possible before the budget was exhausted.

---

## 4. LMArena leaderboard — COULD NOT VERIFY

**This item could not be verified at all.** What I tried:
- `WebFetch` to `https://lmarena.ai/leaderboard` — returned `HTTP 403 Forbidden` (consistent with the total WebFetch failure documented in §0).
- No `WebSearch` query on LMArena, the #1 model as of late July 2026, or any China-headquartered lab's leaderboard streak (DeepSeek, Alibaba/Qwen, Moonshot, Zhipu, ByteDance, Tencent) was possible — the session's WebSearch budget (200/200) was exhausted by the pricing-research queries in §1–3 before I reached this item, and the tool rejected all further calls outright.

I have **no basis whatsoever** — primary, secondary, or cached — for reporting which model/lab holds #1 on the LMArena overall text leaderboard as of late July 2026, or whether any China-headquartered lab has held #1 for 30+ consecutive days at any point. Nothing in this report should be read as bearing on that question. This item needs a fresh research pass with either working WebFetch access or a replenished WebSearch budget.

---

## Summary for the manuscript authors

**Current top-tier output prices (as of 2026-07-31, per secondary-source WebSearch corroboration — no primary pricing page or Wayback snapshot was fetchable this session):**
- **OpenAI:** GPT-5.6 Sol — $30.00/1M output tokens (unchanged in the Jul 30, 2026 price cut that only hit the lower Luna/Terra tiers)
- **Anthropic:** Claude Opus 5 — $25.00/1M output tokens (top of the standard GA lineup); Claude Fable 5 — $50.00/1M output tokens (Anthropic's separately-branded "most capable widely released model," a premium tier above Opus)
- **Google:** Gemini 3.1 Pro — $12.00/1M output tokens (≤200K context; $18.00 above 200K) — lowest-confidence figure of the three, single-source

**Item 2 (historical OpenAI launch prices):** Substantially verified via multiple independent secondary sources per data point — GPT-4 $60 (Mar 2023), GPT-4 Turbo $30 (Nov 2023), and GPT-4o $15 (May 2024) all confirmed cleanly; GPT-5 $10 (Aug 2025) confirmed for the "GPT-5 Chat" variant specifically, with an unresolved variant-naming ambiguity (a separate "GPT-5" figure at $5 output also appears in the sources).

**Items 3–4:** OpenAI shows a well-corroborated, specifically-dated price event one day before the snapshot (Jul 30, 2026: 80%/20% cuts to its two lower tiers, flagship Sol left unchanged) — and, notably, its flagship output price appears to have *risen* 3x (from $10 to $30) since the Aug 2025 GPT-5 launch rather than falling, per the sources found. Anthropic and Google price-history over the same window could not be checked at all (budget exhausted). The LMArena leaderboard question (item 4) could not be attempted in any form — no WebSearch query was made and the direct WebFetch to lmarena.ai failed — and is fully unverified; a follow-up pass is needed.
