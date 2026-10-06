# CI Platform Wiki

![CI Platform](https://raw.githubusercontent.com/clavicarius/ci-platform/main/assets/social-preview.png)

Willkommen zur Dokumentation der **CI Platform** — zentral bereitgestellte,
wiederverwendbare GitHub Actions Workflows und Composite Actions für mehrere Projekte.

## Was ist die CI Platform?

Dieses Repository liefert eine gemeinsame CI/CD-Basis: Quality- und Security-Checks,
Release-Validierung und wiederverwendbare Pipeline-Bausteine. Consumer-Repositories
binden Workflows per `uses:` ein — typischerweise mit `@v1` als stabile Major-Linie.

```text
Basis-Set (quality + security)
    ↓ optional
Pipeline-Bausteine (build, test, release, docker)
    ↓
Consumer-Repositories
```

## Themenbereiche

Die versionierten Seiten unter `wiki/` werden in das GitHub Wiki veröffentlicht.
Für Inputs, Outputs, Berechtigungen, Secrets und die Consumer-Integration von
Workflows und Actions ist das veröffentlichte Wiki die maßgebliche Dokumentation.

### Plattform & Architektur

- [Architektur](architecture) — Repository-Aufbau, Schichten, Consumer-API vs. plattform-intern
- [Soll-Zielbild](https://github.com/clavicarius/ci-platform/blob/main/docs/ci-platform.md) — verbindliche Spezifikation

### Release & Versionierung

- [Release- und Tagging-Richtlinie](RELEASING) — Tags, Release-Prozess, Branch-Schutz
- [Versionierung](VERSIONING) — SemVer, automatische Tags, Floating Major (`@v1`)

### Workflows & Actions

- [Workflows](Workflows) — Übersicht aller Reusable Workflows (Quality, Security, Release, …)
- [Actions](Actions) — Composite Actions für einzelne Pipeline-Schritte

Kurzüberblick:

| Bereich | Beispiele |
|---|---|
| Quality | Link-Check, Lint, Markdown, YAML |
| Security | CodeQL, Secret Scan, Dependency Review |
| Release | Tag-Validierung, GitHub Release |

## Schnelleinstieg

Workflow in einem Consumer-Repository einbinden:

```yaml
jobs:
  link-check:
    uses: clavicarius/ci-platform/.github/workflows/quality-link-check.yml@v1
```

Composite Action direkt in Steps:

```yaml
- uses: clavicarius/ci-platform/actions/quality-link-check@v1
```

Ausführliche Integration, Berechtigungen und Versionierung: [Repository README](https://github.com/clavicarius/ci-platform/blob/main/README.md).
