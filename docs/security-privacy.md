# Security and privacy

## Security objective

The first QSO-STUDIO workflow should safely inspect untrusted or not-yet-verified evidence without executing it, leaking it, or converting a display surface into an authority channel.

## Assets

- evidence records and their metadata;
- contract manifests and schema digests;
- reviewer observations;
- build artifacts and provenance;
- local configuration and diagnostic exports;
- the distinction between source evidence and Studio interpretation.

## Threats and controls

| Threat | Required control |
|---|---|
| Malformed or oversized input | Byte, depth, field, record, and time limits; bounded diagnostics |
| Script or markup injection | Render source text as inert text; no embedded script execution |
| Contract confusion | Exact identifiers and digests; unknown versions fail closed |
| Path traversal or recursive import | Platform file picker; canonical path checks; no implicit neighboring files |
| Digest substitution | Compute digest over original bytes before parsing and show expected versus actual |
| Misleading authority | Persistent labels for evidence, interpretation, proposal, and external decision |
| Secret collection | No credential fields, key stores, or repository tokens in the first build |
| Data leakage | No network access by default; explicit redacted diagnostic export |
| Dependency compromise | Pinned toolchain, dependency review, SBOM when application code exists |
| Build tampering | Commit-bound CI, artifact checksums, retained workflow evidence |
| Unsafe write path | Write clients absent from the first build, not merely disabled in the interface |

## Privacy model candidate

The first workflow should default to **session-only processing**:

- evidence is read from a user-selected local fixture;
- normalized data remains in memory;
- reviewer notes remain in memory until explicitly exported;
- no analytics or remote logging is enabled;
- diagnostic export excludes record values by default;
- closing the application clears the session unless the charter approves a persistence design.

Data classification and retention remain charter decisions. Studio must display the classification supplied by the integration manifest and must not downgrade it.

## Rendering rules

- Escape all source-provided text.
- Do not load remote images, fonts, frames, stylesheets, or links automatically.
- Display links as text and require deliberate user action before opening them.
- Do not render source-provided HTML or Markdown as trusted markup.
- Apply output-length limits and provide bounded inspection of very large fields.
- Preserve original values for evidence reference while allowing safe truncation in the visual view.

## Diagnostics

Diagnostic events should use stable codes and structural metadata rather than record content. A user-initiated diagnostic export should preview exactly what will be written and provide a redaction step.

Recommended event fields:

```text
event_code
studio_version
build_digest
manifest_id
contract_id
record_type
record_count
input_size
stage
result
finding_codes[]
duration_bucket
```

## Consent-capacity control

The repository contains `QSO-CONSENT-CAPACITY-LOCK-v1`. Documentation and future implementation must preserve its fail-closed behavior and human-final-review requirement. No Studio workflow may weaken or bypass that repository-wide policy.

## Security verification gates

Before any UI candidate is released, evidence should cover:

- hostile-input and resource-exhaustion tests;
- markup/script injection tests;
- path and file-boundary tests;
- dependency, secret, and workflow-permission review;
- network-denial verification for local-only mode;
- diagnostic redaction tests;
- artifact checksum and provenance verification;
- review of authority wording and exported-note labeling;
- independent human approval.
