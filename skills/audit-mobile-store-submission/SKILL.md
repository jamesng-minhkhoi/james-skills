---
name: audit-mobile-store-submission
description: Audit iOS App Store and Google Play submission readiness for native and Expo/React Native apps, including rejection remediation and App Review/Play review evidence packets. Use before creating or updating a store submission to inspect the production artifact, installability, runtime behavior, reviewer access, metadata, display-name identity, screenshots and recordings, privacy and data disclosures, permission UX, monetization, public URLs, account deletion, platform policy, and current Apple/Google deadlines. Produce evidence-backed blockers and open gates; do not submit or change store dashboards unless explicitly requested.
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

Record exact commands, artifact identifiers, device/OS, install source, and
screenshots. Source inspection can establish a risk; it cannot prove the binary
processed, installed, launched, or reached a route.

## 3. Walk the reviewer journey

Start from the actual store install path and complete the primary job. Then
exercise representative secondary paths and all gated surfaces.

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

For every sensitive or interruptive system permission, inspect the exact
pre-permission screen and the native prompt on a physical device:

- explain the feature benefit and what the app will do before requesting;
- use a neutral CTA such as **Continue** or **Next**, never a custom **Allow**
  button that tells the user which answer to give;
- do not draw, imitate, highlight, point at, or otherwise coach the system
  permission dialog or its Allow/Don’t Allow choices;
- verify **Maybe later**, denial, limited access, repeated launch, and Settings
  recovery. Do not re-prompt after a clear denial unless the platform allows a
  meaningful new context;
- confirm the user keeps the core product when notifications are denied unless
  the feature genuinely cannot function, and explain the consequence honestly.

## 4. Build the reviewer evidence packet

Treat App Review Information, Play Console reviewer access, and rejection
attachments as release artifacts. For Apple, prepare and verify the following
against the exact build under review:

1. A physical-device screen recording that starts by launching the app and
   demonstrates the normal core flow, account registration/login/deletion,
   paid content or subscription flow, UGC reporting/blocking, and every
   sensitive permission prompt that applies.
2. Device models and operating systems tested, including the recording device.
3. App purpose, problem, target audience, and value; distinguish an adult
   caregiver audience from a child subject or child-directed product.
4. Setup and access instructions, credentials, MFA/OTP/QR steps, reset path,
   sample files, test data, and expected results.
5. External services, tools, platforms, authentication, payments, data
   providers, analytics, ads, maps, AI, and other dependencies used by core
   functionality.
6. Regional differences, country/locale gates, or an explicit confirmation
   that the reviewed behavior is consistent across regions.
7. Regulated-industry authorization, content licenses, protected third-party
   material rights, or other legal documentation when applicable.

Record each attachment’s filename, capture date, device/OS, app version/build,
and the exact reviewer note that points to it. A simulator screenshot or a
generic product explanation is not equivalent to a physical-device recording
of the submitted build.

When a rejection is supplied, create one finding per guideline and preserve
Apple/Google’s exact requested next step separately from your recommendation.
Track whether the fix is source-only, present in a new artifact, observed on a
device, attached to the portal, or still unverified.

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

Flag any declaration that is broader, narrower, older, or less specific than
the actual binary and SDK behavior. A “no data collected” answer requires
evidence, not intuition.

## 7. Apply platform gates

Use the current official policies and the platform watch reference. At minimum,
check:

### Apple

- App Completeness: crashes, blank/placeholder content, broken links, missing
  review information, unavailable backend, incomplete IAP, and unreproducible
  login or purchase flows;
- accurate metadata and age rating; no hidden/dormant functionality or mismatch
  between listing and binary, including marketplace name versus installed
  display name under Guideline 2.3.8;
- minimum functionality, web wrapper/content aggregator, copycat, spam,
  repackaged template, or saturated-category risk;
- privacy, account deletion, permissions, tracking, third-party AI disclosure,
  privacy manifest, Sign in with Apple, and export compliance;
- in-app purchase rules, reader/physical-goods distinctions, subscriptions,
  restore/cancel flows, and review visibility;
- current SDK, launch screen, accessibility metadata, supported platforms,
  device behavior, and any regional legal or content requirements.

### Google Play

- stable install, launch, responsiveness, no blank pages, broken controls,
  ANRs, crashes, and meaningful functionality/content;
- accurate store listing, screenshots, ads declaration, content rating,
  target audience, privacy policy, and reviewer access;
- Data Safety and account deletion accuracy, including SDKs and web deletion
  path;
- high-risk/sensitive permissions, minimum-scope alternatives, photo/video,
  contacts, location, SMS/call-log, foreground service, and full-screen intent
  declarations when applicable;
- target API, 16 KB page-size compatibility, device/form-factor support,
  Play Billing or permitted regional alternatives, and test-track requirements;
- developer identity, package registration, account status, repeated-rejection
  risk, and production-access requirements.

## 8. Classify findings and gates

Use both impact and evidence status:

- **P0 blocker:** submission cannot proceed or there is serious legal, safety,
  privacy, security, account, or store-removal risk.
- **P1 blocker:** core review journey fails, artifact cannot be inspected, or a
  required declaration/access path is incomplete or contradictory.
- **P2 risk:** material metadata, UX, compatibility, visual, accessibility, or
  policy weakness likely to delay or undermine review.
- **P3 refinement:** low-risk polish or documentation improvement.

Tag each finding with one or more of `ARTIFACT`, `RUNTIME`, `ACCESS`, `METADATA`,
`PRIVACY`, `PERMISSION`, `PAYMENTS`, `CONTENT`, `QUALITY`, `PLATFORM`,
`PORTAL`, `REVIEW-PACKET`, `IDENTITY`, or `LEGAL`.

For every finding record:

- platform and policy/source;
- exact route, file, artifact, portal field, URL, device, or screenshot;
- observed behavior and reproducible steps;
- user/reviewer/store impact;
- evidence level: **source**, **build**, **runtime**, **portal**, **provider**,
  **public URL**, **legal owner**, or **unknown**;
- recommendation, owner/input required, confidence, and verification method.

## 9. Report

Return:

1. **Context and release manifest** — target, platform, version/build, artifact,
   track, audience, regions, and scope.
2. **Verdict** — Ready, Ready with conditions, Not ready, or Unknown due to
   missing external evidence. Give Apple and Google separate verdicts.
3. **Blocker summary** — P0/P1 issues first, with the smallest next action.
4. **Evidence matrix** — artifact, install, runtime, access, metadata, privacy,
   permissions, payments, public URLs, portal, and legal gates.
5. **Platform findings** — Apple and Google sections with policy/source links.
6. **Reviewer runbook** — account, reset, test data, configuration, and notes.
7. **Reviewer evidence packet** — recordings, device/OS matrix, purpose,
   audience, setup, external services, regional behavior, and legal material.
8. **Checks performed** — exact commands, devices/OS, builds, URLs, screenshots,
   recordings, and portal observations.
9. **Open gates and owners** — what requires the user, legal owner, provider,
   Apple, Google, native device, or production confirmation.
10. **Resubmission strategy** — only after the current rejection is understood;
   reply, appeal, fix, or resubmit based on evidence rather than guessing.

Use this finding shape:

| Priority | Platform/tag | Policy/source | Evidence | Impact | Recommendation | Confidence |
| --- | --- | --- | --- | --- | --- | --- |
| P0–P3 |  |  |  |  |  | High/Medium/Low |

Never report “submission complete” unless the exact store submission or
processing state was observed. A completed local audit is a readiness result,
not an Apple or Google approval.
