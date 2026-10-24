---
name: design-uiux
description: Design app screens, flows, landing pages, and dashboards that hold up next to the best shipped products. Use for any UI/UX design, redesign, de-slop, options to choose from, or "show me via artifact" request on mobile (Expo/iOS/Android) or web (Next.js). Shows options on the Design artifact before any code; hands builds to frontend-*-engineering and reviews to the auditor.
---

# Design UIUX

Design is a loop with James, not a document. Read what the product already
is, find out how the best products solve the same job, show distinct options
on a canvas, let James pick, refine the pick to final quality, and only then
plan the build. This skill never edits product code: builds go to
`frontend-mobile-engineering` or `frontend-web-engineering`, and an
independent review goes to the `auditor` agent.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

## Defaults a project can override

- **Canvas:** the Artifact tool's **Design** type (run `quickstart` with
  intent `design`). Never an HTML page, a doc, or Figma unless James asks for
  one. Without the Artifact tool, describe each option in enough detail to
  build it and say the canvas was unavailable.
- **Artboards:** real sizes. Mobile 390×844 (iPhone), plus 375 wide when
  content is tight. Web 1440 desktop and 390 mobile; add 768 when the layout
  changes there.
- **Stack:** mobile is Expo / React Native, iOS-first with Android parity;
  web is Next.js with shadcn/ui and Framer Motion. Design within what the
  stack can render natively.
- **Project truth beats this skill.** A project's design docs (for example
  `design/*.md`, `docs/uiux.md`, `DESIGN_TOKENS`, `ART_DIRECTION`), tokens,
  and shipped components override every default here, including the slop
  tells.

## The loop

### 1. Read the product before drawing

Read the project's design docs and tokens, the PRDs, design logs, and code
comments that record past decisions, then the shipped screens and components
nearest to the request. Note the signature: type, color roles,
radii, surfaces, icon set, avatar and card shapes, motion tokens. Every
option is built from these parts. Rebuild real components faithfully: same
mask, path, radius, and spacing. Never approximate one, and never invent a
new component, color, or radius to make a mockup work. If something new is
truly needed, mark it as new and say why. An option that reverses a
documented decision must name the decision and argue for the change.

State in two or three lines: the user and their job, what success looks
like, and whether this request preserves the visual language or overhauls it.

### 2. Size the request

- **Small fix** (one inconsistency, spacing, radius, a label): sweep every
  screen and sub-screen the request names, and every shared component they
  render, and list each instance with its file and value. Fix values, not
  structure: if the real cause is structural, say so in one line and leave
  it for James to schedule. Show current and fixed side by side on the
  canvas. One proposal, no options, no research. Then wait.
- **Screen or flow redesign:** the full loop.
- **New or creative feature** (gamification, onboarding, a signature moment):
  the full loop with research weighted heavily.
- **Motion:** only after the static design is locked. Then use
  [motion and gesture](references/motion-and-gesture.md).

### 3. Research with a question

Before a redesign or creative work, write the question the references must
answer ("how do the best journaling apps show a streak without guilt?"),
then study a handful of shipped products that answer it, outside the
category first. Convergence across them is a convention; keep it.
Divergence is a choice; name it. Stop when new references stop changing the
answer. Method and how to turn references into rules:
[research and direction](references/research-and-direction.md).

### 4. Show two to four distinct options

Put every option on the Design canvas, labelled A, B, C, side by side, at
real sizes, with real content from the product (real names, counts, copy,
photos, and ID or code formats taken from the code or fixtures), not lorem,
placeholder boxes, or invented formats. Options must differ in idea, such as
structure, focal point, or interaction model, not just in color or spacing.
When James asks for "entire redesign options", at least one option must
rethink the structure. Each option gets one line on its idea and its
trade-off. When the request is about a flow (onboarding, sign-in, a
wizard), each option includes its navigation map: the steps, what kind of
screen each is, and what back does. End with a recommendation and why. Then **stop and wait for the
pick**. Do not build, and do not polish all of them.

Final quality from the first round: real type, color, imagery, and states.
A wireframe is only acceptable when James asks for one.

### 5. Refine the pick

Apply James's feedback to the chosen option only. Add the states the flow
can reach (empty, loading, error, long content, first use versus repeat use)
and the navigation map when there is more than one screen. Before each
showing, run [slop and consistency](references/slop-and-consistency.md),
then compare side by side with the strongest reference. Stop when it is at
least as good. Otherwise, name the gap and iterate.

### 6. Lock, then plan the build

When James approves, write a short implementation plan: the screens and
states, the components to reuse (by file path) and the few to add, the
tokens, the navigation and back behavior, the motion spec if any, and the
open questions. Hand it to the engineering skill. Do not edit product code
from this skill.

## Surface guidance

Load only what the request needs.

| Surface | Load |
| --- | --- |
| Mobile app | [mobile principles](references/mobile-principles.md), [mobile patterns](references/mobile-patterns.md) (navigation grammar, one-way doors, sheets versus routes, feedback) |
| Web app (settings, forms, lists, detail) | [web principles](references/web-principles.md), [web patterns](references/web-patterns.md) |
| Dashboard or admin | [dashboard data](references/dashboard-data.md), [dashboard interaction](references/dashboard-interaction.md) |
| Landing page | [landing message](references/landing-message.md), [landing visual](references/landing-visual.md) |
| Transitions, gestures, micro-interactions | [motion and gesture](references/motion-and-gesture.md) |
| Any review before showing or handing off | [critique and proof](references/critique-and-proof.md) |

## Rules that hold everywhere

- **Flow before pixels.** For multi-screen work, map entry, primary action,
  result, and next step. For each screen, say whether it is a push, a
  replace, a modal, a sheet, or a tab root, and what back does from it. Ask
  for sign-in, permissions, or payment only at the action that needs them,
  never up front.
- **Content shapes the container.** Use a list for scan-and-act work, a
  timeline for events over time, a table for comparison, and a chart only
  when it answers a named question. Do not force everything into cards.
- **One focal point and one primary action per screen.** Group with
  whitespace and surface tone before borders or shadows.
- **Explicit beats clever.** Core actions are visible and labelled, never
  hover-only, gesture-only, or behind an unlabelled icon.
- **Native fidelity on mobile.** Use platform controls, the platform symbol
  set, sheets with detents, large titles where the app uses them, and system
  back. Breaking a platform convention is a choice you must justify.
- **Motion earns its place.** Something seen 100 times a day gets the
  platform default or nothing. Delight is for rare moments.
- **Never fabricate.** No invented metrics, testimonials, reviews, or claims.
  Use the product's real content, or mark a placeholder as one.

## Changing this skill

Run the cases in [the regression set](evals/design-uiux-regression.md)
against the previous version before keeping a change. Older targeted cases:
[direction](evals/direction-regression.md) and
[mobile and motion](evals/mobile-motion-regression.md).
