---
layout: default
title: QSO-STUDIO Documentation
---

# QSO-STUDIO

QSO-STUDIO is the proposed **read-only review and design surface** for the Quantum State Object ecosystem. This documentation candidate explains the product boundary before any application, package, or public site is represented as available.

## Start here

- [Product and UX charter](product-charter.md)
- [Architecture](architecture.md)
- [Read-only review workflow](read-only-review-workflow.md)
- [Integration contracts](integration-contracts.md)
- [Onboarding](onboarding.md)
- [Developer guide](developer-guide.md)
- [Accessibility](accessibility.md)
- [Security and privacy](security-privacy.md)

## Current maturity

| Surface | Status | Meaning |
|---|---|---|
| Documentation | Candidate | Reviewable source exists; publication is not yet authorized. |
| User interface | Not implemented | No supported application or executable is claimed. |
| Integrations | Proposed | Contract ownership and exact schemas remain upstream decisions. |
| Runtime control | Out of scope | Studio does not execute QSO workloads or bypass approval boundaries. |
| Repository writes | Out of scope | Proposed changes remain review artifacts until separately approved. |
| Payment control | Out of scope | Financial information may be displayed only as read-only evidence. |

## Evidence and authority notice

A diagram, mock fixture, passing documentation check, or review approval does not establish runtime capability, repository authority, payment authority, release approval, or publication approval. The documentation source is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`; any future consent-sensitive feature must remain fail closed and separately reviewed.
