# Pointer and device moments

Cursor-following, magnetic buttons, tilt, and parallax on the pointer are
*contingent delight*: they exist only where a pointer exists, degrade to static
state without one, and must never carry information unavailable by any other
route. If the tilt is the only way a panel says "this is interactive", it is a
failure, not a signature.

## Discipline before effect

| Moment | Legitimate job | Red flag |
| --- | --- | --- |
| Card tilt / layered depth | Physicality of a draggable or featured object | Tilt on an entire dense panel: motion steals text stability |
| Magnetic CTA | Reinforce the button is the active target near it | Magnet on every control: strength becomes noise |
| Cursor-follow glare / echo | Highlight a surface under direct interaction | A cursor novelty with no actionable surface under it |
| Pointer parallax band | Space depth distinct from scroll depth | Confusing pointer parallax with scroll density (two drivers, one axis) |
| Themed mouse cursor | Brand moment on a marketing page | Replacing the OS cursor, hiding the text-select caret, or usurping drag handles |

## Tilt and glare (Framer Motion)

```tsx
const useTilt = (maxDeg = 6) => {
  const x = useMotionValue(0), y = useMotionValue(0);
  // min() keeps touch/keyboard users out of the whole path.
  const spring = { stiffness: 150, damping: 15 };
  // On move: x.set()/y.set() from pointer; rotateX = transform(y, [-0.5, 0.5], [-maxDeg, maxDeg])
  // Reset to 0 on pointerleave. Touch devices: `@media (pointer: fine)` gate.
};
```

- `transform-gpu`-style compositing only: tilt animates `rotateX/rotateY` and
  never `top/left/width` — layout motion during a 60 fps pointer loop is jank
  by construction, not by implementation bug.
- Depth layering (`translateZ`) stays ≤ 3 layers; each floating layer must
  survive being rendered alone (some users will never hover).
- Text inside a tilting surface gets a counter-flatten or it loses legibility
  mid-motion; for dense content, tilt chrome (border, glare) not body.

## Magnetic CTA

The magnet radius (typically ≤ button glyph bounds + 24 px) pulls the button
toward the cursor inside the radius and releases with a spring. Return travel
must be the same spring family as the pull, or leaving feels like snapping a
rubber band. Keyboard focus uses the resting state; the magnet NEVER rewrites
focus geometry (focus outline follows the true layout box, not the translated
visual).

## Reduced motion + fallbacks

- Every pointer moment has a static affordance twin: the same emphasis drawn by
  state (hover underline, border, shadow) with zero velocity. Touch, `pointer:
  coarse`, and `prefers-reduced-motion` land on that twin directly.
- Motion never blocks the click: a magnetic or translating button's hit area
  stays pinned to the layout box; hit area dragging to chase the visual is a
  defect, not charm.
- Mouse-only devices: use motion value thresholds, not fire-on-every-mousemove
  state updates; throttle pointermove to a rAF tick.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
