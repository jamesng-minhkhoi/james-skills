---
name: design-uiux-landing-page-web
description: Design distinctive, conversion-aware responsive landing-page UI/UX for products, services, campaigns, launches, and marketing sites. Use when creating page composition, hero/CTA hierarchy, proof sections, pricing presentation, responsive marketing layouts, interaction states, prototypes, or design handoffs. Do not implement product code, campaign infrastructure, analytics, SEO, or release checks.
---

# Craft Landing Page Web

Design the landing page as a focused decision journey, not a collection of
decorated sections. This is a landing-page UI/UX design skill, not a
marketing-operations, copy-production, implementation, SEO, analytics, or
release-verification skill. Establish the visitor's intent, promise, proof,
objections, and next action before choosing the visual treatment.
Use [audit-uiux-web](../audit-uiux-web/SKILL.md) for independent diagnosis and
`frontend-web-engineering` for implementation.

Load [the landing page craft process](references/landing-page-craft-process.md)
for a new page or substantial redesign. Load [message and conversion
architecture](references/message-and-conversion-architecture.md) before writing
headlines, section order, pricing, lead capture, or CTAs. Load [responsive
visual system](references/responsive-visual-system.md) when choosing layout,
type, imagery, interaction, or art direction. Load [critique and proof
checklist](references/landing-page-critique-and-proof.md) before handoff or
claiming the page is complete.

## Non-negotiable order

Intent → Evidence → Offer → Message → Narrative → Structure → System →
Interaction → Responsive → Accessibility/Performance/SEO → Proof

Do not begin with a hero gradient, component library, animation, or generated
copy while the page's audience, promise, proof, or primary action is unclear.

## 1. Frame the conversion job

Write a conversion contract:

- target audience, traffic source, awareness level, and situation;
- visitor job and desired outcome;
- one primary conversion and the business outcome it supports;
- secondary actions and the point at which they become useful;
- strongest credible proof and unresolved objections;
- risk: ordinary, financial, privacy, health, security, or irreversible;
- scope boundary: page-only, content, design system, analytics, SEO, or product;
- success evidence: conversion event, lead quality, activation, or another
  observable outcome.

Separate evidence, hypothesis, and decision. Never invent customer counts,
reviews, partner logos, performance claims, guarantees, or regulated claims.

## 2. Inspect the existing surface

Before changing the page, inspect:

- route and entry points;
- existing content, brand, tokens, components, imagery, and typography;
- analytics events, consent, forms, CRM/provider contracts, and attribution;
- metadata, canonical, sitemap, structured data, and social preview behavior;
- current responsive breakpoints and actual traffic devices;
- existing performance, accessibility, and search constraints;
- comparable products as decision flows, not as surfaces to copy.

Record what is shipped, observed, source-declared, assumed, and unknown.

## 3. Write the message before the composition

Create the minimum message set:

- eyebrow or context, when it reduces uncertainty;
- specific headline naming the audience-relevant outcome;
- supporting explanation with mechanism, constraint, or differentiator;
- primary CTA named by its outcome;
- proof appropriate to the visitor's decision;
- objection handling before the highest-friction commitment.

Avoid vague hero copy such as “Transform your future” when the actual outcome
can be named. Do not make the visitor reconstruct what the product is, who it
is for, or what happens after the CTA.

## 4. Build the narrative and section structure

Choose only sections that advance the decision:

- orientation and promise;
- problem, context, or cost of inaction;
- how it works or what the visitor receives;
- benefits tied to the visitor's job, not a feature inventory;
- credible proof: demo, result, testimonial, case study, comparison, or
  transparent evidence;
- objection, risk, pricing, eligibility, security, or FAQ content;
- primary conversion and a clear next step;
- trust, legal, contact, and footer navigation.

Do not force every landing page into a hero plus identical card grid. Let the
offer, decision complexity, traffic intent, and proof determine the sequence.
Use progressive disclosure for secondary detail while keeping material
constraints, costs, privacy effects, and irreversible consequences explicit.

## 5. Compose hierarchy before decoration

- Make the first viewport answer: what is this, is it for me, why should I
  care, and what can I do next?
- Establish one dominant promise and one primary CTA.
- Use scale, position, contrast, whitespace, grouping, and content before
  adding visual effects.
- Give every section a job and a clear relationship to the previous one.
- Use cards only when they represent distinct objects, plans, decisions, or
  proof; avoid card soup and repeated icon-title-description blocks.
- Make the CTA visually and verbally consistent across the page without
  making every section shout.

## 6. Establish the web visual system

- Reuse or define tokens for type, spacing, color, width, radius, border,
  elevation, motion, and focus.
- Choose typography for reading, hierarchy, personality, and language support;
  do not use oversized display text to hide weak messaging.
- Give imagery an information, trust, demonstration, or emotional role.
  Prefer product-specific art direction to generic stock or decorative blobs.
- Use color semantically and check contrast, dark mode, hover, focus, disabled,
  visited, and error states.
- Design the visual rhythm as a sequence of moments: orientation, emphasis,
  proof, decision, and action.
- Use motion to explain reveal, continuity, hierarchy, progress, or result.
  Remove motion that delays reading, obscures content, or exists only because
  a prototype can animate.

## 7. Design the interaction surface

Cover:

- navigation and anchor behavior;
- links, buttons, hover, focus-visible, pressed, disabled, and visited states;
- forms, validation, submission, pending, success, error, retry, and consent;
- pricing toggles, calculators, accordions, tabs, and disclosure behavior;
- keyboard navigation, screen-reader names, focus order, and focus return;
- reduced motion, touch targets, pointer precision, and no-hover alternatives;
- sticky or repeated CTAs only when they improve task completion without
  covering content or coercing the visitor.

Do not hide a core promise, price, material constraint, or next step behind an
undiscoverable interaction.

## 8. Design responsive behavior as composition

Build from content and intent across representative widths:

- narrow mobile, large mobile, tablet or intermediate width, and desktop;
- long headings, translated strings, zoom, large text, and missing media;
- reordered sections, changed alignment, collapsed navigation, and altered
  image crops where the decision needs a different composition;
- keyboard, safe spacing, touch targets, and readable measure;
- no horizontal overflow, clipped content, accidental fixed-height traps, or
  desktop layout compressed into a phone.

Responsive work is not “make desktop smaller.” Explain each intentional change
in order, density, alignment, interaction, or art direction.

## 9. Prepare the design handoff

Use existing brand, content, consent, SEO, analytics, form, and provider
constraints as design inputs. Keep page-level composition understandable,
content-driven, and composable. Document CTA destinations, form states, content
dependencies, proof provenance, legal/consent requirements, and unresolved
implementation questions.

Do not edit route code, forms, analytics, consent, metadata, structured data,
provider configuration, or campaign infrastructure. Do not fabricate proof or
represent a form as successfully submitted. Hand implementation to
`frontend-web-engineering` and campaign/SEO owners.

## 10. Prove the design

Follow:

Plan → Message Spine → Wireframe → Compose → Prototype → Critique → Handoff

Review:

- message clarity and first-viewport comprehension;
- primary CTA reachability and real outcome;
- responsive layouts and representative content;
- keyboard, screen reader, focus-visible, contrast, reduced motion, and zoom;
- form, consent, loading, success, error, retry, and interruption states;
- performance, image/font loading, layout shift, and animation behavior;
- metadata, indexing, structured-data, social-preview, analytics, consent, and
  form requirements as handoff dependencies rather than implementing them;
- exact routes, viewport sizes, data/content fixtures, design decisions, and
  engineering/campaign gates not observed.

Do not call the product page complete because it looks good at one width or
because a prototype is polished. The design is ready for handoff when its
promise, decision path, responsive behavior, accessible interaction, content
dependencies, and open implementation gates are explicit.
