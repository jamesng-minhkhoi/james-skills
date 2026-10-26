---
name: blender-3d-studio
description: Build, reconstruct, verify, and render 3D assets, mechanical CAD parts, 3D-printable STL/GLB solids, and procedural Three.js models using headless Blender (`bpy` / `bmesh`), image-to-3D staged passes, and deterministic `AGENT_OK` production gates.
---

# Blender 3D Studio & CAD Production Engine (`blender-3d-studio`)

Build, reconstruct, verify, and render 3D assets, mechanical assemblies, 3D-printable watertight solids (`STL`/`STEP`/`GLB`), studio turntables, and procedural Three.js web models using headless Blender (`bpy` / `bmesh`) and deterministic verification gates.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

---

## 1. Progressive Disclosure Router

Load only the reference file required for the active job:

| Task / Mode | Reference to Load | Primary Script / Runner |
| :--- | :--- | :--- |
| **Core `bpy` Execution, Sentinel Rules & Assembly Sequences** | [hard-rules-and-recipes.md](references/hard-rules-and-recipes.md) | `scripts/agent_runtime.py`, `scripts/headless-run.sh` |
| **Image -> 3D Reconstruction (Blender Native or Three.js `img2threejs`)** | [image-to-3d-and-threejs.md](references/image-to-3d-and-threejs.md) | `scripts/make-comparison-sheet.sh` |
| **3D-Print Production Gate, CAD Tolerances & Studio Turntables** | [production-gate-and-print-cad.md](references/production-gate-and-print-cad.md) | `scripts/production-gate.py`, `scripts/turntable-preview.py` |

---

## 2. Core Operating Loop (Never One-Shot a 3D Scene)

Every 3D modeling, reconstruction, or animation task follows this 6-step deterministic loop:

1. **Inspect First:** Read the active scene, unit scale (`scale_length == 1.0`), object hierarchy, bounding boxes, and Blender version before mutating anything.
2. **Lock Contract (`spec.json`):** Confirm target purpose (`both`, `print`, or `render-only`), millimeter dimensions ± tolerances, component hierarchy, and camera views ([image-to-3d-and-threejs.md](references/image-to-3d-and-threejs.md)).
3. **Prefer `bpy.data` / `bmesh` Over `bpy.ops`:** Build geometry via explicit data APIs, `bmesh`, modifiers, or Geometry Nodes so scripts run deterministically in headless mode without 3D Viewport context errors.
4. **Disk-First Sentinel Execution:** Write every pass to a `.py` file on disk and run via `agent_runtime.py` or `headless-run.sh`. Never trust exit code `0` without a last-line `AGENT_OK {...}` JSON sentinel ([hard-rules-and-recipes.md](references/hard-rules-and-recipes.md)).
5. **Verify Numeric Gates Before Visual Gates:**
   - Run bounding-box, transform (`scale = 1,1,1`), manifold (`non_manifold_edges == 0`), and `production-gate.py` checks first.
   - Then render multi-angle diagnostic views (`front`, `3/4`, `side`, `top`) and run `make-comparison-sheet.sh` against the reference image.
6. **Transparent Per-Pass Verdict:** State what changed (with exact coordinates/dimensions), what still differs, per-feature `PASS`/`FAIL`/`UNKNOWN` verdicts, and choose one next action (`continue`, `refine-spec`, `refine-code`, `request-input`, `stop`).

---

## 3. Essential Commands & Runtime Harnesses

### Run a Headless Blender Pass with Sentinel Verification

```bash
skills/blender-3d-studio/scripts/headless-run.sh \
  --blend builds/<slug>/scene.blend \
  --script builds/<slug>/scripts/pass_01_blockout.py
```

### Execute Inside Blender or MCP via `agent_runtime.py`

```python
import sys
sys.path.insert(0, "skills/blender-3d-studio/scripts")
import agent_runtime as rt

rt.run_file("/absolute/path/to/builds/<slug>/scripts/pass_01_blockout.py")
```

### Run the 3D-Print & CAD Production Gate (`production-gate.py`)

```bash
python3 skills/blender-3d-studio/scripts/production-gate.py \
  --scene builds/<slug>/scene.blend \
  --spec builds/<slug>/spec.json \
  --report builds/<slug>/reports/gate-report.json \
  --export-dir builds/<slug>/parts
```

### Build a Camera-Matched Reference vs Render Comparison Sheet

```bash
skills/blender-3d-studio/scripts/make-comparison-sheet.sh \
  builds/<slug>/references/ref_front.png \
  builds/<slug>/renders/pass_02_front.png \
  builds/<slug>/renders/cmp_pass_02.png
```

---

## 4. Non-Negotiable Quality & Safety Rules

- **No State Leaks on Preview or Export:** Always restore touched render/transform settings in a `finally` block (or use `preview_render` / `verify_export` from `scripts/agent-verify-lib.py`).
- **Hash-Bound Evidence:** Any geometry, normal, material, or camera change invalidates prior gate reports and media proofs. Never inherit a `PASS` from an older `.blend` or `spec.json` SHA-256 hash.
- **No Fake Single-View Volumes:** Every non-planar 3D asset must be verified from at least 2 non-degenerate camera angles (`front` + `3/4` + `side/top`) so flat planes or broken backfaces are caught immediately.
- **Separate Statuses:** Keep `media`, `motion`, `fit`, and `manufacture` statuses distinct in delivery reports ([production-gate-and-print-cad.md](references/production-gate-and-print-cad.md)).
