# Quality YAML

**Pfad:** `actions/quality-yaml/action.yml`

## Beschreibung

Validates YAML syntax and structure with yamllint

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `working-directory` | nein | `.` | Directory to scan for YAML files |
| `yaml-glob` | nein | `—` | Glob pattern for YAML files. Defaults to all YAML files in working-directory. |
| `yamllint-config` | nein | `—` | Path to a yamllint configuration file |
| `scan-profile` | nein | `all` | 'Scan scope: all, workflows, compose, or kubernetes' |
| `exclude-paths` | nein | `.git,node_modules,vendor,.venv` | Comma-separated directory names to exclude from scanning |
| `fail-on-findings` | nein | `true` | Fail the workflow when yamllint reports issues |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Outputs:** keine.

**Berechtigungen und Secrets:** `contents: read` zum Lesen des ausgecheckten
Repositorys; keine zusätzlichen Secrets oder Schreibberechtigungen.

**Voraussetzungen und Einschränkungen:** Vor der Action muss das Consumer-Repository
mit `actions/checkout` ausgecheckt werden. Die Scan-Profile `all`, `workflows`,
`compose` und `kubernetes` bestimmen den Umfang; andere Dateitypen werden nicht
gescannt.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/quality-yaml@v1
```

Siehe auch: [workflow-quality-yaml](workflow-quality-yaml)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
