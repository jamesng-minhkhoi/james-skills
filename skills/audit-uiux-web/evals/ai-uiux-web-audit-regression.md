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
- use the shared vocabulary: name the highest proof rung, mark unobserved gates
  `NOT_RUN`/`UNKNOWN`, and give each finding a stable `F-web-<n>` ID.

## Case 6: Engineering-default option set

Prompt/artifact: An analytics dashboard offers exactly three selectable
ranges — today, 7 days, 14 days. Source inspection shows clean structure,
passing tests, and no visible defect.

Expected audit behavior:

- enumerate the domain's natural ranges from the operator's job first
  (yesterday, this week, this month, last month, month-to-date), then compare;
- report missing natural ranges and the arbitrary 14-day endpoint as an
  IA/STRUCTURE finding with user impact and a stable `F-web-<n>` ID — a
  business cannot ask its month-to-date question;
- not pass the screen on command-bar structure while ignoring what the bar
  lets the user choose;
- not demand specific ranges when the design contract names them; the
  finding is the absent comparison to the domain, not the exact count 3.

## Case 7: Phone composition judged only as re-composition

Prompt/artifact: A responsive admin renders a phone composition that re-stacks
desktop content into full-width bordered cards with a full-width floating
segmented control. Every element works; nothing is clipped.

Expected audit behavior:

- load the `mobile-native` skill and the repository's native-pattern
  documentation before rating the phone composition;
- compare against native conventions (inset grouped lists, intrinsic-width
  segmented controls, large-title treatment, safe areas, 44-point targets)
  and report observable deviations as findings with impact and proof level —
  not as taste;
- keep unobserved platform behavior (momentum, scroll, keyboard open) Unknown;
- not mark responsive coverage complete because elements re-compose without
  breakage.

## Case 8: Design contract names the option set

Prompt/artifact: An explicit design contract specifies the selectable ranges
today/7d/14d; structure, tests, and states are otherwise clean.

Expected audit behavior:

- perform the §4.2 domain comparison and record that the contract names the
  ranges — contract-conforming, no finding demanding yesterday or
  month-to-date;
- a missing-natural-options finding applies only when the contract is silent
  or the offered set violates the contract;
- not invent contract language the user never supplied.

## Case 9: Design contract specifies the phone composition

Prompt/artifact: A supplied design contract specifies full-width bordered
cards on the phone composition as the intended look.

Expected audit behavior:

- classify the native-pattern comparison result as contract-conforming or a
  design-contract deviation with consequences, per the file's rule — the
  classification must not be left to taste intuition;
- a generic-web-phone finding is reported as a design-contract deviation
  (with the trade-off stated), or not at all if the contract governs.

## Case 10: Native-pattern dependency unavailable

Prompt/artifact: An audit session cannot load the `mobile-native` skill, and
the repository carries no native-pattern documentation.

Expected audit behavior:

- proceed from native platform conventions alone and mark the gate `NOT_RUN`
  with the platform-convention comparison still performed;
- never silently skip the gate and never `PASS` it without comparison;
- say in the report that the named dependency was unavailable.

## Must not have

A report fails if it contains any of these:

- `PASS` or `READY` for a gate that was not observed;
- a proof label or verdict outside the shared ontology;
- a finding without a stable `F-web-<n>` ID;
- a mobile, keyboard, screen-reader, or performance claim inferred from a
  desktop screenshot;
- a phone composition rated without the native-pattern check applied, or a
  selectable option set passed without comparison to the domain's natural
  options;
- a demanded redesign where the supplied design contract is coherent and the
  only complaints are taste.
