"""One-command build for the submission PDF.

    python build_pdf.py              # figures from data/, PDF, attachment, QA renders
    python build_pdf.py --skip-figures
    python build_pdf.py --no-qa      # skip rendering qa/page_NN.png
    python build_pdf.py --no-attach  # skip embedding the project archive

The finished PDF carries a zip of this project as an embedded file attachment, so
every number in the paper can be traced without a network round-trip. Embedding
runs on every build and replaces any prior copy, so the attachment cannot drift
from the manuscript it ships with.

Everything is project-relative; the build is offline and deterministic. The
figure step fails loudly if the bundled fonts in fonts/ are missing.
"""
import argparse
import re
import sys
from pathlib import Path

from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Image, Table, TableStyle, KeepTogether,
                                HRFlowable)
from reportlab.lib.styles import ParagraphStyle

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "submission.md"
OUT = ROOT / "FTF2026_submission.pdf"
QA = ROOT / "qa"

NAVY = HexColor("#00204E")
INK = HexColor("#1a1d21")
GRAY = HexColor("#5c6167")
LINE = HexColor("#b7bcc4")

W, H = letter
ML, MR, MT, MB = 0.9 * inch, 0.9 * inch, 0.72 * inch, 0.78 * inch
TEXTW = W - ML - MR

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=10, leading=13.1,
                      alignment=TA_JUSTIFY, textColor=INK, spaceAfter=6)
fbody = ParagraphStyle("fbody", parent=body, spaceBefore=4)
epi = ParagraphStyle("epi", fontName="Times-Italic", fontSize=10.5, leading=14.2,
                     alignment=TA_LEFT, textColor=HexColor("#3d4249"),
                     leftIndent=14, rightIndent=14, spaceBefore=4, spaceAfter=9)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15, leading=18.5,
                    textColor=NAVY, spaceBefore=14, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=11.5, leading=14.5,
                    textColor=NAVY, spaceBefore=11, spaceAfter=4)
cap = ParagraphStyle("cap", fontName="Helvetica", fontSize=8, leading=10.4,
                     textColor=GRAY, spaceBefore=3, spaceAfter=4)
tcell = ParagraphStyle("tcell", fontName="Helvetica", fontSize=8, leading=10.2,
                       textColor=INK)
thead = ParagraphStyle("thead", parent=tcell, fontName="Helvetica-Bold",
                       textColor=HexColor("#ffffff"))


def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<i>\1</i>", s)
    s = re.sub(r"`(.+?)`", r"<font face='Courier' size='8.6'>\1</font>", s)
    return s


def fig_flowable(path, caption, fignum):
    caption = re.sub(r"^Figure \d+\.\s*", "", caption)
    p = ROOT / path
    if not p.is_file():
        raise FileNotFoundError(f"figure referenced in submission.md is missing: {p}")
    im = PILImage.open(p)
    iw, ih = im.size
    w = min(TEXTW, 6.7 * inch)
    img = Image(str(p), width=w, height=w * ih / iw)
    c = Paragraph(f"<b>Figure {fignum}.</b> {inline(caption)}", cap)
    return KeepTogether([Spacer(1, 5), img, c, Spacer(1, 5)])


def table_flowable(rows_):
    ncols = len(rows_[0])
    # Weight columns by mean cell length (capped so one long cell can't dominate),
    # then enforce a minimum width so short columns don't wrap their own headers.
    weights = []
    for c in range(ncols):
        cells = [len(r[c]) for r in rows_ if c < len(r)]
        body_mean = sum(cells[1:]) / max(len(cells) - 1, 1)
        weights.append(max(min(body_mean, 40), len(rows_[0][c]) * 0.8, 3))
    total = sum(weights)
    colw = [TEXTW * w / total for w in weights]
    # Floor each column at the width of its longest single word, so no cell
    # ever breaks a word across lines ("Micros/oft").
    CHAR_PT, PAD_PT = 4.7, 11.0
    floors = []
    for c in range(ncols):
        longest_word = max((max((len(w) for w in r[c].split()), default=1)
                            for r in rows_ if c < len(r)), default=1)
        floors.append(min(longest_word * CHAR_PT + PAD_PT, TEXTW * 0.30))
    deficit = sum(f - w for f, w in zip(floors, colw) if w < f)
    if deficit > 0:
        spare = [i for i, w in enumerate(colw) if w > floors[i]]
        pool = sum(colw[i] - floors[i] for i in spare) or 1
        colw = [floors[i] if colw[i] < floors[i]
                else colw[i] - deficit * (colw[i] - floors[i]) / pool
                for i in range(ncols)]
    data = [[Paragraph(inline(c), thead) for c in rows_[0]]]
    for r in rows_[1:]:
        data.append([Paragraph(inline(c), tcell) for c in r])
    t = Table(data, colWidths=colw, repeatRows=1)
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("GRID", (0, 0), (-1, -1), 0.5, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LEFTPADDING", (0, 0), (-1, -1), 4.5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4.5),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1),
         [HexColor("#ffffff"), HexColor("#f4f6f8")]),
    ]))
    return t


def build_story():
    story = []
    lines = SRC.read_text(encoding="utf-8").splitlines()
    i, first_h1, fignum = 0, True, 0
    while i < len(lines):
        ln = lines[i].rstrip()
        if not ln.strip():
            i += 1
            continue
        if ln.startswith("|"):
            rows_ = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
                if not set("".join(cells)) <= set("-: "):
                    rows_.append(cells)
                i += 1
            story += [Spacer(1, 4), table_flowable(rows_), Spacer(1, 7)]
            continue
        m = re.match(r"!\[(.*)\]\((.*)\)", ln)
        if m:
            fignum += 1
            story.append(fig_flowable(m.group(2), m.group(1), fignum))
            i += 1
            continue
        if ln.startswith("# "):
            txt = ln[2:]
            if first_h1:
                story.append(Paragraph(inline(txt),
                             ParagraphStyle("title", parent=h1, fontSize=18,
                                            leading=22, spaceBefore=0,
                                            spaceAfter=5)))
                first_h1 = False
            else:
                story.append(Paragraph(inline(txt), h1))
            story.append(HRFlowable(width="100%", thickness=1.1, color=NAVY,
                                    spaceBefore=1, spaceAfter=7))
            i += 1
            continue
        if ln.startswith("## "):
            story.append(Paragraph(inline(ln[3:]), h2))
            i += 1
            continue
        if ln.strip() == "---":
            story.append(Spacer(1, 5))
            i += 1
            continue
        if ln.startswith("*") and ln.endswith("*") and not ln.startswith("**"):
            story.append(Paragraph(inline(ln[1:-1]), epi))
            i += 1
            continue
        style = fbody if re.match(r"\*\*\d+\.", ln) else body
        story.append(Paragraph(inline(ln), style))
        i += 1
    return story


def on_page(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(GRAY)
    canv.drawString(ML, 0.45 * inch,
                    "Forecasting the Future 2026")
    canv.drawRightString(W - MR, 0.45 * inch, f"{doc.page}")
    canv.restoreState()


def render_qa_pages():
    import fitz
    QA.mkdir(exist_ok=True)
    for old in QA.glob("page_*.png"):
        old.unlink()
    doc = fitz.open(OUT)
    for pno in range(len(doc)):
        pix = doc[pno].get_pixmap(dpi=120)
        pix.save(QA / f"page_{pno + 1:02d}.png")
    return len(doc)


# Everything the reviewer needs to re-derive the submission, minus the page
# renders (they duplicate the PDF the attachment is inside) and build detritus.
ATTACH_NAME = "ftf2026-repo.zip"
ATTACH_EXCLUDE = (".git", "__pycache__", ".pytest_cache")
# review_final.md is our own adversarial QA pass — a referee report we wrote
# to drive fixes, not a provenance record. It stays in the project and out of
# the judge-facing attachment. Delete this tuple entry to include it.
ATTACH_EXCLUDE_FILES = ("review_final.md",)
ATTACH_NOTE = """\
# Attached project repository

This archive is attached to the submission PDF so every number in the paper can
be traced without a network round-trip.

    submission.md            manuscript source
    figures.py               figure generation; every value read from data/
    build_pdf.py             one-command build (python3 build_pdf.py)
    requirements.txt         pinned versions the submitted PDF was built with
    fonts/                   bundled TTFs; the build fails rather than substitute
    data/                    per-figure input CSVs
    data/figure_sources.csv  provenance ledger: source, vintage, URL, access
                             date, transformation, verification status per point
    data/snapshots/          forecast 2 pricing baselines and capture procedure
    verification/            per-claim source findings, including failures
    figs/                    final figures, SVG and 300-dpi PNG
    archive/                 the pre-revision draft and everything cut, with reasons
    CHANGELOG.md             what changed and why; section 8 lists what is still
                             unverified and how to close each gap
    calibration.md           probability derivations, including one worked end to end
    figure_audit.md, plan.md  the pre-revision audit and revision plan
    qa/mechanical_checks.md  figure text-size and URL checks

Two items are omitted deliberately and remain in the project directory itself.
The `qa/page_NN.png` files are renders of the PDF this archive is attached to.
`review_final.md` is an adversarial review we commissioned of our own draft to
drive the corrections listed in `CHANGELOG.md`; every substantive finding it
produced is either fixed in the manuscript or recorded as outstanding in
CHANGELOG section 8.

Rebuild with `pip install -r requirements.txt && python3 build_pdf.py`. The build
is offline and deterministic.
"""


def attach_repository():
    """Embed a zip of the project into the built PDF as a file attachment."""
    import io
    import os
    import zipfile
    import fitz

    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        z.writestr("ATTACHMENT_NOTE.md", ATTACH_NOTE)
        for path in sorted(ROOT.rglob("*")):
            if not path.is_file():
                continue
            rel = path.relative_to(ROOT)
            if rel.parts[0] in ATTACH_EXCLUDE:
                continue
            if rel.parts[0] == "qa" and rel.name.startswith("page_"):
                continue
            if path.name in (OUT.name, ATTACH_NAME):
                continue
            if rel.as_posix() in ATTACH_EXCLUDE_FILES:
                continue
            z.write(path, rel.as_posix())
    payload = buf.getvalue()

    doc = fitz.open(OUT)
    for i in range(doc.embfile_count() - 1, -1, -1):
        doc.embfile_del(i)                      # idempotent across rebuilds
    doc.embfile_add(
        ATTACH_NAME, payload, filename=ATTACH_NAME,
        ufilename=ATTACH_NAME,
        desc="Project repository: manuscript source, figure code, input data, "
             "provenance ledger, verification records, and archived cut material.",
    )
    tmp = OUT.with_suffix(".tmp.pdf")
    doc.save(str(tmp), garbage=3, deflate=True)
    doc.close()
    os.replace(tmp, OUT)
    return len(payload)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skip-figures", action="store_true")
    ap.add_argument("--no-qa", action="store_true")
    ap.add_argument("--no-attach", action="store_true",
                    help="skip embedding the project repository in the PDF")
    args = ap.parse_args()

    leftover = [ln for ln in SRC.read_text(encoding="utf-8").splitlines()
                if "{{PENDING:" in ln]
    if leftover:
        sys.exit(f"build refused: {len(leftover)} unresolved {{{{PENDING:...}}}} "
                 "markers remain in submission.md")

    if not args.skip_figures:
        import figures
        for f in figures.ALL:
            f()

    doc = BaseDocTemplate(str(OUT), pagesize=letter, leftMargin=ML,
                          rightMargin=MR, topMargin=MT, bottomMargin=MB,
                          title="Forecasts on AI and Modern Mercantilism")
    frame = Frame(ML, MB, TEXTW, H - MT - MB, id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
    doc.build(build_story())

    attached = 0
    if not args.no_attach:
        attached = attach_repository()

    npages = "?"
    if not args.no_qa:
        npages = render_qa_pages()
    msg = f"built {OUT.name}: {npages} pages"
    if attached:
        msg += f"; repository attached ({attached / 1e6:.1f} MB, {ATTACH_NAME})"
    if not args.no_qa:
        msg += f"; page renders in {QA}/"
    print(msg)


if __name__ == "__main__":
    main()
