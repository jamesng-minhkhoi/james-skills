# Fresnel and rim

Fresnel = surfaces glow or brighten at grazing angles (edges facing away from
the camera). Its job: silhouette emphasis — the outline as a design element —
or a sci-fi "scanned energy" read. It is the cleanest way to make abstract
geometry read as an *object* without adding lights.

## Core recipe

```glsl
// vNormal/vViewDir are view-space; farness dot product = silhouette factor
float fresnel = pow(1.0 - max(dot(normalize(vNormal), normalize(vViewDir)), 0.0), uPower);
// uPower: 1 = wide soft edge feel; 3 = precise thin edge; 5+ = neon wireframe feel
vec3 color = uBase + fresnel * uRimColor;
// With transparency for the hologram look
float alpha = uBaseAlpha + fresnel * uRimAlpha;
```

| Power | Edge width (from same geometry) | Design use |
| --- | --- | --- |
| 1 | Wide, cushion-like soft halo | Gentle glow, "energy field" feel |
| 2–3 | Crisp defined edge | Product silhouette on page background |
| 5+ | Hairline neon | Schematic scan, data outline |

## When rim glow is the right answer

- Geometry that the camera circles over scroll: the rim keeps the amorphous
  object legible as it turns (silhouette constant while materials change).
- Objects over a busy background: rim separates object from texture without a
  giant drop shadow.
- The "data ghost/scan moment": the page's data question rendered as a glowing
  surface — strong, but only for the one named dramatic moment (delight
  budget).

## When rim fails (name these on the sheet even when choosing)

- White background + white rim: reads as blur or clipping, not glow. Rim color
  must contrast with the page plate behind the canvas.
- Real product photos: rim on a photographed object lies about materiality;
  on product-accurate scenes use it at power ≥ 3 with brand accent only.
- Text/data area on the same layer: rim pulses (animated fresnel) under copy
  read as flashing — keep the rim static wherever text shares the canvas.

## Rim vs. real lighting (the option line)

| Choice | What it implies |
| --- | --- |
| Rim-only (no lights) | Cheapest render, silhouettes only, dreamlike; never a shadow-catcher |
| Rim + one key | The standard "designed still" combo; object + gradient plate |
| Full lighting, no rim | Materiality over silhouette; for product photos resting states |

The sheet names which combination the canvas uses, because that sets the
rendering budget, the fallback plate design, and whether a drop shadow exists
three pixels from the rim.

---
Adapted from [design-on-the-flank](https://github.com/jamesng-minhkhoi/design-on-the-flank)
(Framer Labs/threejs-shaders, MIT); see [NOTICE.md](../../../../../NOTICE.md).
