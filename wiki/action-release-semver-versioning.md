# Compute next semantic version

**Pfad:** `actions/release-semver-versioning/action.yml`

## Beschreibung

Computes the next v<major>.<minor>.<patch> tag.

## Outputs

| Name | Beschreibung |
|---|---|
| `next_tag` | Next semantic version tag (e.g. v0.1.1) |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Inputs:** keine. **Berechtigungen und Secrets:** keine zusätzlichen
Repository-Berechtigungen oder Secrets; für den Tag-Zugriff muss das Checkout-Token
den Zugriff auf Git-Tags erlauben.

**Voraussetzungen und Einschränkungen:** Im aufrufenden Job muss das Repository
ausgecheckt sein. Für korrekte Ergebnisse muss der Checkout die relevanten Tags
enthalten. Die Action berechnet den nächsten Patch-Tag anhand von Tags im Format
`v<major>.<minor>.<patch>`; sie erstellt oder pusht den Tag nicht selbst.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-semver-versioning@v1
```

Siehe auch: [workflow-release-versioning](workflow-release-versioning)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
