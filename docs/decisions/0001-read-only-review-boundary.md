# ADR-0001: Establish a read-only evidence-review boundary

- **Status:** Proposed
- **Date:** 2026-07-19
- **Decision owners:** QSO-STUDIO architect and designated human reviewer

## Context

QSO-STUDIO is described as a visual design, inspection, orchestration, and debugging workspace. Those terms can imply execution, write, payment, or approval authority even though the repository contains no verified application and the ecosystem assigns those responsibilities to other systems.

Beginning with a broad orchestration interface would force premature decisions about contracts, credentials, authorization, distribution, privacy, and support. It would also make it difficult to demonstrate that Studio is merely presenting evidence rather than becoming a new source of truth.

## Decision

The first bounded QSO-STUDIO workflow will be a local, fixture-backed, read-only evidence review:

- inputs are user-selected fixtures or approved evidence exports;
- contract selection uses exact versioned identifiers and digests;
- parsing and validation are bounded and deterministic;
- the normalized review model does not mutate source evidence;
- comparisons and filters are side-effect free;
- reviewer notes are non-authoritative;
- exports cite exact evidence and build references;
- the build contains no upstream write, execution, signing, payment, or autonomous approval client.

The decision does not choose the application platform. It constrains the first workflow independent of whether a later approved implementation is desktop, browser-based, or another form.

## Consequences

### Positive

- Product behavior can be tested with deterministic fixtures.
- Trust and authority boundaries are inspectable.
- Accessibility and hostile-input behavior can be designed before live integration.
- Upstream repositories remain canonical owners of their contracts and actions.
- The first implementation can be small enough for complete evidence and rollback.

### Costs

- The initial Studio will not provide live orchestration.
- Users must import bounded evidence rather than connect directly to systems.
- Contract owners must provide approved schemas, manifests, and fixtures.
- Some visual designs may need revision when live operational constraints are later approved.

## Alternatives considered

### Build a full orchestration console first

Rejected for the initial scope because it combines too many authority and security decisions before contracts and ownership are approved.

### Create only static mockups

Useful for exploration but insufficient as the sole milestone because static mockups do not prove deterministic parsing, validation, accessibility, or evidence traceability.

### Connect to live systems in read-only mode

Deferred. “Read-only” credentials and APIs still introduce identity, network, privacy, availability, and contract risks. A local fixture workflow should establish the review model first.

## Evidence required for acceptance

- explicit product/UX charter approval;
- selected user group and first supported platform;
- approved integration manifest for one record type;
- deterministic fixture and expected-result set;
- threat model and privacy classification;
- accessible workflow prototype and test plan;
- proof that the candidate has no write or execution client;
- reproducible build, checksums, provenance, recovery, and rollback evidence;
- human review and recorded acceptance.

## Follow-up decisions

Separate ADRs are required for platform/distribution, persistence, remote retrieval, identity and authorization, plugins, signing, write-back, payment operations, telemetry, and production support.
