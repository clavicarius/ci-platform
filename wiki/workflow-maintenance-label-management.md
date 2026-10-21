# Maintenance Label Management

**Files:**

```text
.github/workflows/maintenance-label-management.yml
actions/maintenance-label-management/action.yml
```

## Purpose

The platform-internal workflow synchronizes repository labels with
`.github/gh-labels.csv` whenever it changes on `main`: labels in the CSV are
created or updated, and labels not in the CSV are removed. It can also be run
manually and skips if the CSV file does not exist.

## Permissions

```yaml
permissions:
  contents: read
  issues: write
```

`issues: write` is required to manage labels. The workflow supplies
`${{ github.token }}` to the action.

## Consumer use

The reusable action is suitable for consumer repositories. See
[Repository Label Management](action-maintenance-label-management) for its CSV
format and a complete example workflow.

---

See also: [Workflows](Workflows) | [Wiki Home](Home)
