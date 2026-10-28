# Three canvas

Use this module when the design needs a real 3D scene: product geometry, a
particle/morph/field moment, spatial walkthrough, or material studies. Before
proposing it, pass the [honesty gate](../../creative-catalog.md#decide-the-discipline-first):
state the bundle cost, the moment that earns it, and the 2D alternative.
No scene is *decided* here — scenes are designed here and built by
[frontend-web-engineering](../../../../frontend-web-engineering/SKILL.md).

Stack default on web: `three` via `@react-three/fiber` (R3F), helpers from
`@react-three/drei` where they cut boilerplate honestly. Direct `three`
bootstrap is reserved for projects not on React.

| Topic | Use for |
| --- | --- |
| [Scene fundamentals](01-scene-fundamentals.md) | Camera, scale, aspect, and the R3F mental model |
| [Geometry, particles, instancing](02-geometry-and-particles.md) | Shapes, arrays, morphing, density |
| [Materials and lighting](03-materials-and-lighting.md) | Surface look, studio setups, shadows |
| [Textures and assets](04-textures-and-assets.md) | Image maps, environment maps, models, loading states |
| [Motion inside the scene](05-scene-animation.md) | Frame-driven and scroll-driven motion; interaction hooks |
| [SSR and bundle honesty](06-ssr-and-bundle.md) | Next.js reality: dynamic import, budget, measured claims |

Mobile-first note: on Expo, `react-native-skia` is the default shader/graphics
answer; real `three` on native is a last resort (see
[signature motion · mobile](../signature-motion/05-mobile-reanimated.md)).

## Design-level decisions this module forces

Every scene proposal answers, on the option sheet:

1. **Anchors:** what is the scene keyed to — viewport scroll, pointer, time. Name the single drive source.
2. **Scale:** does the scene fill a hero, a band, or the whole page. Whole-page scenes change page height contracts.
3. **The quiet frame:** what the scene shows at reduced motion / before fonts / with WebGL unavailable.
4. **Counted cost:** estimated geometry count, material complexity, and pixel ratio caps proposed up front.

---

Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
