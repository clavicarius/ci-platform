# Quality Lint

**Pfad:** `actions/quality-lint/action.yml`

## Beschreibung

Runs code quality linters for PHP, JavaScript, Python, YAML, and Markdown

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `auto-detect` | nein | `true` | Automatically detect which linters to run based on project files |
| `php` | nein | `false` | Force PHP linting (PHP_CodeSniffer, PHPStan) |
| `javascript` | nein | `false` | Force JavaScript/TypeScript linting (ESLint, Prettier) |
| `python` | nein | `false` | Force Python linting (Ruff, flake8, pylint) |
| `yaml` | nein | `false` | Force YAML linting (yamllint) |
| `markdown` | nein | `false` | Force Markdown linting (markdownlint) |
| `skip-markdown` | nein | `false` | Disable Markdown linting even when auto-detection would enable it |
| `skip-yaml` | nein | `false` | Disable YAML linting even when auto-detection would enable it |
| `working-directory` | nein | `.` | Directory to run linters in |
| `php-version` | nein | `8.3` | PHP version for PHP linters |
| `node-version` | nein | `20` | Node.js version for JavaScript linters |
| `python-version` | nein | `3.12` | Python version for Python linters |

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/quality-lint@v1
```

Siehe auch: [workflow-quality-lint](workflow-quality-lint)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
