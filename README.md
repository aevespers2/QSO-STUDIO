# QSO-STUDIO

`QSO-STUDIO-DOCS-CANDIDATE-001`

QSO-STUDIO is the proposed read-only design, inspection, and evidence-review workspace for Quantum State Objects and the broader QSO ecosystem.

## Documentation candidate

The repository contains a reviewable documentation tree under [`docs/`](docs/index.md). **It is not published as an authorized GitHub Pages site.** Publication remains a separate decision requiring an approved target, exact-head evidence, accessibility/security/privacy/licensing review, rollback planning, and resulting-route verification.

Start with:

- [Documentation front door](docs/index.md)
- [Product and UX charter](docs/product-charter.md)
- [Architecture](docs/architecture.md)
- [Read-only evidence review](docs/read-only-review-workflow.md)
- [Integration contracts](docs/integration-contracts.md)
- [Independent ecosystem conformance consumer](docs/ecosystem-conformance-consumer.md)
- [Architecture review quorum conformance](docs/architecture-review-quorum-conformance.md)
- [Onboarding](docs/onboarding.md)
- [Developer guide](docs/developer-guide.md)
- [Accessibility overview](docs/accessibility.md)
- [Accessibility review evidence](docs/accessibility-review-evidence.md)
- [Security and privacy](docs/security-privacy.md)
- [Punch list](punchlist.md)

## Product boundary

Studio may visualize governed records, genomes, messages, provenance, proposals, freeze points, experiment evidence, payment-related evidence, release state, and synthetic review diagnostics. It does not bypass upstream authorization, execute QSO workloads, mutate repositories, appoint reviewers, decide architecture, approve proposals autonomously, hold production credentials, or settle payments.

The first bounded workflows are fixture-backed and read-only. An annotation, review projection, or exported packet remains a proposal or diagnostic artifact until a separate authorized process accepts and applies it.

## Current status

- Documentation: candidate, with deterministic checks.
- Accessibility: requirements and exact-artifact review protocol documented; no accessibility certification is claimed.
- UI or executable: not implemented.
- Integrations: proposed and blocked on exact upstream contracts.
- Ecosystem manifest consumer: synthetic, independently implemented, and bound to `QSO-FABRIC#21@25036a5cfcea79e204a4660ddd1af09c054935b1`; it grants no admission or runtime authority.
- Architecture-review consumer: synthetic, independently implemented, and rebound to `qso-field.github.io#24@a56b1fa93f151ee14f3cdd4183b89a10e268e352`; it grants no appointment, quorum, decision, activation, merge, or release authority.
- Pages publication: not authorized or represented as active.
- Release: blocked on charter and governance decisions.

QSO-STUDIO PR #4 diverged from current `main`. Its manifest-consumer work was superseded by merged PR #7, and its architecture-review consumer has now been extracted onto a current-main repair branch with a renewed producer tuple. PR #4 remains historical evidence and must not be treated as current validation.

This repository is governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
