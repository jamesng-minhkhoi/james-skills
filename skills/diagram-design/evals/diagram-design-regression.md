# Diagram Design Regression Eval

## Trigger Prompts
1. "Draw an editorial system architecture diagram for our Next.js + FastAPI + Postgres + Redis stack and export it as HTML and PNG."
2. "Redraw this messy `.drawio` / Mermaid sequence diagram into a clean warm-paper publication figure for our docs and X launch post."
3. "Create a 2x2 quadrant positioning chart and a medallion Bronze-Silver-Gold data pipeline diagram matching our brand palette."

## Expected Behavior
- Loads `skills/diagram-design/SKILL.md`, `references/svg-primitives-and-checklist.md`, and the matching `references/type-*.md`.
- Enforces the 4px grid, max 2 coral focal elements, open chevron arrowheads, arrows drawn before boxes, and orthogonal `r=8` right-angle connectors with 6–10px masked arrow-label gaps.
- Verifies output with `python3 skills/diagram-design/scripts/self_check.py` and `python3 skills/diagram-design/scripts/verify-geometry.py`.
