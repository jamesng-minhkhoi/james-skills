# Scroll story

Use this module when the page's story is *driven by scroll progress*: scrubbing
a sequence, pinning a section while it changes, parallax depth, or feeding a
canvas/shader with scroll velocity. Static-on-view reveals are
[signature motion](../signature-motion/index.md), not this module.

Foundational rule: **the user's finger owns the page.** Scroll-driving
techniques map story progress *from* scroll; they never hijack, reverse, or
lock scroll to a script. A reader must be able to reach every word and CTA by
plain scrolling alone — on an imperfect trackpad, on mobile, with wheel
inertia, and with reduced motion.

| Topic | Use for |
| --- | --- |
| [Scrubbing basics](01-scrubbing.md) | Mapping progress to transforms, mocking first, tolerance bands |
| [Pinned sequences](02-pinned-sequences.md) | Pin-then-narrate sections, step storytelling, safe exit rules |
| [Parallax and depth](03-parallax.md) | Depth layers, drift, rate discipline, textual safety |
| [Scroll-fed canvas](04-scroll-fed-canvas.md) | Scroll as uniform/param driver for WebGL and shader scenes |
| [Touch and mobile](05-touch-and-mobile.md) | Native scroll physics; what pinning means on touch |

---

Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs + gsap-skills, MIT); see [NOTICE.md](../../../../../NOTICE.md).
