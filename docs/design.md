# Design contracts

## Design principles

### Evidence before interpretation

Every important conclusion shown in Studio should be traceable to the exact record, contract version, validation result, and digest that produced it. Interpretive labels must be distinguishable from source fields.

### Authority is visible

Views should state whether an item is source evidence, normalized data, a local annotation, a proposal, a human decision, or an externally executed result. Color alone must never communicate this distinction.

### Read-only by construction

The first workflow has no command client, repository token, payment credential, signing key, or mutable upstream connector. A disabled button is not an adequate boundary; the capability should be absent from the build.

### Determinism where review depends on it

Given the same fixture bundle, manifest, locale, timezone configuration, and Studio version, parsing, validation, ordering, comparison, and export references should be reproducible.

### Progressive disclosure

The default view summarizes identity, source, time, integrity, status, and highest-severity findings. Raw fields and diagnostic details remain available without overwhelming the primary review path.

## Integration manifest

Before a record type is supported, Studio should receive a version-controlled manifest entry similar to:

```yaml
record_type: qso.genome
contract_id: qso-genome/v1
owner: QSO-GENOMES
media_types:
  - application/json
schema_digest: sha256:...
compatibility:
  read:
    - "1.x"
  write: []
fixture_set: fixtures/qso-genome-v1/
classification: internal-research
retention: session-only
```

The manifest is not a schema registry implementation. It is a design contract that identifies which external authority Studio is relying on and which operations are permitted.

## Review model

The normalized review model should expose common fields without erasing domain-specific content.

```text
ReviewRecord
├── record_type
├── record_id
├── contract_id
├── source
│   ├── owner
│   ├── source_id
│   └── imported_at
├── integrity
│   ├── algorithm
│   ├── expected_digest
│   ├── actual_digest
│   └── status
├── temporal
│   ├── observed_at
│   ├── effective_at
│   └── sequence
├── status
├── relationships[]
├── findings[]
├── attributes{}
└── evidence_reference
```

Unknown or domain-specific fields belong in `attributes` with their original names and types. Studio should not invent cross-domain equivalence without an approved mapping.

## Finding model

Validation, compatibility, security, and review findings should share a consistent shape:

```text
Finding
├── code
├── severity: info | warning | error | critical
├── source: parser | contract | integrity | policy | reviewer
├── message
├── record_id
├── field_path
├── evidence_reference
└── remediation_hint
```

A remediation hint is guidance only. It must not silently repair source evidence.

## Review-note export

A review note should contain:

- Studio version and build digest;
- manifest and contract identifiers;
- evidence bundle digest;
- selected record identifiers;
- deterministic comparison parameters;
- reviewer-entered text;
- export timestamp and timezone;
- a conspicuous statement that the note is non-authoritative.

The export should exclude raw sensitive values unless explicitly selected and visibly previewed.

## Visual design requirements

- Status, severity, and authority use text labels and icons in addition to color.
- Timelines have table and ordered-list alternatives.
- Graph views have relationship lists and keyboard navigation.
- Large datasets use virtualized or paged presentation without changing deterministic sort order.
- Empty, loading, partial, incompatible, and error states are designed rather than treated as edge cases.
- Source values and local annotations use distinct typography and labels.
- Destructive or authoritative language is avoided when the application lacks that authority.

## Future ADR triggers

A new architecture decision record is required before adding any of the following:

- remote data retrieval;
- persistent local storage;
- user accounts or organization permissions;
- plugins or extensions;
- write-back to an upstream system;
- cryptographic signing;
- payment operations;
- automated approvals;
- execution or scheduling commands;
- collection of telemetry beyond local diagnostic export.
