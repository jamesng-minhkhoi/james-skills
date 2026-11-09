---
name: design-uiux
description: Design app screens, flows, landing pages, and dashboards that hold up next to the best shipped products. Use for any UI/UX design, redesign, de-slop, options to choose from, or "show me via artifact" request on mobile (Expo/iOS/Android) or web (Next.js). Shows options on the Design artifact before any code; hands builds to frontend-*-engineering and reviews to the auditor.
---

# Design UIUX

Design is a loop with James, not a document. Read what the product already
is, find out how the best products solve the same job, show distinct options
on a canvas, let James pick, refine the pick to final quality, then plan the
build and the rules it must keep. This skill never edits product code: builds
go to `frontend-mobile-engineering` or `frontend-web-engineering`, and an
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
documented decision must name the decision and argue for the change. Where
the docs keep a rule table, cite its IDs.

State in two or three lines: the user and their job, what success looks
like, and whether this request preserves the visual language or overhauls it.

### 2. Size the request

- **Small fix** (one inconsistency, spacing, radius, a label): sweep every
  screen and sub-screen the request names, and every shared component they
  render, and list each instance with its file and value. Fix values, not
  structure: if the real cause is structural, say so in one line and leave
  it for James to schedule. Show current and fixed side by side on the
  canvas. One proposal, no options, no research. Then wait.
- **Screen or flow redesign:** run the [twelve gates](references/critique-and-proof.md)
  first. The table is the brief: every gate answered, evidence beside every
  verdict, `NOT_RUN` where nothing was rendered. Then the full loop.
- **New or creative feature** (gamification, onboarding, a signature moment):
  the full loop with research weighted heavily. When the idea is a signature
  moment — animated hero, scroll story, 3D or shader-backed scene — open the
  [creative catalog](references/creative-catalog.md) after research; its
  honesty and frequency gates apply before any technique is proposed.
- **Motion refinements** (transitions, micro-interactions on an existing
  design): only after the static design is locked. A request that is a
  signature moment (the creative feature bullet above) owns its motion design
  at the option stage and is not stalled waiting for a lock.

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
and the navigation map when there is more than one screen.

Before drawing, list the status states the current screen shows (still
processing, failed, unsupported, offline) and put each on a board with its
shipped string. A round focused on interaction or gestures still carries
them, because a round that leaves them out reads as approval to drop them.

Before drawing, also list every destination (details, delete, share, close)
with each trigger that reaches it. Keep one standing on-screen control per
destination and at most one custom gesture. These do not count against the
limit: system gestures (edge back), the same motion gated at a second
boundary, a press-and-hold menu (a shortcut that mirrors items reachable
elsewhere), and a grabber on the control itself (the drag affordance of that
one control, not a second control). A destructive action
has exactly one visible home, meaning a place reachable without a gesture,
menu items included. Merging parts of two options is where this breaks most,
because each option brings its own way in.

Before each showing, run [slop and consistency](references/slop-and-consistency.md);
from the second showing on, also build the
[rendered proof](references/rendered-proof.md) sheet at the project's real
widths. Then compare side by side with the strongest reference. Stop when it
is at least as good. Otherwise, name the gap and iterate.

A round is the boards shown since James's last reply. When he rejects it,
remove its boards in the next publish, keeping only references he named; when
he picks one, keep it and remove the others once he moves on (older versions
stay recoverable from the artifact's history). The Design artifact's own note
to skip verification covers publishing only: a canvas board is a drawing, so
its proof stays `declared`. Before the second showing run the real component
per [rendered proof](references/rendered-proof.md), or record the `rendered`
rung as not reached and its gates `NOT_RUN`. Overlaps and uneven padding
show up only when rendered.

Re-run the same twelve-gate table on the pick. A verdict that regressed is a
new finding, even if the screen looks better.

Check the pick against every established rule it touches. A rule the pick
breaks is a finding with its ID, not a taste note; either fix it or name the
decision being reversed.

### 6. Lock, then plan the build

When James approves, write a short implementation plan: the screens and
states, the components to reuse (by file path) and the few to add, the
tokens, the navigation and back behavior, the motion spec if any, and the
open questions. Add the handoff rules from
[critique and proof](references/critique-and-proof.md), each with its ID and
how the build checks it, plus the hand-over block from
[rendered proof](references/rendered-proof.md). Hand it to the
engineering skill. Do not edit product code from this skill.

## Surface guidance

Load only what the request needs.

| Surface | Load |
| --- | --- |
| Mobile app | [mobile principles](references/mobile-principles.md), [mobile patterns](references/mobile-patterns.md) (navigation grammar, one-way doors, sheets versus routes, feedback) |
| Web app (settings, forms, lists, detail) | [web principles](references/web-principles.md), [web patterns](references/web-patterns.md) |
| Dashboard or admin | [dashboard data](references/dashboard-data.md), [dashboard interaction](references/dashboard-interaction.md) |
| Landing page | [landing message](references/landing-message.md), [landing visual](references/landing-visual.md) |
| Signature moment (animated hero, scroll story, kinetic type, 3D canvas, shader field) | [creative catalog](references/creative-catalog.md), then only the module topics it routes to |
| Transitions, gestures, micro-interactions | [motion and gesture](references/motion-and-gesture.md) |
| A component opens, closes, confirms, loads, or changes text (dropdown, modal, toast, tooltip, tabs, toggle, success, error, skeleton, AI status) | [transitions catalogue](references/transitions-catalog.md): the moment → transitions.dev slug map with a check per row; cite the slug in the handoff, never paste code |
| A number the user changes on screen (total, price, balance, filtered stat) | [digit pop-in](references/library/signature-motion/06-digit-pop-in.md): the swap with fixed drivers and frame proof; live or polled numbers and status words route through its decision table |
| Surface feels flat, empty, or needs a background (any surface) | [background textures](references/background-textures.md): 22 options, each with its job, cheap build, and failure mode |
| Redesign diagnosis, or any review before showing or handing off | [critique and proof](references/critique-and-proof.md) (the twelve gates) |

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
- **Gesture-first, with a visible and an assistive path.** On mobile, enter
  values and act on rows by drag, swipe, or scrub, because thumbs prefer them
  to tap-steppers and segmented tabs in a sheet. Each gesture also has a
  visible control (menu, detail, or labelled icon) and an assistive path
  (adjustable value or accessibility actions). A documented project control
  wins over this rule (see "Project truth" above); otherwise this rule is the
  stated reason for departing from platform controls, and the custom control
  (ruler, ring, wheel) is marked new per step 1. Patterns:
  [touch-first input](references/mobile-patterns.md#touch-first-input-and-actions).
  A screen that gets any custom gesture gets a
  [gesture map](references/mobile-patterns.md#gesture-map-before-gesture-boards)
  before its boards, because a gesture whose motion the content already uses
  (swipe up on a list that scrolls) never fires or hijacks the content.
- **Say whose it is.** Subject, glance-sheet, and delete placement rules:
  [mobile patterns](references/mobile-patterns.md#glance-sheet-dedicated-screen).
- **Pictures carry the meaning; text is the last resort.** A hero is an
  illustration or a data picture, not a title, a grey subtitle, and a number
  saying the same thing. Details:
  [slop and consistency](references/slop-and-consistency.md).
- **Native fidelity on mobile.** Use platform controls, the platform symbol
  set, sheets with detents, large titles where the app uses them, and system
  back. Breaking a platform convention is a choice you must justify.
- **Motion earns its place.** Something seen 100 times a day gets the
  platform default or nothing. Delight is for rare moments.
- **Never fabricate.** No invented metrics, testimonials, reviews, or claims.
  Use the product's real content, or mark a placeholder as one.
- **Every correction becomes a rule.** Write it into the project's rule
  table with its reason. Rewrite the rule it changes; never append a
  contradiction or a log line.

## Changing this skill

Change from a failure, not a preference. A repeated correction belongs in the
project's design doc first; only what holds across projects belongs here.

Run the cases in [the regression set](evals/design-uiux-regression.md)
against the previous version before keeping a change. Older targeted cases:
[direction](evals/direction-regression.md) and
[mobile and motion](evals/mobile-motion-regression.md).
