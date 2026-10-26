# SVG Primitives, Connectors, 4px Grid & Pre-Output Checklist

This reference provides the exact token palette, SVG primitive markup, connector routing laws, 4px grid complexity budgets, taste checklist, and import/export workflows for `diagram-design`.

---

## 1. Typography & Semantic Palette

### Three typefaces, three jobs

| Role | Default Font | Weight / Style | Used for |
|---|---|---|---|
| **Display** | Instrument Serif | 400 regular & italic | Page title (`h1`), editorial emphasis |
| **UI / Body** | Geist | 400, 500, 600 | Subtitle, prose, card titles, **node names in diagrams** |
| **Mono / Technical** | Geist Mono | 400, 500 | Eyebrows, badges, legends, **technical sublabels**, arrow labels, colophon |

**Never use JetBrains Mono.** Load Google Fonts (`Instrument Serif`, `Geist`, `Geist Mono`).

### Default Warm Paper Palette

```css
:root {
  --paper:       #f5f5f5;               /* page background */
  --paper-2:     #ebebeb;               /* card / framed container bg */
  --ink:         #2d3142;               /* primary text & borders */
  --ink-muted:   #4f5d75;               /* secondary text, default arrows */
  --ink-faint:   #7a8399;               /* captions, colophon */
  --coral:       #eb6c36;               /* PRIMARY ACCENT — focal / highlight */
  --coral-soft:  rgba(235,108,54,0.12); /* focal node fill */
  --slate-soft:  rgba(79,93,117,0.10);  /* secondary node fill */
  --ink-soft:    rgba(45,49,66,0.06);   /* neutral node fill */
  --link-blue:   #2e5aa8;               /* external / I/O accent */
  --link-soft:   rgba(46,90,168,0.10);  /* external node fill */
  --rule:        rgba(45,49,66,0.12);   /* hairlines, card borders */
  --grid-dot:    rgba(45,49,66,0.12);   /* SVG background dot pattern */
}
```

### Node Semantic Color Mapping

| Node type | Fill | Stroke | Tag text | When to use |
|---|---|---|---|---|
| **Focal / Highlight** | `rgba(235,108,54,0.12)` | `#eb6c36` (1.2px) | `#eb6c36` | The 1–2 things the diagram is *about*. **Max 2 per diagram.** |
| **Neutral / Processing** | `rgba(45,49,66,0.05)` | `#2d3142` (1px) | `#2d3142` | Default services, steps, stages |
| **Storage / State / Infra** | `rgba(79,93,117,0.10)` | `#4f5d75` (1px) | `#4f5d75` | Databases, caches, queues, config, state |
| **External / I/O** | `rgba(46,90,168,0.08)` | `#2e5aa8` (1px) | `#2e5aa8` | Clients, 3rd-party APIs, user input, webhooks |
| **Dashed / Optional** | `#f5f5f5` | `#4f5d75` dashed `4,3` | `#4f5d75` | Optional paths, fallbacks, async side-effects |
| **Container / Zone** | `rgba(45,49,66,0.02)` | `rgba(45,49,66,0.22)` dashed `5,4` | `#4f5d75` | Grouping boundary (VPC, cluster, bounded context) |

---

## 2. SVG Primitives & Connector Rules

### Required `<defs>` — dot grid + 3 arrow markers

```svg
<defs>
  <pattern id="dots" width="22" height="22" patternUnits="userSpaceOnUse">
    <circle cx="1" cy="1" r="0.9" fill="rgba(45,49,66,0.12)"/>
  </pattern>
  <marker id="arr-muted" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M0,1.5 L8,5 L0,8.5" fill="none" stroke="#4f5d75" stroke-width="1.3"/>
  </marker>
  <marker id="arr-coral" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M0,1.5 L8,5 L0,8.5" fill="none" stroke="#eb6c36" stroke-width="1.4"/>
  </marker>
  <marker id="arr-blue" viewBox="0 0 10 10" refX="8" refY="5"
          markerWidth="6" markerHeight="6" orient="auto-start-reverse">
    <path d="M0,1.5 L8,5 L0,8.5" fill="none" stroke="#2e5aa8" stroke-width="1.3"/>
  </marker>
</defs>
<rect width="100%" height="100%" fill="url(#dots)"/>
```

**Arrowheads are open chevrons (`fill="none"`), never filled triangles.** Draw arrows before boxes so z-order puts lines behind nodes.

### Six Non-Negotiable Connector Rules

1. **Rounded right-angle (orthogonal) connectors are mandatory.** Never use diagonal `<line>` or slanted paths between off-axis nodes. Every bend must be a quarter-arc with `r=8` (`r=6` minimum for tight layouts). See [type-architecture.md](type-architecture.md) for the elbow-path formula.
2. **Label-to-connector margin: 6–10px gap, always.** Place the label centered above (or beside, for vertical segments) the line with a minimum 6px gap between the bottom of the label's opaque mask rect and the connector stroke.
3. **No overlapping connectors.** Two connectors must never share a stroke path or run on top of each other. When two orthogonal arrows cross at a point, use the bridge/hop primitive ([type-architecture.md](type-architecture.md)). Offset parallel arrows by ≥12px.
4. **Shared edge → fan the attach points.** Spread multiple connectors along a shared box edge with ≥12px between adjacent attach points (`offset = L * k / (N + 1)`).
5. **Do not pass behind non-endpoint boxes** unless geometrically unavoidable on a direct orthogonal path (in which case use `stroke-dasharray="4,3"` and place the label at the visible source end).
6. **A label mask must not overlap a node drawn after it.** Place labels on open canvas segments and verify with `python3 scripts/verify-geometry.py <file>`.

### Node Box & Arrow Label Markup

```svg
<!-- Node Box: 1. Opaque paper mask -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="#f5f5f5"/>
<!-- 2. Styled box -->
<rect x="X" y="Y" width="W" height="H" rx="6" fill="FILL" stroke="STROKE" stroke-width="1"/>
<!-- 3. Rectangular type tag (rx=2, NOT a pill) -->
<rect x="X+8" y="Y+6" width="28" height="12" rx="2" fill="transparent" stroke="STROKE@0.40" stroke-width="0.8"/>
<text x="X+22" y="Y+15" fill="STROKE@0.8" font-size="7" font-family="'Geist Mono', monospace"
      text-anchor="middle" letter-spacing="0.08em">API</text>
<!-- 4. Node name (Geist sans) -->
<text x="CX" y="CY+2" fill="#2d3142" font-size="12" font-weight="600"
      font-family="'Geist', sans-serif" text-anchor="middle">Node Name</text>
<!-- 5. Technical sublabel (Geist Mono) -->
<text x="CX" y="CY+18" fill="#4f5d75" font-size="9"
      font-family="'Geist Mono', monospace" text-anchor="middle">tech:port</text>

<!-- Arrow Label: Mask sits 14px above arrow (8px text + 6px gap) -->
<rect x="MID_X-18" y="ARROW_Y-20" width="36" height="12" rx="2" fill="#f5f5f5"/>
<text x="MID_X" y="ARROW_Y-11" fill="#7a8399" font-size="8"
      font-family="'Geist Mono', monospace" text-anchor="middle" letter-spacing="0.06em">WRITE</text>
```

---

## 3. 4px Grid & Complexity Budget

All font sizes, padding, node dimensions, gaps, and x/y coordinates must be divisible by 4 (exempt: stroke widths `0.8, 1, 1.2`, opacity values, and `22x22` dot pattern).

| Limit | Rule | Limit | Rule |
|---|---|---|---|
| Max nodes | 9 | Max tree / org depth | 4 (max 12 org nodes) |
| Max arrows / transitions | 12 | Max layers (stack/pyramid) | 6 |
| Max coral elements | 2 | Max circles (venn) | 3 |
| Max lifelines (sequence) | 5 | Max radar axes / series | 5 (1 focal) |
| Max lanes (swimlane) | 5 | Max bars / line series | 8 bars / 5 series |
| Max items (quadrant) | 12 | Max tasks (Gantt) | 12 |
| Max entities (ER) | 8 | Max points (scatter) | 30 |
| Max nesting levels | 6 | Max motion ([animation.md](animation.md)) | 8 steps, 12 items, 2 simultaneous |

---

## 4. Pre-Output Checklist (Taste Gate)

- **Type & Remove Test:** Chose semantic pattern ([semantic-patterns.md](semantic-patterns.md)) and loaded `type-*.md`? Removed any node, arrow, or label that layout/color already signals?
- **Signal:** Coral used on ≤2 elements? Bottom horizontal legend strip covers every type used and `viewBox` height expanded by ~60px?
- **Accessible SVG:** `<svg role="img" aria-labelledby="<slug>-title <slug>-desc">` with `<title>` as first child before `<defs>`?
- **Geometry & Self-Check:** Arrows drawn before boxes? Every off-axis connector uses `r=8` orthogonal elbows? Every arrow label has a `#f5f5f5` mask and 6–10px gap? All coords divisible by 4? Passed `python3 scripts/self_check.py <file>` and `python3 scripts/verify-geometry.py <file>`?
- **Variants & Import/Export:** See [output-spec.md](output-spec.md), [import-drawio.md](import-drawio.md), [import-mermaid.md](import-mermaid.md), [export.md](export.md), [primitive-annotation.md](primitive-annotation.md), [primitive-sketchy.md](primitive-sketchy.md), and [primitive-terminal.md](primitive-terminal.md).
