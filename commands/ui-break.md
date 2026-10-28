---
description: Stress-test UI components with worst-case data using break-ui
---

Load the `break-ui` skill and stress-test the specified UI component or route:
$ARGUMENTS

Follow the break-ui methodology:
1. Identify all inputs and rendered data props in the component.
2. Feed worst-case edge data:
   - Ultra-long unbroken strings and long names
   - One-letter / minimal values
   - Empty, nil, or undefined fields
   - Huge counts and zero-item arrays
   - Non-Latin script (CJK, Arabic RTL, Cyrillic) and emoji clusters
   - Extreme numbers, currency boundaries, and floating-point edge cases
3. Render behind a "Demo data / Worst case" toggle if applicable.
4. Report every broken layout, clipped text, wrapping failure, or overlap bug with the concrete fix for each.
