# Blender 3D Studio Regression Eval

## Trigger Prompts
1. "Model a parametric 3D-printable enclosure with M3 mounting bosses in headless Blender, export watertight STL/GLB files, and verify with the production gate."
2. "Reconstruct this hardware product from reference photos in Blender (or procedural Three.js) pass-by-pass with camera-matched comparison sheets and a 360 turntable render."
3. "Create an exploded-view assembly animation of our multi-part mechanical device in Blender and render a studio preview."

## Expected Behavior
- Loads `skills/blender-3d-studio/SKILL.md` and the matching reference (`references/hard-rules-and-recipes.md`, `references/image-to-3d-and-threejs.md`, or `references/production-gate-and-print-cad.md`).
- Executes Blender passes through `scripts/agent_runtime.py` or `scripts/headless-run.sh` requiring `AGENT_OK` JSON sentinels.
- Runs numeric/manifold checks (`scripts/production-gate.py`, `scripts/verify-3dprint-tolerances.py`) before visual comparison sheets (`scripts/make-comparison-sheet.sh`).
