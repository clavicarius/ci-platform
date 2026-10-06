# Compute next simple version

**Pfad:** `actions/release-simple-versioning/action.yml`

## Beschreibung

Computes the next immutable v<major> tag.

## Outputs

| Name | Beschreibung |
|---|---|
| `next_tag` | Next simple version tag (e.g. v2) |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Inputs:** keine. **Berechtigungen und Secrets:** keine zusätzlichen
Repository-Berechtigungen oder Secrets; für den Tag-Zugriff muss das Checkout-Token
den Zugriff auf Git-Tags erlauben.

**Voraussetzungen und Einschränkungen:** Im aufrufenden Job muss das Repository
ausgecheckt sein. Für korrekte Ergebnisse muss der Checkout die relevanten Tags
enthalten. Die Action berücksichtigt Tags im Format `v<major>` und erstellt oder
pusht den berechneten Tag nicht selbst.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/release-simple-versioning@v1
```

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
