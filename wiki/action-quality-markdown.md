# Quality Markdown

**Pfad:** `actions/quality-markdown/action.yml`

## Beschreibung

Checks Markdown documentation quality with markdownlint and Lychee

## Inputs

| Name | Erforderlich | Standard | Beschreibung |
|---|---|---|---|
| `working-directory` | nein | `.` | Directory to scan for Markdown files |
| `markdown-glob` | nein | `—` | Glob pattern for Markdown files. Defaults to all Markdown files in working-directory. |
| `markdownlint-config` | nein | `—` | Path to a markdownlint configuration file |
| `enable-markdownlint` | nein | `true` | Run markdownlint checks for syntax, headings, and tables |
| `enable-link-check` | nein | `true` | Run Lychee link checks in Markdown files |
| `fail-on-link-errors` | nein | `true` | Fail the workflow when broken links are found |
| `lychee-args` | nein | `—` | Additional arguments passed to Lychee |
| `create-link-issue` | nein | `false` | Create or update a GitHub issue when broken links are found |
| `issue-title` | nein | `Markdown Link Checker Report` | Title of the GitHub issue for broken links |
| `issue-label` | nein | `dead-link` | Label used for the broken link GitHub issue |
| `link-report-file` | nein | `./lychee/out.md` | Lychee report output file |

## Verwendung

```yaml
uses: clavicarius/ci-platform/actions/quality-markdown@v1
```

Siehe auch: [workflow-quality-markdown](workflow-quality-markdown)

---

Siehe auch [Actions](Actions) | [Wiki Home](Home)
