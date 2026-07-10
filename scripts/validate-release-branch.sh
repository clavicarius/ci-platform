#!/usr/bin/env bash
set -euo pipefail

COMMIT_SHA="${INPUT_COMMIT_SHA:-${GITHUB_SHA:-}}"
RELEASE_BRANCH="${RELEASE_BRANCH:-main}"

if [ -z "$COMMIT_SHA" ]; then
  echo "No commit SHA provided." >&2
  exit 1
fi

git fetch origin "$RELEASE_BRANCH"

if ! git branch -r --contains "$COMMIT_SHA" \
  | grep -qE "^[[:space:]]*origin/${RELEASE_BRANCH}$"; then
  echo "::error::Release tags must be created from the ${RELEASE_BRANCH} branch." >&2
  echo "The commit $COMMIT_SHA is not on origin/${RELEASE_BRANCH}." >&2
  exit 1
fi

echo "OK: tag commit is on origin/${RELEASE_BRANCH}."
