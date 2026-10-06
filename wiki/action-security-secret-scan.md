# Security Secret Scan

**Pfad:** `actions/security-secret-scan/action.yml`

## Beschreibung

Scans repositories for leaked secrets using Gitleaks and GitHub Secret Scanning alerts

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `gitleaks-config` | nein | `—` | Path to a custom Gitleaks configuration file relative to the repository root |
| `scan-mode` | nein | `auto` | 'Scan scope: auto (event-based), full (entire repository history), or diff (changes only)' |
| `check-github-alerts` | nein | `true` | Fail when open GitHub Secret Scanning alerts exist for the repository |
| `enable-gitleaks-comments` | nein | `true` | Enable Gitleaks pull request comments |
| `fail-on-findings` | nein | `true` | Fail the workflow when secrets are detected |

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/security-secret-scan@v1
```

Siehe auch: [workflow-security-secret-scan](workflow-security-secret-scan)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
