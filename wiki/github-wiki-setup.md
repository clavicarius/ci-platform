# GitHub Wiki einrichten

Die veröffentlichte Wiki-Startseite: [CI Platform Wiki](https://github.com/clavicarius/ci-platform/wiki/Home)

Die GitHub Wiki ist nicht der Ordner `wiki/` im Quell-Repository. GitHub speichert
Wiki-Seiten in einem separaten Repository namens `clavicarius/ci-platform.wiki.git`.
Der Ordner `wiki/` in diesem Repository ist eine versionierte Quelle und muss in die
Wiki übertragen werden.

## Wiki aktivieren

1. Öffne **Settings** im Repository `clavicarius/ci-platform`.
2. Öffne **General** und scrolle zu **Features**.
3. Aktiviere **Wikis**.
4. Öffne den Reiter **Wiki** und erstelle bei Bedarf die Startseite.

Die Wiki-Funktion kann nur von Repository-Maintainern aktiviert werden. Falls **Wikis**
nicht verfügbar ist, prüfe die Organisationsrichtlinien oder nutze die versionierten
`wiki/`-Seiten im Repository.

## Seiten übertragen

Klone das separate Wiki-Repository und kopiere die gewünschten Markdown-Seiten an dessen
Wurzel. GitHub erwartet die Wiki-Seiten dort, nicht in einem Unterordner namens `wiki/`.
Zum Beispiel:

```bash
git clone https://github.com/clavicarius/ci-platform.wiki.git
cp wiki/*.md ci-platform.wiki/
cd ci-platform.wiki
git add .
git commit -m "Add CI platform wiki pages"
git push
```

Der Befehl `cp` setzt voraus, dass du dich im geklonten Quell-Repository befindest. Passe
den Pfad bei Bedarf an. Wiki-Seiten werden unabhängig von der Branch- und Release-Version
des Quell-Repositorys veröffentlicht; Änderungen müssen deshalb separat übertragen und
gepflegt werden.

Lege in der Wiki bei Bedarf eine `_Sidebar.md` an, um Seiten in der Navigation
aufzulisten. Die Links der bereitgestellten Seiten verweisen auf Wiki-Seiten beziehungsweise
auf Dateien im Quell-Repository, damit sie auch nach dem Übertragen funktionieren.

## `docs/` umbenennen?

`docs/` sollte nicht in `wiki/` umbenannt werden. Die Workflows und bestehenden Links
erwarten `docs/workflows/`, und `docs/ci-platform.md` ist die verbindliche
Architektur-Spezifikation. Der Ordner `wiki/` ergänzt diese Repository-Dokumentation für
allgemeines Wissen; er ersetzt weder die Workflow-Dokumentation noch aktiviert er die
separate GitHub Wiki.
