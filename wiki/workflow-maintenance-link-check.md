# Maintenance Link Check

Datei:

```
.github/workflows/maintenance-link-check.yml
```

> **Breaking change (v1):** Umbenannt von
> `check-broken-links-in-markdown.yml`. Betrifft nur dieses Repository
> (kein `workflow_call`). Externe Consumer, die den Dateipfad direkt
> referenziert haben, müssen auf den neuen Namen umstellen.

---

## Zweck

Der **Maintenance Link Check Workflow** führt eine geplante wöchentliche
Linkprüfung für dieses Repository aus.

Er ist **repository-intern** und nicht als wiederverwendbarer `workflow_call`
konzipiert. Für einbindbare Linkprüfungen in anderen Repositories siehe
[Quality Link Check](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-link-check).

---

## Trigger

| Trigger | Beschreibung |
|---|---|
| `schedule` | Sonntags um 11:11 UTC |
| `workflow_dispatch` | Manueller Start |

---

## Verhalten

- prüft Links mit Lychee
- erstellt oder aktualisiert ein Issue bei defekten Links
- schließt das Issue automatisch, wenn alle Links wieder gültig sind

---

## Siehe auch

- [Quality Link Check](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-link-check)
- [Quality Base Set](https://github.com/clavicarius/ci-platform/wiki/workflow-quality-base-set)

---

Siehe auch [Workflows](Workflows) | [Wiki Home](Home)

## Plattform-interner Vertrag

| Eigenschaft | Vertrag |
|---|---|
| Status | Plattform-intern; kein `workflow_call` |
| Inputs / Outputs | Keine |
| Berechtigungen / Secrets | `contents: read`, `issues: write`; kein manuell konfiguriertes Secret |
| Voraussetzungen / Einschränkungen | Nur für dieses Repository; GitHub Issues und das konfigurierte Label müssen verfügbar sein. |
| Beispiel | Die oben genannten `schedule`- und `workflow_dispatch`-Trigger |
| Deprecation | [Sunset-Policy](Workflows#deprecation-und-sunset) |
