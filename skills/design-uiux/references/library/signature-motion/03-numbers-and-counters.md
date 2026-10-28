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
| Duration | Proportional to legibility: a 6-digit tick the user must read takes 1.2–1.8 s; a background ticker may loop faster |
| Locale | Thousands separators, decimals, currency, and suffix from the project's formatting util — the count is a formatted string, never `Math.round` typed digits |
| Reduced motion | Static final value renders immediately; no count at all |

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

## Milestone feedback (result motion)

When a wait completes (upload, mentor match, survey submission), the number
lands with a one-beat emphasis: scale 1.0→1.06→1.0 spring plus token color
confirmation. One beat, then it is over; a looping celebratory spin around a
metric competes with the next thing the user needs to read.

## Count-up pitfalls

- Spring-based counters undershoot then correct: with `damping` too low the
  displayed value dips below start. Verify the first 200 ms do not show a
  *lower* number than the settle value claims.
- Looping tickers (live revenue dashboards) need a visible data-freshness
  indicator, or the loop lie is worse than a stale truth. Never fake "live"
  cadence.
- Counters inside scroll stories graduate to
  [scroll story · fed-by-scroll](../scroll-story/04-scroll-fed-canvas.md)
  choreography — a count that begins as the pin arrives reads as orchestrate,
  one that triggers on a stray intersection reads as two different designers.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
