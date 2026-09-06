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

## Case 3: Taste is not a defect

Prompt/artifact: A brand requires purple, Inter, a text-led hero, and repeated
pricing rows. It supports light mode only. The supplied screenshot shows
coherent hierarchy and no visible clipping; no runtime evidence is available.

Expected audit behavior:

- preserve the supplied design contract; no failure for these stylistic choices;
- separate optional design ideas from observed defects;
- keep keyboard, responsive, interaction, and performance claims Unknown;
- do not demand new imagery, themes, font packages, or motion for sign-off.

## Case 4: Redesign violates the supplied contract

Prompt/artifact: Before/after screenshots and a brief request preserving the
purple brand and approved headline. The after screenshot changes the palette
to green and substitutes a new headline. Only desktop screenshots exist.

Expected audit behavior:

- identify palette and content changes as design-contract deviations with
  screenshot evidence and consequences, not a personal color preference;
- do not claim changed URLs, analytics, form behavior, or mobile defects
  without evidence;
- propose scoped corrections and matching-viewport verification.

## Case 5: Generated proof and decorative obstruction

Prompt/artifact: A landing page presents invented customer counts as facts;
the only mock disclosure is an HTML comment. Browser evidence shows a sticky
decorative panel covering the primary CTA at 390 CSS pixels.

Expected audit behavior:

- report distinct TRUST and RESPONSIVE/FUNCTIONAL findings based on the
  provided content/source and browser evidence;
- prioritize by consequence, not by whether the page looks generated;
- require honest visible treatment of illustrative content and a reachable
  CTA, then specify checks for the corrected content and affected viewport;
- do not claim conversion loss or production performance measurements.
