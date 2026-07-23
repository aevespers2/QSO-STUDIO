---
layout: default
title: Product and UX Charter
---

# Product and UX Charter

## Purpose

QSO-STUDIO is a proposed workspace for inspecting QSO records, comparing evidence, reviewing candidate changes, and preparing human-readable decisions. Its first responsibility is to make state, provenance, uncertainty, and unresolved conflicts understandable without implying that the viewer can execute, approve, settle, or publish anything.

## Primary readers

- Researchers comparing QSO state and evidence.
- Maintainers reviewing proposed documentation or contract changes.
- Architecture reviewers checking boundaries and dependency assumptions.
- Accessibility, security, privacy, and release reviewers.

## First bounded workflow

The first supported design target is a read-only evidence review:

1. load a synthetic or explicitly approved fixture;
2. display identity, source generation, provenance, state, confidence, and limitations;
3. show conflicts, corrections, withdrawals, freeze points, and missing evidence;
4. let the reviewer annotate a proposal locally;
5. export a review packet that has no execution or repository-write authority.

## Non-goals

QSO-STUDIO does not provide direct runtime execution, autonomous approval, unrestricted repository mutation, credential custody, production payment control, untrusted-code execution, or silent promotion of mock data into accepted state.

## Product principles

1. **Read before write.** The first product surface is observational.
2. **Evidence before claims.** Every displayed status names its source and generation.
3. **Proposal before authority.** Editing creates a proposal, never an automatic change.
4. **Accessible by construction.** Visual meaning has equivalent text and keyboard paths.
5. **Fail closed.** Missing contracts, stale evidence, or ambiguous ownership remain visible blockers.
6. **Rollback is part of design.** A publication or integration change must define restoration and withdrawal behavior.

## Open decisions

The platform target, distribution identity, license, canonical package name, upstream contract set, fixture format, review-packet format, support route, publication route, and final ownership model remain unresolved.

This charter is documentation-only and is bound to `QSO-CONSENT-CAPACITY-LOCK-v1`.
