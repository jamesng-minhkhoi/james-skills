# Scene fundamentals

A 3D scene is a *composed shot*: what R3F/any renderer show you is a camera
looking into a world. Most creative 3D failures are camera and scale failures,
not geometry failures. Design the frame before building the world.

## The mental model (design-relevant subset)

| Element | Design decision it owns |
| --- | --- |
| Camera (`<PerspectiveCamera>`) | Focal length feel: narrow FOV (~30°) flattens and dignifies a product; wide (~60°+) exaggerates space |
| Position/orbit point | Where the "substance" sits in frame; whole storytelling lives here |
| Aspect | Hero-band scenes must compose for 1440×~700 *and* 390×~500 cropped crops, not one canvas scaled |
| Scale | Units are abstract; pick one reference unit (e.g. 1 ≈ product width) and keep all distances relative to it |
| Background/env | The scene backdrop is a design surface: flat tone, gradient plate, or transparent to page |

## Scale discipline for product shots

Real product dimension beats eyeballing: if the asset ships with real-world
scale, compose from it (e.g. a 70 cm object at 70 units). Otherwise the
camera-to-subject distance ratio nears 1:1 and perspective distortion eats the
silhouette. Cheat-sheet distances: fill-the-frame product ≈ 2.5–4× subject
width at 35° FOV; environmental context ≈ 6–10×.

## The one-shot composition rule

A hero scene is at most 1–2 reiterated compositions (an establishing frame plus
sub-frames). Each deserves deliberate camera angles: pick 3 candidates as
stills, identify what each *emphasizes* (silhouette, material, context), and
keep the one that matches the moment's job from the catalog. The rest is
camera churning.

## On designating "quiet" compositions

Because the scene must appear immediately (pre-hydration and reduced motion),
each scene design names:

- the **quiet frame:** camera position + light look that works as a static
  image without any animation whatsoever; and
- the **edge case:** what renders when WebGL is blocked — usually the project's
  2D hero absorbing the frame with a layout fallback, not a gray rectangle.

An R3F scene whose quiet frame equals a random camera pose is an undesigned
deliverable.

## Common failure triads

| Symptom | Cause | Composition fix |
| --- | --- | --- |
| Product looks "toy-like" | Camera too close/wide (fisheye distortion) | Longer lens, further back, ~30° FOV |
| Scene mood = default gray | No intent in neutral background + basic lighting | Treat gradient/plate/env map as art direction (see materials topic) |
| Subject off-center on resize | Camera aspect assumption breaks at mobile crops | Compose per aspect; use `camera.lookAt` targets re-fit by breakpoint |
| Motionless dead scene | Camera, subject, and light all static in one vector | The design question: which single element moves, and why |

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
