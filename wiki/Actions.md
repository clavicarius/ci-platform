# Actions

Composite Actions der CI-Plattform. Jede Action kann direkt in eigenen Workflows verwendet werden.

## Quality

| Action | Beschreibung |
|---|---|
| [quality-link-check](action-quality-link-check) | Checks repository links and manages a GitHub issue report |
| [quality-lint](action-quality-lint) | Runs code quality linters for PHP, JavaScript, Python, YAML, and Markdown |
| [quality-markdown](action-quality-markdown) | Checks Markdown documentation quality with markdownlint and Lychee |
| [quality-yaml](action-quality-yaml) | Validates YAML syntax and structure with yamllint |

## Security

| Action | Beschreibung |
|---|---|
| [security-dependency-review](action-security-dependency-review) | Reviews pull request dependency changes for known security vulnerabilities |
| [security-secret-scan](action-security-secret-scan) | Scans repositories for leaked secrets using Gitleaks and GitHub Secret Scanning  |

## Release

| Action | Beschreibung |
|---|---|
| [release-semver-versioning](action-release-semver-versioning) | Computes the next v<major>.<minor>.<patch> tag. |
| [release-simple-versioning](action-release-simple-versioning) | Computes the next immutable v<major> tag. |
| [release-validate-branch](action-release-validate-branch) | Verifies that a release tag points to a commit on the release branch |
| [release-validate-tag-immutable](action-release-validate-tag-immutable) | Rejects tag updates (force-push or move) on push events |
| [release-validate-tags](action-release-validate-tags) | Validates version tag format and monotonicity for simple versioning |

## Validate

| Action | Beschreibung |
|---|---|
| [validate-branch-name](action-validate-branch-name) | Validates pull request source branch names against a regex policy |

---

Siehe auch [Wiki Home](Home)
