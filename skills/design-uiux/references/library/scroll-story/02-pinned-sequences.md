# Pinned sequences

Pin-then-narrate: a section pins in place while scroll continues, and its
content advances through states. This is the most over-used scroll technique —
on the option sheet it should justify why the sequence cannot live as plain
scrolling blocks. Cost is real: pinned sections make page height, anchors, and
findability harder, and they are where users get trapped.

## Types, from safest to most invasive

| Type | What it does | Use when |
| --- | --- | --- |
| Sticky-chapter | Native `position: sticky` rail meets sliding content column | Most storytelling needs; no JS pin at all |
| Soft pin | Element visually holds; document keeps scrolling honestly beneath (translate compensation) | Needs a pinned feel without scroll hijack |
| Hard pin (ScrollTrigger `pin`) | Scroll lock content through sequence | One hero narrative per page and short (≤ 2 viewport heights scrolled); never under other content |

Multi-step sequence never justifies whole-page scroll-lock. A pinned zone
ornamenting *reading* content silently steals scroll length from writing-prevalent
pages and anchors from deep-linking.

## Framer Motion: sticky-first

Prefer CSS `position: sticky` for the rail plus a scroll-driven value for the
content stage. This keeps page height honest — scroll length is unaffected,
and back/anchor/f100% zoom behavior is inherited free.

## GSAP ScrollTrigger pin

```ts
gsap.timeline({
  scrollTrigger: {
    trigger: section, pin: section, pinSpacing: true,  // pinSpacing keeps flow height; leave true
    start: "top top", end: () => "+=" + window.innerHeight * 1.5,
    anticipatePin: 1,
    snap: { snapTo: 1 / 4, duration: 0.3, ease: "power2.inOut", delay: 0.1 }, // optional step queue
  },
});
```

`snap` is a UX decision, not a default: it paralyzes inertia for fast scrollers.
Use for a 3-4-state sequence with a step-reading job, and never globally on a
long page. `anticipatePin: 1` avoids a one-frame pan-flash of unpinned
content on fast wheel entry.

## Escape hatches are content, not chrome

A pinned sequence must end by handing the next section the same visual weight
it entered with: header/footer access, "skip to content" anchors, and the
reading rhythm of adjacent sections must survive. Offer a skip link when the
sequence exceeds two screens of scroll, and never place a CTA inside a pinned
zone where the user cannot reach it without finishing the sequence (they can
always reach it, or it is a trap).

## The trap triads to check on the sheet

1. **Anchor breakage:** in-page anchors that used to be reachable are now
   consumed by the pinned scroll distance; link check on every target.
2. **Backward story:** scrub back must retrace the story faithfully;
   out-of-order reversed states confuse orientation mid-scroll.
3. **Mobile reality:** if the mock pins, verify against
   [touch and mobile](05-touch-and-mobile.md) before shipping — most desktop
   pins degrade to a sticky rail or vertical-ized cards.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
