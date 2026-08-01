# Calibration

Reasoning behind the probabilities that changed in this revision, the reference classes behind them, and one derivation worked start to finish. Numbering is **final** (1–16); the original draft number appears in parentheses where it differs. Forecasts 15 and 16 were added when the page limit rose; 16 restores a forecast cut earlier in this same revision, and that reversal is recorded in `CHANGELOG.md` section 8b. **Forecast 17 (USD/JPY) was cut in the final compliance pass** for the reason its own derivation below already gave, that its criterion is blind to cause; the derivation is kept as the record of why it was priced and then dropped (`CHANGELOG.md` section 8e).

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

## Forecast 14 — net customs duties: 70% → **25%**, forced by an external ruling

The only forecast in the set repriced by an event rather than by rethinking. Evidence in `verification/V11_august_2026_sweep.md` §§1–3; the full derivation is in `research_companion.md` §5.

### What the 70% assumed

FY2025 net customs duties printed $194.9B against a $250B FY2027 threshold. The series had risen $118B in one year. A further $55B over two years read as a modest ask, and refund litigation was treated as a discount rather than as a regime question.

### What broke the assumption

The Supreme Court held 6–3 on **February 20, 2026** that IEEPA does not authorize tariffs, retroactive to inception. This is not a haircut on a growth path. It removes the statutory basis for most of what produced the FY2025 figure.

### The four inputs

1. **Refunds subtract from the resolution line.** The forecast resolves on *net* duties. The Court of International Trade ordered ~$165B refunded with interest, in stages; Penn Wharton put revenue at risk above $175B. June 2026 net already printed **−$25.6B** ($23.6B gross against $49.2B refunded).
2. **Replacement is partial.** CRFB (2026-07-23): Section 301 and 338 restore **under 60%** of lost IEEPA revenue; post-January-2025 actions score ~**$825B below** CBO's February 2026 baseline through FY2036.
3. **Replacement is contested.** Section 122, the February bridge, was ruled illegal by the CIT pending appeal.
4. **The base is large.** Section 301 covers ~**$949B** of 2026 imports at 10–12.5%, which is over $118B of gross before pre-existing 232 and 301 lines.

### Derivation

P(YES) = P(successor regime survives challenge through FY2027) × P(gross clears ~$250B plus residual refunds | survival)
= 0.55 × 0.45 ≈ **0.25**

Both terms are judgment. There is no prior instance of a tariff regime this large being voided and reconstituted under different authorities inside two years, so the reference class is empty and I do not pretend otherwise.

### What would move it

**Up:** Congressional ratification by statute would largely settle input 3 and justify a substantial revision. Appellate reversal on Section 122 would do less, since that authority is time-limited by design.

**Down:** an adverse ruling on the Section 301 forced-labor actions, or a refund schedule extending materially into FY2027.

---

## Forecast 5 (was 6) — robots: fallback corrected, 68% held

The draft's fallback — MIIT China installations over the last available IFR world total — changes source and denominator simultaneously, which can move the computed share without anything happening in the world. Removed. **If the IFR discontinues the series, the forecast is unresolved.**

The probability is unchanged at 68%, and the underlying data survived checking with one caveat worth recording: the 2024 observation pairs a rounded China figure (295,000) with a unit-precise world figure (542,076), and the resulting 54.4% is *my* division — the IFR's own prose says 54%. The threshold is >54.0%, so this distinction is live at the margin, and the manuscript now states the computation rather than presenting 54.4% as an IFR figure. The series also spans multiple editions, and the IFR revises back-years; the one revision I could check moved 2022 by about 0.03 points, well inside the plotted precision.

One citation problem remains and is disclosed rather than papered over: the forecast cites "World Robotics 2028," an edition that does not exist yet. Given the IFR's consistent September cadence and each edition covering the prior calendar year, an edition published around September 2028 is the one that will carry calendar-2027 installations. If the IFR renames or re-times its editions, the resolution follows the **first published IFR figure for calendar-2027 installations**, whatever the edition is called.

## Forecast 10 (was 11) — LMArena: fallback removed, 20% held

The Artificial Analysis fallback is gone. A different benchmark measures a different thing and can reverse the outcome, so substituting one is not a fallback but a new forecast. **If LMArena is discontinued or changes methodology such that "the overall text leaderboard" no longer exists, the forecast is unresolved.** Probability unchanged at 20%: the barrier is the 30-consecutive-day hold, not reaching #1 once.

Verification could not establish the current leaderboard state — the leaderboard would not load through the environment's proxy and the search allowance was exhausted. The 20% therefore rests on the structural argument (export controls bind the frontier; the hold requirement is demanding) and not on a fresh reading of who is #1 today. Flagged in `verification/V10_ai_pricing_leaderboard.md`.

## Forecast 8 (was 9) — capex: definition enforced, 30% held

Every historical bar and every comparison must use the forecast's own boundary: cash-flow **purchases of property and equipment, excluding finance leases**. Verification established that company guidance frequently does not use that boundary — Meta's guidance explicitly includes finance-lease principal payments, and Microsoft's most recent figure is stated on a fiscal-year basis net of a lease reclassification. Consequences, all visible in the figure:

1. The 2026 guidance bar is drawn hatched as an **estimate**, not as an actual, and the source note states that guidance boundaries differ from the actuals line.
2. The sell-side markers for 2027 and 2028 are **deleted**. The ">$1.0T 2027 consensus" and "UBS ≈ +6% for 2028" could not be attributed to anything citable. Under the rule that an unverified number is verified, labelled an estimate, or cut, they are cut — and the manuscript's claim is narrowed to what is defensible: I could locate no published estimate modelling a contraction.
3. The draft's orange dot plotting "forecast 9's contrarian branch" at a specific dollar level is deleted. A probability is not a data point.

30% holds. It is a coherence-driven number: forecast 7 at 56% and forecast 11 at 30% both describe recognition of the same gap, and a 2028 capex contraction cannot sit near zero while those hold.

---

## Forecast 15 (world models) — **40%**, newly derived

The framework does not predict that world models will disappoint. It predicts an asymmetry, and the forecast is written to catch the asymmetry rather than the capability.

**What is already established (July 2026).** DeepMind's Genie 3 generates persistent interactive 3D environments in real time at 24 fps and ships to subscribers through Project Genie. NVIDIA's Cosmos 3, released June 22, 2026, is an omnimodal world model aimed at physical AI, with embodied reasoning, task planning, and action modeling spanning vehicles, robots, and egocentric human motion. Benchmark attention has moved from video realism toward closed-loop usefulness (WorldArena, World-in-World, RoboTrustBench). Capability and availability are therefore not the open question.

**What the framework says.** Claim 4: as knowledge becomes codified, its price falls and value migrates to what stays scarce. A world model is an attempt to codify the physical world, so the codified layer should cheapen fast — as it has — while the scarce complements remain real interaction data and physical position. The binding constraint should therefore appear at deployment, not at model quality.

**Why the criterion is disclosure by the end user.** Vendor adoption is already visible and proves little: NVIDIA reports roughly two million cumulative Cosmos downloads, which is a vendor claim about developers, not evidence of production robots. The decision-relevant event is an industrial operator outside technology putting a world model into its own robot training loop and saying so in a filing, transcript, or release. That is the same disclosure discipline as forecast 7, and for the same reason: it is checkable and it cannot be satisfied by press enthusiasm.

**Derivation.**

- **Base condition — does it happen at all?** Synthetic physics-aware training data is already standard practice among robotics and AV developers, and the large industrial adopters of warehouse robotics have both the capital and the volume to justify it. That the underlying activity occurs somewhere among the Fortune 500 non-technology set before end-2028: **0.75**.
- **Does the operator disclose it?** Higher than forecast 9's equivalent term, for a specific reason: NVIDIA and its peers actively co-market named customer deployments, and an operator has no legal exposure in saying it trains robots on synthetic data. Contrast forecast 9, where disclosing workflow-data licensing invites employment and privacy scrutiny, which is why that stage sits low. But the disclosure must name the model class and the operator's own facilities, which corporate communications often blur into generic "AI" language: **0.55**.

0.75 × 0.55 ≈ 0.41, printed as **40%**.

**Sensitivity.** If the disclosure term were 0.70, the answer is 53%; if 0.40, it is 30%. The forecast is most fragile to how specifically firms describe their automation, which is a communications habit rather than a technical fact — a weakness worth naming.

**What it cannot show.** Resolving YES does not establish that world models drove the automation, only that one was disclosed in the loop. Resolving NO is weak evidence, since 40% means NO is already the expected outcome. This forecast informs mainly in the YES direction.

## Forecasts 16 and 17 — restored, probabilities carried, and 17 later cut

Both were cut earlier in this revision and restored when the page limit rose to 15. Neither probability was re-derived, because the environment could not re-read the underlying series; carrying the original numbers is the honest option and is recorded as such.

**Forecast 16 (LA28 delivery), 70%.** Original number retained. The reasoning that produced it: a fixed, unmovable date; a program that has already publicly conceded delivery risk by replacing eleven of its original projects in a March 2024 board action; and a threshold set below the program's own target rather than at it. The restoration rationale is framework-level, not evidential — relationship 4 concerns policy delay as such, so a transit program on a hard deadline is a legitimate test rather than an analogy, which is what the earlier cut had judged it to be. The project list governs resolution and is carried unverified; it should be confirmed against the board report before submission.

**Forecast 17 (the yen), 30%.** Original number retained, built from the August 2024 carry unwind (roughly 12% peak-to-trough in five weeks) as the reference-class event, doubled against the unconditional base rate for a seventeen-month window on the argument that yen funding sits beneath a meaningful share of AI-buildout leverage.

The reason this forecast was cut, and the reason restoring it is defensible, are the same fact stated twice. The criterion resolves YES on any carry unwind, including one with no mercantilism or AI anywhere in the chain. I did not repair that by adding conditions, because every conditioning clause I considered — requiring a coincident BoJ action, or an intervention, or a named funding stress — made the forecast either unresolvable or a different forecast. So the limitation is restated in the manuscript: forecast 17 establishes co-movement with the framework, not attribution to it. Forecast 13 carries the identical caveat and is treated the same way. What the synthesis adds is a mechanism the earlier draft could not name: relationship 2 predicts fragility from correlated positioning and leverage, and the yen is the cleanest instrument on which that fragility is priced.

The structural conditions I would ordinarily cite — where USD/JPY sits against its multi-decade range, and the Bank of Japan's tightening path — are carried from the prior draft and were not re-verified this pass. The 30% therefore rests on the reference event and the funding-channel argument alone.

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
