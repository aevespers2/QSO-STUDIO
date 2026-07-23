---
layout: default
title: Read-Only Evidence Review
---

# Read-Only Evidence Review

## Goal

Provide one deterministic workflow that lets a reviewer understand a QSO-related record without granting execution, repository-write, approval, publication, or payment authority.

## Required input envelope

A fixture or governed source must provide:

- source repository and immutable source identifier;
- contract or schema identifier and version;
- record identifier and record class;
- exact evidence references and availability state;
- correction, supersession, and withdrawal status;
- creation and observation timestamps with clock assumptions;
- declared limitations and unresolved ownership.

Unknown or incomplete envelopes are shown as blocked rather than guessed.

## Review sequence

1. **Verify source identity.** Compare the supplied repository, commit, contract, and evidence references with the review packet.
2. **Classify the record.** Distinguish source state, derived interpretation, proposal, review, decision, and operational result.
3. **Inspect provenance.** Show the path from source to displayed representation and identify transformations.
4. **Inspect currentness.** Mark moved, expired, superseded, withdrawn, or unreachable evidence.
5. **Inspect conflicts.** Present contradictions and missing interfaces without choosing a winner automatically.
6. **Annotate locally.** Capture reviewer notes as a separate proposal layer.
7. **Export deterministically.** Include source identities, viewer version, annotations, limitations, and checksums.
8. **Hand off separately.** Repository changes or runtime actions require an independent authorized workflow.

## Display states

- `CURRENT_OBSERVATION`
- `STALE_SOURCE`
- `MISSING_EVIDENCE`
- `CONFLICTING_EVIDENCE`
- `CORRECTION_PENDING`
- `SUPERSEDED`
- `WITHDRAWN`
- `PROPOSAL_ONLY`
- `REVIEW_COMPLETE_PENDING_DECISION`

These labels describe the viewer's evidence state; they do not create upstream authority.

## Accessibility requirements

Every state has a textual label, programmatic description, keyboard-reachable detail view, and non-color indicator. Graphs and timelines require equivalent ordered prose.

## Rollback and withdrawal

A review packet must identify its inputs. If an input is corrected or withdrawn, the packet becomes stale and must not be represented as current. A replacement packet preserves the prior identifier and records why it was superseded.

The workflow remains governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
