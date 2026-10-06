# Available Workflows

Dieses Verzeichnis dokumentiert die Consumer-Workflows und plattform-internen Workflows
des Repositorys. Nur Workflows mit `workflow_call` sind als Consumer-API einbindbar.

Siehe auch: [CI-Plattform Soll-Zielbild](../ci-platform.md) | [CI Platform Wiki](https://github.com/clavicarius/ci-platform/wiki/Home)

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
| [Quality Link Check](quality-link-check.md) | Ja | Prüft Links und verwaltet automatisch Reports |
| [Quality Lint](quality-lint.md) | Ja | Führt einheitliche Codequalitätsprüfungen durch |
| [Quality Markdown](quality-markdown.md) | Ja | Prüft Markdown-Syntax, Struktur und Links |
| [Quality YAML](quality-yaml.md) | Ja | Prüft YAML-Dateien auf Syntax und Struktur |
| [Release GitHub](release-github.md) | Ja | Erstellt GitHub Releases für bestehende Git Tags |
| [Release Validate Tags](release-validate-tags.md) | Ja | Prüft Tag-Format und Monotonie |
| [Release Validate Tag Immutable](release-validate-tag-immutable.md) | Ja | Lehnt Tag-Updates (Force-Push) ab |
| [Release Validate Branch](release-validate-branch.md) | Ja | Prüft, ob Tag auf dem Release-Branch liegt |
| [Security CodeQL](security-codeql.md) | Ja | Führt statische Sicherheitsanalysen durch |
| [Security Dependency Review](security-dependency-review.md) | Ja | Prüft neue Dependencies in Pull Requests |
| [Security Secret Scan](security-secret-scan.md) | Ja | Verhindert das versehentliche Committen von Secrets |
| [Quality Base Set](quality-base-set.md) | Nein — plattform-intern | PR-Gate und Release-Orchestrierung; kein `workflow_call` |
| [Release Versioning](release-versioning.md) | Nein — plattform-intern | Versions-Tags für dieses Repository; kein `workflow_call` |
| [Validate Platform](validate-platform.md) | Nein — plattform-intern | YAML-, actionlint- und ShellCheck-Validierung |
| [Validate Branch Name](validate-branch-name.md) | Nein — plattform-intern | PR-Branch-Prüfung für dieses Repository |
| [Maintenance Link Check](maintenance-link-check.md) | Nein — plattform-intern | Geplante Linkprüfung dieses Repositorys |

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
