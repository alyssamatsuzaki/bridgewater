import re
from PIL import Image as PILImage
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.platypus import (BaseDocTemplate, Frame, PageTemplate, Paragraph,
                                Spacer, Image, Table, TableStyle, KeepTogether,
                                HRFlowable)
from reportlab.lib.styles import ParagraphStyle

NAVY = HexColor("#16324f")
INK = HexColor("#22262b")
GRAY = HexColor("#5c6167")
LINE = HexColor("#b7bcc4")

W, H = letter
ML, MR, MT, MB = 0.9 * inch, 0.9 * inch, 0.75 * inch, 0.8 * inch
TEXTW = W - ML - MR

body = ParagraphStyle("body", fontName="Times-Roman", fontSize=10, leading=13.8,
                      alignment=TA_JUSTIFY, textColor=INK, spaceAfter=7)
fbody = ParagraphStyle("fbody", parent=body, spaceBefore=6)
epi = ParagraphStyle("epi", fontName="Times-Italic", fontSize=10.5, leading=14.5,
                     alignment=TA_LEFT, textColor=HexColor("#3d4249"),
                     leftIndent=14, rightIndent=14, spaceBefore=4, spaceAfter=10)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=15.5, leading=19,
                    textColor=NAVY, spaceBefore=16, spaceAfter=4)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=12, leading=15,
                    textColor=NAVY, spaceBefore=13, spaceAfter=5)
cap = ParagraphStyle("cap", fontName="Helvetica", fontSize=8, leading=10.6,
                     textColor=GRAY, spaceBefore=3, spaceAfter=4)
note = ParagraphStyle("note", fontName="Times-Italic", fontSize=9, leading=12.4,
                      textColor=GRAY, spaceBefore=10,
                      borderColor=LINE, borderWidth=0.6, borderPadding=7)
tcell = ParagraphStyle("tcell", fontName="Helvetica", fontSize=8.4, leading=10.8,
                       textColor=INK)
thead = ParagraphStyle("thead", parent=tcell, fontName="Helvetica-Bold",
                       textColor=HexColor("#ffffff"))

def inline(s):
    s = s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    s = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", s)
    s = re.sub(r"(?<!\w)\*(?!\s)(.+?)(?<!\s)\*(?!\w)", r"<i>\1</i>", s)
    return s

def fig_flowable(path, caption, fignum):
    caption = re.sub(r"^Figure \d+\.\s*", "", caption)
    im = PILImage.open(path)
    iw, ih = im.size
    w = min(TEXTW, 6.7 * inch)
    hgt = w * ih / iw
    img = Image(path, width=w, height=hgt)
    c = Paragraph(f"<b>Figure {fignum}.</b> {inline(caption)}", cap)
    return KeepTogether([Spacer(1, 6), img, c, Spacer(1, 6)])

story = []
lines = open("submission.md").read().splitlines()
i, first_h1, fignum = 0, True, 0
while i < len(lines):
    ln = lines[i].rstrip()
    if not ln.strip():
        i += 1
        continue
    if ln.startswith("|"):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            cells = [c.strip() for c in lines[i].strip().strip("|").split("|")]
            if not set("".join(cells)) <= set("-: "):
                rows.append(cells)
            i += 1
        data = [[Paragraph(inline(c), thead) for c in rows[0]]]
        for r in rows[1:]:
            data.append([Paragraph(inline(c), tcell) for c in r])
        t = Table(data, colWidths=[2.30 * inch, 1.15 * inch, 3.25 * inch],
                  repeatRows=1)
        t.setStyle(TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), NAVY),
            ("GRID", (0, 0), (-1, -1), 0.5, LINE),
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("TOPPADDING", (0, 0), (-1, -1), 4),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
            ("LEFTPADDING", (0, 0), (-1, -1), 5),
            ("RIGHTPADDING", (0, 0), (-1, -1), 5),
            ("ROWBACKGROUNDS", (0, 1), (-1, -1),
             [HexColor("#ffffff"), HexColor("#f4f6f8")]),
        ]))
        story += [Spacer(1, 4), t, Spacer(1, 8)]
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
                         ParagraphStyle("title", parent=h1, fontSize=19,
                                        leading=23, spaceBefore=0, spaceAfter=6)))
            first_h1 = False
        else:
            story.append(Paragraph(inline(txt), h1))
        story.append(HRFlowable(width="100%", thickness=1.1, color=NAVY,
                                spaceBefore=1, spaceAfter=8))
        i += 1
        continue
    if ln.startswith("## "):
        story.append(Paragraph(inline(ln[3:]), h2))
        i += 1
        continue
    if ln.strip() == "---":
        story.append(Spacer(1, 6))
        i += 1
        continue
    if ln.startswith("*[Verify"):
        story.append(Paragraph(inline(ln.strip("*")), note))
        i += 1
        continue
    if ln.startswith("*") and ln.endswith("*") and not ln.startswith("**"):
        story.append(Paragraph(inline(ln[1:-1]), epi))
        i += 1
        continue
    style = fbody if re.match(r"\*\*\d+\.", ln) else body
    story.append(Paragraph(inline(ln), style))
    i += 1

def on_page(canv, doc):
    canv.saveState()
    canv.setFont("Helvetica", 7.5)
    canv.setFillColor(GRAY)
    canv.drawString(ML, 0.45 * inch, "Forecasting the Future 2026 \u2014 submission")
    canv.drawRightString(W - MR, 0.45 * inch, f"{doc.page}")
    canv.restoreState()

doc = BaseDocTemplate("/mnt/user-data/outputs/FTF2026_submission_with_figures.pdf",
                      pagesize=letter, leftMargin=ML, rightMargin=MR,
                      topMargin=MT, bottomMargin=MB,
                      title="Forecasting the Future 2026: Submission")
frame = Frame(ML, MB, TEXTW, H - MT - MB, id="f")
doc.addPageTemplates([PageTemplate(id="p", frames=[frame], onPage=on_page)])
doc.build(story)
print("built")
