#!/usr/bin/env python3
"""Synchronize GitHub repository labels from a semicolon-delimited CSV file."""

from __future__ import annotations

import argparse
import csv
import json
import logging
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence

DEFAULT_CSV = Path(".github/gh-labels.csv")
REQUIRED_COLUMNS = {"category", "color", "description"}
COLOR_PATTERN = re.compile(r"[0-9a-fA-F]{6}")
LOGGER = logging.getLogger(__name__)


class LabelSyncError(Exception):
    """Raised when label configuration or GitHub CLI operations fail."""


@dataclass(slots=True)
class Label:
    """Represent a GitHub label and its desired properties."""

    name: str
    color: str
    description: str


def normalize_color(color: str, line_number: int | None = None) -> str:
    """Validate a hex color and return it without a leading hash."""
    normalized = color.strip().removeprefix("#")
    if not COLOR_PATTERN.fullmatch(normalized):
        location = f" on CSV line {line_number}" if line_number else ""
        raise LabelSyncError(
            f"Color must be a six-digit hex value{location}: {color!r}."
        )
    return normalized.upper()


def load_labels(csv_path: Path) -> dict[str, Label]:
    """Load and validate desired labels from a semicolon-delimited CSV."""
    if not csv_path.is_file():
        raise LabelSyncError(f"Label configuration file not found: {csv_path}")

    labels: dict[str, Label] = {}
    try:
        with csv_path.open(encoding="utf-8-sig", newline="") as source:
            reader = csv.reader(source, delimiter=";", strict=True)
            headers = next(reader, None)
            if headers is None:
                raise LabelSyncError(f"Label configuration is empty: {csv_path}")

            normalized_headers = [header.strip().lower() for header in headers]
            if len(normalized_headers) != len(set(normalized_headers)):
                raise LabelSyncError("CSV contains duplicate column names.")
            if "label" not in normalized_headers and "name" in normalized_headers:
                normalized_headers[normalized_headers.index("name")] = "label"
            if not REQUIRED_COLUMNS.union({"label"}).issubset(normalized_headers):
                raise LabelSyncError(
                    "CSV header must include Category;Label;Color;Description."
                )

            for line_number, row in enumerate(reader, start=2):
                if not row or all(not value.strip() for value in row):
                    continue
                if len(row) != len(normalized_headers):
                    raise LabelSyncError(
                        f"Invalid number of columns on CSV line {line_number}."
                    )

                values = dict(zip(normalized_headers, row))
                name = values["label"].strip()
                color = values["color"].strip()
                description = values["description"].strip()
                if not name:
                    raise LabelSyncError(
                        f"Label name is required on CSV line {line_number}."
                    )
                if not color:
                    raise LabelSyncError(
                        f"Color is required on CSV line {line_number}."
                    )
                if not description:
                    raise LabelSyncError(
                        f"Description is required on CSV line {line_number}."
                    )
                if name in labels:
                    raise LabelSyncError(
                        f"Duplicate label {name!r} on CSV line {line_number}."
                    )
                labels[name] = Label(
                    name=name,
                    color=normalize_color(color, line_number),
                    description=description,
                )
    except (csv.Error, OSError, UnicodeError) as error:
        raise LabelSyncError(f"Could not read label configuration: {error}") from error
    return labels


class GitHubClient:
    """Encapsulate all GitHub CLI interactions."""

    def __init__(self, repository: str | None = None) -> None:
        """Create a client for a repository or determine the current repository."""
        self.repository = repository or self.get_current_repository()
        if self.repository.count("/") != 1 or any(
            not part for part in self.repository.split("/")
        ):
            raise LabelSyncError(
                f"Invalid repository {self.repository!r}; expected owner/repository."
            )

    @staticmethod
    def _run(command: list[str]) -> subprocess.CompletedProcess[str]:
        """Run a GitHub CLI command with consistent UTF-8 handling."""
        try:
            return subprocess.run(
                command,
                check=True,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
            )
        except FileNotFoundError as error:
            raise LabelSyncError("GitHub CLI (gh) is not installed.") from error
        except subprocess.CalledProcessError as error:
            detail = (error.stderr or error.stdout or "").strip()
            raise LabelSyncError(
                f"GitHub CLI command failed: {detail or error.cmd!s}"
            ) from error

    @classmethod
    def get_current_repository(cls) -> str:
        """Determine the current repository using the GitHub CLI."""
        result = cls._run(
            ["gh", "repo", "view", "--json", "nameWithOwner", "-q", ".nameWithOwner"]
        )
        repository = result.stdout.strip()
        if not repository:
            raise LabelSyncError("Could not determine the current GitHub repository.")
        return repository

    def get_existing_labels(self) -> dict[str, Label]:
        """Fetch all existing repository labels in a single GitHub CLI call."""
        result = self._run(
            [
                "gh",
                "label",
                "list",
                "--json",
                "name,color,description",
                "--limit",
                "10000",
                "--repo",
                self.repository,
            ]
        )
        try:
            entries = json.loads(result.stdout)
            return {
                entry["name"]: Label(
                    name=entry["name"],
                    color=entry["color"].upper(),
                    description=entry.get("description") or "",
                )
                for entry in entries
            }
        except (json.JSONDecodeError, KeyError, TypeError, AttributeError) as error:
            raise LabelSyncError(
                "GitHub CLI returned an invalid repository label list."
            ) from error

    def create_label(self, label: Label) -> None:
        """Create a repository label."""
        self._write_label(label, overwrite=False)

    def update_label(self, label: Label) -> None:
        """Update an existing repository label."""
        self._write_label(label, overwrite=True)

    def _write_label(self, label: Label, overwrite: bool) -> None:
        """Create a label, optionally forcing an update of an existing label."""
        command = [
            "gh",
            "label",
            "create",
            "--color",
            label.color,
            "--description",
            label.description,
            "--repo",
            self.repository,
        ]
        if overwrite:
            command.append("--force")
        command.extend(["--", label.name])
        self._run(command)

    def delete_label(self, name: str) -> None:
        """Delete a repository label."""
        self._run(
            [
                "gh",
                "label",
                "delete",
                "--yes",
                "--repo",
                self.repository,
                "--",
                name,
            ]
        )


def sync_labels(
    client: GitHubClient,
    desired_labels: dict[str, Label],
    overwrite: bool = False,
    prune: bool = False,
) -> dict[str, int]:
    """Synchronize desired labels with GitHub and return operation counts."""
    existing_labels = client.get_existing_labels()
    LOGGER.info("Loaded GitHub labels: %d", len(existing_labels))
    counts = {"created": 0, "updated": 0, "deleted": 0, "skipped": 0}

    for name, desired in desired_labels.items():
        existing = existing_labels.get(name)
        if existing is None:
            LOGGER.info("Creating: %s", name)
            client.create_label(desired)
            counts["created"] += 1
        elif (
            existing.color != desired.color
            or existing.description != desired.description
        ) and overwrite:
            LOGGER.info("Updating: %s", name)
            client.update_label(desired)
            counts["updated"] += 1
        else:
            LOGGER.info("Skipping: %s", name)
            counts["skipped"] += 1

    if prune:
        for name in sorted(existing_labels.keys() - desired_labels.keys()):
            LOGGER.info("Deleting: %s", name)
            client.delete_label(name)
            counts["deleted"] += 1
    return counts


def parse_arguments(arguments: Sequence[str] | None = None) -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Synchronize GitHub repository labels from a CSV file."
    )
    parser.add_argument(
        "--repo",
        help="GitHub repository in owner/repository format (default: current repository).",
    )
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help=f"Semicolon-delimited labels CSV (default: {DEFAULT_CSV}).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Update existing labels when color or description differs.",
    )
    parser.add_argument(
        "--prune",
        action="store_true",
        help="Delete GitHub labels that are absent from the CSV.",
    )
    return parser.parse_args(arguments)


def main(arguments: Sequence[str] | None = None) -> int:
    """Run the label synchronization command-line utility."""
    logging.basicConfig(level=logging.INFO, format="%(message)s")
    options = parse_arguments(arguments)
    if sys.version_info < (3, 12):
        LOGGER.error("Python 3.12 or later is required.")
        return 1
    try:
        desired_labels = load_labels(options.csv)
        client = GitHubClient(options.repo)
        LOGGER.info("Repository: %s", client.repository)
        LOGGER.info("Loaded CSV labels: %d", len(desired_labels))
        counts = sync_labels(
            client,
            desired_labels,
            overwrite=options.overwrite,
            prune=options.prune,
        )
        LOGGER.info(
            "Summary\nCreated: %(created)d\nUpdated: %(updated)d\n"
            "Deleted: %(deleted)d\nSkipped: %(skipped)d",
            counts,
        )
        LOGGER.info("Done.")
    except LabelSyncError as error:
        LOGGER.error("%s", error)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
