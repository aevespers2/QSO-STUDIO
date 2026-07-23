# Changelog

`QSO-STUDIO-DOCS-CANDIDATE-001`

## Unreleased

### Product
- 2026-07-16 — Established product/UX charter approval and documentation integrity as the first QSO-STUDIO objective.
- 2026-07-16 — Defined the initial user outcome as a truthful read-only evidence-review workflow; runtime execution, repository writes, credentials, and payment control remain out of scope.
- 2026-07-23 — Added a reviewable documentation candidate without representing a site, application, package, or integration as released.

### Architecture
- Studio separates source evidence, normalized presentation, accessible review, local proposals, exported review packets, human/repository review, and any later upstream action.
- Added explicit source, rendering, proposal, repository, runtime, and financial trust boundaries.
- Added a prose-equivalent Mermaid architecture diagram.
- Preserved the runtime-local versus Fabric-level record-role collision as an unresolved integration blocker.

### Added
- `docs/index.md` documentation front door.
- Product and UX charter.
- Architecture and trust-boundary outline.
- Fixture-oriented read-only evidence-review workflow.
- Integration contract map.
- Onboarding and developer guides.
- Accessibility and security/privacy requirements.
- `punchlist.md` with completed documentation work and blocking decisions.
- Deterministic documentation validator and hostile regression suite.

### Changed
- Replaced the unsupported statement that a GitHub Pages site is already published with an accurate documentation-candidate notice.
- Aligned `README.md`, `taskchain.md`, `release.md`, `punchlist.md`, and `changelog.md` to one candidate identifier and publication boundary.
- Distinguished passing documentation checks from charter approval, publication approval, release approval, interface acceptance, and implementation authority.

### Fixed
- Removed the contradiction between the README's former `docs/`/Pages claim and the repository's actual contents.
- Added explicit currentness, correction, withdrawal, provenance, accessibility, and rollback requirements.
- Prevented annotations and exported review packets from being described as repository or runtime changes.

### Security
- Required synthetic and non-sensitive public materials, inert rendering, strict inputs, least privilege, explicit network/storage policy, source provenance, dependency review, and rollback propagation.
- Retained `QSO-CONSENT-CAPACITY-LOCK-v1` governance across the documentation candidate.

### Accessibility
- Required logical headings, descriptive links, text alternatives, non-color state indicators, keyboard access, reflow, reduced motion, accessible graphs/timelines, and error recovery.

### Release
- Documentation candidate remains blocked on charter, platform, license, ownership, upstream contracts, manual reviews, publication approval, and resulting-route verification.

### Deployment
- No Pages publication, application deployment, package release, or infrastructure change is authorized by this documentation milestone.

## Entry format
- Date
- Category: Product / Architecture / Added / Changed / Fixed / Security / Accessibility / Release / Deployment
- Summary
- Evidence: issue, PR, commit, workflow, artifact, or deployment record
- Impact and migration notes where applicable
