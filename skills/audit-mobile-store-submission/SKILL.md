---
name: audit-mobile-store-submission
description: Audit iOS App Store and Google Play submission readiness for native and Expo apps, including rejection remediation, artifact inspection, portal state, and review evidence. Use before a submission to inspect the production artifact, installability, runtime behavior, reviewer access, metadata, display-name identity, screenshots, privacy disclosures, permissions, monetization, public URLs, account deletion, policy, and current deadlines. Produce evidence-backed blockers and open gates; do not submit or change store dashboards unless asked.
---

# Audit Mobile Store Submission

Determine whether a specific production artifact is ready for Apple App Store,
Google Play, both, or neither. Audit the shipped binary, store listing, public
URLs, reviewer access, privacy declarations, and portal state as separate
evidence surfaces.

Read [the rejection patterns](references/rejection-patterns.md) when a review
has failed or the app is low-effort, template-heavy, AI-generated, or in a
saturated category. Read [the current platform watch](references/current-platform-watch.md)
on every release audit because policy deadlines and requirements change. Use
[the evidence matrix](references/submission-evidence-matrix.md) to label what is
implemented, observed, portal-confirmed, or still unknown.

For every audit, also use [the release evidence contract](references/release-evidence-contract.md).
For Review or Release mode, use [the reviewer test matrix](references/reviewer-test-matrix.md)
and [the portal state model](references/portal-state-model.md). When a binary is
available, use [the artifact inspection guide](references/artifact-inspection.md)
and the bundled inspection script. For family, health, AI, financial, safety,
regulated, or protected-content apps, read [claims and regulated content](references/claims-and-regulated-content.md).
After completing an audit, use [friendly PDF reporting](references/pdf-reporting.md)
and `scripts/render-audit-pdf.py` when a non-technical deliverable is useful.

Shared vocabulary: [ontology](../_shared/ontology.md). Use its proof ladder, verdicts, and finding IDs.

## Operating rules

- Audit the exact version, build number/version code, bundle ID/package name,
  signing identity, track, storefronts, and artifact submitted or intended for
  submission. Never generalize from another build.
- Separate source/local evidence from runtime, native-device, provider,
  App Store Connect, Play Console, production, and legal evidence.
- Treat forum discussions as rejection signals and debugging clues, not policy
  authority. Verify each conclusion against the current official Apple or
  Google source.
- When a rejection message, portal export, screenshot, or recording is
  provided, preserve its exact reviewed version/build, review date, device,
  submission ID, guideline, and requested evidence. A later resubmission is a
  new evidence snapshot; never assume the fix is present in the reviewed
  artifact.
- Treat the signed artifact/runtime as the authority for shipped behavior, the
  store portal as the authority for listing and processing state, and source
  code/configuration as evidence of intent or risk only. When they conflict,
  report the conflict instead of averaging the claims.
- Do not guess legal ownership, privacy answers, age ratings, health claims,
  financial claims, content rights, account credentials, or portal state.
  Mark them **Unknown** and request the missing evidence.
- Do not submit, release, change metadata, alter a policy declaration, or
  contact a reviewer unless the user separately authorizes that action.
- Do not call an app “ready” when a required external gate was not observed.

## 0. Select the audit scope

Choose the smallest complete mode:

- **Preflight:** source, configuration, artifact, metadata, URLs, and policy
  declarations; no claim of native or portal confirmation.
- **Review:** Preflight plus a production-like install, core journey, reviewer
  access, representative devices, and release evidence.
- **Release:** Review plus real portal state, store processing, platform
  compliance, final screenshots, policy forms, and explicit unresolved gates.
- **Rejection remediation:** parse the rejection message and attachments into
  exact findings, reproduce the reviewed build where possible, map each fix to
  a new build, and verify the complete resubmission evidence packet.

Set a platform scope: **Apple**, **Google**, or **Both**. Record whether the
app has accounts, subscriptions or purchases, ads, user-generated content,
children as a target audience, health/financial/security functionality,
location/contacts/photos/SMS/call-log access, third-party AI, or region-specific
behavior. These facts determine which checks apply.

Before testing, create the evidence ledger from the release contract reference.
Do not use a percentage or an unmeasured completeness label unless the
required-item denominator is explicit. Every required row must be **Observed**, **Portal
confirmed**, **Provider/legal confirmed**, **Open**, or **Unknown**.

## 1. Establish the release contract

Write a context brief:

- product, target user, core value, category, countries, and audience;
- platform, app ID/package, version, build/version code, release track, and
  intended devices/form factors;
- artifact path and provenance: local build, CI, EAS, TestFlight, internal,
  closed, or production;
- backend environment, feature flags, authentication, demo data, and review
  credentials;
- review snapshot: submission ID, review date/device, reviewed version/build,
  rejection guidelines, portal status, reviewer attachments, and current
  resubmission version/build;
- monetization, permissions, SDKs, data flows, public support/privacy URLs,
  legal/content-rights owner, and whether the audience is a child or an adult
  acting for a child or other dependent;
- scope boundary and what evidence is available.

Create a release manifest from the repository and artifact. At minimum inspect
app config, native manifests, entitlements, signing, target SDK, dependencies,
privacy manifests, permissions, URL schemes, associated domains, versioning,
build profile, and store metadata. For Expo projects inspect `app.json` or
`app.config.*`, `eas.json`, generated native files when present, and the exact
EAS build profile used.

If the repository contains `.codegraph/`, use CodeGraph before broad text
search to locate release configuration, navigation, permission calls, payment
flows, account deletion, and feature flags. Record the exact commands and
paths used so another agent can reproduce the audit.

## 2. Verify the artifact and install path

Prove the artifact is the one intended for review:

- production configuration, not a development client, debug build, local API,
  placeholder environment, or expired certificate;
- correct bundle ID/package name, version/build, signing, architectures,
  entitlements, target SDK, and supported device declarations;
- installs from the intended TestFlight, Play test track, or production path;
- launches from a clean install and after upgrade from the prior release;
- does not require a local server, developer account, seeded database, or
  unavailable VPN to show the core value;
- handles slow, offline, denied-permission, expired-session, and provider
  failure states without a blank or misleading success screen.
- keeps the installed identity discoverable: compare the marketplace name,
  signed `CFBundleDisplayName`/`CFBundleName` (Apple), Android application
  label, launcher label, Settings/app-switcher label, and any Expo/native name
  overrides. The bundle ID/package name is identity-critical but does not cure
  a confusing display-name mismatch.

Record exact commands, artifact identifiers, SHA-256/hash when available,
device/OS, install source, and screenshots. Use the artifact inspection guide
or `scripts/inspect-release-artifact.sh` when an IPA, APK, AAB, or app bundle is
available. Source inspection can establish a risk; it cannot prove the binary
processed, installed, launched, or reached a route.

## 3. Walk the reviewer journey

Start from the actual store install path and complete the primary job. Then
exercise representative secondary paths and all gated surfaces.

Define the primary journey before testing it as `entry → action → first value →
recovery`. Map every store claim and reviewer-requested feature to a journey
row. “Representative” does not permit skipping a promised, paid, permission-
gated, account, or regulated feature.

Use the reviewer test matrix to test clean install, cold launch, force-quit,
background/resume, offline and slow network, denied permissions, resettable
accounts, locale/timezone/region, and dependency failure. Do not run the
review path with a debugger, local server, seeded developer database, or
privileged test state that the reviewer will not have.

Check:

- first launch, onboarding, navigation, back, logout, and account deletion;
- sign-in, sign-up, password reset, SSO, MFA/OTP, geo-gates, memberships,
  invite codes, QR codes, and any reviewer-only configuration;
- core create/read/update/delete actions, search, filters, uploads, sharing,
  deep links, notifications, background work, and resume after interruption;
- loading, empty, no-results, offline, timeout, permission denial, validation,
  provider failure, retry, duplicate submission, and destructive recovery;
- subscription or purchase discovery, sandbox/test purchase, restore, expired,
  cancelled, pending, failed, and already-owned states;
- user-generated content reporting, blocking, moderation, deletion, and abuse
  contact where applicable.

For every gated path, verify that the reviewer can reach it without personal
data, an expiring account, a region-specific phone number, inaccessible device,
or unavailable third-party service. Capture a reviewer runbook with reset
steps, credentials, test data, expected results, and fallback instructions.

### Permission-request integrity

For every sensitive or interruptive permission, inspect the pre-permission
screen and the native prompt on a physical device. Benefit first, neutral CTA,
no coaching of the system dialog, honest denial path. Checklist:
[permission integrity](references/permission-integrity.md).

## 4. Build the reviewer evidence packet

Treat reviewer access and rejection attachments as release artifacts. Use
[the reviewer evidence packet](references/reviewer-evidence-packet.md) for the
recording, device matrix, access steps, external services, and legal material,
and record each attachment's hash, build, device, and verification status.

## 5. Audit listing and public trust surfaces

Compare the binary with every store-facing promise:

- name, subtitle/short description, full description, keywords, category,
  audience, age/content ratings, ads label, pricing, subscriptions, and
  screenshots/app previews;
- screenshots show the current build, real functionality, supported devices,
  correct language, and no misleading UI or unshipped feature;
- support URL, privacy URL, terms/EULA, account-deletion URL, marketing site,
  and contact details load over HTTPS, are public, match the app, and work on a
  clean device/browser;
- claims are specific, supportable, and consistent across metadata, app copy,
  privacy policy, data declarations, and reviewer notes;
- marketplace name and installed display name are sufficiently similar for a
  user to find the downloaded app. Check this on-device, not only in source or
  App Store Connect/Play Console;
- rights exist for icons, images, fonts, audio, content, brands, AI output,
  health data, user content, and third-party services;
- the app is meaningfully differentiated from template/repackaged or saturated
  category submissions.

Do not treat a polished screenshot, a landing page, or a passing local build as
proof that the store promise is true.

## 6. Audit privacy, data, permissions, and SDKs

Build a data map from code, manifests, SDK docs, network behavior, the privacy
policy, and store forms, then reconcile collected/shared/retained/deleted data,
SDK behavior, permission rationale and denial paths, Apple App Privacy and
required-reason APIs, and Google Play Data Safety. Use [the privacy and data map](references/privacy-and-data-map.md)
for the reconciliation checklist and the claim-to-proof row.

## 7. Apply platform gates

Use the current official policies, [the platform gates](references/platform-gates.md)
for the stable Apple and Google checklist, and [the current platform watch](references/current-platform-watch.md)
for deadlines and new requirements. When they disagree, the current official
policy wins and the conflict is reported.

## 8. Classify findings and gates

Use both impact and evidence status:

- **P0 blocker:** submission cannot proceed or there is serious legal, safety,
  privacy, security, account, or store-removal risk.
- **P1 blocker:** core review journey fails, artifact cannot be inspected, or a
  required declaration/access path is incomplete or contradictory.
- **P2 risk:** material metadata, UX, compatibility, visual, accessibility, or
  policy weakness likely to delay or undermine review.
- **P3 refinement:** low-risk polish or documentation improvement.

Apply these verdict gates in addition to priority: an unresolved official
rejection is at least P1; missing required evidence in Review or Release is a
blocker; an artifact/listing/portal mismatch is a blocker until reconciled; and
an unobserved required behavior remains **Unknown** rather than passing.

Tag each finding with one or more of `ARTIFACT`, `RUNTIME`, `ACCESS`, `METADATA`,
`PRIVACY`, `PERMISSION`, `PAYMENTS`, `CONTENT`, `QUALITY`, `PLATFORM`,
`PORTAL`, `REVIEW-PACKET`, `IDENTITY`, or `LEGAL`.

For every finding record:

- platform and policy/source;
- exact route, file, artifact, portal field, URL, device, or screenshot;
- observed behavior and reproducible steps;
- user/reviewer/store impact;
- proof rung: the highest of **declared**, **rendered**, **interactive**,
  **connected**, **failure-tested**, **device**, **production**, plus the domain
  source (**portal**, **provider**, **public URL**, **legal owner**);
- recommendation, owner/input required, confidence, and verification method.

## 9. Report

Return:

1. **Context and release manifest** — target, platform, version/build, artifact,
   track, audience, regions, and scope.
2. **Verdict** — `READY`, `READY_WITH_CONDITIONS`, `NOT_READY`, or `UNKNOWN`
   (missing external evidence). Give Apple and Google separate verdicts.
3. **Blocker summary** — P0/P1 issues first, with the smallest next action.
4. **Evidence matrix** — artifact, install, runtime, access, metadata, privacy,
   permissions, payments, public URLs, portal, legal, and evidence-ledger
   gates, including required-item coverage.
5. **Platform findings** — Apple and Google sections with policy/source links.
6. **Reviewer runbook** — account, reset, test data, configuration, and notes.
7. **Reviewer evidence packet** — recordings, device/OS matrix, purpose,
   audience, setup, external services, regional behavior, and legal material.
8. **Checks performed** — exact commands, devices/OS, builds, URLs, screenshots,
   recordings, and portal observations.
9. **Open gates and owners** — what requires the user, legal owner, provider,
   Apple, Google, native device, or production confirmation.
10. **Portal state** — app/build/IAP or track status as directly observed.
11. **Resubmission strategy** — only after the current rejection is understood;
   reply, appeal, fix, or resubmit based on evidence rather than guessing.
12. **Stakeholder PDF** — after the Markdown report is complete, render and
   visually inspect a readable PDF for non-technical readers; keep the Markdown
   as the editable source of truth.

Give every finding a stable ID, `F-store-<n>` (for example `F-store-03`), and
put it in the first cell as `P1 · F-store-03`. The builder closes by ID; a
re-audit reopens or adds, and never renumbers.

Use this finding shape:

| Priority | Platform/tag | Policy/source | Evidence | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  | High/Medium/Low |

Never report “submission complete” unless the exact store submission or
processing state was observed. A completed local audit is a readiness result,
not an Apple or Google approval.
