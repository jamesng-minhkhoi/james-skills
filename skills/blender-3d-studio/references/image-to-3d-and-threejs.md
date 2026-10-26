# Image-to-3D Reconstruction (Blender Native & Procedural Three.js)

This reference governs reconstructing objects, hardware, or characters from reference images into either **native Blender geometry (`bpy` / `bmesh`)** or **procedural Three.js code (`img2threejs`)**, with camera-matched comparison sheets and strict anti-overclaiming rules.

---

## 1. Phase -1 — Pre-Contract Discovery & Multi-Modal Dossier

Before writing `spec.json` or running any construction pass on a mechanical, industrial, or detailed reference:

1. **Pin Primary Reference Bytes (`source-registry.json`):** Record SHA-256 hashes and source authority (`primary_photo`, `owner_dimension`, `technical_drawing`, or `secondary_generated_sheet`) in `builds/<slug>/references/`.
2. **Engineering & CMF Decomposition (`super-detail-prompt.md`):** Deconstruct every visible and occluded sub-assembly into millimeter envelopes, symmetry/asymmetry, coaxial pivot coordinates, fastener families, and PBR/OpenPBR material finishes.
3. **Confirm Target Purpose (Socratic Gate):** Confirm with the user whether the target is:
   - `both` (3D-printable closed manifold solids + studio media)
   - `print` (watertight CAD/STL with manufacturing tolerances)
   - `render-only` (hero stills, turntable, or procedural Three.js web prop)

---

## 2. Native Blender Staged Construction (`bpy` / `bmesh`)

Never one-shot a complex mesh. Build and verify in 5 ordered stages under `builds/<slug>/`:

| Stage | Focus | Required Verification |
| :--- | :--- | :--- |
| **Pass 1 — Blockout** | Primary silhouette, overall bounding dimensions, coordinate frame, camera match | Numeric bounding-box check + silhouette overlay |
| **Pass 2 — Primary Form** | Shared surfaces, body transitions, bevel hierarchy, panel boundaries | Multi-angle (`front`, `side`, `3/4`, `top`) clay/workbench render |
| **Pass 3 — Functional Detail** | Apertures, bores, fasteners, ribbing, seams, separate moving parts | Component coverage check + close-up crop inspection |
| **Pass 4 — Materials & Lighting** | Independent PBR channels (albedo, roughness, metallic, normal), studio 3-point or HDRI lighting | De-lit vs lit material response check |
| **Pass 5 — Polish & Delivery** | Clean naming, applied transforms (`scale = 1,1,1`), manifold check, turntable/hero render | `make-comparison-sheet.sh` + `production-gate.py` |

### Camera-Matched Comparison Sheet
After each visual pass, generate a side-by-side comparison sheet before choosing a verdict:

```bash
skills/blender-3d-studio/scripts/make-comparison-sheet.sh <reference.png> <render.png> <comparison-sheet.png>
```

---

## 3. Procedural Three.js Track (`img2threejs`)

When the target deliverable is a real-time web 3D model (`Group` factory `createObjectNameModel(spec, options)` in TypeScript + Three.js):

1. **Structured Spec Before Code:** Define the component hierarchy, `topologyClass` (`lathe`, `extrude`, `tube`, `subd-box`, `instanced-array`), PBR material scalars (`metalness`, `roughness`, `clearcoat`, `ior`), and `featureReviewTargets`.
2. **Projection-First for Patterned Finishes:** For patterned surfaces, decals, or specific reference skins, solve the camera, de-light the reference crop, and project/bake onto UVs rather than faking complex photo patterns with noisy procedural shaders.
3. **Action-Ready & Explodable Hierarchy:**
   - Name every mesh and expose pivots/sockets on `root.userData.sculptRuntime`.
   - Keep distinct functional parts on separate named meshes (never fuse separate components into a single inert lump).
   - Explode layouts by scaling part offsets about the model center so every part is inspectable and clickable.
4. **Multi-Angle Verification:** A non-planar 3D form must hold from at least 2 orbit camera angles (`front/hero` + `3/4` + `side/top`) to catch flat-plane silhouette fakes.

---

## 4. Reference Review Rubric & Transparency Contract

After every pass, state explicitly:
1. **What changed** (with exact coordinates, dimensions, or parameters).
2. **What still differs** from the reference (unseen back/underside inference, simplified details, camera delta).
3. **Per-feature verdict:** Give every critical feature an explicit `PASS`, `FAIL`, or `UNKNOWN` verdict with its proof view and falsifier — never hide a failed identity feature behind a single global score.
4. **Next action:** Choose exactly one of `continue`, `refine-spec`, `refine-code`, `request-input`, or `stop`. Two repeats of the same visible failure require changing the modeling approach rather than tweaking the same parameter.
