# ADR-0002: Separate the Review Contract from the Host Shell

- **Status:** Proposed
- **Date:** 2026-07-21
- **Decision owners:** A.L.I.S.T.A.I.R.E. Architect, QSO-STUDIO owner, AionUi owner, Repository `1` authority owner
- **Related:** ADR-0001, `portable-trust-review-profile.md`, `obstruction-and-gluing.md`

## Context

QSO-STUDIO and AionUi can both present portfolio evidence, status, annotations, proposals, corrections, revocations, and recovery information. Without an explicit ownership boundary, the two repositories can evolve incompatible review models or imply different authority from the same user action.

The portfolio also separates review from authoritative disposition:

- source repositories and adapters own source records;
- Repository `0` prepares bounded proposals and evidence;
- Repository `1` or an approved successor owns candidate canonical disposition, capabilities, revocation, and recovery state;
- named human authorities own approvals appropriate to their domains;
- execution, repository mutation, release, deployment, publication, and payment remain external to a read-only review surface.

A UI session, button, annotation, or polished export must not become an authority root merely because it is convenient.

## Decision

Adopt the following candidate split:

1. **QSO-STUDIO owns the domain-neutral review contract.** This includes the normalized review model, authority-state vocabulary, comparison semantics, annotation model, non-authoritative export profile, accessibility requirements, and deterministic compatibility fixtures.
2. **AionUi is an optional host shell and adapter.** It may render the accepted QSO-STUDIO review contract inside its desktop or WebUI experience, but it must not redefine review, approval, capability, correction, revocation, or canonical-state semantics.
3. **Repository `1` or another approved trust service remains the authority source.** Studio and AionUi display disposition and capability records but cannot create them through local UI state.
4. **Human approval remains separately represented.** A reviewer annotation may be referenced by an external approval record, but it is not itself an approval token.
5. **Public Pages remain documentation-only.** Static Pages builds contain no credentials, private records, authenticated operations, or authority-bearing controls.
6. **Privileged adapters require separate acceptance.** Any authenticated gateway, upstream write, command, signing, payment, release, deployment, or repository-mutation client requires its own ADR, threat model, capability contract, tests, recovery plan, and approval.

## Contract boundary

The shared adapter boundary should carry only versioned, typed review data:

```text
source or authority record
        ↓
QSO-STUDIO review contract
        ↓
AionUi host adapter or native Studio renderer
        ↓
non-authoritative annotation/export
        ↓
external approval or authority system
```

The adapter must preserve:

- record and subject identity;
- contract/profile version;
- source repository and immutable source reference;
- integrity, attribution, temporal, replay, correction, and revocation state;
- privacy classification and redaction state;
- authority class and explicit non-authority of UI annotations;
- deterministic comparison and presentation parameters;
- accessibility semantics and text alternatives.

## Consequences

### Positive

- one review vocabulary can be tested across multiple interfaces;
- AionUi can reuse a stable contract without becoming canonical state;
- QSO-STUDIO remains implementable as a focused review tool or library;
- accessibility and hostile-input behavior can be verified once and reused;
- approval, execution, and canonical disposition remain independently governed;
- UI replacement or recovery does not change portfolio authority.

### Costs

- both repositories must share fixtures and version compatibility rules;
- adapter changes require coordinated review;
- domain-specific records need explicit mappings instead of ad hoc presentation;
- some inherited AionUi behavior may need to remain disabled or outside the accepted adapter;
- the portfolio must designate a registry or ownership process for the neutral review profile.

## Rejected alternatives

### Make AionUi the canonical review and approval system

Rejected because the inherited desktop/WebUI shell would become coupled to authority, private-data, credential, and recovery concerns before those responsibilities are reviewed.

### Make QSO-STUDIO the complete operations console

Rejected because it would collapse evidence review, proposal, approval, execution, repository writes, payments, and canonical state into one trust boundary.

### Permit each UI to define its own record model

Rejected because records, corrections, revocations, and authority states could diverge silently, preventing reliable cross-interface review and recovery.

### Treat UI actions as authoritative when authenticated

Rejected because authentication identifies a session or actor; it does not by itself prove that the actor has the exact capability, policy approval, scope, expected state, or recovery authority for a consequential action.

## Acceptance conditions

This ADR may move to `Accepted` only when:

- QSO-STUDIO and AionUi owners approve the split;
- Repository `1` or another authority owner approves the display-only disposition boundary;
- the first exact record profile and deterministic fixture set are selected;
- shared review, annotation, comparison, export, correction, revocation, and recovery schemas are versioned;
- public/private topology, privacy, retention, cache, and diagnostic rules are approved;
- compatibility fixtures pass in both a native Studio renderer and an AionUi adapter candidate;
- accessibility, hostile-input, stale-state, replay, correction, revocation, freeze, and recovery tests pass;
- no direct execution, credential, repository-write, payment, release, deployment, or self-approval path is present.

## Rollback

If the shared adapter produces authority ambiguity, privacy downgrade, inaccessible state, incompatible interpretations, stale revocation handling, or recovery dependence on a compromised shell:

1. disable the AionUi adapter;
2. preserve reviewed records, fixtures, logs, and exports;
3. return to the last accepted read-only QSO-STUDIO contract or static fixture renderer;
4. invalidate affected caches and sessions;
5. record the incompatibility and require a new ADR before re-enabling integration.

Rollback does not delete source evidence or rewrite historical review records.
