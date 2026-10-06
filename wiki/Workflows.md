# Workflows

Dieses Verzeichnis dokumentiert die Consumer-Workflows und plattform-internen Workflows
des Repositorys. Nur Workflows mit `workflow_call` sind als Consumer-API einbindbar.

Siehe auch: [CI-Plattform Soll-Zielbild](https://github.com/clavicarius/ci-platform/blob/main/docs/ci-platform.md) | [Wiki Home](Home)

Jeder Workflow wird separat dokumentiert und beschreibt:

- Zweck
- Einsatzgebiet
- Voraussetzungen
- benötigte Berechtigungen
- Konfiguration
- Beispielintegration
- Verhalten bei Fehlern

---

# Workflow Übersicht

| Workflow | Consumer-tauglich | Beschreibung |
|---|---|---|
| [Quality Link Check](workflow-quality-link-check) | Ja | Prüft Links und verwaltet automatisch Reports |
| [Quality Lint](workflow-quality-lint) | Ja | Führt einheitliche Codequalitätsprüfungen durch |
| [Quality Markdown](workflow-quality-markdown) | Ja | Prüft Markdown-Syntax, Struktur und Links |
| [Quality YAML](workflow-quality-yaml) | Ja | Prüft YAML-Dateien auf Syntax und Struktur |
| [Release GitHub](workflow-release-github) | Ja | Erstellt GitHub Releases für bestehende Git Tags |
| [Release Validate Tags](workflow-release-validate-tags) | Ja | Prüft Tag-Format und Monotonie |
| [Release Validate Tag Immutable](workflow-release-validate-tag-immutable) | Ja | Lehnt Tag-Updates (Force-Push) ab |
| [Release Validate Branch](workflow-release-validate-branch) | Ja | Prüft, ob Tag auf dem Release-Branch liegt |
| [Security CodeQL](workflow-security-codeql) | Ja | Führt statische Sicherheitsanalysen durch |
| [Security Dependency Review](workflow-security-dependency-review) | Ja | Prüft neue Dependencies in Pull Requests |
| [Security Secret Scan](workflow-security-secret-scan) | Ja | Verhindert das versehentliche Committen von Secrets |
| [Quality Base Set](workflow-quality-base-set) | Nein — plattform-intern | PR-Gate und Release-Orchestrierung; kein `workflow_call` |
| [Release Versioning](workflow-release-versioning) | Nein — plattform-intern | Versions-Tags für dieses Repository; kein `workflow_call` |
| [Validate Platform](workflow-validate-platform) | Nein — plattform-intern | YAML-, actionlint- und ShellCheck-Validierung |
| [Validate Branch Name](workflow-validate-branch-name) | Nein — plattform-intern | PR-Branch-Prüfung für dieses Repository |
| [Maintenance Link Check](workflow-maintenance-link-check) | Nein — plattform-intern | Geplante Linkprüfung dieses Repositorys |
| [Maintenance Wiki Sync](workflow-maintenance-wiki-sync) | Nein — plattform-intern | Veröffentlicht `wiki/` in das GitHub Wiki |

---

# Verwendung

Workflows mit `workflow_call` werden direkt aus dem Repository eingebunden:

```yaml
jobs:
  example:
    uses: clavicarius/ci-platform/.github/workflows/<workflow>.yml@v1
```

Beispiel:

```yaml
jobs:
  link-check:
    uses: clavicarius/ci-platform/.github/workflows/quality-link-check.yml@v1
```

**Plattform-interne Workflows** (Quality Base Set, Release Versioning,
Validate Platform, Validate Branch Name und Maintenance) sind nicht per
`uses:` einbindbar.
Siehe jeweilige Workflow-Dokumentation.

---

# Versionierung

Produktive Projekte sollten immer eine stabile Version verwenden:

```yaml
@v1
```

Nicht:

```yaml
@main
```

---

# Neue Workflows

Beim Hinzufügen eines neuen Workflows muss erstellt werden:

```
.github/workflows/<workflow>.yml
docs/workflows/<workflow>.md
```

Die Dokumentation ist Bestandteil des Workflows.

---

Siehe auch: [CI-Plattform Soll-Zielbild](https://github.com/clavicarius/ci-platform/blob/main/docs/ci-platform.md) | [Wiki Home](Home)
