# Maintenance Wiki Sync

> Veröffentlichte Dokumentation: [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/workflow-maintenance-wiki-sync)

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

Damit bleibt das veröffentlichte [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/Home)
mit der versionierten Quelle im Haupt-Repository konsistent.

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

- [Wiki Home](../../wiki/Home.md)
- [Maintenance Link Check](maintenance-link-check.md)
