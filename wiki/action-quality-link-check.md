# Quality Link Check

**Pfad:** `actions/quality-link-check/action.yml`

## Beschreibung

Checks repository links and manages a GitHub issue report

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `issue-title` | nein | `Link Checker Report` | Title of the GitHub issue |
| `issue-label` | nein | `dead-link` | Label used for the GitHub issue |
| `output-file` | nein | `./lychee/out.md` | Lychee report output file |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Outputs:** keine.

**Berechtigungen und Secrets:** `contents: read`; zusätzlich `issues: write`, um
Link-Reports zu erstellen, zu aktualisieren oder zu schließen. Es ist kein
Repository-Secret erforderlich; die Action verwendet `github.token`.

**Voraussetzungen und Einschränkungen:** Vor der Action muss das Consumer-Repository
mit `actions/checkout` ausgecheckt werden. GitHub Issues müssen aktiviert und das
konfigurierte Label muss vorhanden sein. Die Action scannt nur Dateien des
ausgecheckten Arbeitsverzeichnisses.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/quality-link-check@v1
```

Siehe auch: [workflow-quality-link-check](workflow-quality-link-check)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
