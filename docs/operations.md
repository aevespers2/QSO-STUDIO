# Operations, recovery, and rollback

## Documentation build

The documentation workflow performs a strict MkDocs build and uploads the resulting static site as a short-lived workflow artifact. It does not deploy to GitHub Pages.

### Local verification

```bash
python -m pip install "mkdocs==1.6.1"
mkdocs build --strict
```

Record:

- commit SHA;
- Python and MkDocs versions;
- command and result;
- artifact name and size;
- content checksum;
- workflow run URL when CI is used.

## Publication procedure candidate

Publication remains blocked until the charter identifies the site owner, audience, privacy classification, canonical URL, retention, review authority, and rollback owner. Once approved, a publication workflow should:

1. build from an exact reviewed commit;
2. run strict link and documentation checks;
3. produce a checksummed artifact;
4. retain build provenance;
5. require the approved environment and reviewers;
6. publish only the reviewed artifact;
7. verify the deployed content and canonical URL;
8. preserve the prior artifact for rollback.

## Operational states

| State | Meaning | Allowed action |
|---|---|---|
| Draft | Documentation or product design under active change | Local build and PR review |
| Candidate | Exact commit has build evidence | Human review; no product claim |
| Published docs | Approved static documentation artifact is live | Monitor links and integrity |
| UI alpha | Future bounded application candidate | Approved test users only |
| Withdrawn | Artifact has integrity, scope, privacy, or safety concern | Remove publication and preserve evidence |

## Incident triggers

Treat the following as documentation or product incidents:

- published content claims an unimplemented capability;
- site content differs from the approved artifact digest;
- a contract owner or authority boundary is misrepresented;
- sensitive evidence is included in documentation or diagnostics;
- an external link becomes unsafe or misleading;
- the documentation build is no longer reproducible;
- the site becomes inaccessible for a primary review path;
- a future UI sends a network request in local-only mode;
- an export appears to confer approval or execution authority.

## Incident response

1. Stop publication or distribution of the affected artifact.
2. Preserve the commit, workflow logs, artifact digest, deployment record, and report.
3. Identify whether the issue is content, build, dependency, publication, privacy, accessibility, or authority-related.
4. Restore the last verified artifact when doing so reduces harm.
5. Correct the source on a dedicated branch.
6. Re-run the complete included-scope evidence package.
7. Obtain human approval before republishing.
8. Record the incident and recovery evidence in the changelog or an issue.

## Recovery

Documentation source is canonical; generated `site/` output is disposable. Recovery should begin from the last reviewed commit, recreate the environment from pinned dependencies, rebuild, compare digests, and verify representative pages before publication.

For a future application, user evidence files must remain external and unchanged. Session state should be recoverable only when an approved persistence design exists; otherwise recovery means restarting a clean session and re-importing the evidence.

## Rollback

Rollback criteria include:

- unsupported capability or publication claims;
- broken primary navigation or inaccessible core content;
- artifact digest mismatch;
- unresolved high-severity security or privacy finding;
- incorrect authority, ownership, or contract mapping;
- loss of reproducibility or provenance;
- failure of the immutable repository consent-capacity policy.

Rollback restores the prior verified artifact or removes publication entirely. It must not erase incident evidence.
