# Numbers and counters

Counters encode one claim: *this number is real and just changed*. The motion
job is cause-and-effect or result — never decoration. A rendered count
that the product's data does not support is fabricated proof; the "never
fabricate" rule applies here harder than anywhere else in this module.

## The truthfulness contract

| Field | Rule |
| --- | --- |
| Source | The number comes from project data, fixtures, or the CMS named in the option sheet |
| Start | Count from a meaningful origin (0, previous period), not from a random art target |
| End | If the end value is unknowable at design time, the component takes it as a prop; never hardcode an audience-glaring lie |
| Duration | Proportional to legibility: a 6-digit count the user must read takes 1.2–1.8 s |
| Locale | Thousands separators, decimals, currency, and suffix from the project's formatting util — the count is a formatted string, never `Math.round` typed digits |
| Reduced motion | Static final value renders immediately; no count at all |

## Count-up or swap? Decide by who changes the number

- **The user's action changes it** (cart total, price toggle, balance,
  filtered stat). Use [digit pop-in](06-digit-pop-in.md). Only the changed
  digits move, and it shows only real values.
- **The data changes it** (a live price, a polled tile, a ticker). Use
  `transitions-dev` number-subtle-change, a quiet in-place cross-fade. Never
  re-run a count-up from 0 on each poll. Show freshness.
- **It changes several times a second** (upload percent). Swap the text with
  no motion.
- **It appears for the first time and its size is the story.** Use the
  count-up below.

The full table is in [digit pop-in](06-digit-pop-in.md#which-number-motion-decide-by-who-changes-it-then-by-how-often).

## Framer Motion counter

```tsx
"use client";
import { useMotionValue, useSpring, useTransform, useReducedMotion } from "framer-motion";
import { formatNumber } from "<project>/format"; // real formatting util

function Metric({ value }: { value: number }) {
  const reduced = useReducedMotion();
  const mv = useMotionValue(0);
  const spring = useSpring(mv, { stiffness: 80, damping: 20 });
  const text = useTransform(spring, (v) => formatNumber(Math.round(v)));
  // Eagerly settle without motion, or never run the tween:
  if (reduced) mv.jump(value); else mv.set(value); // set-on-mount drives the spring
  return <motion.span>{text}</motion.span>;
}
```

This counter is for the **first reveal only**. It springs through invented
in-between values on *every* change of `value`. When the value later changes
because of the user, render it with [digit pop-in](06-digit-pop-in.md). When
the data changes it, use number-subtle-change.

## Milestone feedback (result motion)

When a wait completes (upload, mentor match, survey submission), the number
lands with a one-beat emphasis: scale 1.0→1.06→1.0 spring plus token color
confirmation. One beat, then it is over; a looping celebratory spin around a
metric competes with the next thing the user needs to read.

## Count-up pitfalls

- Spring-based counters undershoot then correct: with `damping` too low the
  displayed value dips below start. Verify the first 200 ms do not show a
  *lower* number than the settle value claims.
- Live or polled numbers (revenue tiles, tickers) never use this counter or a
  loop. They get `transitions-dev` number-subtle-change and a visible
  freshness label. Never fake "live" cadence.
- Counters inside scroll stories graduate to
  [scroll story · fed-by-scroll](../scroll-story/04-scroll-fed-canvas.md)
  choreography — a count that begins as the pin arrives reads as orchestrate,
  one that triggers on a stray intersection reads as two different designers.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
