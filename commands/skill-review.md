---
description: Run a zero-context pre-ship review of changed skills or routing rules
---

Delegate to the `skill-reviewer` agent or apply its review methodology to the changed skill files:
$ARGUMENTS

Pre-ship checks:
1. Size budgets: description <= 80 words, SKILL.md <= 300 lines, ROUTING.md <= 40 lines.
2. Shared links: links to `../_shared/ontology.md`, no retired synonyms.
3. Eval coverage: at least one behavioral eval case in `evals/`.
4. Cold reader test: read without assuming author context. Flag ambiguous instructions, missing prerequisites, or untracked assumptions.
5. Findings returned with actionable recommendations before committing.
