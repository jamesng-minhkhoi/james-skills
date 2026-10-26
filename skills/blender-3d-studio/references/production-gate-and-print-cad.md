# 3D-Print Production Gate, CAD Tolerances & Studio Rendering

This reference covers the deterministic manufacturing/print gate (`production-gate.py`), fastener/clearance tolerances (`verify-3dprint-tolerances.py`), and headless turntable preview rendering (`turntable-preview.py`).

---

## 1. The Production Contract (`spec.json`)

Whenever a part will be 3D-printed, CNC-machined, or assembled with real hardware:

1. **Author `builds/<slug>/spec.json` before detailing:**
   - Units in millimeters (`mm`), Blender scene in meters (`scale_length == 1.0`) with applied transforms (`scale = (1.0, 1.0, 1.0)`).
   - One Blender object per printed part (`object.name == spec_part["object"]`).
   - Declare `target_dims_mm` ± `tol_mm`, `material`, `process` (`FDM`, `SLA`, `SLS`, `MJF`), `orientation_up`, `min_wall_mm`, `max_overhang_deg`, and `expected_shells` (`1` for a single contiguous solid).
   - Declare every functional bore/boss/slot with axis, center, diameter ± tolerance, and mating fastener standard.
2. **Union Overlapping Solids Before Exporting:**
   - Two intersecting bodies exported to STL remain `2` shells (`expected_shells` failure) unless boolean-unioned into a single manifold solid (`non_manifold_edges == 0`, `non_planar_faces` controlled, positive signed volume).
3. **Place Bore Ring Probes Inside the Bore (`1.3–1.5 mm` depth):**
   - Never place a raycast ring probe exactly on the entry surface plane (`0.0 mm`), where surface grazing yields false misses.

---

## 2. Running the Deterministic Production Gate

Run `scripts/production-gate.py` in an isolated process before any manufacturing or STL delivery claim:

```bash
python3 skills/blender-3d-studio/scripts/production-gate.py \
  --scene builds/<slug>/<file>.blend \
  --spec builds/<slug>/spec.json \
  --report builds/<slug>/reports/gate-report.json \
  --export-dir builds/<slug>/parts
```

### Gate Exit Codes
- `0`: All geometric, manifold, dimension, bore, wall/overhang, and STL round-trip checks passed.
- `1`: One or more part requirements failed (inspect `failed[]` in `gate-report.json`).
- `2`: Spec or scene incomplete.
- `3`: Execution / Blender error.

### Coverage Audit (Read-Only Host Check)
Verify that all declared parts, wall limits, and SHA-256 bindings (`scene + spec + STL`) are up to date without launching Blender:

```bash
python3 skills/blender-3d-studio/scripts/production-gate.py \
  --audit-report builds/<slug>/reports/gate-report.json \
  --scene builds/<slug>/<file>.blend \
  --spec builds/<slug>/spec.json \
  --export-dir builds/<slug>/parts \
  --report builds/<slug>/reports/coverage-audit.json
```

### Tolerance & Fastener Clearance Check
For printed assemblies with mating pins, bores, press-fits, or sliding fits, run:

```bash
/Applications/Blender.app/Contents/MacOS/Blender --factory-startup --disable-autoexec -b builds/<slug>/<file>.blend \
  --python skills/blender-3d-studio/scripts/verify-3dprint-tolerances.py
```

### Honest Scope of Geometry Gates
A passing `production-gate.py` report proves **watertight manifold topology, bounding dimensions, bore diameters, wall/overhang screens, and STL round-trip integrity**. It does **not** prove physical load capacity, post-shrinkage press-fit feel, thermal duty, or real motor torque — report physical test status separately (`manufacture: BLOCKED` until physical pilot evidence is supplied, or `NOT_REQUESTED` for render-only tasks).

---

## 3. Studio Turntable & Multi-View Diagnostic Renders

Use `scripts/turntable-preview.py` inside headless Blender to render diagnostic multi-angle sheets (`front`, `3/4`, `side`, `back`, `top`, `underside`) or a 360° turntable sequence:

```bash
/Applications/Blender.app/Contents/MacOS/Blender --factory-startup --disable-autoexec -b builds/<slug>/<file>.blend \
  --python skills/blender-3d-studio/scripts/turntable-preview.py
```

And use `scripts/agent-verify-lib.py` (`preview_render`, `verify_export`, `check_scene_integrity`) inside your pass scripts to assert postconditions while automatically restoring all render settings in `finally`.
