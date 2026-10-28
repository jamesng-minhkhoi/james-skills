# Touch and mobile

Native scroll on iOS/Android has its own physics: momentum, rubber-banding,
velocity handoff, and hover-less interaction. A scroll story designed purely
against desktop wheel physics will misfire on touch. The rule: **the finger
owns velocity.** Techniques that intercept or re-time native scrolling are the
first candidates for rejection on mobile.

## What degrades on touch

| Desktop technique | Mobile behavior | Verdict |
| --- | --- | --- |
| `position: sticky` rail | Works natively, is the platform scroll idiom | Keep; often the whole mobile story |
| GSAP `pin` (hard scroll lock) | Fights rubber-banding and momentum; scroll-jack feel is amplified | Degrade to sticky rail or step cards |
| Scroll-snap | Platform-supported; snaps to card boundaries | Keep, match snap points to media rhythm |
| Heavy scrub (10+ coupled layers) | Jank risk on mid-tier Android GPU | Reduce layer count, or swap to opacity-only |
| Scroll-fed canvas | Works, but thermal/battery sensitive; mid-tier devices are the budget column | Downgrade pixel ratio aggressively, pause off-screen, or present static-keyframe per step |
| 400-px wheel scrub over a 2-viewport story | Touch travels at very different rate | Re-anchor by viewport fraction, test with slow-drag |

## The step-card fallback

When a desktop pin sequence must degrade, the honest mobile alternative is the
*step card* sequence: each story state is a full-bleed card snapped by native
`scroll-snap`, media paused on view-out. Users scrub instantly with familiar
flick physics and every word stays reachable with no JS at all. This is not a
"lesser" version to apologize for; on mobile it is usually stronger. Design it
as a real option in the sheet's mobile column.

## Reanimated/Expo specifics

- Map scroll progress from `useAnimatedScrollHandler` / `scrollHandler`
  worklets — reading `scrollY` from JS thread state produces late frames.
- `Animated.ScrollView` + `useDerivedValue` R3F/pin equivalents; but for most
  stories native components win: `FlatList` with `pagingEnabled`, or
  `PagerView` ARE the step cards, platform-grade.
- Device-heat and scene-pause rules from
  [signature motion · mobile](../signature-motion/05-mobile-reanimated.md) apply.
- Reduced motion: `AccessibilityInfo.isReduceMotionEnabled` swaps scrubbed
  canvas for its static-keyframe grid — design that grid as its own frame set,
  not an export accident.

## Both-widths check

A scroll story must be evaluated at 1440 and 390 *as two designed options*, not
as one shrunk: the 390 version may be a legitimately restructured story
(vertical stack, sticky header, step cards). If the mobile column of the
option sheet is only desktop scaled down, the design is not done.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
