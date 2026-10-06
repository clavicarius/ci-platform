# Quality Link Check

Datei:

```
.github/workflows/quality-link-check.yml
actions/quality-link-check/action.yml
```

---

## Zweck

Dieser Workflow überprüft automatisch externe und interne Links eines Repositorys.

Er wird eingesetzt, um defekte Links in:

- Markdown-Dokumentationen
- README-Dateien
- Projektinformationen

frühzeitig zu erkennen.

---

## Funktionen

Der Workflow:

- prüft URLs mit Lychee
- erstellt bei Fehlern einen GitHub Issue Report
- aktualisiert vorhandene Reports
- vermeidet doppelte Issues
- schließt behobene Reports automatisch

---

## Voraussetzungen

Das Ziel-Repository benötigt:

```yaml
permissions:
  contents: read
  issues: write
```

Außerdem müssen GitHub Issues aktiviert sein.
Für die direkte Action-Nutzung muss `actions/checkout` davor ausgeführt
werden. Das angegebene Issue-Label sollte im Repository vorhanden sein.

---

## Integration

Beispiel:

```yaml
name: Link Check

on:
  workflow_dispatch:
  schedule:
    - cron: "11 11 * * 0"

permissions:
  contents: read
  issues: write

jobs:

  link-check:
    uses: clavicarius/ci-platform/.github/workflows/quality-link-check.yml@v1
```

Der Composite Action kann auch direkt in einem eigenen Workflow verwendet
werden. In diesem Fall müssen die Dateien des Ziel-Repositorys vor der Action
ausgecheckt werden:

```yaml
name: Link Check

on:
  workflow_dispatch:
  schedule:
    - cron: "11 11 * * 0"

permissions:
  contents: read
  issues: write

jobs:
  link-check:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Check links and manage report issue
        uses: clavicarius/ci-platform/actions/quality-link-check@v1
        with:
          issue-title: "Link Checker Report"
          issue-label: "dead-link"
          output-file: "./lychee/out.md"
```

Die Action akzeptiert optionale Eingaben:

| Eingabe | Standardwert | Beschreibung |
|---|---|---|
| `issue-title` | `Link Checker Report` | Titel des Issues für den Report |
| `issue-label` | `dead-link` | Label zur Suche und Kennzeichnung des Issues |
| `output-file` | `./lychee/out.md` | Pfad der Lychee-Reportdatei |

---

## Ausführung

Der Workflow läuft:

- manuell über `workflow_dispatch`
- automatisch gemäß Zeitplan

Standard:

```
Sonntag 11:11 UTC
```

---

## Fehlerbehandlung

Wenn defekte Links gefunden werden:

1. Lychee erzeugt einen Report.
2. Ein Issue mit dem Titel:

```
Link Checker Report
```

wird erstellt oder aktualisiert.

Label:

```
dead-link
```

---

Wenn alle Links wieder funktionieren:

- das bestehende Issue wird automatisch geschlossen.

---

## Benötigte Komponenten

Verwendete Actions:

- `actions/checkout`
- `clavicarius/lychee-action`
- GitHub CLI (`gh`)

---

## Beispielausgabe

Ein Fehler erzeugt ein Issue:

```
Link Checker Report

Broken links:

- https://example.invalid
- https://old-documentation.example
```

---

## Versionierung

Aktuelle Version:

```
v1
```

Verwendung:

```yaml
uses: clavicarius/ci-platform/.github/workflows/quality-link-check.yml@v1
```

---

## Änderungen

Breaking Changes werden über neue Major-Versionen veröffentlicht:

```
v1 → v2
```

## Consumer API

| Eigenschaft | Vertrag |
|---|---|
| Status | Consumer-tauglich (`workflow_call`) |
| Inputs / Outputs | Keine Workflow-Inputs und keine Outputs. Die Input-Tabelle oben gilt für die direkte Action-Nutzung. |
| Berechtigungen / Secrets | `contents: read`, `issues: write`; keine zusätzlichen Secrets |
| Voraussetzungen / Einschränkungen | Issues aktivieren und Issue-Label anlegen. Für die direkte Action-Nutzung Checkout ausführen. |
| Beispiel | [Integration](#integration) mit `clavicarius/ci-platform` und `@v1` |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |

---

Siehe auch [Workflows](Workflows) | [Wiki Home](Home)
