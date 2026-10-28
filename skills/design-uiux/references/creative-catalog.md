# Creative techniques catalog

Use this router when the request asks for a **signature moment**: an animated
hero, scroll story, kinetic typography, a 3D or shader-backed scene, a
first-run or milestone moment worth remembering. Plain landing, dashboard, and
app-screen design stays in the surface references; this library is for the
moment that makes a product unmistakable.

Read one module index, then only the topic files the request calls for. Never
read the whole library to start a task.

## Decide the discipline first

Creative work still answers the research question from step 3 of the loop.
Before picking a technique, write the moment's job in one sentence: what the
viewer should feel, know, or do, and how often they meet it. A technique with
no stated job is a decoration, and `slop-and-consistency` will reject it.

Two gates apply before any technique below:

- **Frequency gate** — the [motion and gesture](motion-and-gesture.md)
  frequency table decides for every creative technique: 100+ encounters a day
  gets platform default or
  nothing. Landing-page, first-run, and milestone moments are rare by nature
  and may earn more, but a technique for one of those rare moments that ends
  up inside the product's daily flow is judged by the frequency table, not by
  its marketing origin.
- **Honesty gate** — three.js, GLSL, and canvas scenes add hundreds of
  kilobytes and heavy assets. Before a 3D or shader option is presented: state
  the moment that earns it; declare the estimated cost as `unverified` (it is
  only a number to be measured from the real build later); and present a
  materially cheaper plain-2D twin as its own option whenever one plausibly
  exists. An absent twin is a named decision, never an assumption: the sheet
  states the concrete 2D constraint that defeats it, or the twin is on the
  sheet. The option sheet is not blocked on a measurement that no build can
  produce yet — the measured chunk size moves to the handoff rules (see
  [three canvas · SSR and budget](library/three-canvas/06-ssr-and-bundle.md)).

| Context | Load |
| --- | --- |
| Hero, reveal, counter, pointer delight on any page or screen | [signature motion](library/signature-motion/index.md) |
| Narrative controlled by scroll position | [scroll story](library/scroll-story/index.md) |
| Real 3D scene: product view, particle field, spatial walkthrough | [three canvas](library/three-canvas/index.md) |
| Shader-backed look: gradient fields, noise, dissolve, displacement, refraction-ish surfaces | [shader recipes](library/shader-recipes/index.md) |
| Mobile-first signature moment in Expo | [signature motion](library/signature-motion/index.md), then the module's Reanimated topics |

A combined request reads multiple modules' indexes but never every topic under
them. For a scroll-driven WebGL hero: scroll story, three canvas, plus the
shader topic that names the look.

## Adapting source material

The snippets were preserved from MIT sources and adapted to our default stack
(Next.js + Framer Motion + react-three-fiber on the web; Expo + Reanimated on
mobile). Follow the code's technique, not its environment: when a snippet shows
a standalone canvas or GSAP tween loop, adapt it to the project contract —
client components, `useEffect` cleanup, motion-value APIs, and the tokens and
principles already locked for the product. Any snippet that contradicts an
established project rule loses.

Stack translation:

| Source shows | Our stack uses |
| --- | --- |
| GSAP timeline in a plain page | Framer Motion variants and motion values first; GSAP only when sequencing demands it |
| ScrollTrigger pin and scrub | `useScroll` / `useTransform` from Framer Motion, or GSAP ScrollTrigger when pinning |
| Raw `three` bootstrap (scene, camera, renderer, rAF loop) | `@react-three/fiber` (`<Canvas>`, `useFrame`) |

## Rules that hold across all modules

- Creative moments get real content and real tokens from the first rendering:
  the reveal rehearses the actual headline at actual widths.
- Every animated moment names its reduced-motion behavior on the option sheet
  per the accessibility rules in [motion and gesture](motion-and-gesture.md):
  a static variant that still reads correctly. If no reduced variant can carry
  the message, cut the technique — that is the creative-specific rule on top
  of the owner's, not a second definition of reduced motion.
- Web 3D and shaders are client-side only: dynamically import the scene below
  the first paint, never block hydration, and never claim a chunk size you
  did not measure from the build output.
- Do not downgrade an advanced request into a basic card or fade. If something
  is infeasible under the project contract, name the concrete constraint and
  propose the closest behavior that survives it.
- Verify with the proof ladder in [ontology](../../_shared/ontology.md): name
  the highest rung reached — an option sheet or mockup is at best `declared`;
  promote a claim only when the artifact for that rung was actually observed.

---

Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank),
which integrates [Framer Labs](https://github.com/fredm00n/framerlabs) and
[GreenSock's gsap-skills](https://github.com/greensock/gsap-skills). Both
upstreams are MIT; see [NOTICE.md](../../../NOTICE.md).
