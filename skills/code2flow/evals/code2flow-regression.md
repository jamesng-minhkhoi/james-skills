# Code2Flow Regression Eval

## Trigger Prompts
1. "Scan this Next.js App Router repository with code2flow, generate the Mermaid user-flow diagram, and list all high-severity UX gaps."
2. "Audit our Expo Router / SwiftUI navigation stack for dead-end screens, orphan routes, missing error boundaries, and unguarded destructive actions."
3. "Compare `docs/prd.md` against our codebase routes and transitions using code2flow and report every PRD-vs-code drift."

## Expected Behavior
- Loads `skills/code2flow/SKILL.md` and runs `python3 skills/code2flow/scripts/code2flow_audit.py <repo>` (or `npx design-os-code2flow` for full screenshot canvas / PRD story validation).
- Extracts all Route Screens, State Screens (modals/tabs/drawers), and Navigation Edges with `file:line` evidence.
- Audits all 11 structural UX heuristics (`H01_BROKEN_LINK` through `H11_DEEP_CLICK_DEPTH`) without modifying target application source code.
