# Maintenance Wiki Sync

Datei:

```
.github/workflows/maintenance-wiki-sync.yml
```

> **Plattform-intern:** Dieser Workflow veröffentlicht die versionierten
> Wiki-Quellen aus `wiki/` in das GitHub-Wiki-Repository. Er hat kein
> `workflow_call` und ist nicht per `uses:` einbindbar.

---

## Zweck

Der **Maintenance Wiki Sync Workflow** synchronisiert alle Markdown-Dateien
aus `wiki/` in das zugehörige GitHub-Wiki-Repository
(`clavicarius/ci-platform.wiki.git`).

Damit bleibt das veröffentlichte [GitHub Wiki](Home) mit der versionierten
Quelle im Haupt-Repository konsistent.

---

## Trigger

| Trigger | Beschreibung |
|---|---|
| `push` nach `main` | Startet bei Änderungen an `wiki/**`, am Workflow oder am Sync-Skript |
| `workflow_dispatch` | Manueller Start |

---

## Verhalten

- klont `https://github.com/<owner>/<repo>.wiki.git` mit `GITHUB_TOKEN`
- ersetzt den Wiki-Inhalt durch alle `wiki/*.md`-Dateien aus dem Haupt-Repository
- entfernt Wiki-Seiten, die in `wiki/` nicht mehr existieren
- committet und pusht nur, wenn sich der Inhalt geändert hat

---

## Berechtigungen

Der Workflow benötigt `contents: write`, damit `GITHUB_TOKEN` in das
Wiki-Repository pushen kann.

---

## Siehe auch

- [Maintenance Link Check](workflow-maintenance-link-check)
- [Wiki Home](Home)

---

Siehe auch [Workflows](Workflows) | [Wiki Home](Home)

## Plattform-interner Vertrag

| Eigenschaft | Vertrag |
|---|---|
| Status | Plattform-intern; kein `workflow_call` |
| Inputs / Outputs | Keine |
| Berechtigungen / Secrets | `contents: write`; verwendet `github.token`, kein manuell konfiguriertes Secret |
| Voraussetzungen / Einschränkungen | GitHub Wiki muss aktiviert sein. Der Sync ersetzt Wiki-Seiten durch Dateien unter `wiki/` und entfernt dort nicht mehr vorhandene Seiten. |
| Beispiel | Der oben dokumentierte `push`-Trigger oder manueller `workflow_dispatch` |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |
