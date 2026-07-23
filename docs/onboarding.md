---
layout: default
title: Onboarding
---

# Onboarding

## Before contributing

QSO-STUDIO is currently a documentation and design candidate. Do not represent a site, package, application, integration, or supported workflow as released unless the corresponding evidence and approval exist.

## Repository reading path

1. Read the [product charter](product-charter.md).
2. Review the [architecture](architecture.md) and trust boundaries.
3. Follow the [read-only workflow](read-only-review-workflow.md).
4. Check [integration contracts](integration-contracts.md) for unresolved upstream dependencies.
5. Review [accessibility](accessibility.md) and [security/privacy](security-privacy.md) before changing a public route.
6. Read `taskchain.md`, `punchlist.md`, `release.md`, and `changelog.md` before proposing work.

## Safe first contribution

A suitable first contribution improves wording, navigation, text alternatives, link integrity, source attribution, or consistency without changing product scope. Record the exact files changed, validation commands, limitations, and rollback method.

## Documentation validation

Run:

```bash
python3 scripts/check_documentation.py
python3 -m unittest tests.test_documentation -v
```

The checks validate required pages, internal links, headings, authority notices, accessibility text for diagrams, and alignment markers across planning documents.

## Prohibited actions

Do not add production credentials, private source data, direct runtime controls, unrestricted write paths, payment settlement actions, autonomous approvals, or executable untrusted content. Do not publish Pages or create a release without separate approval.

## Evidence expectations

A reviewable documentation change should include an exact source commit, deterministic validation output, retained artifact where available, and a clear statement of what remains proposed or blocked.

The repository remains governed by `QSO-CONSENT-CAPACITY-LOCK-v1`.
