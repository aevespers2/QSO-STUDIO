# Project overview

## Purpose

QSO-STUDIO is intended to reduce the cognitive cost of reviewing QSO ecosystem evidence. It should help authorized people inspect structured records, compare states, trace provenance, understand validation failures, and prepare review notes without collapsing distinct authority domains into a single interface.

The repository begins with documentation because visual interfaces can easily imply powers they do not possess. A polished screen that displays a payment, release, genome, or runtime proposal must not be mistaken for the system that authorizes or executes it.

## Proposed users

The charter candidate recognizes three user groups:

- **Researchers** inspect objects, genomes, state transitions, evidence, and experiment records.
- **Operators** review system health, freeze points, validation results, and release evidence.
- **Maintainers and reviewers** inspect contract compatibility, provenance, documentation, and proposed changes.

These roles are descriptive, not an authorization model. Authentication, authorization, and organization-specific permissions are future decisions owned outside the documentation candidate.

## First bounded outcome

The first product increment should demonstrate one deterministic, read-only workflow using local fixtures:

1. load a signed or checksum-addressed fixture bundle;
2. validate the bundle against an approved versioned contract;
3. display identity, source, timestamps, hashes, status, and validation findings;
4. compare two records without mutating either record;
5. export a non-authoritative review note that cites the exact evidence inspected.

This outcome is intentionally smaller than a complete Studio application. It creates a verifiable seam between user experience design and upstream contract ownership.

## In scope for the charter

- navigation and information architecture for evidence review;
- read-only visualization of approved record types;
- clear provenance, validation, and error presentation;
- local mock fixtures labeled as non-production data;
- review notes and proposals that remain non-authoritative;
- accessibility, privacy, security, and recovery requirements;
- deterministic documentation and future UI verification.

## Out of scope

- direct runtime execution or scheduling;
- direct repository mutation or branch protection changes;
- custody of secrets, private keys, or signing devices;
- payment initiation, custody, settlement, refunds, or disputes;
- autonomous release, governance, or safety approval;
- arbitrary code execution, plugin loading, or remote script evaluation;
- claims that upstream schemas or protocols are final before their owners approve them.

## Ecosystem relationships

QSO-STUDIO is a consumer of approved contracts, not their canonical owner.

| Domain | Expected authority | Studio responsibility |
|---|---|---|
| QSO object/state | QSO runtime or canonical object repository | Validate and render approved representations |
| Genome records | QSO-GENOMES | Display canonicalized content, hashes, compatibility, and findings |
| Search/retrieval evidence | QSO-SEEKER or approved source | Preserve source attribution and retrieval context |
| Fabric/runtime status | QSO-FABRIC or runtime service | Render status without issuing execution commands |
| Payment records | QSO-PAYMENTS or approved ledger adapter | Present read-only records and policy findings |
| Release evidence | Owning repository and CI provider | Display commit, workflow, artifact, and approval evidence |
| Human approval | Designated human authority | Make decision state visible without impersonating it |

The exact repository names, schema versions, and support guarantees must be recorded in a versioned integration manifest before implementation.

## Success measures

A documentation candidate is successful when:

- every capability claim maps to repository evidence;
- every diagram distinguishes display, proposal, approval, and execution;
- unresolved decisions are visible and assigned;
- the documentation builds strictly and reproducibly;
- accessibility and security requirements are testable;
- rollback can restore the previous verified artifact;
- no implementation or publication claim outruns the repository state.
