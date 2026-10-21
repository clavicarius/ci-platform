# Release- und Tagging-Richtlinie

Zurück zur [Wiki-Startseite](https://github.com/clavicarius/ci-platform/wiki/Home).

## Zweck

Diese Richtlinie beschreibt Releases der gemeinsamen CI/CD-Plattform. Consumer
verwenden unveränderliche Tags `vX.Y.Z` oder den beweglichen Major-Alias `vN`;
es gibt keine getrennte Versionierung pro Workflow oder Action.

## Changesets steuern Releases

Das private Root-Package `ci-platform` ist ein Versionsanker. Es wird nicht zu
npm oder GitHub Packages veröffentlicht.

Ein Changeset ist für Änderungen an `.github/workflows/**`, `actions/**` und
von Actions verwendeten Skripten erforderlich. Reine Änderungen an `docs/**`,
`wiki/**`, `.github/ISSUE_TEMPLATE/**`, `CODEOWNERS` oder README-Dateien brauchen
keinen Changeset. Der PR-Check prüft diese Pfade.

Änderungsabsicht wird als Markdown-Datei unter `.changeset/` deklariert:

```markdown
---
"ci-platform": minor
---

Add optional `fail-on-warning` input to `quality-lint` (default remains false).
```

### Verbindliche SemVer-Policy

Da Consumer mit `@v1` sowohl Patch- als auch Minor-Releases automatisch erhalten:

- **patch:** Bugfix ohne Änderung von Inputs, Outputs, Defaults, Permissions oder
  Workflow-Pfaden.
- **minor:** neuer optionaler Input, neuer Workflow/Action oder neues optionales
  Output; bestehende Defaults und der Vertrag bleiben kompatibel.
- **major:** Breaking Change am `workflow_call`-/Action-Vertrag, etwa entfernter
  oder umbenannter Input, geändertes Default-Verhalten, neue erforderliche
  Permissions oder geänderter Dateipfad.

Breaking Changes veröffentlichen eine neue Major-Linie (`v2`); der vorhandene
Alias (`v1`) bleibt auf der letzten kompatiblen Version.

## Release-Ablauf

1. Ein Feature-PR enthält für Vertragsänderungen einen Changeset.
2. Nach Merge nach `main` erstellt bzw. aktualisiert `changesets/action` den
   Version-PR `chore: version packages`. Er aktualisiert `package.json` und
   `CHANGELOG.md`.
3. Ohne Changeset wird kein neues SemVer-Tag erstellt und der Major-Alias bleibt
   unverändert. Docs-/Wiki-only-Merges benötigen keinen Changeset.
4. Nach Merge des Version-PRs liest das Release-Script die Package-Version und
   erstellt `vX.Y.Z` sowie den passenden Alias `vN`.
5. Das GitHub Release verwendet den Changelog-Eintrag aus demselben Changeset.

Der Tag-Push löst keine erneute Versionierung aus. Erneute Läufe sind
idempotent: ein vorhandener Full-Tag wird nie verschoben oder dupliziert; ein
fehlender Major-Alias kann erneut auf den vorhandenen Release-Tag gesetzt werden.

## Tags und Changelog

- **Release-Tag (immutable):** `v<major>.<minor>.<patch>`, z. B. `v1.2.3`.
- **Major-Alias (mutable):** `v<major>`, z. B. `v1`; er zeigt auf den jüngsten
  kompatiblen Release derselben Major-Linie.
- Tags vom Format `ci-platform@1.2.3` werden nicht erzeugt.
- Changesets schreibt einen Abschnitt mit der Überschrift `## 1.2.3` in
  `CHANGELOG.md`. Dieser nicht leere Abschnitt wird am getaggten Commit
  validiert und für das GitHub Release verwendet.

Tag-Schutzregeln sollten Force-Updates für `v*.*.*` verhindern und dem CI-Actor
das Aktualisieren von `v[0-9]+` erlauben.

## Beispiele und Prüfungen

- Gültige Full-Tags: `v0.1.0`, `v1.2.3`, `v10.0.7`.
- Ungültige Full-Tags: `v1`, `v1.0`, `v01.2.3`.
- Nach einem Patch-/Minor-Release muss der passende `vN`-Alias auf denselben
  Commit wie `vX.Y.Z` zeigen.
- Ein Major-Release `v2.0.0` setzt `v2`; `v1` bleibt unverändert.
- Ein Docs-only-Merge ohne Changeset erzeugt keinen neuen Full-Tag.
- Ein erneuter Lauf darf keinen Full-Tag duplizieren oder verschieben.

## Branch Protection für CODEOWNERS

Für den Branch `main` sollte **Require review from Code Owners** aktiviert
sein. Diese Einstellung wird in GitHub Branch Protection bzw. einem Repository
Ruleset verwaltet und kann nicht durch eine Datei im Repository selbst aktiviert
werden.

## Migration vorhandener Tags

Nicht-konforme Alt-Tags werden nicht automatisch umbenannt oder gelöscht. Bei
der Umstellung auf Changesets bleiben existierende `vX.Y.Z`-Tags unverändert;
neue Releases folgen der Changeset-Version und aktualisieren nur ihren passenden
Major-Alias.

## Weiterführende Dokumentation

- [Versionierung](https://github.com/clavicarius/ci-platform/wiki/VERSIONING)
- [Release Versioning Workflow](https://github.com/clavicarius/ci-platform/wiki/workflow-release-versioning)
- [Release GitHub](https://github.com/clavicarius/ci-platform/wiki/workflow-release-github)
- [Tag-Validierung](https://github.com/clavicarius/ci-platform/blob/main/docs/workflows/release-validate-tags.md)

Bei Fragen oder Problemen mit Versionierung/Tagging kann ein Issue oder Pull
Request im Repository geöffnet werden.
