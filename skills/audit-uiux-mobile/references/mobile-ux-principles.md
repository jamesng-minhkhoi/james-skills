# Mobile UX principles

Use these principles to evaluate a real mobile journey. They are heuristics,
not substitutes for user research. For each applicable principle, record a
status — **Strong**, **Concern**, **Critical**, **Unknown**, or **Not
applicable** — plus evidence, user impact, and the smallest useful improvement.

## Contents

- [Explicitness spectrum](#1-explicitness-spectrum)
- [Progressive disclosure](#2-progressive-disclosure)
- [Core interaction heuristics](#3-core-interaction-heuristics)
- [Content and decision quality](#4-content-and-decision-quality)
- [Content-to-structure fit](#5-content-to-structure-fit)
- [Functional state integrity](#6-functional-state-integrity)
- [Principle conflicts](#7-principle-conflicts)
- [Trust and dark-pattern review](#8-trust-and-dark-pattern-review)
- [Mobile-specific principles](#9-mobile-specific-principles)
- [Common failure patterns](#10-common-failure-patterns)

## 1. Explicitness spectrum

Decide how much the interface should say or expose at each moment:

| Level | Use for | Audit question |
| --- | --- | --- |
| **Visible** | Primary actions, current state, high-risk decisions, required input | Can a first-time user see what matters and what to do next? |
| **Directly revealed** | Detail shown after an explicit tap, selection, or expansion | Is the reveal predictable and easy to reverse without losing context? |
| **Contextual** | Guidance, recommendations, constraints, and actions relevant to the current object or moment | Is it available at the point of need and clearly optional when appropriate? |
| **Deferred** | Advanced or low-frequency detail | Is the entry point discoverable, and does disclosure preserve context? |
| **Advanced/hidden** | Internal, unavailable, expert, or unsafe operations | Is it truly appropriate to hide, rather than merely inconvenient to expose? |

Do not hide primary functionality to achieve visual minimalism. Do not turn
optional recommendations into requirements. Do not make users guess whether a
disabled, deferred, or hidden action exists.

## 2. Progressive disclosure

Show the information and choices needed for the current decision first; reveal
detail as the user's intent becomes clearer. Good disclosure reduces clutter
without reducing discoverability.

Check that:

- the first view answers “where am I, what matters, and what can I do?”;
- each reveal has a visible label, familiar affordance, and predictable result;
- the user can return without losing context, input, or progress;
- the design does not split one simple decision across unnecessary steps;
- advanced users have efficient paths without forcing novice users to learn
  hidden gestures or obscure settings.

## 3. Core interaction heuristics

### Visibility of system status

Communicate what is happening, what changed, and what comes next within a
reasonable time. Inspect taps, navigation, saves, uploads, sync, processing,
permissions, and background work. Match feedback intensity to consequence:
inline status for routine updates, interruption for imminent data loss or
urgent decisions.

### Match the user's mental model

Use the user's language, domain concepts, and familiar ordering. Check whether
icons, labels, grouping, natural mapping, and navigation predict the outcome.
Replace internal implementation terms with user language.

### Recognition over recall

Keep labels, choices, prior selections, constraints, and relevant context
visible or easy to retrieve. Prefer contextual suggestions and visible options
over asking users to remember values from another screen or step.

### User control and freedom

Provide clear back, cancel, close, undo, skip, and recovery paths. Let users
leave a flow without losing work when possible. Make destructive actions
explicit and keep gesture-only exits from becoming traps.

### Error prevention

Prevent expensive mistakes with sensible defaults, constraints, previews,
confirmation at the right moment, and separation of destructive actions. Do not
wait for a submission error when the interface can make the valid action clear.

### Error recognition and recovery

State what went wrong in plain language, identify the affected object or field,
and offer the next useful action. Avoid raw error codes, vague “something went
wrong” messages, premature validation, and red styling for routine information.

### Consistency and platform standards

Keep the same word, icon, gesture, position, and result consistent within the
app. Follow iOS and Android conventions unless the product has a strong reason
to diverge; when platforms differ, preserve platform expectations rather than
forcing one abstraction everywhere.

### Flexibility and efficiency

Support a clear novice path and efficient repeat use. Consider recent items,
defaults, search, shortcuts, accessible gestures, and personalization. Every
gesture or shortcut needs a visible alternative for discoverability and
accessibility.

### Minimalist signal-to-noise

Remove information that competes with the user's current goal, but do not
confuse minimalism with hiding. Evaluate hierarchy, cognitive load, attention
switches, card count, decorative elements, and the cost of every extra tap.

### Help in context

Prefer concise guidance at the point of need over a tutorial users must
remember. Explain unfamiliar concepts before commitment, not after failure.

## 4. Content and decision quality

Audit the words and choices, not only the components around them:

- Use familiar, specific labels that describe the result of an action.
- Put the most important information first and make scan order intentional.
- State constraints, pricing, privacy effects, eligibility, and irreversible
  consequences before commitment.
- Distinguish required, recommended, optional, unavailable, and completed
  actions in copy and visual treatment.
- Keep field help, validation, and error copy close to the affected control.
- Avoid vague CTAs such as “Continue” when the next outcome can be named.
- Treat suggestions as suggestions; never disguise growth, upsell, or data
  collection as a required product step.

## 5. Content-to-structure fit

Audit whether the representation matches the user's information task:

- lists support scanning and acting on records;
- grouped sections expose meaningful categories or priorities;
- timelines preserve event order and time context;
- charts answer a defined comparison with honest axes, units, labels, range,
  and an accessible summary;
- tables or structured rows support field comparison, search, filter, sort,
  truncation, selection, and density without becoming compressed desktop UI;
- detail routes or sheets preserve enough context for the action;
- cards represent distinct objects or decisions instead of decorating every
  row.

Test typical, empty, dense, partial, stale, and malformed data. Flag invented
metrics, decorative charts, fake records, and containers chosen without a user
task.

## 6. Functional state integrity

Audit important components as transitions, not isolated screenshots:

`idle → pressed/focused → pending → success | recoverable error`

Add selected, disabled, empty, no-results, offline, permission-denied, stale,
interrupted, resumed, and rollback states where applicable. Check what caused
the transition, where feedback appears, whether the same object preserves its
identity, and whether users can cancel, retry, undo, or continue.

An attractive loading, success, or error screen does not prove the product can
reach it. Distinguish source-declared, manually forced, and naturally observed
states.

## 7. Principle conflicts

Do not resolve these conflicts mechanically. Record the product context,
affected users, risk, and chosen trade-off:

| Tension | Audit question |
| --- | --- |
| Minimalism vs discoverability | What can be removed without hiding a needed action or state? |
| Progressive disclosure vs transparency | Is anything legally, financially, privately, or safety-relevant deferred too far? |
| Gesture efficiency vs accessibility | Is there a visible alternative with equivalent outcome? |
| Platform convention vs brand | Does differentiation preserve the platform mental model and back behavior? |
| Personalization vs consistency | Can the user customize without losing stable locations and labels? |
| Speed vs error prevention | Is confirmation reserved for meaningful risk rather than every action? |
| Guidance vs autonomy | Does help support the decision without interrupting or coercing? |

## 8. Trust and dark-pattern review

Flag patterns that make the user's choice less informed or less reversible:

- consent or permission before the user understands the benefit;
- default opt-in for sensitive sharing, notifications, or paid behavior;
- primary styling for the product's preferred outcome and weak styling for
  cancel, skip, decline, or unsubscribe;
- confirmshaming, artificial urgency, hidden costs, or ambiguous copy;
- destructive actions hidden behind a gesture or placed beside a common action;
- forced registration or onboarding before the core value is demonstrated;
- auto-dismissed warnings, progress that cannot be paused, or loss of work on
  interruption;
- recommendations that look like system requirements.

Ask whether a reasonable user can understand the consequence, choose freely,
change their mind, and recover without penalty.

## 9. Mobile-specific principles

### Reachability and touch comfort

Place frequent and primary actions where they are comfortable to reach for the
target device and posture. Use platform guidance for target size — commonly
44pt on iOS and 48dp on Android — and provide enough separation to prevent
mistaps. Do not rely on a tiny icon, edge swipe, or long press for a critical
action.

### Safe areas, system UI, and keyboard

Check status bars, display cutouts, gesture/navigation insets, bottom bars,
orientation, split-screen or foldable states where relevant, and the software
keyboard. The keyboard must not cover the active field or primary action, and
content must not sit beneath an unsafe system gesture region.

### Gesture discoverability and alternatives

Use familiar gestures for direct manipulation, but never make a core outcome
gesture-only. Provide a visible tap or button alternative for swipe-to-delete,
drag, pull-to-refresh, custom navigation, and dismiss actions. Make gesture
direction, cancellation, and completion understandable.

### Motion and transition integrity

Classify meaningful motion as within-page navigation, between-page navigation,
or direct manipulation. Audit whether the subject preserves semantic identity,
whether progress follows the user's input when appropriate, and whether the
transition communicates cause, hierarchy, result, or recovery. Check the
threshold, cancellation, reversal, interruption, focus, and rollback behavior.
Treat decorative delay, false continuity, fake success animation, gesture
conflict, and reduced-motion loss of meaning as observable findings. Keep
unobserved runtime behavior **Unknown**.

### Short sessions and interruptions

Assume people may be mobile, distracted, offline, interrupted by a call or
notification, or returning after the app was suspended. Preserve progress,
restore context, avoid time-boxed UI, and make resumption obvious.

### Permissions, privacy, and trust

Ask for permissions in context, explain the benefit before the system prompt,
request the minimum scope, and provide a useful path when permission is denied.
Make collection, sharing, destructive effects, and irreversible operations
legible before commitment.

### Adaptive mobile layouts

Check narrow and tall phones, large text, portrait and landscape when
supported, tablets/foldables or expanded windows where applicable, and changed
input methods. Prefer reflow, reveal, or presentation changes over clipped,
scaled-down desktop compositions.

### Accessibility and multimodal feedback

Do not rely on color, motion, sound, or a gesture alone. Provide accessible
names, roles, values, and states; support screen readers, large text, contrast,
reduced motion, voice/switch access, and haptics or visual confirmation when
they clarify important feedback.

## 10. Common failure patterns

Flag these explicitly when observed:

- token-only polish that leaves the journey or hierarchy unchanged;
- progressive disclosure that hides needed information or has an undiscoverable
  trigger;
- onboarding that blocks the core value before users understand it;
- permission prompts before context or without a denied-permission path;
- primary actions buried among equal-weight secondary actions;
- gesture-only functionality, auto-dismissed feedback, or time pressure;
- validation that interrupts typing instead of helping users succeed;
- generic cards, icon soup, or decorative motion that competes with content;
- desktop layouts compressed onto a phone instead of redesigned for reach and
  focus;
- empty, loading, offline, or error states treated as afterthoughts;
- static success feedback disconnected from a real action or data change;
- fabricated metrics, placeholder records, vague generic copy, or impossible
  state combinations presented as real product information;
- every screen forced into the same card/grid template regardless of task;
- visual tokens applied consistently while behavior, navigation, and feedback
  remain inconsistent.

## Sources and further reading

Use these as principles sources, not as permission to copy another product's
visual style:

- Nielsen Norman Group, [10 Usability Heuristics](https://www.nngroup.com/articles/ten-usability-heuristics/)
- Nielsen Norman Group, [Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)
- Nielsen Norman Group, [Recognition and Recall](https://www.nngroup.com/articles/recognition-and-recall/)
- Nielsen Norman Group, [Hostile Error Messages](https://www.nngroup.com/articles/hostile-error-messages/)
- Apple, [Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
- Apple, [Accessibility](https://developer.apple.com/design/human-interface-guidelines/accessibility)
- Apple, [Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback)
- Apple, [Designing for iOS](https://developer.apple.com/design/human-interface-guidelines/designing-for-ios/)
- Android, [Mobile layout basics](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-basics)
- Android, [Mobile accessibility](https://developer.android.com/design/ui/mobile/guides/foundations/accessibility)
- Android, [System bars and insets](https://developer.android.com/design/ui/mobile/guides/foundations/system-bars)
