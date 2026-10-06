# Release Validate Tag Immutable

**Pfad:** `actions/release-validate-tag-immutable/action.yml`

## Beschreibung

Rejects tag updates (force-push or move) on push events

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `tag` | nein | `—` | Tag to validate. When empty, derived from GITHUB_REF. |
| `tag-created` | nein | `—` | > |
| `tag-before` | nein | `—` | > |
| `create-issue-on-failure` | nein | `true` | Create or update a GitHub issue when validation fails |
| `issue-label` | nein | `invalid-tag` | Label used for validation issue reports |
| `issue-title` | nein | `Immutable version tag report` | Title for immutable tag violation issue reports |
| `notify-user` | nein | `—` | GitHub user to mention in issue reports |

## Outputs

| Name | Beschreibung |
|---|---|
| `valid` | Whether the tag passed immutability validation |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Berechtigungen und Secrets:** `contents: read`; `issues: write`, wenn
`create-issue-on-failure` aktiviert ist. Es ist kein Repository-Secret erforderlich;
für Issue-Berichte wird `github.token` verwendet.

**Voraussetzungen und Einschränkungen:** Die Inputs `tag-created` und `tag-before`
müssen zum auslösenden Tag-Push passen; bei direkter Nutzung außerhalb eines
Push-Events sind sie explizit zu setzen. Die Action erkennt Tag-Änderungen, ersetzt
aber keinen GitHub-Tag-Schutz.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-validate-tag-immutable@v1
```

Siehe auch: [workflow-release-validate-tag-immutable](workflow-release-validate-tag-immutable)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
