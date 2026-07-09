# Release Validate Tags

Datei:

```
.github/workflows/validate-version-tags.yml
```

---

## Zweck

Der **Release Validate Tags Workflow** prüft automatisch, ob ein neu gesetztes
Git-Tag dem vorgeschriebenen Versionsformat entspricht und monoton steigend ist.

Er verhindert ungültige Releases durch fehlerhafte Tag-Namen und benachrichtigt
Maintainer bei Verstößen über ein GitHub Issue.

---

## Funktionen

Der Workflow:

- validiert das Tag-Format gegen `^v[1-9][0-9]*$`
- prüft, ob das neue Tag größer ist als alle vorhandenen gültigen Tags
- erstellt automatisch ein GitHub Issue bei Regelverstößen
- kann als wiederverwendbarer Workflow über `workflow_call` aufgerufen werden

---

## Erlaubte Tag-Formate

| Beispiel | Gültig | Grund |
|---|---|---|
| `v1` | ja | Erste Version |
| `v2`, `v10`, `v123` | ja | Monoton steigend |
| `v0` | nein | Kleinste erlaubte Version ist v1 |
| `v01` | nein | Führende Nullen verboten |
| `v1.0` | nein | Nur ganzzahlige Major-Versionen |
| `version1` | nein | Kein `v`-Präfix mit Zahl |

Lücken sind erlaubt (z. B. `v1` → `v4` ist gültig, sofern kein `v2`, `v3`, `v4` existiert).

---

## Inputs

| Name | Typ | Erforderlich | Standard | Beschreibung |
|---|---|---|---|---|
| `tag` | string | nein | `''` | Tag zum Validieren. Leer = aus `github.ref` abgeleitet (bei Push). |

---

## Benötigte Berechtigungen

```yaml
permissions:
  contents: read
  issues: write
```

---

## Integration

### Automatisch bei Tag-Push

Der Workflow läuft automatisch bei jedem `v*`-Tag-Push:

```
git tag v2
git push origin v2
  |
  v
validate-version-tags läuft
  |
  +-- OK  -> weiter
  +-- Fehler -> Issue wird erstellt, Workflow schlägt fehl
```

### Als wiederverwendbarer Workflow

```yaml
jobs:
  validate-tag:
    uses: clavicarius/github-workflows/.github/workflows/validate-version-tags.yml@v1
    with:
      tag: ${{ github.ref_name }}
```

---

## Verhalten bei Fehlern

Wenn das Tag ungültig ist:

- schlägt der Workflow-Job mit einem `::error::`-Annotation fehl
- wird automatisch ein GitHub Issue erstellt, das `@clavicarius` benachrichtigt
- wird kein Release erstellt (nachgelagerte Jobs mit `needs:` werden blockiert)

---

## Weiterführende Dokumentation

- [Release- und Tagging-Richtlinie](../RELEASING.md)
- [Quality Base Set](quality-base-set.md)

---

## Versionierung

```
v1
```

```yaml
uses: clavicarius/github-workflows/.github/workflows/validate-version-tags.yml@v1
```
