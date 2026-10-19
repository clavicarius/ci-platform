# Release Versioning

> Veröffentlichte Dokumentation: [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/workflow-release-versioning)

Datei:

```text
.github/workflows/release-versioning.yml
```

> **Plattform-intern:** Dieser Workflow besitzt kein `workflow_call` und ist
> nicht per `uses:` einbindbar.

## Zweck

Changesets steuert die Versionsabsicht des privaten Root-Package `ci-platform`.
Das Package wird nicht veröffentlicht; es verankert die gemeinsame Version aller
Workflows und Actions.

## Ablauf

| Event | Verhalten |
|---|---|
| `pull_request` | Änderungen an Workflows, Actions oder von Actions verwendeten Skripten müssen einen Markdown-Changeset unter `.changeset/` enthalten. Docs-/Wiki-only-Änderungen benötigen keinen. |
| `push` nach `main` | `changesets/action` öffnet oder aktualisiert `chore: version packages`, wenn Changesets vorliegen. Andernfalls wird nur die bereits veröffentlichte Version geprüft; es entsteht kein neuer Tag. |
| Merge des Version-PRs | Der Release-Script liest `package.json`, erstellt `vX.Y.Z`, bewegt den passenden Major-Alias `vN` und erstellt das GitHub Release aus dem zugehörigen Changelog-Eintrag. |

Das eingebaute Package-Publishing, Tagging und die GitHub-Release-Erstellung der
Action sind deaktiviert. Nur das eigene Release-Script verwaltet die `vX.Y.Z`-
und `vN`-Git-Tags sowie das GitHub Release.

```text
Feature-PR (+ Changeset für Vertragsänderungen)
        ↓ Merge nach main
Changesets-Version-PR (package.json + CHANGELOG.md)
        ↓ Merge
vX.Y.Z (unveränderlich) + vN (beweglich) + GitHub Release
```

Der Version-PR übernimmt die Änderungen der Changesets in `CHANGELOG.md`.
Die Überschrift folgt dem Changesets-Format `## 1.2.3`; sowohl dieses Format als
auch das bestehende `## [v1.2.3] - YYYY-MM-DD` werden vom wiederverwendbaren
Release-Workflow validiert.

## Verbindliche SemVer-Policy für `@vN`

- **patch:** Bugfix ohne Änderung an Inputs, Outputs, Defaults, Permissions oder
  Workflow-Pfaden.
- **minor:** neuer optionaler Input, Workflow/Action oder optionales Output;
  bestehende Defaults und Verträge bleiben kompatibel.
- **major:** Breaking Change am `workflow_call`-/Action-Vertrag, etwa entfernter
  Input, geändertes Default-Verhalten, neue Pflicht-Permissions oder geänderter
  Dateipfad. Ein Major-Release erstellt `vN` der neuen Linie und lässt den
  bisherigen Major-Alias unverändert.

Beispiel:

```markdown
---
"ci-platform": minor
---

Add optional `fail-on-warning` input to `quality-lint` (default remains false).
```

## Changelog und GitHub Release

Changesets aktualisiert `CHANGELOG.md`; das Release-Script entnimmt dem
Versionsabschnitt die GitHub-Release-Notizen. Der Release-Workflow unterstützt
die Changesets-Überschrift `## 1.2.3` ebenso wie bisherige versionierte
Überschriften.

## Berechtigungen und Rekursionsschutz

Der PR-Check benötigt `contents: read`. Die `main`-Versionierung benötigt
`contents: write` und `pull-requests: write`, um die Tags sowie den Version-PR
zu erstellen. Das Workflow-Trigger-Muster enthält nur Branch-Pushes auf `main`
und Pull Requests, keine Tag-Pushes; der Bot-Guard verhindert rekursive
Versionierungs-Läufe.

## Weiterführende Dokumentation

- [Release- und Tagging-Richtlinie](https://github.com/clavicarius/ci-platform/wiki/RELEASING)
- [Versionierung](https://github.com/clavicarius/ci-platform/wiki/VERSIONING)
- [Release GitHub](https://github.com/clavicarius/ci-platform/wiki/workflow-release-github)
