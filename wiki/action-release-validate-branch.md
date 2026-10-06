# Release Validate Branch

**Pfad:** `actions/release-validate-branch/action.yml`

## Beschreibung

Verifies that a release tag points to a commit on the release branch

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `commit-sha` | nein | `—` | Commit SHA the tag points to. Defaults to GITHUB_SHA. |
| `branch` | nein | `main` | Branch release tags must be created from |

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-validate-branch@v1
```

Siehe auch: [workflow-release-validate-branch](workflow-release-validate-branch)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
