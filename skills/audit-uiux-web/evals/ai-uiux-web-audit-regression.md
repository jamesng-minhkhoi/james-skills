# AI UIUX web audit regression cases

Use these fixtures when changing the web audit skill. They protect against
visual-only audits of AI-generated or template-heavy product interfaces.

## Case 1: Static SaaS shell

Prompt/artifact: A generated SaaS dashboard has colorful cards and polished
copy, but buttons are disconnected, desktop columns collapse at tablet width,
and loading/empty/error states are absent.

Expected audit behavior:

- use the forensic overlay and browser proof checklist;
- verify direct URL, refresh, back/forward, keyboard/focus, responsive
  recomposition, and control outcomes where runtime access exists;
- report separate STRUCTURE/RESPONSIVE/FUNCTIONAL/STATE findings with proof
  level, impact, confidence, verification method, and P0–P3 priority;
- route design remediation to the appropriate UIUX design skill and code
  remediation to `frontend-web-engineering`.

## Case 2: One desktop screenshot

Prompt: “This page looks premium in one screenshot; sign off the web UX.”

Expected audit behavior:

- keep responsive, browser-history, keyboard, screen-reader, reduced-motion,
  loading, failure, performance, and provider claims Unknown unless observed;
- return coverage, reality check, findings, owners, and exact next browser or
  automated checks instead of certifying the page.
