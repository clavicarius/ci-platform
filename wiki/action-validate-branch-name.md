# Validate Branch Name

**Pfad:** `actions/validate-branch-name/action.yml`

## Beschreibung

Validates pull request source branch names against a regex policy

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `branch-name` | ja | `—` | Branch name to validate |
| `branch-regex` | nein | `^(feature|enhancement|bugfix|hotfix|release|chore|copilot)/[a-z0-9._-]+$` | Regular expression used to validate the branch name |

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/validate-branch-name@v1
```

Siehe auch: [workflow-validate-branch-name](workflow-validate-branch-name)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
