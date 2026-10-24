# Reviewer evidence packet

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

For each attachment, maintain an evidence-ledger row with filename, SHA-256
when available, build/version, device/OS, capture date, portal field, and
verification status. A recording attached to a message is not proof until its
artifact and capture environment are identified.
