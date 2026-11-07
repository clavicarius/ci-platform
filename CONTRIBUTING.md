# Contributing

## Automated tests

Automated tests are part of every code change:

- New features must include tests for their expected behavior.
- Bug fixes must include a regression test that fails before the fix and passes
  after it.
- Refactorings must preserve or improve existing test coverage.
- Tests should be small, isolated, deterministic, and exercise relevant edge
  cases.

When a suitable automated test cannot be added, explain why in the pull request
and get that exception explicitly justified before merging.

Run the regression suite locally with:

```sh
python3 -m unittest discover -s tests -v
```

The `Validate Platform` workflow runs this suite automatically for pull requests
targeting `main`. When maintaining existing behavior, add regression tests for
previously fixed issues as coverage gaps are identified.
