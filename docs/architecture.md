# Architecture

Dieses Dokument beschreibt die Repository-Struktur im Soll-Zielbild der CI-Plattform.
Die maßgebliche Referenz bleibt [docs/ci-platform.md](ci-platform.md).

## Architektur-Schichten

```text
Basis-Set (quality + security)
    ↓ optional
Pipeline-Bausteine (build, test, release, docker)
    ↓
Consumer-Repositories
```

## Repository-Struktur

```text
ci-platform/
├── .github/
│   └── workflows/
│       ├── quality-base-set.yml          # plattform-intern / consumer-tauglich
│       ├── quality-link-check.yml        # consumer
│       ├── quality-lint.yml              # consumer
│       ├── quality-markdown.yml          # consumer
│       ├── quality-yaml.yml              # consumer
│       ├── security-codeql.yml           # consumer
│       ├── security-dependency-review.yml # consumer
│       ├── security-secret-scan.yml      # consumer
│       ├── release-github.yml            # consumer
│       ├── release-validate-branch.yml   # consumer
│       ├── release-validate-tags.yml     # consumer
│       ├── release-validate-tag-immutable.yml # consumer
│       ├── validate-platform.yml         # plattform-intern
│       ├── build-<purpose>.yml           # optionaler pipeline-baustein
│       └── release-docker.yml            # optionaler pipeline-baustein
│
├── actions/
│   ├── quality-link-check/
│   ├── quality-lint/
│   ├── quality-markdown/
│   ├── quality-yaml/
│   ├── security-codeql/
│   ├── security-dependency-review/
│   ├── security-secret-scan/
│   ├── release-github/
│   ├── release-validate-branch/
│   ├── release-validate-tags/
│   ├── release-validate-tag-immutable/
│   ├── docker-build/                   # geplant
│   └── setup-node/                     # geplant
│
├── scripts/
│   ├── lib/
│   │   ├── logging.sh
│   │   ├── git.sh
│   │   └── docker.sh
│   ├── release/
│   │   └── create-release.sh
│   └── validation/
│       └── validate-yaml.sh
│
├── docs/
│   ├── ci-platform.md
│   ├── architecture.md
│   ├── RELEASING.md
│   └── workflows/
│       ├── README.md
│       └── <workflow>.md
│
├── README.md
├── AGENTS.md
├── CHANGELOG.md
├── CODEOWNERS
└── LICENSE
```

## Verantwortlichkeiten

| Stelle | Zweck |
|---|---|
| `.github/workflows/*.yml` | Trigger, Permissions, Orchestrierung, öffentliche API |
| `actions/<name>/action.yml` | Wiederverwendbare Implementierungsschritte |
| `scripts/` | Interne Hilfslogik und Shell-Utilities |
| `docs/workflows/*.md` | Detaillierte Consumer-Dokumentation |
| `docs/ci-platform.md` | Soll-Zielbild und Architektur-Spezifikation |

## Consumer-API vs. Plattform-intern

| Typ | Zweck | Einbindbar per `uses:` |
|---|---|---|
| Consumer-Workflows | Öffentliche API für andere Repositories | Ja (`workflow_call`) |
| Plattform-interne Workflows | PR-Gates, Validierung, Wartung des ci-platform-Repos | Nein |

Beispiele:

```yaml
jobs:
  quality:
    uses: clavicarius/ci-platform/.github/workflows/quality-base-set.yml@v1
```

```yaml
steps:
  - uses: clavicarius/ci-platform/actions/quality-link-check@v1
```

## Namenskonventionen

### Workflows

```text
<category>-<purpose>.yml
```

Beispiele:

- `quality-link-check.yml`
- `security-codeql.yml`
- `release-github.yml`
- `validate-platform.yml`

### Composite Actions

```text
actions/<category>-<purpose>/action.yml
```

Beispiele:

- `actions/quality-link-check/action.yml`
- `actions/security-secret-scan/action.yml`
- `actions/release-validate-tags/action.yml`

## Release-Pipeline

```text
release-validate-tag-immutable
  → release-validate-tags
    → release-validate-branch
      → release-github
```

Die Plattform verwendet SemVer-Tags (`v1.2.3`) mit einem Floating Major Alias (`@v1`).
Damit bleiben Consumer-Integrationen stabil und kompatibel, während im Repository neue Releases
weiterentwickelt werden.
