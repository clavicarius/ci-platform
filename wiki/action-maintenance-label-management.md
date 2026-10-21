# Repository Label Management

**Path:** `actions/maintenance-label-management/action.yml`

## Description

Synchronizes repository labels with a semicolon-delimited CSV file.

## Inputs

| Name | Required | Default | Description |
|---|---|---|---|
| `csv-file` | No | `.github/gh-labels.csv` | Path to the label configuration |
| `github-token` | Yes | — | Token with permission to manage repository labels |

## Permissions and requirements

The calling workflow needs:

```yaml
permissions:
  contents: read
  issues: write
```

The action uses GitHub CLI with the supplied token. No personal access token or
repository secret is required when using `${{ github.token }}`. Check out the
consumer repository before running the action. GitHub-hosted Ubuntu runners
provide both `gh` and Python 3.

## CSV format

The CSV uses semicolon delimiters and requires `category`, `name`, `color`, and
`description` columns:

```csv
category;name;color;description
Type;bug;D73A4A;"A bug that needs to be fixed."
Priority;priority: high;D73A4A;"High priority; should be addressed soon."
```

The category is for configuration grouping only; GitHub labels do not support a
category property. Color values must be six hexadecimal digits, with an
optional leading `#`. Quote fields containing semicolons or quotes according
to standard CSV rules.

Labels that already exist are updated and missing labels are created. Every
repository label not listed in the CSV is removed, including GitHub's default
labels and labels added manually. Keep the CSV complete; the CSV is validated
before the action changes labels. Repeated runs are idempotent.

## Example

```yaml
permissions:
  contents: read
  issues: write

steps:
  - uses: actions/checkout@v4
  - uses: clavicarius/ci-platform/actions/maintenance-label-management@v1
    with:
      csv-file: .github/gh-labels.csv
      github-token: ${{ github.token }}
```

See also: [Maintenance Label Management workflow](workflow-maintenance-label-management)
