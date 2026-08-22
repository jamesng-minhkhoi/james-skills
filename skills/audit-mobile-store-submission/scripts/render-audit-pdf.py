#!/usr/bin/env python3
"""Render a completed mobile store audit Markdown file as a readable PDF."""

from __future__ import annotations

import argparse
import html
import re
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_LEFT
    from reportlab.lib.pagesizes import A4, letter
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        HRFlowable,
        ListFlowable,
        ListItem,
        Paragraph,
        Preformatted,
        SimpleDocTemplate,
        Spacer,
        Table,
        TableStyle,
    )
except ImportError as exc:  # pragma: no cover - exercised when dependency is unavailable
    print(
        "ERROR: reportlab is required. Install it with "
        "'python3 -m pip install reportlab' or use the bundled Codex Python runtime.",
        file=sys.stderr,
    )
    raise SystemExit(2) from exc


NAVY = colors.HexColor("#172A46")
TEAL = colors.HexColor("#087E8B")
MINT = colors.HexColor("#E8F5F3")
PALE_BLUE = colors.HexColor("#EFF4FA")
INK = colors.HexColor("#253247")
MUTED = colors.HexColor("#68778D")
LINE = colors.HexColor("#D9E1EA")
RED = colors.HexColor("#B42318")
AMBER = colors.HexColor("#9A6700")
GREEN = colors.HexColor("#157347")
FONT = "Helvetica"
FONT_BOLD = "Helvetica-Bold"


@dataclass
class Block:
    kind: str
    value: object


def configure_fonts() -> None:
    """Prefer a Unicode font so Vietnamese and other audit text stays readable."""

    global FONT, FONT_BOLD
    candidates = [
        ("/System/Library/Fonts/Supplemental/Arial Unicode.ttf", "AuditUnicode"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "AuditUnicode"),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", "AuditUnicodeBold"),
    ]
    regular = next((path for path, _ in candidates[:2] if Path(path).is_file()), None)
    bold = next((path for path, name in candidates if name == "AuditUnicodeBold" and Path(path).is_file()), None)
    if regular:
        pdfmetrics.registerFont(TTFont("AuditUnicode", regular))
        FONT = "AuditUnicode"
        if bold:
            pdfmetrics.registerFont(TTFont("AuditUnicodeBold", bold))
            FONT_BOLD = "AuditUnicodeBold"
        else:
            FONT_BOLD = FONT


def clean_inline(value: str) -> str:
    """Convert the Markdown subset used by audit reports to ReportLab markup."""

    value = value.strip()
    value = re.sub(r"!\[([^]]*)\]\([^)]*\)", r"[image: \1]", value)
    links: list[str] = []

    def hold_link(match: re.Match[str]) -> str:
        label = html.escape(match.group(1))
        href = html.escape(match.group(2), quote=True)
        links.append(f'<link href="{href}" color="#087E8B">{label}</link>')
        return f"\x00LINK{len(links) - 1}\x00"

    value = re.sub(r"\[([^]]+)\]\(([^)]+)\)", hold_link, value)
    value = html.escape(value, quote=False)
    value = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', value)
    value = re.sub(r"\*\*([^*]+)\*\*", r"<b>\1</b>", value)
    value = re.sub(r"__([^_]+)__", r"<b>\1</b>", value)
    value = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<i>\1</i>", value)
    value = value.replace("  ", "<br/>")
    for index, link in enumerate(links):
        value = value.replace(f"\x00LINK{index}\x00", link)
    return value


def is_table_separator(line: str) -> bool:
    cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def parse_markdown(text: str) -> list[Block]:
    lines = text.replace("\r\n", "\n").split("\n")
    blocks: list[Block] = []
    index = 0
    paragraph: list[str] = []

    def flush_paragraph() -> None:
        if paragraph:
            blocks.append(Block("paragraph", " ".join(item.strip() for item in paragraph)))
            paragraph.clear()

    while index < len(lines):
        line = lines[index]
        stripped = line.strip()
        if not stripped:
            flush_paragraph()
            index += 1
            continue
        if stripped.startswith("```"):
            flush_paragraph()
            language = stripped[3:].strip()
            index += 1
            code_lines: list[str] = []
            while index < len(lines) and not lines[index].strip().startswith("```"):
                code_lines.append(lines[index])
                index += 1
            if index < len(lines):
                index += 1
            blocks.append(Block("code", (language, "\n".join(code_lines))))
            continue
        heading = re.match(r"^(#{1,3})\s+(.+?)\s*#*$", stripped)
        if heading:
            flush_paragraph()
            blocks.append(Block("heading", (len(heading.group(1)), heading.group(2))))
            index += 1
            continue
        if stripped.startswith(">"):
            flush_paragraph()
            quote_lines: list[str] = []
            while index < len(lines) and lines[index].strip().startswith(">"):
                quote_lines.append(lines[index].strip()[1:].strip())
                index += 1
            blocks.append(Block("quote", " ".join(quote_lines)))
            continue
        if stripped.startswith("|") and index + 1 < len(lines) and is_table_separator(lines[index + 1]):
            flush_paragraph()
            rows = [table_row(lines[index])]
            index += 2
            while index < len(lines) and lines[index].strip().startswith("|"):
                rows.append(table_row(lines[index]))
                index += 1
            blocks.append(Block("table", rows))
            continue
        list_match = re.match(r"^[-*+]\s+(.+)$", stripped)
        ordered_match = re.match(r"^(\d+)[.)]\s+(.+)$", stripped)
        if list_match or ordered_match:
            flush_paragraph()
            ordered = ordered_match is not None
            items: list[str] = []
            while index < len(lines):
                candidate = lines[index].strip()
                match = re.match(r"^(\d+)[.)]\s+(.+)$", candidate) if ordered else re.match(r"^[-*+]\s+(.+)$", candidate)
                if not match:
                    break
                items.append(match.group(2) if ordered else match.group(1))
                index += 1
            blocks.append(Block("list", (ordered, items)))
            continue
        paragraph.append(line)
        index += 1
    flush_paragraph()
    return blocks


def detect_verdict(text: str) -> tuple[str, str]:
    match = re.search(r"\b(Ready with conditions|Not ready|Ready|Unknown)\b", text, re.I)
    if not match:
        return "Audit complete", "neutral"
    value = match.group(1)
    lower = value.lower()
    tone = "green" if lower == "ready" else "amber" if "conditions" in lower or lower == "unknown" else "red"
    return value, tone


def verdict_color(tone: str):
    return {"green": GREEN, "amber": AMBER, "red": RED}.get(tone, TEAL)


def build_styles():
    base = getSampleStyleSheet()
    return {
        "title": ParagraphStyle("AuditTitle", parent=base["Title"], fontName=FONT_BOLD, fontSize=25, leading=30, textColor=NAVY, spaceAfter=5),
        "subtitle": ParagraphStyle("AuditSubtitle", parent=base["Normal"], fontName=FONT, fontSize=10, leading=14, textColor=MUTED, spaceAfter=12),
        "h1": ParagraphStyle("AuditH1", parent=base["Heading1"], fontName=FONT_BOLD, fontSize=17, leading=21, textColor=NAVY, spaceBefore=18, spaceAfter=8, keepWithNext=True),
        "h2": ParagraphStyle("AuditH2", parent=base["Heading2"], fontName=FONT_BOLD, fontSize=13, leading=17, textColor=TEAL, spaceBefore=13, spaceAfter=6, keepWithNext=True),
        "h3": ParagraphStyle("AuditH3", parent=base["Heading3"], fontName=FONT_BOLD, fontSize=11, leading=14, textColor=INK, spaceBefore=10, spaceAfter=4, keepWithNext=True),
        "body": ParagraphStyle("AuditBody", parent=base["BodyText"], fontName=FONT, fontSize=9.4, leading=13.5, textColor=INK, spaceAfter=7),
        "quote": ParagraphStyle("AuditQuote", parent=base["BodyText"], fontName=FONT, fontSize=9, leading=13, textColor=INK, leftIndent=12, borderPadding=8, borderColor=TEAL, borderWidth=2, borderLeft=True, spaceBefore=4, spaceAfter=8),
        "code": ParagraphStyle("AuditCode", parent=base["Code"], fontName="Courier", fontSize=7.3, leading=9, textColor=INK, backColor=PALE_BLUE, borderPadding=7, spaceBefore=4, spaceAfter=8),
        "table": ParagraphStyle("AuditTable", parent=base["BodyText"], fontName=FONT, fontSize=7.2, leading=9.2, textColor=INK),
        "table_head": ParagraphStyle("AuditTableHead", parent=base["BodyText"], fontName=FONT_BOLD, fontSize=7.2, leading=9.2, textColor=colors.white),
        "bullet": ParagraphStyle("AuditBullet", parent=base["BodyText"], fontName=FONT, fontSize=9.2, leading=13, textColor=INK, leftIndent=3, spaceAfter=3),
        "meta": ParagraphStyle("AuditMeta", parent=base["BodyText"], fontName=FONT, fontSize=8.5, leading=11, textColor=INK),
        "verdict": ParagraphStyle("AuditVerdict", parent=base["BodyText"], fontName=FONT_BOLD, fontSize=14, leading=17, textColor=colors.white, alignment=TA_LEFT),
    }


def page_footer(canvas, doc):
    canvas.saveState()
    width, _ = doc.pagesize
    canvas.setStrokeColor(LINE)
    canvas.setLineWidth(0.5)
    canvas.line(doc.leftMargin, 15 * mm, width - doc.rightMargin, 15 * mm)
    canvas.setFont(FONT, 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawString(doc.leftMargin, 9 * mm, "Mobile Store Submission Audit")
    canvas.drawRightString(width - doc.rightMargin, 9 * mm, f"Page {doc.page}")
    canvas.restoreState()


def metadata_card(styles, args, verdict: str, tone: str):
    info: list[object] = []
    if args.app_name:
        info.append(Paragraph(f"<b>App</b><br/>{clean_inline(args.app_name)}", styles["meta"]))
    if args.platform:
        info.append(Paragraph(f"<b>Platform</b><br/>{clean_inline(args.platform)}", styles["meta"]))
    if args.checked_at:
        info.append(Paragraph(f"<b>Checked</b><br/>{clean_inline(args.checked_at)}", styles["meta"]))
    if not info:
        info.append(Paragraph("<b>Report</b><br/>Evidence-backed release audit", styles["meta"]))
    meta = Table([info], colWidths=[None] * len(info), hAlign="LEFT")
    meta.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), MINT), ("BOX", (0, 0), (-1, -1), 0.6, LINE), ("INNERGRID", (0, 0), (-1, -1), 0.3, LINE), ("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10), ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8)]))
    verdict_table = Table([[Paragraph(html.escape(verdict), styles["verdict"])]], colWidths=[None])
    verdict_table.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), verdict_color(tone)), ("LEFTPADDING", (0, 0), (-1, -1), 12), ("RIGHTPADDING", (0, 0), (-1, -1), 12), ("TOPPADDING", (0, 0), (-1, -1), 10), ("BOTTOMPADDING", (0, 0), (-1, -1), 10)]))
    wrapper = Table([[meta], [verdict_table]], colWidths=[None], hAlign="LEFT")
    wrapper.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 0), ("RIGHTPADDING", (0, 0), (-1, -1), 0), ("TOPPADDING", (0, 0), (-1, -1), 0), ("BOTTOMPADDING", (0, 0), (-1, -1), 0)]))
    return wrapper


def table_flowable(rows: list[list[str]], styles, width: float):
    columns = max(len(row) for row in rows)
    normalized = [row + [""] * (columns - len(row)) for row in rows]
    data = []
    for row_index, row in enumerate(normalized):
        style = styles["table_head"] if row_index == 0 else styles["table"]
        data.append([Paragraph(clean_inline(cell), style) for cell in row])
    table = Table(data, colWidths=[width / columns] * columns, repeatRows=1, hAlign="LEFT")
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, PALE_BLUE]),
        ("GRID", (0, 0), (-1, -1), 0.35, LINE),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 6),
        ("RIGHTPADDING", (0, 0), (-1, -1), 6),
        ("TOPPADDING", (0, 0), (-1, -1), 5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 5),
    ]))
    return table


def render(input_path: Path, output_path: Path, args) -> None:
    configure_fonts()
    text = input_path.read_text(encoding="utf-8")
    blocks = parse_markdown(text)
    verdict, tone = detect_verdict(text)
    if args.verdict:
        verdict, tone = args.verdict, detect_verdict(args.verdict)[1]
    styles = build_styles()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc = SimpleDocTemplate(str(output_path), pagesize=A4 if args.page_size == "a4" else letter, rightMargin=18 * mm, leftMargin=18 * mm, topMargin=18 * mm, bottomMargin=21 * mm, title=args.title, author="Mobile Store Submission Audit")
    story: list[object] = [
        Paragraph(clean_inline(args.title), styles["title"]),
        Paragraph("Evidence-backed readiness report for non-technical review", styles["subtitle"]),
        metadata_card(styles, args, verdict, tone),
        Spacer(1, 12),
        HRFlowable(width="100%", thickness=1, color=LINE, spaceBefore=2, spaceAfter=8),
    ]
    for block in blocks:
        if block.kind == "heading":
            level, value = block.value
            story.append(Paragraph(clean_inline(value), styles["h1" if level == 1 else "h2" if level == 2 else "h3"]))
        elif block.kind == "paragraph":
            story.append(Paragraph(clean_inline(block.value), styles["body"]))
        elif block.kind == "quote":
            story.append(Paragraph(clean_inline(block.value), styles["quote"]))
        elif block.kind == "code":
            story.append(Preformatted(block.value[1], styles["code"], maxLineLength=110))
        elif block.kind == "list":
            ordered, items = block.value
            list_items = [ListItem(Paragraph(clean_inline(item), styles["bullet"]), leftIndent=12) for item in items]
            list_options = {"bulletType": "1" if ordered else "bullet", "bulletFontName": FONT, "bulletFontSize": 8, "leftIndent": 14, "bulletOffsetY": 2, "spaceAfter": 6}
            if ordered:
                list_options["start"] = "1"
            story.append(ListFlowable(list_items, **list_options))
        elif block.kind == "table":
            story.append(table_flowable(block.value, styles, doc.width))
            story.append(Spacer(1, 9))
    doc.build(story, onFirstPage=page_footer, onLaterPages=page_footer)


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a completed store audit Markdown file as a polished PDF.")
    parser.add_argument("input", type=Path, help="Completed audit Markdown file")
    parser.add_argument("output", type=Path, help="Output PDF path")
    parser.add_argument("--title", default="Mobile Store Submission Audit")
    parser.add_argument("--app-name", default="")
    parser.add_argument("--platform", default="")
    parser.add_argument("--verdict", default="", help="Ready, Ready with conditions, Not ready, or Unknown")
    parser.add_argument("--checked-at", default="")
    parser.add_argument("--page-size", choices=("a4", "letter"), default="a4")
    args = parser.parse_args()
    if not args.input.is_file():
        print(f"ERROR: input Markdown file does not exist: {args.input}", file=sys.stderr)
        return 2
    try:
        render(args.input, args.output, args)
    except Exception as exc:
        print(f"ERROR: could not render audit PDF: {exc}", file=sys.stderr)
        return 1
    print(f"created={args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
