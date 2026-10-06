# Quality Base Set

> Veröffentlichte Dokumentation: [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-base-set)

Datei:

```
.github/workflows/quality-base-set.yml
```

> **Plattform-intern:** Dieser Workflow besitzt kein `workflow_call` und ist
> nicht per `uses:` einbindbar. Consumer können die einzelnen aufrufbaren
> Workflows direkt einbinden.

---

## Zweck

Der **Quality Base Set Workflow** ist der interne CI-Gate für dieses Repository.

Er führt vor einem Merge nach `main` die vereinheitlichten Qualitäts- und Sicherheitsprüfungen aus
und nutzt dafür die wiederverwendbaren Workflows aus diesem Repository.

Zusätzlich wird bei Git Tags ein GitHub Release über `release-github.yml` erstellt.

---

## Enthaltene Workflows

| Workflow | Trigger | Zweck |
|---|---|---|
| `quality-link-check.yml` | Pull Request | Linkprüfung mit Issue-Report |
| `quality-yaml.yml` | Pull Request | YAML-Syntax und Struktur |
| `quality-markdown.yml` | Pull Request | Markdown-Syntax und Struktur |
| `security-secret-scan.yml` | Pull Request | Secret- und Leak-Prüfung |
| `security-dependency-review.yml` | Pull Request | Dependency-Sicherheit im PR |
| `quality-lint.yml` | Pull Request | Zusätzliche Linter nach Auto-Detect |
| `release-validate-tag-immutable.yml` | Tag `v*` | Lehnt Tag-Updates ab |
| `release-validate-tags.yml` | Tag `v*` | SemVer-Tag-Format prüfen |
| `release-validate-branch.yml` | Tag `v*` | Prüft, ob Tag auf `main` liegt |
| `release-github.yml` | Tag `v*` | GitHub Release für neue Versionen |

---

## Trigger

### Pull Request nach `main`

Alle Qualitäts- und Sicherheitsjobs laufen parallel als Required Checks.

### Tag Push `v*`

Beispiel:

```bash
git tag v1.0.0
git push origin v1.0.0
```

Dadurch wird automatisch ein GitHub Release erstellt.

Der Tag **muss vom `main` Branch** gesetzt werden und dem Tagging-Schema entsprechen.
Wird ein `v*`-Tag auf einem anderen Branch gesetzt oder ist das Format ungültig,
schlagen die Jobs `release-validate-tags` bzw. `release-validate-branch` fehl
und das Release wird nicht erstellt.

Die Release-Validierungs-Jobs (`release-validate-tag-immutable`, `release-validate-tags`,
`release-validate-branch`, `release-github`) werden **nur für SemVer-Tags** ausgeführt,
d.h. Tags, die einen Punkt enthalten (z.B. `v1.0.0`). Einfache Major-Alias-Tags
(z.B. `v1`) werden von der Validierungskette übersprungen und lösen kein Release aus.

---

## Konfiguration im Base Set

### YAML-Prüfung

Für dieses Repository wird der Scan auf GitHub Actions Workflows fokussiert:

```yaml
scan-profile: workflows
```

### Markdown-Prüfung

Linkprüfung ist in `quality-markdown` deaktiviert, weil `quality-link-check` diese Aufgabe übernimmt:

```yaml
enable-link-check: false
```

### Linting

`quality-lint` nutzt Auto-Detect für vorhandene Toolchains, überspringt aber YAML- und Markdown-Prüfungen,
weil diese bereits von `quality-yaml` und `quality-markdown` übernommen werden:

```yaml
auto-detect: true
skip-yaml: true
skip-markdown: true
```

### Release-Tag-Validierung

Im Base-Set wird für Release-Tags explizit das **SemVer-Muster** verwendet:

```yaml
version-pattern: semver
```

---

## Benötigte Berechtigungen

```yaml
permissions:
  contents: read
  issues: write
  pull-requests: write
  security-events: read
```

Für Release-Jobs:

```yaml
permissions:
  contents: write
```

---

## Ablauf bei Pull Requests

```
Pull Request -> main
      |
      +-- quality-link-check
      +-- quality-yaml
      +-- quality-markdown
      +-- security-secret-scan
      +-- security-dependency-review
      +-- quality-lint
      |
      v
Alle Checks grün -> Merge erlaubt
```

---

## Ablauf bei Releases

```
git tag v1.0.0 (nur auf main!)
      |
      v
release-validate-tag-immutable
      |
  OK? |
      +-- Nein -> Fehler, kein Release
      |
      v
release-validate-tags
      |
  OK? |
      +-- Nein -> Fehler, kein Release
      |
      v
release-validate-branch
      |
  OK? |
      +-- Nein -> Fehler, kein Release
      |
      v
release-github
      |
      v
GitHub Release erstellt
```

---

## Verhalten bei Fehlern

Der Pull Request wird blockiert, wenn mindestens einer der Jobs fehlschlägt:

- defekte Links
- ungültiges YAML
- Markdown-Probleme
- erkannte Secrets
- unsichere Dependencies
- Lint-Fehler

---

## Hinweis

Dieser Workflow ist **repository-intern** und dient als Referenzimplementierung für das Basis-Set v1.

Externe Projekte binden die einzelnen Consumer-Workflows direkt ein:

```yaml
jobs:
  link-check:
    uses: clavicarius/ci-platform/.github/workflows/quality-link-check.yml@v1
```

---

## Weiterführende Dokumentation

- [Release- und Tagging-Richtlinie](https://github.com/clavicarius/ci-platform/wiki/RELEASING)
- [Wiki Home](Home)
- [Quality Link Check](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-link-check)
- [Quality YAML](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-yaml)
- [Quality Markdown](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-markdown)
- [Quality Lint](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-lint)
- [Security Secret Scan](https://github.com/clavicarius/ci-platform/wiki/workflow-security-secret-scan)
- [Security Dependency Review](https://github.com/clavicarius/ci-platform/wiki/workflow-security-dependency-review)
- [Release GitHub](https://github.com/clavicarius/ci-platform/wiki/workflow-release-github)
- [Release Validate Tag Immutable](https://github.com/clavicarius/ci-platform/wiki/workflow-release-validate-tag-immutable)
- [Release Validate Tags](https://github.com/clavicarius/ci-platform/wiki/workflow-release-validate-tags)
- [Release Validate Branch](https://github.com/clavicarius/ci-platform/wiki/workflow-release-validate-branch)
