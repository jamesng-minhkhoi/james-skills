# Materials and lighting

Material and light decide whether a scene reads as *designed* or as a default
render. The design task is art direction: choose a surface language and a
lighting setup that serve the product's mood, then name both in the option
sheet so engineering can reproduce them with tokens.

## Surface language, by moment job

| Job | Material direction |
| --- | --- |
| Precision/professional (finance, dev tools) | Matte or lightly rough metal, subtle clearcoat; bulb-free neutral env; low gloss highlights |
| Warm/human (community, care) | Soft matte, warm tints, slight subsurface feel; avoid hard speculars and mirror worlds |
| Wet/vivid (energy, sport) | Higher roughness contrast, saturated emissive accents, punchy rim |
| Playful (kids, games) | Plastic-looking toon or flat-shaded materials; hard-stylized lighting instead of realism |

`MeshStandardMaterial`/`PhysicalMaterial` roughness/metalness picks the family;
a custom shader look belongs to [shader recipes](../shader-recipes/index.md).

## Studio setups worth naming

Name the setup, don't improvise during implementation review:

| Setup | Composition job | Notes |
| --- | --- | --- |
| Three-point | Balanced product stills | Key + fill + rim; rim intensity decides silhouette vs. seam |
| Ambient studio (env map only) | Clean, modern, even | IBL from a neutral HDRI or a generated gradient; fastest to look "right" |
| Single dramatic | Label focus, hero mood | One key light; backgrounds build depth. Never at subtle moments |
| Transparent/void | Scene blushes into the page | No ground plane; shadow catcher only if contact grounding matters |

Lighting truths that constrain design choices:

- **Key light direction is composition.** Top-left keys read classic; rear rim
  reads dramatic; dead-center frontal reads flat. Choose per the moment's job.
- **A scene lit only by toneless env reads as "unlit demo".** At least one
  directional contribution (key or rim) gives surface detail — those micro
  highlights are what sells material in motion.
- **Env maps and IB roles:** environment *radiance* gives reflections; a simple
  gradient environment is very cheap and reads as designed when paired with a
  visible gradient plate in the page design instead of clipping to the canvas.

## Shadows (choose one, name it)

| Choice | When |
| --- | --- |
| No shadows | Void/backdrop scenes; cheaper and often the designed look |
| Contact-only (shadow catcher plane) | Product floating over a designed gradient plate; grounds it with one cheap pass |
| Full soft shadows (PCF/soft map) | Architectural/scene context where geometry sits in a world |

Full shadow maps are the most expensive realism feature and gain little for
hero-band canvases; the sheet should default to the first two.

## Color management non-negotiables

- Render in sRGB output (R3F's default when configured) and design the color
  palette in the page's tokens, then map: scene materials take tokens, not
  arbitrary hex. A scene whose accent color drifts from the brand ramp is a
  missed check, not a taste note.
- Tone mapping choice is aesthetic: ACES softens overshoot (safe default),
  none keeps pure emissive pops. Name it on the sheet because it changes how
  colors land.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs, MIT); see [NOTICE.md](../../../../../NOTICE.md).
