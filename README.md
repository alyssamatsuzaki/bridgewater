# Control Without Feedback — Forecasting the Future 2026

## 1. What this is

This repository is a submission to the "Forecasting the Future 2026" competition: a
manuscript, "Control Without Feedback: Forecasts on AI and Modern Mercantilism"
(`submission.md`), together with the code and data used to build it. The submission
targets a 10-page limit. The built PDF is `FTF2026_submission.pdf`, produced by
`build_pdf.py` from `submission.md` and the figures in `figs/`.

## 2. Repository layout

| Path | Purpose |
|---|---|
| `README.md` | This file. |
| `requirements.txt` | Pinned Python dependencies for building the figures and the PDF. |
| `submission.md` | The manuscript source that `build_pdf.py` renders into the PDF. |
| `build_pdf.py` | Builds `FTF2026_submission.pdf` from `submission.md` and (unless skipped) renders `qa/page_NN.png`. |
| `figures.py` | Regenerates the five figures in `figs/` from the CSVs in `data/`. |
| `FTF2026_submission.pdf` | The built submission PDF; output of `build_pdf.py`. |
| `data/` | Per-figure input CSVs, the `figure_sources.csv` provenance ledger, and `snapshots/` (pricing-page baselines). |
| `figs/` | Generated figure output (SVG + 300-dpi PNG); overwritten each time `figures.py` runs. |
| `fonts/` | Bundled DejaVu Sans TTFs that `figures.py` requires for figure text; the build fails if they are missing rather than substituting a system font. |
| `qa/` | PNG renders of each built PDF page (`page_01.png` … `page_10.png`), for visual proofreading; overwritten by `build_pdf.py` unless `--no-qa` is passed. |
| `verification/` | Per-topic source-verification notes (`V01`–`V10`) documenting how factual claims in the manuscript were checked and what each source does and does not establish. |
| `archive/` | Material cut from the prior 18-page draft, kept for the record rather than deleted; see `archive/README.md`. |
| `plan.md` | The revision plan that cut the draft from 18 pages/18 forecasts to 10 pages/14 forecasts (forecast cut list, page allocation, rationale). |
| `figure_audit.md` | The audit of the original ten figures that decided which were kept as-is, replaced, or deleted. |
| `.gitignore` | Excludes Python bytecode and build temporaries. |

## 3. Environment setup

The build was run with Python 3.11.15 (check locally with `python3 --version`).

```
pip install -r requirements.txt
```

No network access is needed to build. All figure data comes from the CSVs in
`data/`, all figure fonts are bundled in `fonts/`, and the PDF build only reads
files already in this repository.

## 4. Building

```
python3 build_pdf.py
```

This regenerates the five figures from `data/`, builds `FTF2026_submission.pdf`
from `submission.md`, embeds a zip of this project into the PDF as a file
attachment, and renders `qa/page_01.png` … `qa/page_10.png` from the finished PDF
for visual proofreading.

Three flags:

- `--skip-figures` — build the PDF from the figures already in `figs/` instead of
  regenerating them first.
- `--no-qa` — skip rendering the `qa/page_NN.png` pages after the PDF is built.
- `--no-attach` — skip embedding the project archive.

### The embedded project archive

The submitted PDF carries this project inside it as an attachment named
`control-without-feedback-repo.zip` (~3.4 MB), so a reader can trace any number
without a network round-trip. Embedding happens on every build and replaces any
previous copy, so the attachment cannot drift from the manuscript it ships with.
Extract it from the attachments pane of most desktop PDF readers, or with:

```
python3 -c "import fitz; d=fitz.open('FTF2026_submission.pdf'); \
open('repo.zip','wb').write(d.embfile_get(0))"
```

Two things are held back and listed as omitted in the archive's own
`ATTACHMENT_NOTE.md`: the `qa/page_NN.png` renders, which duplicate the PDF the
archive is attached to, and `review_final.md`, the adversarial review commissioned
of our own draft to drive corrections. Both remain in the project directory. The
exclusion lists are `ATTACH_EXCLUDE` and `ATTACH_EXCLUDE_FILES` in
`build_pdf.py`; empty them to ship everything.

The build refuses to run if any unresolved `{{PENDING:...}}` marker remains in
`submission.md` — it exits with an error naming how many were found instead of
producing a PDF with placeholder text in it. Separately, the figure step fails
loudly (raises, does not fall back) if the bundled TTFs in `fonts/` are missing,
so a machine without the fonts can't silently produce figures rendered in a
different, unbundled font.

## 5. Regenerating figures only

```
python3 figures.py
```

This writes each figure to `figs/` as both an SVG and a 300-dpi PNG. Every
plotted value is read from a CSV under `data/` — there are no hard-coded numbers
in the plotting code — so changing what a figure shows means editing its CSV,
not `figures.py`.

## 6. Data provenance

`data/figure_sources.csv` is the provenance ledger: one row per plotted value,
across all five figures. Its columns are:

`figure, series, date, value, unit, status, vintage, source_org, publication_title, url, access_date, transformation`

The rule is that nothing is plotted unless it has a row here — every point in
every figure traces back to one of these rows, which record the source
organization, the publication, the URL, the date it was accessed, and any
transformation applied to get from the published number to the plotted one.

The `status` column records how each value was checked. The values that appear
in the file, and what each means:

- `search_confirmed` — confirmed against a primary or clearly-attributed
  source found via search.
- `search_confirmed_naming_ambiguity` — confirmed the same way, but the
  underlying source has a naming ambiguity that could not be fully resolved
  (e.g. which named model variant the price applies to).
- `search_confirmed_range_upper_unconfirmed` — the lower end of a reported
  range was confirmed directly; the upper end was not located in a primary
  table and is carried as reported.
- `triangulated` — no source directly states the value; it was inferred by
  combining other confirmed figures (e.g. a fiscal year's total backed out
  from an adjacent year's total and a reported year-over-year change).
- `carried_unverified` — carried forward from the prior draft of this
  manuscript without independent re-verification in this revision pass.
- `estimate` — not an observed print but an estimate, derivation, or company
  guidance; drawn hatched or hollow in the figures rather than solid.
- `no_print` — no observation exists for that period (e.g. a government
  shutdown delayed a release); drawn as a gap in the figure, not interpolated.
- `snapshot_secondary_only` — a pricing-page baseline that rests on secondary
  reporting because direct capture of the pricing page failed in this build
  environment; see `data/snapshots/README.md`.

Two additional rules govern the whole ledger: first prints govern — later
revisions to a series are ignored, and the vintage recorded is always the
first published print — and missing observations are drawn as gaps rather
than interpolated (the October 2025 core PCE gap, caused by a delayed BEA
release, is the example in the current figures).

`data/snapshots/` holds the archived pricing-page baselines that Forecast 2
resolves against. Its own `README.md` records that the capture did not
succeed from this build environment (outbound requests to the provider
pricing pages and to web.archive.org returned 403), so the current baseline
values rest on secondary reporting rather than a direct page capture, and
describes the outstanding step — capturing each provider's pricing page from
an unrestricted network and recording the result and a Wayback URL — that
still needs to happen before submission.

## 7. Figure design system

The four-color palette is fixed and used consistently across all figures:

- `#00204E` (navy) — observed primary data
- `#707B7C` (slate) — baseline or comparison series
- `#E65F00` (orange) — projection or estimate
- `#C0392B` (red) — forecast threshold (dashed line only)

Figures are designed at a fixed width of 6.7 inches, with a minimum text size
of 8pt, and are exported as both SVG and 300-dpi PNG.

## 8. Verification records

`verification/` contains one Markdown file per research topic (`V01` through
`V10`, plus a `V08b` follow-up), each documenting the sourcing behind a
cluster of related claims in the manuscript: what was checked, which channel
was used (direct fetch vs. search-result snippet), what each source actually
supports, and where a claim could not be independently confirmed. Read a
`V##` file when you want to know why a specific number or claim in the
manuscript is trusted at the level it is, beyond what fits in
`data/figure_sources.csv`.

## 9. Archive

`archive/` holds everything removed from the submission during the July 2026
revision, with the reason for each removal, per `archive/README.md`:

- `original/` — the complete pre-revision `submission.md`, `figures.py`, and
  `build_pdf.py` as submitted for review (18 pages, 18 forecasts, 10 figures).
- `forecasts_cut.md` — full text of the four cut forecasts, with the cut
  rationale for each.
- `prose_cut.md` — passages removed from the surviving parts of the
  manuscript, each with the reason.
- `figures_cut/` — final PNGs of the five retired charts, with the reason
  each was deleted or replaced.

Nothing here was deleted from history; it was moved to `archive/` instead.

## 10. Note on publication

This repository is deliberately unpublished. It exists only for the
competition submission process, and no remote has been configured for public
release.
