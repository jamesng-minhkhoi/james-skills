# Parallax and depth

Parallax layers move at different scroll rates to imply depth. Its job is
*composition: rereadable sense of space* — not attention-getting. Over-used, it
becomes the "floating blobs" slop tell; two disciplined layers with an artistic
reason beat five layers moved for effect.

## Rate discipline

Express depth as deliberately-chosen multipliers of document scroll, not
random offsets:

| Layer class | Typical rate | Role |
| --- | --- | --- |
| Foreground content (text, CTA) | 0 — never moves relative to its flow position | Reading stability is sacred |
| Mid layer (cards, device mock) | 0.9–0.95 | Slight depth without distracting reading rhythm |
| Background texture/scene | 0.6–0.8 | Creates the depth gap |
| Ambient atmosphere (grain, glow) | 0.3–0.5 or fixed | Pure atmosphere; no information payload |

- Foreground text NEVER parallax-shifts: reading comprehension is measurably
  hurt when lines drift under a finger, and compensation coupling (moving
  text that lags the scroll then re-syncs) turns into a race condition between
  two choreographies. If a design needs moving text, it is a headline as
  object (kinetic type), not parallax body.
- Layer rates must not invert during the journey: if backgrounds move *faster*
  than the mid layer at any progress point, the depth metaphor stutters.
- Drifting text: `will-change` and blur-on-transform rules; never animate
  filter blur on large raster text blocks (jank by construction).

## Framer Motion layered depth

```tsx
const useDepth = (ref, rate: number) => {
  const { scrollYProgress } = useScroll({ target: ref, offset: ["start end", "end start"] });
  return useTransform(scrollYProgress, [0, 1], [0, -100 * rate]);
};
// Three refs: bg = useDepth(ref, 0.8), mid = 0.93, fg = none (in flow).
```

## What not to parallax

- Text blocks smaller than a heading (captions, legal, data) — drift makes
  them feel like ads.
- Elements the user can interact with (buttons, inputs): motion-relative hit
  targets.
- Anything inside a story told by [pinned sequences](02-pinned-sequences.md):
  composing two scroll choreographies on one element produces
  designer-blamed crossover states; pick one boss, and other layers obey it.

## Depth without motion

Reserve the option: depth also reads via scale + shadow + saturation bias and
*no movement at all* — a static layered composition survives reduced motion
and capture-screenshots. Show that still-frame variant on the sheet so depth
survives the reduced-motion check.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
