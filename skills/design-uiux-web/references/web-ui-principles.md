# Web UI principles

Use these as decision principles, not a visual style mandate. Status values in
a critique should be Strong, Concern, Critical, Unknown, or Not applicable,
with evidence and user impact.

## Contents

- [Explicitness and progressive disclosure](#explicitness-and-progressive-disclosure)
- [NN/G interaction principles](#nng-interaction-principles)
- [Hierarchy, scanability, and rhythm](#hierarchy-scanability-and-rhythm)
- [Signifiers and system feedback](#signifiers-and-system-feedback)
- [User intent, conventions, and content](#user-intent-conventions-and-content)
- [Semantic color and themes](#semantic-color-and-themes)
- [Component consistency and interaction completeness](#component-consistency-and-interaction-completeness)
- [Motion](#motion)
- [Sources](#sources)

## Explicitness and progressive disclosure

Use a spectrum:

Visible → Directly revealed → Contextual → Deferred → Advanced/hidden

Visibility should increase with frequency, consequence, uncertainty, and need
for orientation. Hidden controls need a discoverable trigger, familiar
placement, and a visible or accessible equivalent for core actions. Sequence
complexity through context, not a one-time wall of onboarding text.

## NN/G interaction principles

Apply the 10 heuristics to the actual task:

- visibility of system status;
- match between system and real world;
- user control and freedom;
- consistency and standards;
- error prevention;
- recognition rather than recall;
- flexibility and efficiency of use;
- aesthetic and minimalist design;
- error recognition, diagnosis, and recovery;
- help and documentation.

Treat these as questions. Where status is pending, make it visible. Where an
action is consequential, provide control, prevention, confirmation, undo, or
recovery. Where a term or icon is unfamiliar, use the user's language and
contextual help.

## Hierarchy, scanability, and rhythm

Web users scan. Use meaningful headings, front-loaded labels, grouping,
whitespace, contrast, and predictable alignment to create information scent.
Do not interpret the F-pattern as a layout target; use strong cues to guide
attention toward the content and action that matter.

Captivating design uses structure, rhythm, restraint, and a small amount of
intentional surprise. Complexity is justified only when it improves
understanding, feedback, or personality.

## Signifiers and system feedback

Controls should look actionable and communicate their state. Check hover,
focus-visible, pressed, selected, disabled, loading, success, error, empty,
no-results, permission, and offline states. Feedback should appear near the
user's attention and persist according to consequence.

## User intent, conventions, and content

Start with what the user is trying to accomplish, not what looks impressive in
a reference image. Respect familiar web conventions for navigation, reading
order, controls, and browser behavior unless a deviation clearly improves the
task and is explained by the context. Content structure is part of the design:
headings, labels, examples, status wording, and next-step copy should make the
interface understandable before visual effects are added.

When a long result set or feed is involved, choose pagination, load more, or
infinite scroll based on the user's need for position, comparison, sharing,
footer access, and control. Do not use infinite scroll by default.

## Semantic color and themes

Treat color as a communication system, not a decoration budget:

1. neutral foundation and surface layers;
2. functional accents with state ramps for links, focus, selection, and action;
3. semantic colors for success, warning, danger, info, and data categories;
4. light/dark theme adaptations that preserve meaning and contrast.

The 60-30-10 rule is an optional visual heuristic, not a product-UI gate. Do
not force a palette into those percentages or use color as the only status
signal. Prefer perceptually consistent ramps such as OKLCH when practical,
then test contrast, color-vision differences, disabled states, charts, and
dark mode. Reserve saturated color for meaning or emphasis.

## Component consistency and interaction completeness

Consistency means shared behavior and meaning, not identical decoration. A
component family should define default, hover, focus-visible, pressed,
selected, disabled, pending, success, error, and reduced-motion behavior as
needed. Every reveal or animation needs a purpose, trigger, timing, easing,
dismissal, keyboard path, touch path, and recovery path.

AI-specific patterns are conditional. Prompt composers, attachment previews,
history, memory controls, inline editing, progress transparency, and
uncertainty cues belong in products whose user job involves AI. They are not a
generic quality signal and should not be imported into ordinary SaaS UI.

## Motion

Use motion to explain reveal, continuity, hierarchy, progress, or result. Check
frequency, interruption, performance, and reduced motion. A delightful
transition can guide attention; decorative movement competing with reading or
core work is a defect.

## Sources

Kole Jain:

- [Resources](https://www.kolejain.com/resources)
- [Every UI/UX Concept Explained](https://www.youtube.com/watch?v=EcbgbKtOELY)
- [The Formula Behind Truly Captivating UI Sections](https://sozai.app/transcript/formula-truly-captivating-ui-sections/)
- [4 UI Design Hacks to Kill Boring Designs](https://sozai.app/transcript/ui-design-hacks-kill-boring-designs/)
- [5 SaaS UI/UX Mistakes That Scream You Vibe Code](https://sozai.app/transcript/saas-ui-ux-mistakes-vibe-code/)

NN/G:

- [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/)
- [F-Shaped Reading Pattern](https://www.nngroup.com/articles/f-shaped-pattern-reading-web-content/)
- [Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)
- [Animation for Attention and Comprehension](https://www.nngroup.com/articles/animation-usability/)
- [Animated Dashboard Sidebar Tutorial](https://sozai.app/transcript/animated-dashboard-sidebar-tutorial-figma/)
- [11 Micro Animations](https://sozai.app/transcript/micro-animations-level-up-ui-free-figma/)
- [7 UI/UX Mistakes](https://sozai.app/transcript/ui-ux-mistakes-beginner/)
- [How to Think Like a Genius UI/UX Designer](https://sozai.app/transcript/think-like-genius-ui-ux-designer/)
- [7 UI Components for AI Startups](https://sozai.app/transcript/7-ui-components-design-unicorn-ai/)
- [7 Color Mistakes](https://sozai.app/transcript/7-color-mistakes-ruin-ui-designs/)
- [Why 60-30-10 Is Ruining Product UI](https://sozai.app/transcript/60-30-10-rule-ruining-ui-designs/)
