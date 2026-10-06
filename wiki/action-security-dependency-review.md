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

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/security-dependency-review@v1
```

Siehe auch: [workflow-security-dependency-review](workflow-security-dependency-review)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
