# Release Validate Branch

**Pfad:** `actions/release-validate-branch/action.yml`

## Beschreibung

Verifies that a release tag points to a commit on the release branch

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `commit-sha` | nein | `—` | Commit SHA the tag points to. Defaults to GITHUB_SHA. |
| `branch` | nein | `main` | Branch release tags must be created from |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Outputs:** keine. **Berechtigungen und Secrets:** `contents: read`; keine
zusätzlichen Secrets oder Schreibberechtigungen.

**Voraussetzungen und Einschränkungen:** Das Repository muss im aufrufenden Job
ausgecheckt sein und der Ziel-Branch muss remote verfügbar sein. Die Action prüft,
ob der angegebene Commit zum konfigurierten Branch gehört; sie validiert weder
Tag-Namen noch erstellt sie Tags.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-validate-branch@v1
```

Siehe auch: [workflow-release-validate-branch](workflow-release-validate-branch)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
