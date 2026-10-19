# Versioning

The repository uses Changesets to declare the intent of platform releases. The
private root package `ci-platform` is a shared version anchor only; nothing is
published to npm or GitHub Packages.

## Public version references

- Full release tags are immutable and use `v<major>.<minor>.<patch>`, for
  example `v1.2.3`.
- The mutable `v<major>` alias points to the latest compatible release in that
  major line, for example `v1`.
- Consumers using `@v1` automatically receive patch and minor releases.
- No `ci-platform@1.2.3` tags are created.

## Changeset policy

Changes to `.github/workflows/**`, `actions/**`, or scripts called by Actions
require a Changeset. Docs-/Wiki-only changes, issue templates, CODEOWNERS, and
README-only changes do not.

| Bump | Use when |
|---|---|
| `patch` | Bug fix without changing inputs, outputs, defaults, permissions, or workflow paths. |
| `minor` | Add an optional input, workflow/action, or optional output while preserving existing behavior and defaults. |
| `major` | Break the `workflow_call`/action contract, change a default, require new permissions, or change a workflow path. |

For example:

```markdown
---
"ci-platform": minor
---

Add optional `fail-on-warning` input to `quality-lint` (default remains false).
```

A breaking release creates the new major alias (for example `v2`) and never
moves the previous major alias (`v1`) to the breaking version.

## Release flow

1. A feature PR includes a Changeset when it changes a required path.
2. After merge to `main`, Changesets opens or updates the `chore: version
   packages` PR and updates `package.json` and `CHANGELOG.md`.
3. A merge without a Changeset creates no new SemVer tag and does not move a
   major alias.
4. After the version PR merges, CI reads the package version, creates the
   immutable `vX.Y.Z` tag, moves only its corresponding `vN` alias, and creates
   the GitHub Release from that Changeset changelog entry.

The tag push does not trigger versioning again. Reruns do not duplicate or move
an existing full version tag. The platform changelog heading follows the
Changesets format `## 1.2.3`; GitHub release validation accepts this heading.

For details, see [Release and Tagging Policy](RELEASING) and the
[Release Versioning workflow](workflow-release-versioning).

## Operational examples

- **Docs-only merge:** no Changeset is needed; the package version, full tag, and
  major alias remain unchanged.
- **Patch or minor Changeset:** the version PR updates the shared version, then
  CI creates the new full tag and moves the same-major alias.
- **Major Changeset:** `v2.0.0` creates or moves `v2`; `v1` remains on its
  previous compatible release.
- **Rerun:** an existing `vX.Y.Z` tag is not recreated or moved. CI can finish
  updating its matching alias and GitHub Release.
