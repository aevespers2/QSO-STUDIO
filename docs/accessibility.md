---
layout: default
title: Accessibility
---

# Accessibility

Accessibility is a release gate, not a later enhancement. QSO-STUDIO must remain understandable when color, animation, pointing devices, large screens, or visual diagrams are unavailable.

This page defines the accessibility requirements. The separate [accessibility review evidence protocol](accessibility-review-evidence.md) defines exact-artifact review states, methods, records, correction links, and fail-closed stop conditions. The protocol is `DOCUMENTED_NOT_CERTIFIED`; it does not certify this source, a rendered Pages artifact, a synthetic consumer, or a future interface.

## Documentation requirements

- One clear page title and logical heading order.
- Descriptive link text and stable reading paths.
- Tables with headers and concise captions or introductions.
- Equivalent prose immediately following meaningful diagrams.
- No required meaning conveyed by color, shape, icon, motion, position, or layout alone.
- Plain-language definitions for evidence state, authority state, currentness, correction, withdrawal, supersession, and rollback.
- Explicit separation of source evidence, interpretation, annotation, proposal, review diagnostic, human disposition, and external action.

## Future interface requirements

- Complete keyboard operation with visible focus.
- Semantic controls, names, descriptions, and error messages.
- Text scaling and responsive reflow without information loss.
- Sufficient contrast and non-color state indicators.
- Reduced-motion behavior and no essential time-limited interaction.
- Accessible alternatives for graphs, timelines, provenance paths, conflict views, and dense evidence.
- Recovery guidance that identifies the failed action and preserves user work.
- Persistent visibility of uncertainty, provenance, correction, withdrawal, and stale-state warnings.

## Evidence expectations

A future release must retain automated and manual accessibility results against the same exact candidate artifact. The record must identify source commit, build, artifact digest, route, environment, methods, reviewer role, results, limitations, and correction or supersession links. Automated success does not replace keyboard, screen-reader, zoom, reflow, contrast, reduced-motion, cognitive-comprehension, and error-recovery review.

The permitted evidence states are `NOT_REVIEWED`, `PARTIAL`, `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`, `SUPERSEDED`, `WITHDRAWN`, and `CORRECTED`. A partial, blocked, unknown, stale, or superseded result must never be presented as a pass.

## Accessibility rollback

A change is withdrawn when it removes a keyboard path, hides focus, breaks heading or landmark structure, introduces color-only meaning, removes diagram prose, prevents scaling, obscures provenance or uncertainty, collapses proposal into approval, or makes error recovery inaccessible. Preserve the failed generation, link the correction, and restore the last verified accessible artifact or leave the route unpublished.

This page is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
