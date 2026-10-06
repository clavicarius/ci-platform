# Actions

Composite Actions der CI-Plattform. Die versionierten Seiten in diesem Wiki sind die
maßgebliche Dokumentation der Action-API. Alle aufgeführten Actions sind consumer-tauglich
und können in eigenen Workflows verwendet werden.

## Quality

| Action | Consumer-tauglich | Beschreibung |
|---|---|---|
| [quality-link-check](action-quality-link-check) | Ja | Checks links and manages a GitHub issue report |
| [quality-lint](action-quality-lint) | Ja | Runs PHP, JS, Python, YAML and Markdown linters |
| [quality-markdown](action-quality-markdown) | Ja | Checks Markdown with markdownlint and Lychee |
| [quality-yaml](action-quality-yaml) | Ja | Validates YAML with yamllint |

## Security

| Action | Consumer-tauglich | Beschreibung |
|---|---|---|
| [security-dependency-review](action-security-dependency-review) | Ja | Reviews pull request dependencies for known vulnerabilities |
| [security-secret-scan](action-security-secret-scan) | Ja | Scans for secrets with Gitleaks and GitHub Secret Scanning |

## Release

| Action | Consumer-tauglich | Beschreibung |
|---|---|---|
| [release-semver-versioning](action-release-semver-versioning) | Ja | Computes the next v<major>.<minor>.<patch> tag. |
| [release-simple-versioning](action-release-simple-versioning) | Ja | Computes the next immutable v<major> tag. |
| [release-validate-branch](action-release-validate-branch) | Ja | Checks a release tag's branch |
| [release-validate-tag-immutable](action-release-validate-tag-immutable) | Ja | Rejects tag updates on push events |
| [release-validate-tags](action-release-validate-tags) | Ja | Validates tag format and monotonicity |

## Validate

| Action | Consumer-tauglich | Beschreibung |
|---|---|---|
| [validate-branch-name](action-validate-branch-name) | Ja | Validates branch names against a regex policy |

---

Siehe auch [Wiki Home](Home)
