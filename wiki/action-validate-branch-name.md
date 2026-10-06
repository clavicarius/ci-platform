# Validate Branch Name

**Pfad:** `actions/validate-branch-name/action.yml`

## Beschreibung

Validates pull request source branch names against a regex policy

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `branch-name` | ja | `—` | Branch name to validate |
| `branch-regex` | nein | `^(feature\|enhancement\|bugfix\|hotfix\|release\|chore\|copilot)/[a-z0-9._-]+$` | Regular expression used to validate the branch name |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Outputs:** keine. **Berechtigungen und Secrets:** keine; die Action prüft
lediglich den als Input übergebenen Branch-Namen.

**Voraussetzungen und Einschränkungen:** `branch-name` muss angegeben werden.
Das Standard-Regex bildet die Branch-Konvention dieses Repositorys ab; Consumer
mit anderer Konvention müssen `branch-regex` anpassen.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/validate-branch-name@v1
```

Siehe auch: [workflow-validate-branch-name](workflow-validate-branch-name)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
