# Changelog

`QSO-STUDIO-DOCS-CANDIDATE-001`

## Unreleased

### Product
- 2026-07-16 — Established product/UX charter approval and documentation integrity as the first QSO-STUDIO objective.
- 2026-07-16 — Defined the initial user outcome as a truthful read-only evidence-review workflow; runtime execution, repository writes, credentials, and payment control remain out of scope.
- 2026-07-23 — Added a reviewable documentation candidate without representing a site, application, package, or integration as released.
- 2026-07-23 — Added bounded synthetic ecosystem-manifest and architecture-review consumers without representing QSO-STUDIO as admitted, operational, appointed, or authorized to decide or execute.
- 2026-07-23 — Added an exact-artifact accessibility review protocol without representing documentation, a rendered site, synthetic consumers, or a future UI as accessibility-certified.

### Architecture
- Studio separates source evidence, normalized presentation, accessible review, local proposals, exported review packets, synthetic review diagnostics, human/repository review, architecture decision, activation, and any later upstream action.
- Added explicit source, rendering, proposal, repository, runtime, governance, and financial trust boundaries.
- Added prose-equivalent Mermaid architecture diagrams.
- Preserved the runtime-local versus Fabric-level record-role collision as an unresolved integration blocker.
- Bound the manifest consumer to QSO-FABRIC PR #21 head `25036a5cfcea79e204a4660ddd1af09c054935b1`, Git blob `5070ac6615b8127b14a9f230678f58a081c6c2c4`, and SHA-256 `c5e6d2e42fdbe9703d9f28c7f65ffff02208bff52fa96ee7090bfcbcb5dea728`.
- Bound the architecture-review consumer to QSO Field PR #24 head `a56b1fa93f151ee14f3cdd4183b89a10e268e352`, run `30000668553`, artifact `8560824564`, and digest `sha256:f266006a19bd8a5d95b4c7aeedfc0bac950f1932d7b58eef88ee7eac6f62e77a`.
- Separated accessibility requirements from exact-artifact review evidence and from publication, product, release, runtime, repository, reviewer, architecture, and payment authority.

### Added
- `docs/index.md` documentation front door.
- Product and UX charter.
- Architecture and trust-boundary outline.
- Fixture-oriented read-only evidence-review workflow.
- Integration contract map.
- Independent ecosystem-conformance consumer guide.
- Independent architecture-review quorum conformance guide.
- Immutable consumer source tuples and synthetic fixtures.
- Strict consumers, source-before-parse identity gates, and hostile regression suites.
- SHA-pinned, read-only, exact-head consumer workflows with retained evidence.
- Onboarding and developer guides.
- Accessibility and security/privacy requirements.
- `docs/accessibility-review-evidence.md` with `DOCUMENTED_NOT_CERTIFIED` status, review-surface matrix, text evidence and authority states, accessible evidence-flow diagram, exact-artifact binding, manual review protocols, a documentation-only YAML record, fail-closed stop conditions, correction, withdrawal, supersession, rollback, reviewer onboarding, and FYSA-120 mapping.
- `punchlist.md` with completed documentation work and blocking decisions.
- Deterministic documentation validator and hostile regression suite.

### Changed
- Replaced the unsupported statement that a GitHub Pages site is already published with an accurate documentation-candidate notice.
- Aligned `README.md`, `docs/index.md`, `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` to one candidate identifier and publication boundary.
- Distinguished passing documentation, manifest, review-corpus, and accessibility checks from charter approval, publication approval, accessibility certification, ecosystem admission, reviewer appointment, real quorum, architecture decision, interface acceptance, release approval, and implementation authority.
- Rebuilt the useful QSO-STUDIO PR #4 consumers from current `main` rather than force-updating a diverged branch.
- Rebound the architecture-review source tuple from historical QSO Field head `49a93b25f1b04c13b97fef93a786afa4bf1048c4` to current PR #24 head `a56b1fa93f151ee14f3cdd4183b89a10e268e352` while preserving the independent evaluator and corpus identities.
- 2026-07-23 — Extended documentation validation to relevant `main` pushes so future resulting-default heads receive their own retained exact-head evidence generation.
- 2026-07-23 — Required the accessibility review protocol as part of the deterministic documentation surface and aligned release gates, artifact requirements, rollback, and planning controls.

### Fixed
- Removed the contradiction between the README's former `docs/`/Pages claim and the repository's actual contents.
- Added explicit currentness, correction, withdrawal, provenance, accessibility, supersession, and rollback requirements.
- Prevented annotations and exported review packets from being described as repository or runtime changes.
- Prevented stale PR #4 exact-head evidence from being represented as current after `main` advanced.
- Added fail-closed source-tuple drift, raw-byte drift, duplicate-key, non-finite-number, Boolean/integer confusion, unsafe-default, identifier, version, governance, self-review, quorum, dissent, appeal, supersession, and authority-promotion checks.
- Closed the documentation workflow gap that previously left resulting `main` documentation heads without automatic retained validation.
- Prevented source-level or partial accessibility checks from being described as rendered-artifact certification.

### Security
- Required synthetic and non-sensitive public materials, inert rendering, strict inputs, least privilege, explicit network/storage policy, source provenance, dependency review, and rollback propagation.
- Retained `QSO-CONSENT-CAPACITY-LOCK-v1` governance across the documentation and consumer candidates.
- Kept workflow permissions read-only, disabled persisted checkout credentials, pinned external Actions, bounded execution time, and isolated generated evidence outside the checkout.

### Accessibility
- Required logical headings, descriptive links, text alternatives, non-color state indicators, keyboard access, reflow, reduced motion, accessible graphs/timelines, and error recovery.
- Added equivalent prose for consumer and accessibility evidence-flow diagrams.
- Defined `NOT_REVIEWED`, `PARTIAL`, `PASS`, `FAIL`, `BLOCKED`, `UNKNOWN`, `SUPERSEDED`, `WITHDRAWN`, and `CORRECTED` evidence states.
- Defined source evidence, interpretation, annotation, proposal, review diagnostic, human disposition, and external action as separate authority-bearing classes.
- Added exact source/build/artifact/environment binding, manual keyboard/screen-reader/zoom/contrast/motion/comprehension review, correction-linked evidence, and fail-closed stop conditions.

### Release
- Documentation, accessibility-evidence, and consumer candidates remain blocked on charter, platform, license, ownership, upstream contracts, namespace/payload partitioning, reviewer-governance decisions, rendered manual reviews, publication approval, and resulting-route verification.

### Deployment
- No Pages publication, accessibility certification, application deployment, package release, ecosystem admission, reviewer appointment, architecture activation, or infrastructure change is authorized by this milestone.

## Entry format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Accessibility / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
