# Portable Trust Review Profile

## Status

This document is a **candidate review-surface contract** for QSO-STUDIO. It does not create an application, backend, credential, approval service, device inventory collector, remediation client, repository writer, or canonical-state authority.

QSO-STUDIO remains a domain-neutral, read-only evidence-review workspace. AionUi may later host a compatible desktop or WebUI adapter, but the host shell must not redefine the underlying review semantics or silently gain approval authority.

## Purpose

The portable device-trust foundation uses Repository `0` to observe, compare, propose, execute only separately authorized changes, and verify results. Repository `1` is the candidate independent authority for quarantine, capability issuance, revocation, canonical disposition, checkpoints, and recovery.

QSO-STUDIO provides a bounded human review surface across that lifecycle:

```text
observation
  → Repository 0 proposal
  → Repository 1 quarantine and disposition
  → narrow capability
  → bounded execution
  → execution receipt
  → Repository 1 reconciliation
  → correction, revocation, or recovery checkpoint
```

Studio may display, compare, annotate, filter, and export review material. Display, selection, annotation, export, or operator attention does not create approval, authorization, canonical truth, or execution permission.

## Responsibility boundary

| Function | Owner | QSO-STUDIO role |
|---|---|---|
| Device observation | JusticeForMe, PhantomBlock, or another approved adapter | Display source identity, completion, provenance, limitations, and integrity status |
| Local analysis and proposal | Repository `0` | Display proposal scope, expected pre-state/post-state, risk, rollback, and evidence |
| Quarantine and authority decision | Repository `1` | Display disposition and authority evidence without recreating or overriding it |
| Capability issuance and revocation | Repository `1` or approved authority | Display exact scope, identity binding, expiry, revocation, and issuer evidence |
| Bounded execution | Approved executor | Display requested action and resulting receipt; never execute directly |
| Canonical reconciliation | Repository `1` | Display accepted, rejected, partial, disputed, corrected, or unknown status |
| Human annotation | QSO-STUDIO | Produce non-authoritative review records tied to immutable source identities |
| Desktop/WebUI hosting | AionUi or another approved shell | Render a compatible adapter without changing review or authority semantics |

## Identity separation

The following records must retain separate identifiers and digests:

1. device identity;
2. platform profile and baseline-policy identity;
3. source observation;
4. interpretation or temporal assessment;
5. Repository `0` proposal;
6. Repository `1` quarantine admission;
7. authority disposition;
8. capability;
9. execution attempt;
10. execution receipt;
11. resulting-state observation;
12. canonical reconciliation;
13. review annotation;
14. export package;
15. correction;
16. revocation;
17. recovery checkpoint.

A shared correlation identifier may link these records, but it must not replace their individual identities. The interface must prevent a user from mistaking delivery, display, execution success, or annotation for canonical acceptance.

## Review record

A candidate review record should contain:

```yaml
review_record_version: qso.studio.review.v1
review_id: urn:qso-studio:review:...
reviewed_record:
  record_type: observation | proposal | disposition | capability | receipt | checkpoint
  record_id: urn:...
  digest: sha256:...
  schema_or_profile: urn:...
  source_repository: owner/repository
  source_commit: immutable-sha
context:
  device_id: urn:device:...
  platform_profile_id: urn:platform-profile:...
  baseline_policy_id: urn:baseline-policy:...
  correlation_id: urn:portable-trust-case:...
reviewer:
  identity_reference: urn:reviewer:...
  role: analyst | operator | security-reviewer | approver-observer
  authentication_assurance: external-reference
assessment:
  status: noted | needs-information | concern | compatible | incompatible | unknown
  reason_codes: []
  notes: non-authoritative text
  compared_records: []
  limitations: []
created_at: RFC3339 timestamp
expires_at: optional RFC3339 timestamp
privacy:
  classification: public | internal | confidential | restricted
  redactions: []
authority:
  creates_approval: false
  creates_capability: false
  creates_canonical_state: false
```

The review record is append-only evidence about a human review act. Any operational approval must be represented by an independently governed approval record or Repository `1` disposition that references the review record when appropriate.

## Required presentation states

Every record view must expose at least:

- record type, identity, version, producer, source repository, and immutable source commit;
- integrity status and digest verification result;
- device and workspace binding where applicable;
- platform profile and baseline-policy version;
- collection or execution completion state;
- freshness, clock uncertainty, and replay status;
- privacy classification and applied redactions;
- capability scope, expiry, issuer, executor, and revocation state;
- canonical disposition and whether it is pending, accepted, rejected, partial, disputed, corrected, revoked, or unknown;
- limitations, unsupported controls, missing artifacts, and parser warnings;
- correction, supersession, revocation, incident, freeze, and recovery links.

The interface must never collapse `UNKNOWN`, `UNSUPPORTED`, `PARTIAL`, `STALE`, `REVOKED`, or `UNVERIFIED` into a reassuring or compliant state.

## View modes

### Case timeline

A chronological view of observations, proposals, decisions, capabilities, receipts, corrections, revocations, and recovery checkpoints. Ordering must distinguish event time, observation time, receipt time, and canonical-record time.

### Evidence comparison

A side-by-side or structured comparison that preserves:

- record identity and version;
- canonicalization and digest method;
- source and transformation lineage;
- per-field presence, conflict, uncertainty, and redaction;
- semantic differences between absent, false, unknown, unsupported, and not collected.

### Capability review

A view showing the exact device, workspace, operation, path, adapter, tool, command class, network destinations, expected pre-state, expected post-state, duration, retries, rollback, and required approvals.

### Result reconciliation

A view that compares:

- expected pre-state;
- observed pre-state;
- authorized action;
- execution result;
- expected post-state;
- observed post-state;
- Repository `1` reconciliation.

Execution success alone must not be shown as canonical success.

### Recovery view

A view of device loss, theft, compromise, replacement, revocation, key rotation, quarantine, clean reinstall, evidence preservation, and bounded restart status. Recovery controls remain external to Studio unless a separately approved action contract is introduced later.

## QSO-STUDIO and AionUi

The lowest-coupling candidate is:

- QSO-STUDIO owns the **domain-neutral review contract**, normalized review model, accessibility requirements, and non-authoritative export semantics;
- AionUi remains an inherited desktop/WebUI host shell that may implement an optional compatible adapter;
- static Pages in either repository remain public, read-only, credential-free, and limited to non-sensitive documentation or synthetic portfolio metadata;
- any authenticated or privileged mode uses a separately approved backend and cannot infer authority from the UI session alone.

Neither repository may independently redefine approval, capability, canonical-state, correction, revocation, or recovery semantics.

## Privacy and redaction

Portable-trust records may contain hostnames, account names, installed software, network configuration, addresses, certificates, device identifiers, paths, and security findings. The review surface must:

- default to the most restrictive inherited classification;
- redact secrets and sensitive identifiers before logs, screenshots, exports, or public artifacts;
- distinguish redacted from absent fields;
- avoid storing sensitive raw records in browser storage by default;
- define session, cache, clipboard, export, and diagnostic retention;
- propagate privacy changes, corrections, and revocations to derived views and exports;
- prevent public Pages builds from including real device inventories or private evidence.

## Correction and revocation

Corrections and revocations are first-class records. The review system must:

1. preserve the original record and its prior review history;
2. mark superseded or revoked material clearly;
3. link the correcting or revoking authority and reason;
4. invalidate stale comparisons, summaries, exports, and cached derived state;
5. require re-review where the correction changes a material conclusion;
6. avoid rewriting history as though the original record never existed.

## Accessibility requirements

Portable-trust review must be possible without color, pointer-only interaction, animation, or visual diagrams. Every state and relationship requires text equivalents, stable focus order, keyboard operation, semantic headings, table alternatives, scalable content, and explicit error recovery.

Critical states such as revoked, wrong-device, stale, partial, unsupported, privacy-restricted, and emergency freeze require text labels and cannot rely on color alone.

## Fail-closed behavior

Studio must refuse or visibly quarantine a review when:

- the record type or version is unsupported;
- record identity, digest, source commit, or required lineage is missing;
- device or workspace binding conflicts;
- a capability is expired, revoked, broadened, or issued by an unsupported authority;
- the source is stale or replay status is unresolved;
- privacy classification cannot be enforced;
- a required artifact is missing or does not match its digest;
- correction or revocation state is unresolved;
- parser limits are exceeded;
- a host shell attempts to inject action authority into the review contract.

## Pairwise compatibility fixtures

Required fixture groups include:

- observation adapter → Repository `0` proposal;
- Repository `0` proposal → Repository `1` quarantine;
- Repository `1` disposition → QSO-STUDIO display;
- capability → executor request;
- executor receipt → Repository `1` reconciliation;
- QSO-STUDIO review record → external approval reference;
- QSO-STUDIO review contract → AionUi adapter;
- correction or revocation → cached views and exports;
- emergency freeze → active review sessions.

Each group needs positive, malformed, unsupported-version, wrong-device, wrong-workspace, stale, replayed, partial, privacy-downgrade, correction, revocation, and rollback cases where applicable.

## Triple-overlap witnesses

The portfolio must prove consistent behavior across at least:

1. observation adapter → Repository `0` → QSO-STUDIO;
2. Repository `0` → Repository `1` → QSO-STUDIO;
3. Repository `1` → executor → QSO-STUDIO;
4. Bridge or Digitalis → Repository `1` → QSO-STUDIO;
5. QSO-STUDIO → AionUi → external approval authority;
6. correction authority → QSO-STUDIO → exported review package;
7. revocation authority → QSO-STUDIO → cached session;
8. emergency stop → Repository `1` → QSO-STUDIO recovery view.

## Non-goals

This profile does not authorize:

- device inspection or remediation;
- network probing, traffic interception, or remote administration;
- storage of credentials or signing keys;
- Repository `1` disposition or capability issuance;
- direct repository writes, merges, releases, deployments, or payments;
- executing commands, scripts, plugins, or retrieved content;
- using public GitHub Pages as a privileged operations console;
- claiming that a displayed device is secure merely because records are present.

## Acceptance requirements

Before implementation, approve:

- QSO-STUDIO as the domain-neutral review-contract owner or designate an alternative;
- the AionUi relationship and adapter boundary;
- record identities, namespaces, canonical serialization, hashing, and signing rules;
- privacy classification, redaction, retention, export, and deletion policy;
- Repository `1` disposition and correction/revocation semantics;
- exact supported record profiles and deterministic fixtures;
- named human approval, security, privacy, incident, emergency-stop, and recovery owners.
