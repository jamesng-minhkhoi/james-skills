# CV & Career-Ops Regression Eval

## Trigger Prompts
1. "Rewrite my resume bullets using the Google XYZ formula and export a 2-page monochrome PDF and diagnostic audit report for a Staff Engineer role."
2. "Evaluate this job description with the A–G career-ops framework, check for ghost-job or compensation red flags, and give me my STAR+Reflection interview plan."
3. "Draft a <=200 character LinkedIn outreach message to the hiring manager and a tailored cover letter for this AI Product Engineer role."
4. "Walk through this employment offer contract clause-by-clause and list consistency deltas, negotiation topics, and questions for my employment lawyer."

## Expected Behavior
- Loads `skills/cv-and-career-ops/SKILL.md` and the matching reference (`references/cv-pipeline-and-xyz-design.md`, `references/job-evaluation-a-to-g.md`, or `references/outreach-cover-and-offer-prep.md`).
- Enforces zero fabrication of employers, titles, or metrics; uses scope indicators when analytics are private.
- Delivers complete Blocks A–G on job evaluations, active-voice zero-em-dash cover letters (`350–420` words), and descriptive (non-legal-advice) clause walks on offer contracts.
