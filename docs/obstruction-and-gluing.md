# Obstruction and Gluing Analysis

## Purpose

This ledger treats each repository as a local architectural section and each contract as a gluing map. A portfolio feature composes only when overlapping repositories agree on identity, state, authority, versioning, privacy, evidence, correction, revocation, and recovery semantics.

This is an engineering compatibility analysis, not a claim that a formal homology computation has been completed.

## Active obstructions

| ID | Obstruction | Repositories or planes | Risk | Candidate repair |
|---|---|---|---|---|
| ST-01 | Review-surface ownership collision | QSO-STUDIO, AionUi | Both can become competing sources for review, annotation, export, or approval semantics | Keep QSO-STUDIO domain-neutral; constrain AionUi to an optional compatible host adapter |
| ST-02 | Display and approval collapse | QSO-STUDIO, AionUi, Repository `1`, external human approval | A displayed selection or button could be mistaken for authorization | Require separately identified approval/disposition records; UI acts remain non-authoritative |
| ST-03 | Record-identity collapse | Seeker, Digitalis, Bridge, Repository `0`, Repository `1`, Studio | Observation, interpretation, transport, proposal, disposition, receipt, and review can share one misleading identity | Preserve typed identities and digests linked by correlation references |
| ST-04 | Device/workspace subject collision | Repositories `0` and `1`, Studio, delegated engineering shells | Device authorization may be misread as repository authority, or a repository task may run on the wrong device | Bind device and workspace independently and display both bindings |
| ST-05 | Local and canonical state collision | Repository `0`, Repository `1`, Studio | Local proposal or execution success can appear canonical | Show local, quarantined, authorized, executed, and reconciled states separately |
| ST-06 | Capability-class confusion | Portable remediation, engineering, provider, repository, release, deployment | A narrow capability could be broadened through generic UI treatment | Use typed capabilities and exact resource, action, executor, environment, and expiry fields |
| ST-07 | Completion-state optimism | JusticeForMe, PhantomBlock, Repository `0`, Studio | Partial or failed collection may look complete | Require per-check completion and preserve `UNKNOWN`, `UNSUPPORTED`, and `PARTIAL` |
| ST-08 | Observation duplication and conflict | JusticeForMe, PhantomBlock, other adapters | Duplicate observations can inflate confidence or conflicts can disappear | Canonical field vocabulary, deduplication keys, conflict semantics, source lineage, and fixtures |
| ST-09 | Temporal ambiguity | Temporal invariants, Seeker, Bridge, Repository `1`, Studio | Event, observation, receipt, and canonical times can be conflated | Display typed clocks, uncertainty, freshness, replay, and ordering source |
| ST-10 | Transformation opacity | Digitalis, Bridge, Studio | A derived or transformed record may appear source-equivalent | Require declared transformation, lineage, input/output digests, and losslessness status |
| ST-11 | Privacy downgrade | All evidence producers, Studio, AionUi, Pages | Sensitive records may be shown, cached, exported, or published at a weaker classification | Inherit the strictest classification; explicit redaction and export policy; public-build checks |
| ST-12 | Correction divergence | Source authority, Repository `1`, Studio, AionUi | Corrected records may coexist with stale summaries and exports | First-class corrections, supersession links, cache invalidation, and re-review |
| ST-13 | Revocation propagation gap | Repository `1`, capability issuer, Studio, executors | Revoked capabilities or evidence may remain active in sessions or exports | Revocation events, session invalidation, visible revoked state, and bounded propagation checks |
| ST-14 | Cache and session authority leakage | Studio, AionUi, browser/desktop shells | Old UI state may survive identity, policy, or authority changes | Cache identity/version binding, short retention, invalidation, and no browser secret storage |
| ST-15 | Public/private topology collision | GitHub Pages, desktop/WebUI mode, backend services | Static public documentation may be treated as an authenticated operations console | Separate public documentation from privileged adapters and backends |
| ST-16 | Export authority ambiguity | Studio, AionUi, external review systems | A review export may be mistaken for signed approval or canonical evidence | Mark exports non-authoritative and bind source identities, redactions, and limitations |
| ST-17 | Emergency-stop dependency | Repository `1`, Studio, AionUi, executor | The same compromised component may be required to stop itself or display recovery truth | Independent freeze/revocation authority and read-only recovery view |
| ST-18 | Contract-version drift | Neutral profiles, Studio, AionUi, Repository `1` | Interfaces may parse records differently or silently accept unsupported versions | Exact profile registry, deny-by-default version admission, and compatibility fixtures |
| ST-19 | Accessibility-state loss | Studio, AionUi | Critical authority or security state may be encoded only visually | Text labels, semantic structure, keyboard path, table alternatives, and non-color indicators |
| ST-20 | Diagnostic provenance loss | Studio, adapters, parsers | Parser warnings and redactions may be separated from the reviewed record | Bind diagnostics and parser version to the review session and export |

## Material obstruction

The highest-priority obstruction is **ST-01 combined with ST-02**: QSO-STUDIO and AionUi overlap as review surfaces, but the portfolio lacks one accepted contract for review records, annotations, comparison, exports, approval references, corrections, revocations, and recovery state.

Without that contract, two interfaces can display the same evidence differently, infer different authority, or create incompatible review artifacts. The lowest-coupling repair is to:

1. keep QSO-STUDIO as the candidate domain-neutral review-contract and accessibility owner;
2. keep AionUi as an inherited desktop/WebUI shell with an optional compatible adapter;
3. require Repository `1` or an external approved authority to own disposition and capability state;
4. preserve UI actions as non-authoritative unless a separately governed approval record is created;
5. validate both surfaces against shared deterministic fixtures.

This remains a recommendation until formally approved.

## Pairwise gluing matrix

| Edge | Required agreement | Fail-closed cases |
|---|---|---|
| Observation adapter → Repository `0` | device identity, profile, completion, provenance, field vocabulary, privacy | wrong device, partial collection, unsupported field, digest mismatch |
| Repository `0` → Repository `1` | proposal version, expected state, scope, replay, issuer/requester identity | stale, replayed, wrong head, unsupported version, broadened scope |
| Repository `1` → QSO-STUDIO | disposition identity, canonical status, correction/revocation, privacy | unknown issuer, missing digest, revoked disposition, privacy downgrade |
| Capability → QSO-STUDIO | exact device/workspace/action/executor/expiry/revocation | wrong subject, expired, broadened, unsupported authority |
| Executor receipt → QSO-STUDIO | attempt identity, capability binding, pre/post state, partial failure | receipt without capability, mismatched executor, unverifiable post-state |
| Digitalis/Bridge → QSO-STUDIO | transformation identity, lineage, input/output digest, transport receipt | opaque transform, lost lineage, delivery presented as truth |
| QSO-STUDIO → AionUi | review model, state vocabulary, accessibility, non-authority, redaction | approval injection, unsupported state coercion, sensitive public cache |
| QSO-STUDIO → external approval authority | immutable reviewed record, review identity, limitations, separate approval result | annotation treated as approval, stale review, wrong record digest |
| Correction/revocation → Studio session | supersession, invalidation, re-review, export handling | stale cache, old export shown current, revoked capability active |
| Emergency stop → QSO-STUDIO | freeze identity, affected scope, evidence preservation, recovery owner | automatic unlock, hidden freeze, recovery through compromised authority |

## Triple-overlap witnesses

### Adapter → Repository `0` → QSO-STUDIO

Prove that collection completion, unsupported controls, conflicting observations, source provenance, and privacy remain consistent from raw adapter output through proposal review.

### Repository `0` → Repository `1` → QSO-STUDIO

Prove that local staging, quarantine, disposition, capability, and canonical reconciliation remain distinct and that Studio cannot convert a proposal into authority.

### Repository `1` → executor → QSO-STUDIO

Prove executor identity, capability scope, expiry, revocation, partial execution, rollback, and resulting-state mismatch handling.

### Seeker/Digitalis → Bridge → QSO-STUDIO

Prove record, interpretation, transport artifact, delivery receipt, and review identity remain distinct and that delivery does not imply acceptance.

### QSO-STUDIO → AionUi → external approval authority

Prove both interfaces render the same state vocabulary and record identity, preserve non-authoritative annotations, and emit compatible approval references without granting authority.

### Correction authority → Repository `1` → QSO-STUDIO

Prove original history is retained, superseded conclusions are invalidated, and material corrections trigger re-review.

### Revocation authority → QSO-STUDIO → active session/export

Prove revoked capabilities, evidence, or identities are marked and invalidated in active views, caches, and future exports.

### Emergency stop → Repository `1` → QSO-STUDIO recovery view

Prove freeze state is independently visible, no automatic unlock occurs, evidence remains preserved, and restart requires approved recovery state.

## Required deterministic fixture groups

Each applicable contract edge requires fixtures for:

- valid supported record;
- malformed record;
- unsupported profile or version;
- missing identity or digest;
- wrong device;
- wrong workspace;
- stale record;
- replayed request;
- partial collection or execution;
- conflicting observations;
- privacy downgrade;
- broadened capability;
- expired capability;
- revoked capability;
- wrong executor;
- expected-state mismatch;
- correction and supersession;
- emergency freeze;
- rollback and recovery;
- inaccessible or ambiguous presentation.

## Ownership decisions required

| Decision | Candidate | Alternatives |
|---|---|---|
| Domain-neutral review contract | QSO-STUDIO | neutral contract repository or QSO Field registry |
| Desktop/WebUI host shell | AionUi | independent future client |
| Canonical disposition and capability | Repository `1` | approved successor trust authority |
| Review approval | external named human authority | separately chartered approval service |
| Generic envelope and profile registry | unassigned | QSO Field, neutral package, or dedicated registry repository |
| Privacy and retention policy | unassigned | portfolio governance plus repository-specific overlays |
| Correction and revocation authority | source authority plus Repository `1` reconciliation | dedicated canonical evidence authority |
| Emergency stop and recovery | independent named security authority | approved recovery quorum |

## Release blockers

QSO-STUDIO must remain documentation-only until:

- review-surface ownership and AionUi boundaries are approved;
- at least one exact upstream profile and fixture set is accepted;
- normalized review, annotation, comparison, export, correction, and revocation contracts are versioned;
- privacy, redaction, retention, cache, and public/private topology are approved;
- deterministic pairwise and triple-overlap fixtures pass;
- accessibility and hostile-input review evidence exists;
- no direct execution, credential, repository-write, payment, or self-approval path is present;
- incident, freeze, rollback, and recovery owners are named.
