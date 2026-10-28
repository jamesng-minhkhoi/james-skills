# Design UIUX regression cases

Real requests from James's projects, kept close to their original wording.
Use them when changing this skill: run the previous and candidate versions on
the same case with hooks off, label the outputs X and Y at random, and have a
judge score both against the rubric, then repeat with the order swapped.
Cases read the real repositories but must not edit them or publish anything.

## Cases

1. **Slop redesign, mobile** — repo `petio/petio-mobile`. "improve the design
   of the memories grid view please. it looks like AI slop. show me via
   artifact"
2. **Options requested, mobile** — repo `home_service_mvp/mobile`. "improve
   uiux of the job request screen please. propose uiux and i will choose from
   your options"
3. **Transitions, mobile** — repo `petio/petio-mobile`. "our screen
   transitions feel like AI slop. how could we improve all to make our app
   feel studio crafted / production ready? show me via artifact"
4. **Creative feature** — repo `petio/petio-mobile`. "show me streak design. i
   want to improve gamify for the app. make it playful but still clean like
   Apple. show me via artifact"
5. **Flow with sign-in** — repo `petio/petio-mobile`. "I want login screen out
   of onboarding flow and only requires login when needed. how should
   onboarding look? show me via artifact"
6. **Small fix** — repo `petio/petio-mobile`. "help me check and fix setting
   screen the border radius not consistent, show me via artifact first"
7. **Landing page** — repo `home_service_mvp/landingpage`. "show me
   landingpage design via design artifact. I want full bleed photo and clean
   design not AI slop. take time to research rules to de-slop"
8. **Dashboard** — repo `cafe-web-next`. "the admin orders page feels like a
   spreadsheet. redesign it to be calm and scannable, show me options"
9. **Handoff as checkable rules** — repo `ugc/ugc`. "the creator info screen is
   approved. hand it to engineering." Expected: the plan above plus a
   handoff table that reuses the project's rule IDs and status, names how
   each rule is checked (static, rendered, manual), records existing
   violations as a shrink-only baseline, and marks what a static design
   cannot prove as `NOT_RUN` gates for engineering. No code.
10. **Correction becomes a rule** — repo `ugc/ugc`. "no scroll bar allow" on
    a filter row. Expected: rewrite the project's rule (the row fits the
    phone width; rarer cuts move to the bar's pull-down), apply it to the
    current options, and update the rule's reason. No separate log or
    appended contradiction. Promote it here only if it holds beyond this
    project.
11. **Deterministic diagnosis** — repo `cafe-web-next`. "the admin phone UI
    has a lot of issues. find what is wrong before redesigning it." Expected:
    the twelve-gate table before options, one verdict per gate with file:line
    evidence; `NOT_RUN` for rendered and device gates because no browser was
    run; findings sorted priority then gate. It finds the row body that looks
    pressed but only the title opens (`components/admin/mobile/mobile-list.tsx`),
    the duplicate create action in the toolbar and empty state on the mobile
    list screens, the row's own action repeated in its ⋯ sheet, the competing
    filled actions on an empty ingredients screen, and the raw palette and
    sub-12px map labels. No options before the table, and no `PASS` from taste.
12. **Rendered proof before a second showing** — repo `ugc/ugc`. "refine
    option B with my notes and show it to me again." Expected: rebuilds the
    picked option, then renders the real component (not the design canvas) at
    the widths the product ships, fills `L1`–`L5` with measured values, and
    states whether an independent critic scored the twelve gates at this
    showing or is deferred to handoff and why. Anything not rendered is
    `NOT_RUN`, never a pass.

## Rubric

Score each 0–2. The case number in brackets marks where a criterion matters
most; elsewhere score it only when it applies.

| Criterion | 2 means |
| --- | --- |
| Artifact | Proposes the Design artifact (canvas artboards at real device or viewport sizes); never an HTML page, Figma, or a doc; no code before approval |
| Options | Two to four genuinely different directions with a recommendation, then waits for the pick (1, 2, 4, 7, 8); a single scoped fix for a small fix (6) |
| Grounding | Reads the project's design docs, tokens, and real components first and rebuilds them faithfully; does not invent a new visual language or new components |
| Diagnosis | A redesign starts with the twelve-gate table, evidence beside every verdict, `NOT_RUN` where nothing was rendered, and findings sorted priority then gate; no `PASS` from taste (11) |
| Rendered proof | Before a repeat showing and at handoff, the sheet renders the real component at the shipped widths, `L1`–`L5` carry measured values, and `L6`–`L10` name what a fresh critic saw or `NOT_RUN`; a canvas screenshot is never offered as a render (12) |
| Research | Gathers references with a named question before designing creative or best-in-class work (3, 4, 7) |
| Slop | Avoids the tells James has named (shadows, borders, dividers, outlined wrappers, floating animation, decorative gradients, dashes, cluttered chips, stock-looking photos) and runs a consistency check |
| Fidelity | Final-quality design direction with real content and states, not a wireframe; static design locked before motion (3, 4) |
| Flow | Navigation map with what each step is and what back does; login only where an action needs it (5) |
| Proportion | Depth matches the request; no padding, no ceremony on a small fix |
| Handoff | The handoff carries rule IDs, status, and how each is checked, splitting static from rendered and manual; existing debt is a baseline, not a pass; unprovable behavior is a `NOT_RUN` gate (9) |
| Vocabulary | Names the highest proof rung reached and never calls an unobserved state pass |

## Must not have

A candidate fails regardless of rubric score if it contains any of these:

- an HTML page, Figma file, or doc in place of the Design artifact;
- product code before the direction is approved;
- one option when options were requested, or a single option dressed up as a
  choice;
- invented tokens, components, or type when the repository already has them;
- a wireframe or placeholder content presented as the final direction;
- any named slop tell, or a consistency check claimed without naming what was
  checked;
- a prose-only handoff when the project keeps a rule table or guard suite;
- a redesign critique with no gate verdicts, or a `PASS` on a rendered gate
  without a render;
- a canvas screenshot, thumbnail, or artboard export offered as rendered proof;
- a finding with no file:line evidence or measurement, or options offered
  before the diagnosis table;
- a new rule baselined, or an existing baseline raised, to make a check pass;
- a second rule minted where the project's doc already states one;
- a correction recorded only in chat, or appended as a contradiction.

Accept a candidate only when its total is higher, it wins on Artifact,
Options, and Grounding in most cases, and it does not lose case 6.
