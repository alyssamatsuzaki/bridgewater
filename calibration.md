# Calibration

Reasoning behind the probabilities that changed in this revision, the reference classes behind them, and one derivation worked start to finish. Numbering is **final** (1–14); the original draft number appears in parentheses where it differs.

A note on what the reference classes can and cannot bear. The environment used for this revision could not open primary documents directly — every outbound fetch to `bea.gov`, `sec.gov`, `federalreserve.gov`, `ifr.org`, provider pricing pages, and `web.archive.org` returned 403 through the proxy, and the search allowance was exhausted partway through. Where a base rate below rests on the historical record rather than on a table I could re-read this week, it says so. No count is presented as exhaustive when it was assembled by search, and `verification/` records what each source actually established.

---

## Forecast 2 (was 2) — token prices: 90% → **80%**

### The ambiguity the ruling identified

"Most capable model" stops being well defined the moment providers add premium tiers, which is exactly what has happened. The July 31, 2026 baseline snapshot finds a market where the top of each lineup is no longer the cheap end of a descending series: OpenAI's designated top general-purpose tier prices output at $30 per million tokens, above the $10 that GPT-5 launched at in August 2025, and Anthropic ships a separately branded tier above its standard top model. A forecast that says "most capable" without a rule is a forecast whose resolution can be argued either way in 2027.

### Pre-registered selection rule (fixed as of July 31, 2026)

1. The model counted for a provider is the one that provider's own public pricing page **designates as its top general-purpose text tier** on the baseline date.
2. If the page designates none, count the **highest-priced generally available** general-purpose text model listed on it.
3. Successors and renames inherit the slot. A model retired without replacement drops out; the provider's new top-designated tier takes over.
4. Separately branded premium tiers count **only if the pricing page itself** designates them the top tier — not because they benchmark higher.
5. Standard on-demand **output** pricing only. Batch, cached-input, priority, and negotiated rates are excluded.
6. Comparison is always **provider against its own baseline**, never across providers.

Rule 4 is the load-bearing one. It is deliberately mechanical: it turns "most capable" into "what the seller says is on top," which is checkable from an archived page and cannot be re-litigated by benchmark results.

### Baseline snapshot

`data/snapshots/README.md` records the intended capture and its failure in this environment, with the exact commands to run before submission. This matters and should not be waved through: **the baseline is the thing the forecast resolves against**, and it currently rests on secondary reporting (status `snapshot_secondary_only` in `data/figure_sources.csv`). Capturing three HTML pages and three Wayback URLs from an unrestricted network closes it.

### Probability

The reference class is thin and points both ways.

- **For YES.** Four OpenAI flagship launch prices over twenty-nine months — $60, $30, $15, $10 — contain two adjacent steps that individually exceeded 50%, and the window contains next-generation launches from all three providers. Inference cost per unit of capability has fallen relentlessly on every public series. Three providers means three independent chances, and only one has to fire.
- **Against YES.** The most recent step in that same series was a 33% cut, not 50%. More importantly the direction at the top of the lineup has reversed: the current designated top tier is priced above its predecessor, which is what "premium tier" means commercially. July 2026's price action cut lower tiers and left the flagship untouched — evidence that providers are now segmenting rather than uniformly deflating. Under the pre-registered rule, cuts to cheaper tiers do not resolve this forecast.

The draft's 90% was priced against a world where the flagship was the deflating end of the market. Under the rule as now written, YES requires the *top* tier specifically to halve. Three shots on goal keep the probability high; demonstrated premiumization pulls it down. **80%**, inside the 80–85% band the ruling suggested and at its lower edge, because the premiumization evidence is recent, specific, and adverse.

---

## Forecast 6 (was 7) — EU enforcement: 62% → **35%**, recalculated from scratch

Not an adjustment of 62%. The AI Act trigger that carried much of the original number does not exist in the window's first sixteen months, so the old figure has no claim on the new one.

### What verification established

- **Regulation (EU) 2026/1744** (the Digital Omnibus), in force July 27, 2026, defers Annex III high-risk obligations from August 2, 2026 to **December 2, 2027**. Workplace AI systems are Annex III. Only Article 50 transparency duties attach in August 2026. The forecast window runs to December 31, 2028, so the high-risk regime is live for the final **thirteen** months, not the whole window.
- The remaining legal basis is real and unaffected: GDPR minimization and purpose limitation, Italy's Workers' Statute Article 4, German case law confining keystroke logging (BAG 2 AZR 681/16), works-council codetermination.

### Base rate

Formal proceedings, 2018 to July 2026, from the search-assembled record in `verification/V02_eu_ai_enforcement.md` (best-effort, not proven exhaustive):

| Element | Count against the six named firms | Nearest comparators |
|---|---|---|
| Employee-monitoring data | **1** — CNIL v. Amazon France Logistique (Dec 2023, €32M, reduced to €15M on appeal Dec 2025) | H&M Hamburg 2020 (€35.3M) — employee monitoring, non-tech firm |
| AI-training data | **1** — Garante v. OpenAI (Dec 2024, €15M), **annulled** on one-stop-shop jurisdictional grounds, March 2026 | Irish DPC inquiry into X/xAI over Grok training data (opened April 2025) — the cleanest AI-training precedent anywhere, against a firm outside the six |
| **Both elements in one docket** | **0** | none found anywhere |

So: roughly one employee-monitoring proceeding against these six firms per eight years, one AI-training proceeding that did not survive review, and zero instances of the conjunction the forecast requires.

### Derivation

The event is a conjunction, and each element has to happen inside twenty-nine months:

- **A trigger visible to a regulator.** The MCI episode is the model, and it raised salience sharply — but MCI captured *US* employees, so it gives an EU authority no jurisdiction. YES needs comparable capture touching EU staff and becoming publicly known. Reasonably likely given how these firms operate at scale: **0.55**.
- **An authority opening formally, with the AI-training nexus in its stated scope**, given a trigger. This is where the base rate bites. Employee-monitoring cases route to national DPAs and labour inspectorates rather than through the Irish one-stop-shop bottleneck, which is favourable. But authorities have opened one such proceeding in eight years, the Garante annulment is a live warning about jurisdictional overreach, and the criterion requires the AI-training purpose to appear in the authority's *own* scoping language — not merely in press coverage. Conditional: **0.60**.
- **Timing.** Both must land before December 31, 2028, with the widening effect of the high-risk regime available only in the last thirteen months: this is folded into the two figures above rather than multiplied separately, since the trigger estimate is already window-scoped.

0.55 × 0.60 ≈ 0.33, rounded to **35%** to reflect that the noyb-style complaint pipeline creates paths I have not enumerated.

Per the ruling, no sensitivity band appears in the forecast line. The relevant sensitivity: if the conditional-opening term were 0.75 instead of 0.60, the answer would be 41%; if the trigger term were 0.40, it would be 24%. The forecast is most fragile to the trigger term, which is why the self-audit names this forecast as one of the three most likely to be wrong.

---

## Forecast 7 (was 8) — datacenter capacity disclosure: 65% → **56%**

### The problem with the criterion

The criterion measures **public disclosure by the company**, not cancellation. Those are different events, and the draft's 65% priced them as one. The ruling: keep the disclosure criterion, state both stages, derive them independently. Both stages are derived below from their own evidence, and the product is printed as it falls out — it is not reverse-engineered from 65%.

### Stage 1 — P(a ≥1 GW cancellation or indefinite deferral occurs) = **0.80**

Five companies, twenty-nine months, announced US pipelines that no credible energization schedule supports, and a constraint set — transformers, interconnection queues, skilled trades — that is physical rather than financial. Analyst reporting already describes lease cancellations and expirations at Microsoft in 2025–26 at plausibly gigawatt scale. The pipeline is large enough that 1 GW is a small fraction of it. The residual 0.20 covers the world where demand stays strong enough that everything announced gets built or quietly re-phased below the 1 GW threshold.

### Stage 2 — P(the company itself discloses it | it happened) = **0.70**

This is where the draft was wrong, and the evidence is specific.

- **Adverse.** The most prominent pullback episode to date is instructive precisely because of *who* produced the numbers: analysts published the capacity figures, and the company's public response read as clarification rather than confirmation. The criterion explicitly excludes third-party reporting of lease non-renewals — so that entire episode, had it been at 1 GW, would have resolved **NO**. That is direct evidence against assuming disclosure follows cancellation.
- **Favourable.** The criterion is broader than a press release: an SEC filing or an official earnings-call transcript counts. At gigawatt scale, exits carry impairments, terminated commitments, and lease adjustments that surface in filings, and analysts ask direct questions on calls that executives answer on the record. Over twenty-nine months and five companies, sustained non-disclosure of a gigawatt-scale reversal is hard.

The pull between "companies avoid quantifying retreat" and "filings and transcripts force it eventually" lands at **0.70**.

### Product

0.80 × 0.70 = 0.56 → **56%**. Both stages appear in the manuscript's derivation so a reviewer can attack either one separately.

---

## Forecast 5 (was 6) — robots: fallback corrected, 68% held

The draft's fallback — MIIT China installations over the last available IFR world total — changes source and denominator simultaneously, which can move the computed share without anything happening in the world. Removed. **If the IFR discontinues the series, the forecast is unresolved.**

The probability is unchanged at 68%, and the underlying data survived checking with one caveat worth recording: the 2024 observation pairs a rounded China figure (295,000) with a unit-precise world figure (542,076), and the resulting 54.4% is *our* division — the IFR's own prose says 54%. The threshold is >54.0%, so this distinction is live at the margin, and the manuscript now states the computation rather than presenting 54.4% as an IFR figure. The series also spans multiple editions, and the IFR revises back-years; the one revision I could check moved 2022 by about 0.03 points, well inside the plotted precision.

One citation problem remains and is disclosed rather than papered over: the forecast cites "World Robotics 2028," an edition that does not exist yet. Given the IFR's consistent September cadence and each edition covering the prior calendar year, an edition published around September 2028 is the one that will carry calendar-2027 installations. If the IFR renames or re-times its editions, the resolution follows the **first published IFR figure for calendar-2027 installations**, whatever the edition is called.

## Forecast 10 (was 11) — LMArena: fallback removed, 20% held

The Artificial Analysis fallback is gone. A different benchmark measures a different thing and can reverse the outcome, so substituting one is not a fallback but a new forecast. **If LMArena is discontinued or changes methodology such that "the overall text leaderboard" no longer exists, the forecast is unresolved.** Probability unchanged at 20%: the barrier is the 30-consecutive-day hold, not reaching #1 once.

Verification could not establish the current leaderboard state — the leaderboard would not load through the environment's proxy and the search allowance was exhausted. The 20% therefore rests on the structural argument (export controls bind the frontier; the hold requirement is demanding) and not on a fresh reading of who is #1 today. Flagged in `verification/V10_ai_pricing_leaderboard.md`.

## Forecast 8 (was 9) — capex: definition enforced, 30% held

Every historical bar and every comparison must use the forecast's own boundary: cash-flow **purchases of property and equipment, excluding finance leases**. Verification established that company guidance frequently does not use that boundary — Meta's guidance explicitly includes finance-lease principal payments, and Microsoft's most recent figure is stated on a fiscal-year basis net of a lease reclassification. Consequences, all visible in the figure:

1. The 2026 guidance bar is drawn hatched as an **estimate**, not as an actual, and the source note states that guidance boundaries differ from the actuals line.
2. The sell-side markers for 2027 and 2028 are **deleted**. The ">$1.0T 2027 consensus" and "UBS ≈ +6% for 2028" could not be attributed to anything citable. Under the rule that an unverified number is verified, labelled an estimate, or cut, they are cut — and the manuscript's claim is narrowed to what we can defend: we could locate no published estimate modelling a contraction.
3. The draft's orange dot plotting "forecast 9's contrarian branch" at a specific dollar level is deleted. A probability is not a data point.

30% holds. It is a coherence-driven number: forecast 7 at 56% and forecast 11 at 30% both describe recognition of the same gap, and a 2028 capex contraction cannot sit near zero while those hold.

---

# One derivation, start to finish: Forecast 13 (was 15) — core PCE

**Claim.** US core PCE inflation prints at or above 3.0% year over year in at least six of the twelve months of calendar 2027, on BEA first prints. **55%.**

### Step 1 — the reference class, and its limits

The natural class is: from a starting point with core PCE in the high-2s to low-3s, how often does the following year contain at least six months at or above 3.0%? I could not compute this cleanly. The intended procedure was to pull the monthly core PCE series from 1985 and evaluate every start month with y/y between 2.8% and 4.0%, checking the window twelve to twenty-three months later. Every route to the series returned 403 in this environment, and I declined to compute a fraction from memory and present it as a base rate.

What the historical record does support, qualitatively and stated as such: since the mid-1980s, US core PCE has crossed durably from above 3.0% to below it on few occasions, and each came with an identifiable cause — the early-1990s disinflation arrived with a recession, and the 2023–24 descent arrived as pandemic supply shocks unwound. Neither transition happened while trade policy was actively adding to goods costs. **Inflation in the high-2s-to-low-3s is sticky absent either a demand shock or an unwinding supply shock.** That is the prior the arithmetic below encodes. It is weaker than a computed frequency and is labelled as such; a reviewer should treat Step 1 as a structural claim, not a measured base rate.

### Step 2 — decompose the event

Six of twelve months is close to "does the year *start* at or above the threshold and not fall away quickly," so the natural decomposition is on the entry condition:

> P(YES) = P(enters 2027 at ≥3.0%) × P(≥6 qualifying months | entered at ≥3.0%) + P(enters below 3.0%) × P(≥6 qualifying months | entered below)

### Step 3 — the entry term: **0.65**

Anchors, first prints, as of July 30, 2026: core PCE 3.3% y/y in June, the seventh consecutive print at or above 3.0%, with the three most recent at 3.3% or higher. *(These anchors are carried from the prior draft; the environment could not re-open BEA's release archive to re-verify them — see the note below and `verification/V08_macro_series.md`.)*

Getting below 3.0% by the December 2026 reference month requires roughly 0.4 points of disinflation in six months. Against it: the July 2026 Section 301 round, hitting sixty economies, is still passing through, and tariff pass-through to core goods runs with a lag measured in quarters. For it: a restrictive policy rate held through five meetings, Q2 real GDP at 1.5% annualized, and consensus expecting the 2026 energy shock to wash out of the y/y comparison. Disinflation of that size in that window is possible but not the central case: **0.65** that 2027 opens at or above 3.0%.

### Step 4 — the conditional terms: **0.75** and **0.15**

*Given entry at or above 3.0%:* only six of twelve months must qualify, and the early months of the year inherit the entry level almost mechanically — y/y prints move slowly. Failure requires disinflation that both arrives early in 2027 and persists, which historically needs a demand shock. A 2027 recession would do it — and that is precisely the scenario where forecasts 7 and 8 also fire, so this term is where the framework's internal correlation lives. **0.75.**

*Given entry below 3.0%:* re-acceleration to six qualifying months would require the tariff channel to reassert itself hard and fast after having just faded. Possible, not likely: **0.15.**

### Step 5 — arithmetic

    P(YES) = 0.65 × 0.75  +  0.35 × 0.15
           = 0.4875       +  0.0525
           = 0.54  →  printed as 55%

### Step 6 — sensitivity

| Input varied | Value | P(YES) |
|---|---|---|
| Entry term | 0.55 | 0.48 |
| Entry term (used) | 0.65 | 0.54 |
| Entry term | 0.75 | 0.60 |
| Conditional-given-entry | 0.65 | 0.48 |
| Conditional-given-entry (used) | 0.75 | 0.54 |
| Conditional-given-entry | 0.85 | 0.61 |

The forecast is roughly equally sensitive to both terms, and no plausible input combination pushes it far from a coin flip. That is the honest content of the 55%: a small, deliberate lean toward persistence, against market pricing that expects decline. It is not a conviction call, and the manuscript does not dress it as one.

### Step 7 — what would change it

A single core print at or below 2.8% before year-end 2026 would cut the entry term materially and pull the forecast toward 45%. Two consecutive prints at 3.4% or higher would push it toward 60%. A recession call landing in the first half of 2027 attacks the conditional term directly.

### Verification status of the anchors — stated plainly

The eighteen monthly first prints behind this derivation and behind the manuscript's Figure 4 are carried from the prior draft (`carried_unverified` in `data/figure_sources.csv`). Every attempt to re-read BEA's release archive from this environment returned 403, and the search allowance was exhausted before the series could be checked month by month. The 2025 values are consistent with the published record as I know it; the 2026 values could not be checked at all. This is the single largest outstanding evidence risk in the submission, it affects a live forecast, and it is listed as such in `CHANGELOG.md` rather than left for a reviewer to discover.
