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

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-validate-tag-immutable@v1
```

Siehe auch: [workflow-release-validate-tag-immutable](workflow-release-validate-tag-immutable)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
