---
layout: default
title: Developer Guide
---

# Developer Guide

## Current repository model

The repository is documentation-first. Code should not be introduced merely to make diagrams appear implemented. Any future UI work begins only after the product charter, platform target, fixture format, and integration boundaries are approved.

## Proposed source layout

```text
docs/                  public documentation candidate
scripts/               deterministic repository checks
tests/                 regression tests for documentation controls
fixtures/              future synthetic-only review inputs
src/                    future UI source after approval
```

The `fixtures/` and `src/` directories are not required for the current documentation milestone.

## Change classes

- **Editorial:** wording, structure, navigation, accessibility alternatives.
- **Governance:** authority boundaries, ownership, source precedence, correction, withdrawal, rollback.
- **Contract documentation:** exact producer/consumer tuples and blocked decisions.
- **Implementation:** UI, parser, storage, networking, export, packaging; requires separate scope approval.

## Review requirements

Every change should identify its class, source generation, affected reader routes, tests, security/privacy impact, accessibility impact, and rollback. Contract changes must preserve upstream ownership and must not convert a proposed identifier into an accepted interface.

## Documentation conventions

- Use one descriptive H1 per page.
- Provide equivalent prose after meaningful diagrams.
- Use explicit maturity labels: proposed, blocked, review, tested, implemented, withdrawn, historical.
- Prefer repository-relative links.
- Separate source observations, interpretations, proposals, reviews, decisions, and operational results.
- Name exact evidence when making a verification claim.

## Future implementation guardrails

The first UI must be read-only, fixture-backed, keyboard operable, and free of production credentials. Rendering treats imported content as untrusted data. Exports preserve provenance and remain proposal artifacts.

This guide is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
