# Web UX principles

Use these as questions applied to the user's task, not as a checklist detached
from context. Rate each relevant principle Strong, Concern, Critical, Unknown,
or Not applicable, with evidence and user impact.

## Explicitness and progressive disclosure

Use the visibility spectrum:

`Visible → Directly revealed → Contextual → Deferred → Advanced/hidden`

Increase visibility with frequency, consequence, uncertainty, and orientation
need. Keep primary actions, current status, cost, permission effects,
irreversible consequences, and recovery visible. A hidden control needs a
discoverable trigger, familiar placement, preserved context, and an accessible
equivalent for core actions.

Ask:

- Can a first-time user identify what this page is for and what to do next?
- Does disclosure reduce overload without hiding decision-critical information?
- Are hover, tooltip, icon-only, or overflow actions available to keyboard,
  touch, zoom, and assistive-technology users?

## Usability heuristics applied to web tasks

- **System status:** loading, saving, pending, success, stale, failure, and
  background work are visible near the user's attention.
- **Real-world match:** domain language, units, dates, ordering, and workflow
  match the user's mental model.
- **User control:** back, cancel, close, escape, undo, retry, pause, and
  unsaved-change recovery work as expected.
- **Consistency and standards:** browser conventions, controls, URLs,
  headings, navigation, and component states remain predictable.
- **Error prevention:** constraints, defaults, previews, confirmations, and
  duplicate-submit protection prevent costly mistakes.
- **Recognition over recall:** labels, selected state, context, history, and
  visible options reduce memory burden.
- **Flexibility:** shortcuts, search, filters, keyboard paths, and efficient
  repeat actions help experienced users without confusing new users.
- **Minimalist signal-to-noise:** every surface, color, icon, motion, and label
  earns its place through comprehension, feedback, orientation, or personality.
- **Error recovery:** messages identify what happened, what is affected, and
  how to fix or retry without losing work.
- **Help and documentation:** unfamiliar concepts have contextual help without
  replacing clear primary UI.

## Hierarchy, content, and structure

Web users scan. Check heading order, information scent, alignment, whitespace,
content density, primary-action prominence, and predictable grouping. Do not
use the F-pattern as a layout target; use strong cues and task order.

Choose list, table, grouped list, detail, editor, split view, tabs, dialog,
sheet, pagination, load more, or infinite scroll from the user's need for
comparison, position, sharing, control, and completion. Do not force every
surface into cards, KPI tiles, a hero, or a generic dashboard grid.

## Responsive re-composition

Responsive quality is a change in composition, not a shrunken desktop. Check:

- navigation collapse and orientation;
- reading order and primary-action placement;
- table/list transformation and horizontal overflow;
- density, truncation, wrapping, and long content;
- dialogs, sheets, menus, and sticky/fixed regions;
- keyboard open, touch input, hover absence, and focus visibility;
- zoom, large text, localization, RTL, and narrow intermediate widths.

## Accessibility and inclusive interaction

Check semantic landmarks, one useful page heading, logical heading hierarchy,
native controls where possible, accessible names, labels, descriptions,
validation association, error announcements, focus-visible styling, focus
order, focus return, keyboard access, modal containment, contrast, zoom,
non-color status, reduced motion, and target operability. Do not treat an
automated accessibility score as proof of a usable journey.

## Semantic color and visual restraint

Treat color as a communication system:

1. neutral foundation and surface layers;
2. functional accents for actions, links, selection, and focus;
3. semantic ramps for success, warning, danger, and information;
4. data colors only when categories need them and a non-color explanation exists.

Check whether one dominant accent is enough, whether parallel cards are being
color-coded without meaning, whether raw colors drift outside tokens, and
whether contrast and dark mode preserve meaning. Saturation is not hierarchy by
itself. Do not use 60-30-10 as a pass/fail rule.

## Motion and feedback

Motion should explain reveal, continuity, hierarchy, progress, or result. When
motion is requested, verify the trigger, purpose, timing/easing, interruption,
keyboard/touch equivalent, reduced-motion alternative, and observed result.
Hover-only movement or a page-load flourish does not satisfy a requirement for
meaningful product motion. Check layout shift, focus continuity, and whether
motion delays reading or work.

## Trust and dark patterns

Check costs, defaults, consent, subscriptions, permissions, destructive actions,
cancellation, urgency, hidden consequences, and recovery. Flag visual or copy
choices that obscure an option, pressure a decision, or make cancellation
harder than commitment.

## Sources

- [Nielsen Norman Group: 10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- [Nielsen Norman Group: Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- [Nielsen Norman Group: Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/)
- [Nielsen Norman Group: Visual Hierarchy](https://www.nngroup.com/articles/visual-hierarchy-ux-definition/)
- [Nielsen Norman Group: Animation for Attention and Comprehension](https://www.nngroup.com/articles/animation-usability/)
- [W3C: Web Content Accessibility Guidelines](https://www.w3.org/TR/WCAG22/)
