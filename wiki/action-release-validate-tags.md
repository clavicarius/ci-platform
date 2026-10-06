# Release Validate Tags

**Pfad:** `actions/release-validate-tags/action.yml`

## Beschreibung

Validates version tag format and monotonicity for simple versioning

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `tag` | nein | `—` | Tag to validate. When empty, derived from GITHUB_REF. |
| `version-pattern` | nein | `simple` | 'Version pattern preset: simple, semver, or custom regex' |
| `check-monotonicity` | nein | `true` | Check monotonicity for simple versioning |
| `create-issue-on-failure` | nein | `true` | Create or update a GitHub issue when validation fails |
| `issue-label` | nein | `invalid-tag` | Label used for validation issue reports |
| `invalid-format-issue-title` | nein | `Invalid version tag report` | Title for invalid format issue reports |
| `not-monotonic-issue-title` | nein | `Invalid version tag (not monotonic) report` | Title for not monotonic issue reports |
| `notify-user` | nein | `—` | GitHub user to mention in issue reports |

## Outputs

| Name | Beschreibung |
|---|---|
| `valid` | Whether the tag passed validation |
| `max_tag` | Highest existing valid tag for simple versioning |
| `tag` | Validated tag name |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Berechtigungen und Secrets:** `contents: read`; `issues: write`, wenn
`create-issue-on-failure` aktiviert ist. Es ist kein Repository-Secret erforderlich;
für Issue-Berichte wird `github.token` verwendet.

**Voraussetzungen und Einschränkungen:** Das Repository und seine Tags müssen
zugänglich sein. Monotonieprüfung wird für das einfache Versionsmuster verwendet;
SemVer- und benutzerdefinierte Muster werden anhand des Formats geprüft.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-validate-tags@v1
```

Siehe auch: [workflow-release-validate-tags](workflow-release-validate-tags)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
