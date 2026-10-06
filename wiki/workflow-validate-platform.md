# Validate Platform

Datei:

```
.github/workflows/validate-platform.yml
```

> **Plattform-intern:** Dieser Workflow validiert das Repository `ci-platform`.
> Er hat kein `workflow_call` und ist nicht per `uses:` einbindbar.

---

## Zweck

Der **Validate Platform Workflow** prüft Pull Requests nach `main` auf
YAML-Probleme, ungültige GitHub-Actions-Workflow-Syntax und Shell-Fehler.

## Prüfungen

| Prüfung | Werkzeug | Umfang |
|---|---|---|
| YAML | yamllint | `.github/workflows/` |
| Workflow-Syntax | actionlint | GitHub-Actions-Workflows |
| Shell | ShellCheck (Warnungen und Fehler) | alle Shell-Skripte unter `scripts/` |

## Trigger und Berechtigungen

| Trigger | Beschreibung |
|---|---|
| `pull_request` nach `main` | Führt alle Plattform-Validierungen aus |

Der Workflow benötigt ausschließlich `contents: read`.

ShellCheck wird separat auf den Shell-Skripten ausgeführt; actionlint prüft
Workflow-Syntax ohne seine optionale ShellCheck-Integration.

---

Siehe auch [Workflows](Workflows) | [Wiki Home](Home)

## Plattform-interner Vertrag

| Eigenschaft | Vertrag |
|---|---|
| Status | Plattform-intern; kein `workflow_call` |
| Inputs / Outputs | Keine |
| Berechtigungen / Secrets | `contents: read`; keine zusätzlichen Secrets |
| Voraussetzungen / Einschränkungen | Prüft ausschließlich Workflow-YAML und Skripte dieses Repositorys; benötigt yamllint, actionlint und ShellCheck. |
| Beispiel | Der oben beschriebene `pull_request`-Trigger nach `main` |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |
