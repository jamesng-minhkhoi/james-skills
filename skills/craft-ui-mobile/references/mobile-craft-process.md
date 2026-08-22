# Mobile craft process

This reference turns visual polish into a repeatable product-design process.
Use it for a new screen, redesign, or multi-state flow. For a tiny local fix,
apply only the relevant sections.

## The craft ladder

### 1. Intent before interface

Write one sentence:

> When [situation], [user] needs to [job] so they can [outcome].

Use that sentence to reject features and decoration that do not help the job.
Name the moment of value, not the database operation.

### 2. Flow before fidelity

Sketch the flow with the smallest useful set of screens and states. Look for
missing search, skip, save, back, no-results, and recovery paths. Include the
first-time and repeat-user path. A screen that looks complete but strands a
user after an error is not complete.

### 3. Content before containers

Gather realistic labels and records before choosing cards or columns. Test long
names, translated copy, missing values, timestamps, status combinations, and
the maximum practical item count. Let the data determine whether the UI wants a
list, timeline, grouped sections, chart, sheet, or detail view.

### 4. References before invention

Study a few real products with a similar task. Extract the pattern, not the
brand: placement, density, disclosure, feedback, and navigation behavior.
Record what is being borrowed and why. Do not copy a web pattern that depends
on hover, pointer precision, or desktop width into a touch-first mobile flow.

### 5. Wireframe before decoration

Build a low-fidelity structure with the primary action, content order, empty
space, and state placeholders. Check the first viewport at a glance. If the
flow is unclear in grayscale, color will only hide the problem.

### 6. System before one-off polish

Set or reuse the local rules for:

- type roles and readable line lengths;
- spacing rhythm and content alignment;
- semantic colors and contrast;
- icon family, size, stroke, and labeling;
- component shapes, touch areas, and state styles;
- elevation, borders, materials, and dark-mode behavior;
- motion durations, easing, haptics, and reduced-motion fallback.

Use project tokens. A reference designer's exact radius or spacing value is not
a universal rule; consistency with the product system and platform is the rule.

### 7. Subtract before adding

Run a removal pass:

- remove redundant arrows when the action is already obvious;
- remove borders and shadows that do not create meaningful grouping or depth;
- remove decorative gradients, glows, and strokes that compete with content;
- remove repeated labels or cards that add no decision value;
- remove a new component when an existing one can carry the change.

Then run an affordance pass: every remaining control should look actionable,
respond to touch, and communicate its result.

### 8. Make invisible UI intentional

A finished mobile surface includes what is not immediately visible: sheets,
menus, confirmation, tooltips or contextual help, keyboard behavior, focus,
loading, retry, saved state, error recovery, and interruption resume.

Hidden does not mean undiscoverable. Use a visible affordance, familiar gesture
with a visible alternative, or contextual reveal. Never put a core action only
behind long press, edge swipe, or an unlabeled icon.

### 9. Let motion earn its place

First decide whether motion is necessary. If it is, classify it as
within-page navigation, between-page navigation, or direct manipulation. Use
the [motion and gesture system](mobile-motion-gesture-system.md) to write a
motion contract for each meaningful transition or gesture:

| Change | Category | Subject | User benefit | Commit/cancel | Reduced-motion fallback |
| --- | --- | --- | --- | --- | --- |
|  |  |  |  |  |  |

Useful motion can confirm a press, preserve spatial continuity, show progress,
reveal a related detail, or celebrate a meaningful success. If the benefit
cannot be named, remove the animation. Direct manipulation must define progress,
threshold, cancellation, reversal, and recovery. Do not use a web hover effect
on mobile; translate it into press, focus, selected, or contextual feedback.

### 10. Critique in layers

Review in this order:

1. **Outcome:** Can the user complete the intended job?
2. **Flow:** Are entry, next step, back, cancel, skip, and recovery clear?
3. **Hierarchy:** Is the focal point and primary action obvious in one second?
4. **Content:** Are labels, data, states, and decisions understandable?
5. **System:** Are spacing, type, icons, color, radii, and components coherent?
6. **Interaction:** Do touch, keyboard, sheets, gestures, and feedback work?
7. **Polish:** Do depth, motion, personality, and visual details improve the
   product rather than distract from it?

Fix the earliest failed layer first. Do not tune shadows on a screen whose
primary action is still unclear.

## Mobile acceptance checklist

- Primary user job and success state are explicit.
- Primary action is visible, reachable, and named by its outcome.
- Flow includes back, cancel, skip, retry, no-results, and interruption paths
  where relevant.
- Data shape and realistic copy fit the chosen composition.
- Existing primitives and tokens are reused; exceptions are intentional.
- Touch targets, safe areas, keyboard, large text, and platform conventions are
  checked.
- No core behavior depends on hover, hidden gesture, or unlabeled icon.
- If a gesture exists, its ownership, conflict rules, commit threshold,
  cancellation, recovery, and visible/accessibility alternative are defined.
- Press, loading, success, error, empty, offline, and disabled states are
  designed where applicable.
- Motion is optional by design, has a named purpose and reduced-motion behavior,
  and is proven in progress as well as at rest.
- Screenshots show the real route and representative states, not only a mock.

## Process sources

The process is generalized from Kole Jain's public resource library and videos:

- [Resources](https://www.kolejain.com/resources)
- [How to think like a genius UI/UX designer](https://www.youtube.com/watch?v=HE4rLEQpiXY)
- [Every UI/UX concept explained](https://www.youtube.com/watch?v=EcbgbKtOELY)
- [Master the 3 Types of CRAZY Mobile UI Swipe Interactions](https://www.youtube.com/watch?v=14h1VnkQvIc)
- [7 UI/UX mistakes beginners make](https://sozai.app/transcript/ui-ux-mistakes-beginner/)
- [The 3 dashboard UI flaws](https://sozai.app/transcript/dashboard-ui-flaws-never-built-one/)
- [11 micro animations](https://sozai.app/transcript/micro-animations-level-up-ui-free-figma/)

Use the ideas as craft guidance, not as a mandate to reproduce a particular
visual style, web layout, or arbitrary measurement.
