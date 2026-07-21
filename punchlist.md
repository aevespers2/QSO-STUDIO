# QSO-STUDIO Punch List

Statuses: `OPEN` · `BLOCKED` · `IN PROGRESS` · `REVIEW` · `DONE` · `NOT APPLICABLE`

This checklist records evidence. A documentation file existing is not by itself proof that a product or release gate has passed.

## P0 — Charter and documentation integrity

| Item | Status | Evidence required |
|---|---|---|
| Approve target users and primary workflow | BLOCKED | Recorded human decision |
| Approve first supported platform and distribution model | BLOCKED | Accepted ADR |
| Approve ecosystem role and canonical contract owners | BLOCKED | Versioned integration map |
| Approve QSO-STUDIO as domain-neutral review-contract owner or designate an alternative | BLOCKED | Governance decision and migration plan |
| Approve AionUi host-adapter boundary and prohibit competing review semantics | BLOCKED | Cross-repository ADR and shared fixtures |
| Approve data classification, privacy, redaction, caching, export, and retention defaults | BLOCKED | Privacy decision and reviewer |
| Approve license and support/security ownership | BLOCKED | Repository metadata and policy |
| Separate display, annotation, proposal, approval, capability, execution, repository writes, canonical state, and payment authority | REVIEW | Architecture, portable-trust profile, and ADR review |
| Replace unsupported Pages claim with truthful build status | REVIEW | README, workflow, strict build result |
| Add project overview, architecture, design, portable-trust, gluing, workflow, onboarding, security, accessibility, and operations docs | REVIEW | Documentation PR |

## P1 — Reproducible documentation artifact

| Item | Status | Evidence required |
|---|---|---|
| Strict MkDocs configuration | DONE | `mkdocs.yml` and successful exact-branch build |
| Pinned CI documentation toolchain | DONE | Successful Documentation workflow run |
| Internal link and navigation validation | REVIEW | Exact-head `mkdocs build --strict` after portable-trust additions |
| Accessibility review of documentation | OPEN | Keyboard, heading, link, table, diagram-alternative, and critical-state review |
| Security/privacy review of documentation and workflow | OPEN | Permission, dependency, redaction, and public-build review |
| Artifact checksum and provenance | REVIEW | Exact-head artifact digest and workflow metadata retained in pull request evidence |
| Publication owner, environment, and canonical URL | BLOCKED | Charter decision |
| Publication verification and rollback rehearsal | BLOCKED | Approved deployment evidence |

## P2 — First read-only workflow contract

| Item | Status | Evidence required |
|---|---|---|
| Select one record type and exact contract owner/version | BLOCKED | Approved manifest entry |
| Approve normalized review-record identity and version | BLOCKED | Versioned schema and registry entry |
| Define bounded parser limits | OPEN | Versioned design and tests |
| Define normalized review model | REVIEW | Design and portable-trust profile review |
| Define finding and compatibility model | REVIEW | Design review |
| Define separate source, interpretation, proposal, disposition, capability, receipt, reconciliation, annotation, export, correction, revocation, and checkpoint identities | REVIEW | Contract review and fixtures |
| Create deterministic fixture matrix | BLOCKED | Upstream contracts and fixture hashes |
| Define accessible summary, detail, timeline, comparison, capability, reconciliation, and recovery states | OPEN | UX specification and test cases |
| Define non-authoritative review-note export | REVIEW | Contract and wording review |
| Define correction, supersession, revocation, cache invalidation, and re-review behavior | OPEN | Versioned contract and tests |
| Prove absence of write/execution/payment/capability clients | BLOCKED | Implementation and dependency evidence |

## P2A — Portable-trust gluing

| Item | Status | Evidence required |
|---|---|---|
| Approve Repository `0`/`1` route and identities | BLOCKED | Accepted portable-trust contract |
| Approve JusticeForMe/PhantomBlock observation vocabulary and conflict semantics | BLOCKED | Shared adapter fixtures |
| Approve Repository `1` disposition, correction, revocation, and recovery semantics | BLOCKED | Authority contract and owner |
| Approve QSO-STUDIO ↔ AionUi review compatibility contract | BLOCKED | Shared positive and negative fixtures |
| Wrong-device and wrong-workspace rejection | OPEN | Deterministic fixtures |
| Stale and replayed record handling | OPEN | Deterministic fixtures |
| Partial and conflicting observation handling | OPEN | Deterministic fixtures |
| Broadened, expired, revoked, or wrong-executor capability handling | OPEN | Deterministic fixtures |
| Expected-state, post-state, partial-execution, and rollback handling | OPEN | Deterministic fixtures |
| Privacy downgrade, public-build exclusion, and redaction handling | OPEN | Security/privacy fixtures |
| Correction, revocation, active-session, cache, and export invalidation | OPEN | Propagation fixtures |
| Emergency freeze and recovery-view behavior | OPEN | Tabletop and deterministic fixtures |
| Triple-overlap witnesses across adapters, Repositories `0`/`1`, executors, Bridge/Digitalis, Studio, and AionUi | OPEN | Immutable fixture bundle and results |

## P3 — Future UI candidate

| Item | Status | Evidence required |
|---|---|---|
| Minimal application skeleton | BLOCKED | P0–P2A acceptance |
| Unit, component, contract, integration, and smoke tests | BLOCKED | Exact-head test reports |
| Hostile-input and resource-limit tests | BLOCKED | Security report |
| Keyboard and assistive-technology workflow tests | BLOCKED | Accessibility report |
| Build artifacts, SBOM, checksums, and provenance | BLOCKED | Release evidence bundle |
| Recovery and rollback rehearsal | BLOCKED | Recorded result |
| Human release approval | BLOCKED | Named reviewer and decision |

## Evidence log

- 2026-07-21 — Added the portable-trust review profile, twenty-item obstruction ledger, pairwise gluing matrix, triple-overlap witnesses, and expanded release blockers. Exact-head validation is pending after these changes.
- 2026-07-19 — Documentation workflow passed the pinned strict build and produced the `qso-studio-site` artifact; exact-head identifiers and digest are retained in the pull request evidence.
- 2026-07-19 — Consent Capacity Lock passed on the documentation candidate. Charter, publication, application, and release approval remain blocked or in review.
