---
description: Run scripts/lint-skills.sh to check skill size budgets, links, and ontology
---

Execute `./scripts/lint-skills.sh` in the workspace root.
Report:
1. Any skill exceeding word limit (<= 80 words) or line limit (<= 300 lines).
2. Any missing links to `_shared/ontology.md`.
3. Any skills missing behavior eval cases in `evals/`.
4. Suggest concrete trim recommendations for any failing skills.
