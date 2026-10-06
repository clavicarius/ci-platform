# Security Dependency Review

**Pfad:** `actions/security-dependency-review/action.yml`

## Beschreibung

Reviews pull request dependency changes for known security vulnerabilities

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `fail-on-severity` | nein | `moderate` | Fail when vulnerabilities meet or exceed this severity level |
| `fail-on-scopes` | nein | `—` | Comma-separated dependency scopes that should fail the review |
| `deny-licenses` | nein | `—` | Comma-separated SPDX license identifiers that should fail the review |
| `allow-licenses` | nein | `—` | Comma-separated SPDX license identifiers that are explicitly allowed |
| `config-file` | nein | `—` | Path to a dependency review configuration file |
| `external-repo-token` | nein | `—` | Token for fetching an external dependency review configuration file |
| `comment-summary-in-pr` | nein | `true` | Add a dependency review summary comment to the pull request |
| `retry-on-snapshot-warnings` | nein | `false` | Retry the review when snapshot dependency warnings occur |

## Consumer-Einsatz

**Status:** consumer-taugliche Composite Action.

**Outputs:** keine.

**Berechtigungen und Secrets:** `contents: read`; `pull-requests: write`, wenn
`comment-summary-in-pr` aktiviert ist. Bei einer privaten,
externen Konfigurationsdatei ist ein mit `external-repo-token` übergebener Token
erforderlich; kein anderes Repository-Secret wird automatisch übernommen.

**Voraussetzungen und Einschränkungen:** Die Action muss in einem
Pull-Request-Workflow verwendet werden. Dependency-Review-Daten sind nur für
unterstützte Paket-Ökosysteme und auswertbare Änderungen verfügbar.

**Deprecation:** Bei einer Abkündigung gelten die [Sunset-Regeln](Workflows#deprecation-und-sunset).

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/security-dependency-review@v1
```

Siehe auch: [workflow-security-dependency-review](workflow-security-dependency-review)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
