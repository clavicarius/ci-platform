# Release- und Tagging-Richtlinie

## Zweck

Dieses Dokument legt die Konvention für Versions-Tags im Repository fest und
beschreibt den Prozess zum Erstellen gültiger Tags sowie die automatische
Prüfung per GitHub Action.

## Regeln

- Format: `vNNN` (Regex: `^v[1-9][0-9]*$`)
  - Keine führenden Nullen (z. B. `v01` ist ungültig).
  - Erste zulässige Version ist `v1` (`v0` ist nicht erlaubt).
- Monoton steigend: Neue Tags müssen numerisch größer sein als die aktuell
  größte existierende Version. Lücken sind erlaubt (z. B. `v1` → `v4` ist
  zulässig, solange `v4` > höchstes existierendes Tag).
- Bereits veröffentlichte Tags dürfen nicht verändert (forciert neu gesetzt)
  werden. Das Neusetzen bereits verwendeter Tag-Namen wird abgelehnt.

## Verantwortung

- Repository-Maintainer(s) sind verantwortlich für die Freigabe neuer Tags.
  Bei Unklarheiten oder Konflikten ist @clavicarius zu benachrichtigen.

## Ort der Dokumentation

- Diese Regel steht in `docs/RELEASING.md`.

## Wie man ein gültiges Tag setzt (Kurz-Anleitung)

1. Lokales Commit erstellen und pushen.
2. Lokales Tag erstellen: `git tag vN` (z. B. `git tag v5`) — wähle N so,
   dass N > höchste existierende `vNNN`.
3. Tag pushen: `git push origin v5`
4. Wenn ein Release erstellt wird, wähle dasselbe Tag (`v5`).
5. Die GitHub Action prüft das Tag automatisch; bei Fehlern schlägt der
   Release-/Tag-Workflow fehl und Maintainer werden benachrichtigt.

## Beispiele

- Gültig: `v1`, `v2`, `v10`, `v123`
- Ungültig: `v0`, `v01`, `v001`, `v1.0`, `version1`, `v1a`

## Automatisierte Prüfung (Kurz)

- Eine GitHub Action (`.github/workflows/release-validate-tags.yml`) prüft
  Tag-Pushes und Release-Publishes. Sie validiert Format und Reihenfolge und
  schlägt fehl bei Verstößen. Zusätzlich wird ein Issue für ungültige Tags
  erstellt.

## Migration vorhandener Tags

- Bestehende nicht-konforme Tags werden nicht automatisch umbenannt oder
  gelöscht. Eine separate Migration kann bei Bedarf geplant werden.

## Tests

- Testfälle (lokal/test-Repo) sollten u. a. enthalten: `v1`, `v2`, `v10`,
  `v01` (ungültig), `v0` (ungültig), Versuch, `v2` erneut zu setzen
  (abweisen).

## Kontakt / Fragen

- Bei Fragen: @clavicarius
