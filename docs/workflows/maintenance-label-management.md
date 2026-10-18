# Maintenance Label Management

> Published documentation: [GitHub Wiki](https://github.com/clavicarius/ci-platform/wiki/workflow-maintenance-label-management)

Files:

```text
.github/workflows/maintenance-label-management.yml
actions/maintenance-label-management/action.yml
```

## Purpose

Creates and updates repository labels from `.github/gh-labels.csv` when that file
changes on `main`. The workflow can also be started manually and skips when the
configuration file is absent.

## Permissions

```yaml
permissions:
  contents: read
  issues: write
```

`issues: write` is required to create or update labels. The workflow uses
`${{ github.token }}`; no personal access token or repository secret is needed.

## CSV format

Use a semicolon-delimited CSV file with this header:

```csv
category;name;color;description
Type;bug;D73A4A;"A bug that needs to be fixed."
Priority;priority: high;D73A4A;"High priority; should be addressed soon."
```

The `category` field groups labels in the configuration; GitHub labels do not
have a category property, so it is not sent to GitHub. `color` must be six
hexadecimal digits, optionally prefixed by `#`. Quote values that contain
semicolons or quotes using standard CSV quoting rules.

The action creates missing labels and updates the color and description of
existing labels. Running it repeatedly is safe.

## Reusable action

Check out the consumer repository before invoking the action:

```yaml
name: Manage Labels

on:
  push:
    branches:
      - main
    paths:
      - '.github/gh-labels.csv'
  workflow_dispatch:

permissions:
  contents: read
  issues: write

jobs:
  labels:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: clavicarius/ci-platform/actions/maintenance-label-management@v1
        with:
          csv-file: .github/gh-labels.csv
          github-token: ${{ github.token }}
```

The action inputs are `csv-file` (default `.github/gh-labels.csv`) and the
required `github-token`. GitHub CLI (`gh`) and Python 3 must be available on the
runner; both are preinstalled on GitHub-hosted Ubuntu runners.
