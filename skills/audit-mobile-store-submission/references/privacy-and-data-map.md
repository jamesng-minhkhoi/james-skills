# Privacy, data, permissions, and SDK map

Build a data map from code, native manifests, SDK documentation, network
behavior, privacy policy, and store forms. Reconcile:

- data collected, shared, linked to identity, used for tracking, retained, and
  deleted;
- first-party and third-party SDK behavior, including analytics, ads, crash
  reporting, auth, payments, maps, social login, and third-party AI;
- permission rationale, timing, minimum scope, denied path, and whether a core
  feature works without unnecessary permission;
- Apple App Privacy details, privacy manifest and required-reason APIs, ATT,
  account deletion, Sign in with Apple, export compliance, and privacy policy;
- Google Play Data Safety, data deletion questions, privacy policy, ads,
  restricted permissions, target audience/content, and sign-in details.

For family, baby, education, health, or development products, distinguish the
person using the app from the person whose data is recorded. Audit age-rating,
target-audience, child-safety, health/medical, and data-retention implications
without inferring a legal classification from the product name alone.

For every material store claim, create a claim-to-proof row: exact wording,
screen or route, runtime/provider evidence, screenshot or recording, region,
audience, rights/authorization, and reviewer-facing explanation. Use the claims
reference for health, child/family, AI, financial, safety, UGC, and protected
third-party content.

Flag any declaration that is broader, narrower, older, or less specific than
the actual binary and SDK behavior. A “no data collected” answer requires
evidence, not intuition.
