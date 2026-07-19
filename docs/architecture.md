# Architecture

## Architectural objective

QSO-STUDIO should be an adapter-based review application with a deliberately narrow core. The core accepts versioned evidence bundles, validates them through explicitly selected contracts, maps them into a stable review model, and renders them without acquiring upstream authority.

## Context diagram

```mermaid
flowchart LR
    U[Researcher or operator]
    S[QSO-STUDIO]
    C[Versioned contract manifest]
    F[Local fixtures or approved evidence export]
    R[Review-note export]
    H[External human review]
    A[Authorized upstream systems]

    U -->|inspect and compare| S
    C -->|schema and compatibility rules| S
    F -->|read-only records| S
    S -->|non-authoritative note| R
    R --> H
    H -->|separate approved action| A
    A -. no direct command path .-> S
```

The dotted relationship is descriptive only: upstream systems may provide exports to Studio, but the first workflow does not create a command channel from Studio to those systems.

## Logical components

```mermaid
flowchart TB
    I[Input boundary]
    P[Parser]
    V[Contract validator]
    N[Review-model normalizer]
    Q[Query and comparison service]
    UI[Accessible presentation layer]
    E[Review-note exporter]
    O[Observability and diagnostics]

    I --> P
    P --> V
    V -->|valid or findings| N
    N --> Q
    Q --> UI
    UI --> E
    I --> O
    P --> O
    V --> O
    N --> O
    E --> O
```

### Input boundary

Accepts only configured local fixtures or approved evidence exports. It records the input filename or source identifier, byte length, media type, digest, and import time. It does not follow embedded links or execute embedded content.

### Parser

Decodes a supported serialization format with explicit size, depth, and field-count limits. Unknown fields are preserved for diagnostics when safe, but they are not silently promoted into trusted model fields.

### Contract validator

Selects a schema by an exact identifier from the integration manifest. Validation findings are data, not exceptions hidden from the user. Unsupported versions fail closed with a clear compatibility message.

### Review-model normalizer

Maps validated domain records into a stable presentation model containing identity, source, time, integrity, status, relationships, findings, and raw evidence references. Normalization must not rewrite the source record.

### Query and comparison service

Supports deterministic filtering, sorting, relationship traversal, and field-by-field comparison over the normalized model. Queries are local and side-effect free in the first workflow.

### Accessible presentation layer

Renders summaries, detail views, timelines, tables, relationship views, validation findings, and textual alternatives for every visual representation.

### Review-note exporter

Produces a non-authoritative document containing reviewer-entered observations plus immutable references to evidence digests, schema identifiers, and Studio version. It never emits an approval token or execution instruction.

### Observability and diagnostics

Records local diagnostic events needed to reproduce parsing, validation, and rendering failures. Sensitive record content is excluded by default; diagnostic export requires deliberate user action and redaction review.

## Trust boundaries

```mermaid
flowchart LR
    subgraph Untrusted[Untrusted or not-yet-verified]
      X[Evidence files]
      Y[Embedded text and links]
    end
    subgraph Studio[QSO-STUDIO process]
      B[Bounded parser]
      V[Validator]
      M[Read-only review model]
      P[Presentation]
    end
    subgraph External[Separate authority]
      H[Human reviewer]
      U[Upstream runtime/repository/payment systems]
    end

    X --> B
    Y --> B
    B --> V
    V --> M
    M --> P
    P --> H
    H --> U
```

Boundary rules:

1. Input content is untrusted until parsed and validated.
2. Rendering never interprets record text as executable markup.
3. Studio's normalized model is a view, not a new canonical record.
4. Exported notes contain references, not authority.
5. Any future write connector requires a separate ADR, threat model, contract, test plan, and release approval; it is not part of the current scope.

## Deployment candidates

The charter has not selected a platform. The architecture should remain portable across:

- a local static prototype using fixture data;
- a packaged desktop application with local-only storage;
- a browser application backed by a separately governed read-only gateway.

These are alternatives, not simultaneous commitments. The first platform decision must consider offline operation, data classification, update ownership, accessibility testing, signing, distribution, and support burden.

## Failure behavior

Studio should fail closed at the boundary it can control:

- unsupported contract: show incompatibility and do not normalize;
- digest mismatch: quarantine the bundle in memory and show the expected and actual digests;
- malformed record: preserve a bounded diagnostic excerpt and continue only with independent records;
- missing attribution: label the record incomplete and prevent authoritative-looking export;
- renderer failure: provide a plain-text record view;
- export failure: leave evidence unchanged and report the destination and error without partial authority artifacts.
