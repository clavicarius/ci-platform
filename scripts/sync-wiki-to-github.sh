#!/usr/bin/env bash
set -euo pipefail

SOURCE_DIR="${SOURCE_DIR:-wiki}"
REPOSITORY="${REPOSITORY:?REPOSITORY is required}"
COMMIT_SHA="${COMMIT_SHA:-unknown}"

: "${GH_TOKEN:?GH_TOKEN is required}"

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Source directory not found: $SOURCE_DIR" >&2
  exit 1
fi

workdir=$(mktemp -d)
trap 'rm -rf "$workdir"' EXIT

wiki_clone_url="https://x-access-token:${GH_TOKEN}@github.com/${REPOSITORY}.wiki.git"

git clone --depth 1 "$wiki_clone_url" "$workdir/wiki-repo"

find "$workdir/wiki-repo" -mindepth 1 -maxdepth 1 ! -name '.git' -exec rm -rf {} +

shopt -s nullglob
md_files=("$SOURCE_DIR"/*.md)

if [ "${#md_files[@]}" -eq 0 ]; then
  echo "No markdown files found in $SOURCE_DIR" >&2
  exit 1
fi

cp "${md_files[@]}" "$workdir/wiki-repo/"

cd "$workdir/wiki-repo"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

git add -A

if git diff --staged --quiet; then
  echo "No wiki changes to publish."
  exit 0
fi

git commit -m "Sync wiki from ${COMMIT_SHA}"
git push origin HEAD

echo "Wiki published successfully."
