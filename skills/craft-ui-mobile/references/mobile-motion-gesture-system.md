# Mobile motion and gesture system

Use this reference when a screen includes navigation motion, swipe interaction,
dragging, card browsing, sheets, reordering, dismissal, or meaningful state
transitions. It turns “make it feel smooth” into a behavior contract that can
be implemented and verified.

## First decide whether motion is needed

Motion is optional. Choose no motion when an animation would delay a frequent
task, add ambiguity, compete with critical content, or provide no identifiable
user benefit. A static state change with clear feedback is often better for
settings, dense data entry, and repetitive operations.

When motion is useful, name its job:

- **Continuity:** preserve the identity or spatial relationship of an object.
- **Hierarchy:** show what entered, left, expanded, or became important.
- **Cause and effect:** connect the user's action to the resulting state.
- **Progress:** show direct manipulation or meaningful work in progress.
- **Result:** confirm a completed, recoverable action.
- **Personality:** add a brief, non-blocking moment that supports the product.

If the benefit cannot be stated in one sentence, remove the motion.

## Classify the interaction

Choose the closest category before choosing an animation technique.

| Category | Typical use | Design responsibility |
| --- | --- | --- |
| Within-page navigation | Carousel, gallery, card stack, segmented content, local detail reveal | Preserve local context and the identity of the subject while the user explores nearby content |
| Between-page navigation | Push/pop route, detail screen, modal, full-screen sheet, interactive back | Communicate hierarchy and preserve the relationship between source and destination |
| Direct swipe or drag | Dismiss, archive, reorder, page, reveal, confirm, move, or compare | Follow the user's finger, make the commit rule understandable, and support cancellation or recovery |

Do not call every horizontal movement a swipe interaction. A timed route
transition, a scroll gesture, and a direct-manipulation control have different
ownership, progress, thresholds, and accessibility requirements.

## Motion contract

Write a contract for every important motion before implementation:

| Field | Decision |
| --- | --- |
| Trigger | Tap, swipe, drag, navigation, save, loading, or system event |
| Category | Within-page, between-page, direct manipulation, or no motion |
| Subject | What moves, what stays fixed, and what maintains semantic identity |
| User benefit | Continuity, hierarchy, cause/effect, progress, result, or personality |
| Progress source | Time-based, gesture-controlled, scroll-linked, or state-based |
| Start state | Visible state before the interaction |
| Commit rule | Release, distance, velocity, explicit action, or completed work |
| Cancel rule | How the interaction returns to the original state |
| Completion | Final state, feedback, and next focus target |
| Interruption | Behavior on reversal, navigation away, backgrounding, or data change |
| Timing | Duration and easing family for non-interactive portions |
| Feedback | Visual, haptic, audio, or non-motion alternative; match intensity to consequence |
| Accessibility | Reduced-motion behavior, focus order, labels, and non-gesture alternative |
| Performance | Native/UI-thread strategy, clipping/blur constraints, and target device |

Do not use a decorative animation to hide an undefined state transition.

## Direct-manipulation state model

For a swipe or drag, model the interaction separately from the final action:

`idle → tracking → committed | cancelled → settled`

When the action changes data, include the product state as well:

`idle → tracking → pending → success | recoverable error → settled`

Define what the user sees at rest, during progress, at the commit threshold,
after release, and after cancellation. A gesture should not jump from the
default state directly to an unexplained result.

### Thresholds and cancellation

- Prefer a simple, explainable commit rule. Do not make users guess whether
  distance, velocity, or both will win.
- Make progress visible before commitment through translation, scale, reveal,
  label, color, or another meaningful signal.
- Let users reverse or cancel before the commit point when the action is
  consequential or destructive.
- Define fast flicks, slow drags, incomplete drags, repeated attempts, and
  release outside the active surface.
- After commitment, show a durable result and provide undo, rollback, or retry
  when the product contract allows it.
- Do not use haptics as the only indication that a threshold was crossed.

## Gesture ownership and conflict rules

For every gesture, document who owns the gesture and when ownership changes.
Check conflicts with:

- vertical scrolling and nested scrolling;
- system-edge back gestures;
- sheets and interactive dismissal;
- sliders, maps, carousels, and reorder handles;
- tap, long press, and selection mode;
- keyboard dismissal and safe-area insets.

Specify the active region, direction lock, touch slop, threshold, velocity
behavior, cancellation path, and visible alternative. Do not let a custom
gesture silently steal a platform gesture or make a core action gesture-only.

## Navigation continuity

For within-page transitions:

- keep the explored subject visually connected to its previous position;
- preserve surrounding context when it helps orientation;
- distinguish paging, selection, expansion, and dismissal;
- keep the next action and current position understandable.

For between-page transitions:

- use direction to communicate hierarchy where the platform convention supports
  it;
- make forward and back behavior coherent and reversible;
- preserve the source context when returning;
- move focus to the destination's title or primary content;
- avoid shared-element effects when they create false object identity.

## Accessibility and reduced motion

Reduced motion is a change in motion behavior, not a removal of meaning.

- Replace large travel, parallax, rapid scaling, and decorative springing with
  opacity, instant state changes, or short low-travel transitions.
- Preserve progress, selection, success, error, and focus feedback without
  relying on movement.
- Provide visible controls for actions that would otherwise require a swipe.
- Ensure VoiceOver/TalkBack users can discover, perform, cancel, and recover
  the same task through accessible actions.
- Keep focus and semantic labels stable after route changes, expansion,
  deletion, reordering, and modal dismissal.
- Test large text, contrast, touch targets, and screen-reader traversal in the
  final state rather than only in the default state.

## Native performance and platform fit

Prefer native or UI-thread-friendly transforms and opacity for interactive
motion. Avoid requiring layout recalculation, expensive blur, large masks, or
unbounded shadows on every frame. Check the actual target platform because a
motion that looks acceptable in a design tool may clip, tear, drop frames, or
feel delayed in the runtime.

Use the platform's established back behavior, sheet semantics, scroll physics,
haptics, safe-area handling, and reduced-motion setting. Adapt the contract to
the project's framework rather than copying a web prototype literally.

## Proof matrix

Review interactive motion at these checkpoints:

| Checkpoint | Evidence |
| --- | --- |
| Rest | Screenshot or recording of the discoverable starting state |
| In progress | Slow drag, partial transition, and visible feedback |
| Threshold | Evidence just before and after commitment |
| Completion | Durable result, focus, and next action |
| Cancellation | Reversal, incomplete release, and rollback |
| Conflict | Gesture competing with scroll, edge-back, sheet, or control |
| Accessibility | Reduced motion, large text, screen reader, and visible alternative |
| Interruption | Background, navigation away, network failure, or data update |
| Runtime | Device recording and performance observation on the target platform |

The final review should state which checkpoints were observed and which remain
unknown. Source inspection and a static screenshot cannot prove gesture quality.

## Critique prompts

- Is motion necessary for this task, or is it decoration?
- What is the subject of the motion, and what relationship does it preserve?
- Is this within-page navigation, between-page navigation, or direct manipulation?
- Can a first-time user discover the gesture without already knowing it exists?
- What happens at 25%, 50%, the threshold, release, reversal, and cancellation?
- Does the gesture conflict with scrolling or a system gesture?
- Is there a visible alternative for a core action?
- Does reduced motion preserve meaning and feedback?
- Does the interaction still feel native on the actual device?
