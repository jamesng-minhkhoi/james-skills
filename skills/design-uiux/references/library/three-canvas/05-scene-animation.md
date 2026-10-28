# Motion inside the scene

Scene motion has four drivers. Pick **one primary driver per moment**;
composing more than one unnamed driver creates behaviors nobody can design
against.

## Driver map

| Driver | Jobs it serves | Design contract line |
| --- | --- | --- |
| Time (idle) | Ambient life: rotation drift, pulse, float | "breathes ±1.5° at 8 s period; pauses off-screen" |
| Pointer | Inspection: turntable tilt, hover highlight | "±12° lean toward pointer within bounds; static twin exists" |
| Scroll | Navigate: camera path, reveal order, canvas feeds from [scroll story](../scroll-story/04-scroll-fed-canvas.md) | "progress 0→1 maps to camera A→B; keyframes at 0/.5/1" |
| Interaction/click | Cause-effect: trigger morph, snap state | "click marks candidate → burst + settle in 600 ms" |

Frame-driven motion is `useFrame((state, delta) => …)` in R3F; all `delta`
scaled, never per-frame constants — 120 Hz displays must not double speed.

## Idle motion: designed amplitude, not wobble

Idle drift is not decoration; it is the *alive* contract between scrolls and
between interactions. Rules:

- Amplitude is small and named (degrees or percent of subject size) — idle
  motion reads as design when the viewer can't consciously track it, breaks
  as noise when it loops visibly.
- Loop period ≥ 4 s for organic drift; visible loop seams always defect.
- Idle motion pauses on `visibilitychange`, off-screen (IntersectionObserver +
  `frameloop` control), and under `prefers-reduced-motion` (renders the quiet
  frame).

## Morphing: states with names, not tweens

A morphing moment (particles rearranging, geometry reshaping) is a *state
machine*, and design names its states the way flows are named:
`invested → transferred → settled` — not "morph instance 2". Each state:

1. has a **designed end-point** (a legitimate still);
2. has a **transition duration and ease** matched to the semantic weight
   (money movement goes slower than decorative flicker);
3. uses the **same easing family** as the page's DOM motion, so scene and
   interface read as one product (align the tokens).

## Pointer discipline

- Pointer targets are raycast-designed: what is *hoverable/clickable* in 3D
  gets the same affordance language as DOM (cursor, highlight, outline) —
  invisible hit zones violate "explicit beats clever".
- Touch has no persistent pointer: touch interactions either act as taps (no
  lean/tilt tracking) or as direct drag with the
  [drag contract](../../motion-and-gesture.md). Never render a hover-only
  teaching state on touch.
- All event handlers on the canvas attach through R3F's event system, which
  ties raycasts to the model — events registered in `useEffect` against the
  raw element bypass the raycast order and are harder to keep in design sync.

## When the scene moves the DOM instead

Camera motion pulling page layout (parallax between canvas and text, scene
frame rescale on scroll) is the tail-to-head pattern — the design must define
what the text layer does while the camera travels (fade to the rim, park above
the fold, follow the focal plane). An unplanned text-during-camera-travel
experience reads as broken rather than immersive.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
