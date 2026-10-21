# Release Versioning

Datei:

```text
.github/workflows/release-versioning.yml
```

> **Plattform-intern:** Dieser Workflow besitzt kein `workflow_call` und ist
> nicht per `uses:` einbindbar.

## Zweck

Der Workflow prüft erforderliche Changesets auf Pull Requests und orchestriert
die Changesets-Version-PRs nach einem Merge auf `main`. Das private Root-Package
`ci-platform` ist Versionsanker, kein Registry-Package.

## Trigger und Verhalten

| Event | Verhalten |
|---|---|
| `pull_request` | Ein Changeset ist bei Workflow-, Action- und von Actions verwendeten Skriptänderungen erforderlich. Docs-/Wiki-only-Änderungen benötigen keinen. |
| `push` nach `main` | Changesets öffnet oder aktualisiert `chore: version packages`, wenn Changesets vorliegen. Ein Merge ohne Changeset erzeugt keinen neuen Full-Tag. |
| Merge des Version-PRs | Das Release-Script liest `package.json`, setzt `vX.Y.Z` und den passenden Major-Alias `vN` und erstellt das GitHub Release mit dem Changelog-Eintrag. |

## Versionierung

- Release-Tags `vX.Y.Z` sind unveränderlich.
- Major-Aliase `vN` sind beweglich und zeigen auf den neuesten kompatiblen
  Release derselben Major-Linie.
- Das eingebaute Package-Publishing, Tagging und die GitHub-Release-Erstellung
  der Action sind deaktiviert; das eigene Release-Script erstellt ausschließlich
  die vereinbarten Git-Tags und das GitHub Release.
- Ein Major-Release erstellt den neuen Alias (`v2`); der alte Alias (`v1`)
  bleibt auf seiner bisherigen Linie.
- Es gibt keine npm-/GitHub-Package-Veröffentlichung und keine Tags im Format
  `ci-platform@1.2.3`.
- Das Workflow-Trigger-Muster hört auf `main`-Branch-Pushes und Pull Requests,
  nicht auf Tag-Pushes. Der Bot-Guard verhindert rekursive Runs.

## Changelog

Changesets schreibt Releases in `CHANGELOG.md`, zum Beispiel mit der Überschrift
`## 1.2.3`. Der zugehörige nicht leere Abschnitt speist das GitHub Release.
Der wiederverwendbare Release-Workflow akzeptiert das Changesets-Format und
bisherige Überschriften der Form `## [v1.2.3] - YYYY-MM-DD`.

## Berechtigungen

- Pull-Request-Check: `contents: read`
- Version-PR und Release: `contents: write`, `pull-requests: write`

## Weiterführende Dokumentation

- [Release- und Tagging-Richtlinie](RELEASING)
- [Versionierung](VERSIONING)
- [Release GitHub](workflow-release-github)
- [Workflows](Workflows)

## Plattform-interner Vertrag

| Eigenschaft | Vertrag |
|---|---|
| Status | Plattform-intern; kein `workflow_call` |
| Inputs / Outputs | Keine |
| Berechtigungen | PR-Check `contents: read`; Versionierung `contents: write`, `pull-requests: write` |
| Voraussetzungen | Changesets PRs müssen einen Changeset für Änderungen an erforderlichen Pfaden enthalten. |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |
