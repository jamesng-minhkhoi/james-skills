# Blender Operational Hard Rules, Execution Recipes & Assembly Sequences

This reference defines the execution contract (`agent_runtime.py` + `headless-run.sh`), operational hard rules, and staged assembly/exploded-view rules for `blender-3d-studio`.

---

## 1. Explicit Execution Context & Sentinel Contract

Never assume MCP Python locals persist across tool calls, and never trust process exit code `0` alone when running Blender scripts.

### Disk-First Execution via `agent_runtime.py`
Write every Blender mutation or verification pass to a reviewed `.py` file on disk and execute it through `agent_runtime.py`, which owns the namespace, `__file__`, traceback formatting, and last-line `AGENT_OK` / `AGENT_FAIL` JSON sentinel:

```python
import sys
sys.path.insert(0, "skills/blender-3d-studio/scripts")
import agent_runtime as rt

rt.run_file("/absolute/path/to/reviewed-pass.py")
# Emits last stdout line: AGENT_OK {...} | AGENT_FAIL {...}
```

### Isolated Headless Execution via `headless-run.sh`
For headless builds, verification passes, or fault probes, run Blender through `scripts/headless-run.sh`:

```bash
skills/blender-3d-studio/scripts/headless-run.sh \
  --blend /absolute/path/to/scene.blend \
  --script /absolute/path/to/pass.py
```

Exit codes of `headless-run.sh`:
- `0`: Last stdout line was `AGENT_OK {...}`
- `1`: Last stdout line was `AGENT_FAIL {...}`
- `2`: Script exited without emitting a sentinel (silent abort, `sys.exit`, or crash)
- `3`: Blender crashed or returned a non-zero Python exit code

---

## 2. Operational Hard Rules

| Trigger | Required Behavior | Enforcement |
| :--- | :--- | :--- |
| **Every new pass/session** | Read active scene, file path, Blender version, unit scale (`scale_length == 1.0`), and active camera; include all imports and assertions inside the disk script. | `agent_runtime.run_file` + `rt.load_lib` |
| **Any tool reply** | Inspect structured `AGENT_OK` / `AGENT_FAIL` status, traceback, and declared postconditions. Transport success alone is never proof. | `headless-run.sh` exit `0/1/2/3` |
| **Timeout after mutation** | Mark outcome `UNKNOWN`; read and reconcile scene state before sending another mutation. Never infer rollback or blindly resend. | Controller discipline |
| **Preview or export check** | Use a disposable headless process or restore every touched render/transform setting in a `finally` block (`preview_render` and `verify_export` in `agent-verify-lib.py`). | `agent-verify-lib.py` |
| **Temporary transform for export/plate** | Restore **every axis touched** (`x`, `y`, and `z`) in `finally`, then re-read one placed object and assert its world coordinates. | Controller discipline |
| **Geometry or motion change** | Invalidate affected topology, contact, load, and export evidence. Never inherit a gate report from an older scene/spec SHA-256 hash. | `production-gate.py` SHA-256 binding |
| **Surprising geometry measurement** | Validate the measurement checker before changing geometry. For small evaluated meshes far from origin, translate vertices to a local centroid and use `float64` scalar arithmetic for signed volume. | `production_gate/` volume checker |

---

## 3. Removable Assembly & Exploded-View Sequences

Use this 8-step sequence for assembly/exploded films of multi-part mechanical or printed products:

1. **Contract before motion:** Identify every physical unit, assembly receiver, final datum, fastener pairing, and dependency while keeping the approved source scene immutable.
2. **Unit manifest:** Register each printed/purchased part once with reversible final transforms; pair rigid screw heads and threads.
3. **Dependency graph:** Order `receiver -> internal hardware -> mating unit -> retention -> wiring -> covers`.
4. **Staging layout:** Separate waiting subassemblies in world space and camera projection with gaps derived from actual bounding envelopes.
5. **Swept-path verification:** Test arrivals and seats through time against already installed parts (`waiting`, `transit`, and `terminal mating` phases). A correct final seated pose does **not** prove the waiting pose or approach path is collision-free.
6. **Short animatic (`<= 120` frames):** Inspect the critical interval, analogous joints, and first/last camera framing before any full render batch.
7. **Frozen render manifest:** Lock input `.blend` hash, renderer/device, samples, resolution, camera, and frame range. Any geometry/camera/lighting change starts a new frame directory.
8. **Decoded delivery:** Verify frame count, dimensions, duration/fps, and decoded frames while keeping `media`, `motion`, `fit`, and `manufacture` statuses separate.
