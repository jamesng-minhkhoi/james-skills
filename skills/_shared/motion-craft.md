# Motion craft checklist

The craft-level rules for UI motion. The rules here are shared; each skill only
links to them:
`design-uiux` writes them into motion contracts, `audit-uiux-web` and
`audit-uiux-mobile` check rendered motion against them, and `animate` /
`animate-expo` build to them. The deeper why and the exact curves live in
[review-animations standards](../review-animations/STANDARDS.md); this file is
the checklist, not a second copy of that reference.

**Apply the frequency gate first.** Every rule below assumes the moment has
already earned motion (see the frequency table in
[design-uiux motion and gesture](../design-uiux/references/motion-and-gesture.md)).
A rule never makes a 100+/day action animate. No motion is a passing answer.

Each rule gives a default value, when it applies, and the **flag** an auditor
raises when it is broken. Numbers are starting values to tune by feel, not
hard limits, unless the rule says otherwise.

## Timing and easing

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M1 | Ease-out for entrances | strong ease-out `cubic-bezier(0.23, 1, 0.32, 1)` | anything appearing or entering | `ease-in` or `linear` on an entrance; the element starts slow while the user watches |
| M2 | Dropdowns run 150–250 ms | ~180 ms | dropdowns, selects, menus, small popovers | over 300 ms, or so fast (<100 ms) it reads as a cut |
| M9 | Ease-in-out for moves | strong ease-in-out `cubic-bezier(0.77, 0, 0.175, 1)` | an element already on screen moving or morphing to a new place | ease-out on a move makes it stop abruptly; `linear` reads mechanical |
| M15 | Exits are ~20% shorter than entrances | 200 ms in → ~160 ms out | every pair of enter/exit | exit equal to or longer than the entrance; the dismissed thing lingers after the user decided |
| M13 | No bounce on everyday UI | spring `bounce: 0`, or ≤ 0.1 | menus, dialogs, toasts, tabs, form controls | visible overshoot on a routine control; reserve bounce for drag release and rare playful moments |

## Origin and scale

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M4 | Scale to 0.97 on press | `scale(0.97)`, 100–160 ms ease-out | any pressable: buttons, cards, rows | no pressed state at all, or a heavy press (<0.93) that looks broken |
| M10 | Popovers start at 0.95 | `scale(0.95)` + `opacity: 0` → 1 | popovers, menus, tooltips | `scale(0)` (appears from nothing), or a large scale jump |
| M11 | Enter from the trigger | `transform-origin` at the trigger edge | popovers, menus, context sheets | grows from its own centre while anchored to a button; modals are exempt and stay centred |
| M12 | Exit back to the trigger | reverse of M11, same origin | the same surfaces on close | closes toward the centre or a different edge than it opened from |

## Choreography

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M3 | Stagger list rows by ~30 ms | 30 ms per row, cap total stagger at ~300 ms | list or grid entrances on first view | stagger ≥ 80 ms per row, a stagger that blocks tapping, or one that replays on every scroll/refresh |
| M6 | Stagger details as they settle | primary block lands first, secondary text/meta ~40–60 ms after | cards and detail panels revealing content | every inner element lands at once (flat), or the primary content waits for decoration |
| M16 | Overlap old and new states | outgoing and incoming crossfade in the same window | tab content, step changes, swaps | out-then-in sequencing with a blank gap between states |
| M8 | Pulse to confirm success | one brief scale or glow pulse (~1.0 → 1.05 → 1.0) | a completed, user-caused action (saved, sent, added) | looping pulses, a pulse with no user action, or a pulse as the *only* success signal (pair with text or icon) |

## Physicality

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M5 | Stretch a moving knob ~12% | knob widens ~12% along travel while moving, back to round at rest | custom switch knobs, slider thumbs, segmented-control pills | a custom knob slides rigidly; native platform switches are exempt — keep the platform control |
| M7 | Move objects along arcs | slight curved path (offset x and y with different easings) | an object travelling across the screen (add-to-cart, fly-to-target) | a long straight diagonal that reads mechanical; short in-place moves are exempt |
| M17 | Use masks for reveals and colour changes | `clip-path: inset(...)` (web) or a masked view (native) | text/image reveals, active-tab colour, hold-to-confirm fill | a reveal faked with `height`/`width` animation, or a colour swap that flashes |
| M18 | Crossfade icons with blur | old icon fades + scales to ~0.8 with `blur(2px)`; new icon fades/scales in from ~0.8 | icon state swaps (copy → check, play → pause) | a hard icon swap, or two icons visibly overlapping with no blend; keep blur <20 px (expensive on Safari / Android) |

## Gestures

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M14 | Don't tween while held | 1:1 tracking during drag; animate only after release | drag, swipe, scrub, pull | easing or a duration applied while the finger is down, so the element lags the pointer |
| M19 | Rubber-band past bounds | resistance rises with overdrag, then springs back | scroll edges, sheets, carousels, draggable panels | a hard invisible wall, or overdrag with no resistance |

## Continuity

| # | Rule | Default | Applies to | Flag when |
|---|---|---|---|---|
| M20 | Reuse the same identity for one object | Motion `layoutId` (web); Reanimated shared transition tag or a single persistent view (native) | an object that moves between two layouts: active-tab pill, card → detail, selected chip | the same object unmounts and a copy mounts elsewhere (a jump or double), or a shared element links two things that are not the same object |

## Platform translation

- **Web (Motion / CSS):** M11/M12 via `transform-origin` (Base UI / Radix
  expose `--transform-origin`); M20 via `layoutId`; M17 via `clip-path`;
  M18 via `filter: blur()`; animate `transform` and `opacity` only.
- **Expo / React Native (Reanimated 4):** M4 as a CSS transition on press,
  M14/M19 in a gesture worklet on the UI thread, M20 with a shared
  transition tag or one persistent absolutely positioned element, M18 by
  crossfading opacity (never animate `BlurView` intensity). Platform
  navigation, tabs, and switches keep their native motion; these rules apply
  to custom surfaces only.
- **Reduced motion:** drop M5, M7, M8, M19 overshoot and any travel; keep
  M1/M15 timing as short opacity fades and keep the non-motion success signal
  from M8.

## Using the IDs

- **Design** (`design-uiux`): in each motion contract's Timing and Feedback
  rows, cite the rule IDs the motion follows, and state any deliberate break
  with its reason.
- **Audit** (`audit-uiux-web`, `audit-uiux-mobile`): a craft finding cites the
  rule ID in its evidence, e.g. "`F-web-7` — M11: menu scales from centre,
  not the trigger". Timing values need a recording or DevTools capture;
  inferred from source alone they are `unverified`, and an unobserved rule is
  `NOT_RUN`, never pass. Severity follows the [ontology](ontology.md); a
  craft rule alone is usually P3, P2 when it delays a frequent task or hides
  state.
- **Build** (`animate`, `animate-expo`): run the checklist as part of the
  self-check before hand-off.

---

Source: "20 Ways to Make Beautiful AI Animations" image supplied by the user
on 2026-11-06 (author not stated; status `unverified`). Rule names follow
that list; default values are reconciled with the existing
[review-animations standards](../review-animations/STANDARDS.md)
(Emil Kowalski, MIT — see [NOTICE](../../NOTICE.md)).
