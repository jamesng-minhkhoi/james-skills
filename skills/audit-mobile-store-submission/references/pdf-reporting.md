# Friendly PDF reporting

Use the PDF export after completing the Markdown audit. The PDF is a
communication artifact for non-technical stakeholders; the Markdown remains
the source of truth for editing and evidence.

## Render

```sh
python3 scripts/render-audit-pdf.py \
  path/to/audit.md \
  output/pdf/app-store-audit.pdf \
  --app-name "Example App" \
  --platform "Apple App Store + Google Play" \
  --verdict "Not ready" \
  --checked-at "2026-08-23"
```

Use the bundled Codex Python runtime when the system Python does not contain
ReportLab. Keep the Markdown beside the PDF so the evidence can be updated
without treating the PDF as the editable source.

## Content expectations

Before rendering, ensure the Markdown contains:

- separate Apple and Google verdicts;
- a short blocker summary before detailed findings;
- an evidence table with status and owner;
- exact build/device/portal context;
- open gates and next actions written in plain language;
- policy/source links that remain readable when printed.

The renderer supports headings, paragraphs, bullets, numbered lists,
blockquotes, code blocks, and GitHub-style pipe tables. Keep table cells short;
move long explanations into findings below the table.

## Visual QA

After creating the PDF, render it to PNG and inspect representative pages:

```sh
pdftoppm -png output/pdf/app-store-audit.pdf tmp/pdfs/app-store-audit
pdfinfo output/pdf/app-store-audit.pdf
```

Check the cover/header, first blocker table, a page containing a long table, and
the final page for clipped text, unreadable table cells, broken links, missing
page numbers, or orphaned headings. Do not claim the PDF is complete until the
latest rendering has been visually checked.
