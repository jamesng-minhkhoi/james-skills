# Mobile equivalents (Reanimated)

On Expo, the equivalent moment is built with Reanimated worklets driven by the
UI thread. The translation is real, not approximate: some web signature
techniques have no honest Reanimated twin, and shipping them as pretense is
where native UX debts are born. When a web-only technique is requested,
propose the closest native behavior and name the substitution as a choice.

## Translation table

| Web technique | Native reality | Verdict |
| --- | --- | --- |
| Masked line stagger | `Animated.Text` entering `FadeInDown`-style layouts, or shared-element handoff between route entry and hero | Direct equivalent; keep per-line, not per-glyph |
| Viewport reveal system | `Animated.ScrollView` + `useAnimatedScrollHandler`/`useSharedValue` scroll-position thresholds, or Layout Animations for view entry | Direct equivalent (Shipped screens use platform entering/exit primitives first) |
| Counter | `useDerivedValue` interpolating on a shared value; format inside a worklet | Direct; string formatting in worklets is cheap enough for 1–2 digits/60fps, otherwise tween stepped frames |
| Pointer tilt/magnet | No pointer. Do NOT fake via touch-move: dragging a *scrolling* page to tilt a card breaks scrolling | Substitute: spring press-in scale + native press feedback |
| Variable-font hover weight | No hover. That moment does not exist on touch | Substitute: selected-state weight change, or skip the idea |
| Cursor glare | No cursor | Skip; the native press state is the ergonomics |
| gyro / device-tilt parallax | `expo-sensors` DeviceMotion; must be opt-in (permission dialog is a cost) and never drives scroll | Rare: propose only for with-permission AR-ish canvases; the permission prompt is part of the option's trade-off |

Handoff detail stays with
[`frontend-mobile-engineering`](../../../../frontend-mobile-engineering/SKILL.md)-owned
build rules — this skill specifies behavior, not Reanimated wiring.

## Native-native idioms belong in the pitch first

Before importing a web pattern, name what iOS/Android would ship here:
platform sheets with detents, large-title collapse, transition-through shared
elements, symbol-driven feedback. For a first-run or rarely-seen moment, the
platform idiom is often the stronger reference — replacing it is a named
divergence, and
[mobile principles](../../mobile-principles.md) owns that argument.

## Reduced motion on native

Honor the OS setting (`AccessibilityInfo.isReduceMotionEnabled` and its iOS
subscription; Android `Settings` equivalent), not a custom toggle. The reduced
variant is still *the designed state*: if the un-animated layout was never
drawn, the reduced experience is undesigned and the technique does not pass.

## What not to attempt

- Per-glyph split animations on device: layout cost × glyph count on the UI
  thread; if splitting is essential, split per-line and use `FadeIn` masks.
- Scroll-jacked storytelling on touch: scrolled finger must own velocity
  ([scroll story · touch reality](../scroll-story/05-touch-and-mobile.md));
  pinning that intercepts swipe is the native selves worst offender.
- Shader canvas on React Native via three/r3f-native: heavy and fragile;
  prefer `react-native-skia` for shader-look (catalog routes it there).

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
