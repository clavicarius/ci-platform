# GitHub Release

Datei:

```
.github/workflows/release-github.yml
```

---

## Zweck

Der **GitHub Release Workflow** erstellt ein GitHub Release für einen bestehenden Git Tag.

Er ist als wiederverwendbarer Workflow konzipiert und kann am Ende einer Release-Pipeline
aus anderen Repositorys eingebunden werden.

---

## Funktionen

Der Workflow:

- erstellt ein GitHub Release für einen vorhandenen Tag
- generiert Release Notes automatisch aus Commits und Pull Requests
- erlaubt eigene Release Notes
- prüft auf einen passenden CHANGELOG-Eintrag und fügt ihn den Release Notes hinzu
- kann Artefakte aus dem aufrufenden Workflow anhängen
- unterstützt Draft- und Prerelease-Releases
- stellt Release-Metadaten als Outputs bereit

Für einen Tag `v1.2.0` muss `CHANGELOG.md` am getaggten Commit einen nicht leeren
Abschnitt `## [v1.2.0]` enthalten, optional mit Datum
(`## [v1.2.0] - YYYY-MM-DD`). Ohne passenden Eintrag wird das Release nicht erstellt.
Eigene Release Notes ersetzen die automatisch generierten Notizen, der Changelog-
Abschnitt wird in beiden Fällen angefügt.

---

## Typischer Ablauf

```
git tag v1.2.0
       |
       v
     Build
       |
       v
      Test
       |
       v
    Release
```

Build und Tests bleiben Aufgabe des aufrufenden Workflows. Dieser Workflow übernimmt nur die Release-Erstellung.

---

## Inputs

| Name | Typ | Erforderlich | Standard | Beschreibung |
|---|---|---|---|---|
| `tag` | string | ja | - | Git Tag, für den ein Release erstellt wird. Der Tag muss bereits existieren. |
| `release_name` | string | nein | Wert von `tag` | Name des Releases. |
| `draft` | boolean | nein | `false` | Erstellt das Release als Draft. |
| `prerelease` | boolean | nein | `false` | Markiert das Release als Prerelease. |
| `generate_release_notes` | boolean | nein | `true` | Generiert Release Notes automatisch. |
| `body` | string | nein | `''` | Eigene Release Notes. Wenn gesetzt, werden automatisch generierte Notes deaktiviert. |
| `artifact_name` | string | nein | `''` | Name eines einzelnen Artefakts, das an das Release angehängt wird. |
| `artifact_pattern` | string | nein | `''` | Pattern für mehrere Artefakte, die an das Release angehängt werden. |

---

## Outputs

| Name | Beschreibung |
|---|---|
| `release_url` | URL des erstellten Releases. |
| `release_id` | ID des erstellten Releases. |
| `upload_url` | Upload-URL des erstellten Releases. |

---

## Integration

Einbindung bei Tag Push:

```yaml
name: Release

on:
  push:
    tags:
      - 'v*'

permissions:
  contents: write

jobs:
  release:
    uses: clavicarius/ci-platform/.github/workflows/release-github.yml@v1
    with:
      tag: ${{ github.ref_name }}
```

---

## Artefakt anhängen

Ein einzelnes Artefakt aus einem vorherigen Job anhängen:

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Build artifact
        run: |
          mkdir -p dist
          echo "release artifact" > dist/release.txt

      - name: Upload artifact
        uses: actions/upload-artifact@v4
        with:
          name: release-asset
          path: dist/release.txt

  release:
    needs: build
    uses: clavicarius/ci-platform/.github/workflows/release-github.yml@v1
    with:
      tag: ${{ github.ref_name }}
      artifact_name: release-asset
```

Mehrere Artefakte über ein Pattern anhängen:

```yaml
jobs:
  release:
    uses: clavicarius/ci-platform/.github/workflows/release-github.yml@v1
    with:
      tag: ${{ github.ref_name }}
      artifact_pattern: 'release-asset-*'
```

---

## Benötigte Berechtigungen

Das aufrufende Repository muss Schreibzugriff auf Repository-Inhalte erlauben:

```yaml
permissions:
  contents: write
```

Bedeutung:

| Permission | Zweck |
|---|---|
| `contents: write` | Erstellen des GitHub Releases und Hochladen von Assets |

---

## Voraussetzungen

Das Zielrepository benötigt:

- einen bereits vorhandenen Git Tag
- aktivierte GitHub Actions
- passende Repository-Berechtigungen für Releases
- optional vorher hochgeladene Artefakte mit `actions/upload-artifact@v4`

---

## Verhalten bei Fehlern

Der Workflow bricht ab, wenn:

- der angegebene Tag nicht existiert
- das Release bereits existiert
- die Berechtigung `contents: write` fehlt
- angeforderte Artefakte nicht gefunden werden

---

## Versionierung

Aktuelle Version:

```
v1
```

Verwendung:

```yaml
uses: clavicarius/ci-platform/.github/workflows/release-github.yml@v1
```

---

## Weiterführende Informationen

- [Release- und Tagging-Richtlinie](https://github.com/clavicarius/ci-platform/wiki/RELEASING)
- [Wiki Home](Home)
- [Release Validate Tags](https://github.com/clavicarius/ci-platform/wiki/workflow-release-validate-tags)
- [Release Validate Branch](https://github.com/clavicarius/ci-platform/wiki/workflow-release-validate-branch)
- [Quality Base Set](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-base-set)

Offizielle Dokumentation:

- GitHub Releases: https://docs.github.com/en/repositories/releasing-projects-on-github
- GitHub CLI `gh release create`: https://cli.github.com/manual/gh_release_create

## Consumer API

| Eigenschaft | Vertrag |
|---|---|
| Status | Consumer-tauglich (`workflow_call`) |
| Inputs / Outputs | Siehe [Inputs](#inputs) und [Outputs](#outputs) |
| Berechtigungen / Secrets | `contents: write`; keine zusätzlichen Secrets |
| Voraussetzungen / Einschränkungen | Der angegebene Tag muss existieren. Für Artefakte muss ein passendes Artefakt aus einem aufrufenden Job verfügbar sein. |
| Beispiel | [Integration](#integration) mit `clavicarius/ci-platform` und `@v1` |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |

---

Siehe auch [Workflows](Workflows) | [Wiki Home](Home)
