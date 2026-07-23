# Task Chain

`QSO-STUDIO-DOCS-CANDIDATE-001`

States: `PROPOSED` · `READY` · `IN PROGRESS` · `BLOCKED` · `REVIEW` · `DONE`

## Product directive

- **Next objective:** Review the QSO-STUDIO product/UX charter and both current-main synthetic consumers before any application or Pages publication is authorized.
- **User outcome:** A researcher or operator can understand the proposed read-only review workflow, supported boundaries, data/privacy expectations, and integration dependencies without being told that a site, executable, admitted ecosystem component, reviewer registry, or architecture authority exists when it does not.
- **MVP scope:** approved users, workflows, non-goals, platform/distribution target, data classification, privacy/license model, authority boundaries; accurate repository map; accessible documentation candidate; one fixture-oriented read-only workflow specification; independently implemented synthetic manifest and architecture-review consumers; deterministic documentation and conformance checks.
- **Priority:** Documentation integrity, immutable source identity, independent semantic evaluation, and product authority boundaries precede design-system or UI implementation.
- **Success criteria:** every path, publication statement, workflow, capability claim, producer tuple, fixture digest, supersession link, and consumer disposition matches repository evidence; the charter separates visualization, annotation, proposal, review diagnostics, human review, architecture decision, activation, runtime execution, repository writes, and payments; links and diagrams are accessible; documentation validation, provenance, hostile regressions, and rollback evidence pass.
- **Non-goals:** direct runtime execution, unrestricted repository writes, credentials, autonomous approvals, reviewer appointment, architecture decisions, production payment control, untrusted-code execution, ecosystem admission, namespace acceptance, or visual orchestration before contracts are available.
- **Release rationale:** A Studio surface can imply authority belonging to runtime, payment, repository, or ecosystem-governance systems. Truthful read-only contracts and synthetic consumers prevent unsafe coupling before implementation.

## Active chain

| Priority | Task | Owner | Depends on | Status | Acceptance criteria |
|---|---|---|---|---|---|
| P0 | Approve product/UX charter and authority boundary | Architect | Explicit review | BLOCKED | Users, workflows, platforms, ecosystem role, privacy/license model, distribution target, authority boundaries, and unresolved ownership are accepted or revised. |
| P0.1 | Produce accurate documentation and navigation candidate | QSOBuilder | Repository evidence | REVIEW | Front door, charter, architecture, workflow, integration, consumers, onboarding, developer, accessibility, security/privacy, punch-list, and planning controls agree. |
| P0.2 | Validate documentation candidate at exact head | QSOBuilder | P0.1 | REVIEW | Required pages, links, diagrams, markers, planning alignment, hostile regressions, deterministic evidence, and clean-tree checks pass. |
| P0.3 | Rebind independent ecosystem consumer to current `main` and current producer head | QSOBuilder | P0.1-P0.2; QSO-FABRIC PR #21 | DONE | Source tuple binds `25036a5cfcea79e204a4660ddd1af09c054935b1`; exact manifest bytes are verified before parsing; independent hostile regressions pass; stale PR #4 evidence remains historical; no ecosystem or runtime authority is inferred. |
| P0.4 | Rebind architecture-review consumer to current `main` and current QSO Field governance head | QSOBuilder | P0.1-P0.2; qso-field PR #24 | REVIEW | Source tuple binds `a56b1fa93f151ee14f3cdd4183b89a10e268e352`, run `30000668553`, and artifact `8560824564`; local bytes are checked before parsing; independent hostile regressions pass; review completion remains separate from decision and activation; PR #4 is closed unmerged after supersession. |
| P0.5 | Decide Pages publication target and rollback | Architect + publication reviewer | P0-P0.4 | BLOCKED | Authorized source, workflow, permissions, accessibility/security/privacy/license review, rollback, and resulting-route verification are recorded. |
| P1 | Specify one read-only evidence-review fixture | Architect | P0 and accepted upstream contracts | BLOCKED | Deterministic synthetic fixtures define records, provenance, conflicts, corrections, withdrawals, annotations, and errors without execution or write authority. |
| P2 | Build the minimal accessible UI skeleton | Builder | P1 | PROPOSED | Approved workflow passes unit, component, contract, smoke, accessibility, and security tests without credentials or direct execution paths. |

## Builder rules

Do not implement runtime, payment, repository-write, publication, admission, appointment, architecture-decision, activation, or approval authority inside Studio. Unverified upstream concepts may appear only as clearly labeled mock or synthetic fixtures. Passing documentation or consumer checks does not approve the product charter, reviewer population, namespace, interface, publication, or release.

## FYSA-120 mapping

Applied capability areas: CAT-011 narrative and diagram integrity; CAT-012 technical writing and documentation architecture; CAT-013 knowledge graphs and contradiction detection; CAT-017 source identity and onboarding; CAT-019 accessibility and plain language; CAT-031 documentation and conformance validation; CAT-040 rebinding and rollback; CAT-044 hostile evaluation; CAT-052 least-privilege workflow design and digest evidence; CAT-054 supply-chain verification; CAT-059 exact-head evidence transport.

Proposed non-authoritative subdivisions: `012-L — evidence-state interface documentation` and `031-M — cross-repository consumer rebinding after default-branch divergence`.

## Builder log

Record approvals, commits, documentation/accessibility/security commands and results, contract/fixture hashes, producer heads, artifact checksums, publication decisions, rollback evidence, and follow-ups.

This task chain is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
