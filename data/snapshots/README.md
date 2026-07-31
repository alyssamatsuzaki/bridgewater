# Pricing-page snapshots (forecast 2 baseline)

Forecast 2 resolves against each provider's own July 31, 2026 published output-token
price for its designated top general-purpose tier. Those baselines must be archived
by us, because pricing pages are edited in place and Wayback coverage of them is
uneven.

**Status of this build (2026-07-31): the capture did not succeed from this
environment.** All outbound HTTP through the build environment's proxy returned 403
for provider pricing pages and for web.archive.org, so no HTML snapshot could be
written here. The baseline values recorded in `../figure_sources.csv` therefore rest
on secondary reporting and are marked `snapshot_secondary_only`.

**Before submission, capture from an unrestricted network:**

    # for each provider pricing page
    curl -sSL "https://openai.com/api/pricing/"        -o openai_pricing_2026-07-31.html
    curl -sSL "https://www.anthropic.com/pricing"      -o anthropic_pricing_2026-07-31.html
    curl -sSL "https://ai.google.dev/gemini-api/docs/pricing" -o google_pricing_2026-07-31.html
    # and request a Wayback capture of each, recording the returned snapshot URL
    curl -sS "https://web.archive.org/save/https://openai.com/api/pricing/"

Then record, per provider: the model the page designates as top general-purpose tier,
its on-demand output price per 1M tokens, the file name here, and the Wayback URL, in
`../figure_sources.csv`. The selection rule that governs which model counts is
pre-registered in Table 2 of the manuscript and must not be changed after this date.
