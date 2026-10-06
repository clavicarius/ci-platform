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
