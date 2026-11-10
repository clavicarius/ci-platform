# Maintenance Dependency Update

> Veröffentlichte Dokumentation: [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/workflow-maintenance-dependency-update)

Dateien:

```
.github/workflows/maintenance-dependency-update.yml
actions/maintenance-dependency-update/action.yml
```

---

## Zweck

Der wiederverwendbare Workflow führt Renovate im aufrufenden Repository aus.
Renovate erkennt veraltete Abhängigkeiten anhand der Repository-Konfiguration
und erstellt oder aktualisiert dafür Pull Requests.

Dependabot wird stattdessen nativ über `.github/dependabot.yml` konfiguriert;
es läuft unabhängig von diesem Workflow und benötigt keine GitHub Action.
Verwenden Sie nicht gleichzeitig Dependabot und Renovate für dieselben
Ökosysteme, um doppelte Pull Requests zu vermeiden.

---

## Voraussetzungen

- Eine Renovate-Konfiguration im Ziel-Repository, zum Beispiel `renovate.json`.
- Ein Repository-Secret `RENOVATE_TOKEN`, dessen Token Zugriff auf den
  Repository-Inhalt und Pull Requests hat. Verwenden Sie für zusätzliche
  Renovate-Manager nur die dafür erforderlichen Berechtigungen.
- Der aufrufende Workflow muss `contents: write` und `pull-requests: write`
  erlauben.

---

## Geplanter Ablauf

Der Workflow selbst wird durch einen aufrufenden Workflow gestartet. Dieses
Beispiel führt Renovate montags um 06:00 UTC aus und erlaubt einen manuellen
Start:

```yaml
name: Dependency Updates

on:
  schedule:
    - cron: '0 6 * * 1'
  workflow_dispatch:

permissions:
  contents: write
  pull-requests: write

jobs:
  renovate:
    uses: clavicarius/ci-platform/.github/workflows/maintenance-dependency-update.yml@v1
    secrets:
      renovate-token: ${{ secrets.RENOVATE_TOKEN }}
```

Für Dependabot lässt sich der gleiche wöchentliche Zeitplan direkt in dessen
Konfiguration festlegen:

```yaml
version: 2
updates:
  - package-ecosystem: npm
    directory: /
    schedule:
      interval: weekly
      day: monday
      time: '06:00'
      timezone: Etc/UTC
```

---

## Berechtigungen und Verhalten

Der Workflow benötigt `contents: write` und `pull-requests: write`, damit
Renovate Update-Branches pushen und Pull Requests erstellen kann. Er gibt den
Token als Action-Input an Renovate weiter; der Secret-Wert wird nicht in
Workflow-Dateien gespeichert.

---

## Siehe auch

- [Security Dependency Review](security-dependency-review.md)
- [Maintenance Link Check](maintenance-link-check.md)
