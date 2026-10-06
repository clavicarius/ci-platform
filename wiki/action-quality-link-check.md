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

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/quality-link-check@v1
```

Siehe auch: [workflow-quality-link-check](workflow-quality-link-check)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
