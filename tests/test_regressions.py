import json
import os
import subprocess
import tempfile
import textwrap
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run(command, *, cwd=ROOT, env=None):
    return subprocess.run(
        command,
        cwd=cwd,
        env={**os.environ, **(env or {})},
        capture_output=True,
        text=True,
        check=False,
    )


def action_run_block(path, step_name):
    lines = path.read_text().splitlines()
    step = f"    - name: {step_name}"
    start = lines.index(step)
    run_line = lines.index("      run: |", start)
    end = next(
        (
            index
            for index in range(run_line + 1, len(lines))
            if lines[index].startswith("    - name: ")
        ),
        len(lines),
    )
    return textwrap.dedent("\n".join(lines[run_line + 1:end]))


class RegressionTests(unittest.TestCase):
    def test_quality_lint_python_setup_does_not_require_dependency_manifest(self):
        action = (ROOT / "actions/quality-lint/action.yml").read_text()
        setup_python = action.split("    - name: Setup Python\n", 1)[1].split(
            "\n    - name:", 1
        )[0]
        self.assertNotIn("cache: pip", setup_python)
        self.assertNotIn("cache-dependency-path:", setup_python)

    def test_issue_57_78_branch_name_policy_and_custom_regex(self):
        script = ROOT / "scripts/validate-branch-name.sh"
        for branch in (
            "feature/new-feature",
            "enhancement/api",
            "bugfix/fix_1",
            "hotfix/fix.now",
            "release/v1.2.0",
            "chore/cleanup",
            "copilot/update-check",
        ):
            with self.subTest(branch=branch):
                result = run(["bash", str(script)], env={"BRANCH_NAME": branch})
                self.assertEqual(result.returncode, 0, result.stderr)

        for branch in (
            "Feature/new-feature",
            "feature/NewFeature",
            "feature/",
            "fix/login",
        ):
            with self.subTest(branch=branch):
                result = run(["bash", str(script)], env={"BRANCH_NAME": branch})
                self.assertNotEqual(result.returncode, 0)

        result = run(
            ["bash", str(script)],
            env={
                "BRANCH_NAME": "changeset-release/main",
                "BRANCH_REGEX": r"^changeset-release/main$",
            },
        )
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_issue_104_workflow_exempts_automation_authors(self):
        workflow = (ROOT / ".github/workflows/validate-branch-name.yml").read_text()
        self.assertIn(
            "github.event.pull_request.user.login != 'dependabot[bot]'", workflow
        )
        self.assertIn(
            "!contains(github.event.pull_request.user.login, 'copilot')", workflow
        )

    def test_issue_11_dependency_update_workflow_contract(self):
        workflow = (
            ROOT / ".github/workflows/maintenance-dependency-update.yml"
        ).read_text()
        action = (
            ROOT / "actions/maintenance-dependency-update/action.yml"
        ).read_text()
        documentation = (
            ROOT / "docs/workflows/maintenance-dependency-update.md"
        ).read_text()

        self.assertIn("workflow_call:", workflow)
        self.assertIn("renovate-token:", workflow)
        self.assertIn("contents: write", workflow)
        self.assertIn("pull-requests: write", workflow)
        self.assertIn("uses: ./actions/maintenance-dependency-update", workflow)
        self.assertIn("renovatebot/github-action@v46.3.13", action)
        self.assertIn("token: ${{ inputs.github-token }}", action)
        self.assertIn("cron: '0 6 * * 1'", documentation)
        self.assertIn("Dependabot", documentation)

    def test_issue_30_version_tag_formats_and_monotonicity(self):
        script = ROOT / "scripts/validate-version-tag.sh"
        with tempfile.TemporaryDirectory() as directory:
            repo = Path(directory)
            run(["git", "init", "-q"], cwd=repo)
            run(["git", "config", "user.email", "test@example.com"], cwd=repo)
            run(["git", "config", "user.name", "Regression Test"], cwd=repo)
            (repo / "file").write_text("test\n")
            run(["git", "add", "file"], cwd=repo)
            run(["git", "commit", "-qm", "test"], cwd=repo)
            run(["git", "tag", "v2"], cwd=repo)
            run(["git", "tag", "v7"], cwd=repo)
            output = repo / "output"
            accepted = run(
                ["bash", str(script)],
                cwd=repo,
                env={
                    "INPUT_TAG": "v8",
                    "CREATE_ISSUE_ON_FAILURE": "false",
                    "GITHUB_OUTPUT": str(output),
                },
            )
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            self.assertIn("valid=true", output.read_text())
            self.assertIn("max_tag=v7", output.read_text())

            for tag in ("v2", "v1.2", "v0", "1"):
                with self.subTest(tag=tag):
                    rejected = run(
                        ["bash", str(script)],
                        cwd=repo,
                        env={
                            "INPUT_TAG": tag,
                            "CREATE_ISSUE_ON_FAILURE": "false",
                        },
                    )
                    self.assertNotEqual(rejected.returncode, 0)

            for tag in ("v1.2.3", "v0.1.0", "v1.0.0-alpha", "v1.0.0+build"):
                with self.subTest(semver=tag):
                    accepted = run(
                        ["bash", str(script)],
                        cwd=repo,
                        env={
                            "INPUT_TAG": tag,
                            "VERSION_PATTERN": "semver",
                            "CREATE_ISSUE_ON_FAILURE": "false",
                        },
                    )
                    self.assertEqual(accepted.returncode, 0, accepted.stderr)

            rejected = run(
                ["bash", str(script)],
                cwd=repo,
                env={
                    "INPUT_TAG": "v1.2.3.4",
                    "VERSION_PATTERN": "semver",
                    "CREATE_ISSUE_ON_FAILURE": "false",
                },
            )
            self.assertNotEqual(rejected.returncode, 0)

    def test_issue_30_tag_immutability_metadata(self):
        script = ROOT / "scripts/validate-tag-immutable.sh"
        allowed = run(
            ["bash", str(script)],
            env={
                "INPUT_TAG": "v1.2.3",
                "TAG_CREATED": "true",
                "TAG_BEFORE": "0" * 40,
                "CREATE_ISSUE_ON_FAILURE": "false",
            },
        )
        self.assertEqual(allowed.returncode, 0, allowed.stderr)

        moved = run(
            ["bash", str(script)],
            env={
                "INPUT_TAG": "v1.2.3",
                "TAG_CREATED": "false",
                "TAG_BEFORE": "a" * 40,
                "CREATE_ISSUE_ON_FAILURE": "false",
            },
        )
        self.assertNotEqual(moved.returncode, 0)

        no_event_metadata = run(
            ["bash", str(script)],
            env={"INPUT_TAG": "v1.2.3", "CREATE_ISSUE_ON_FAILURE": "false"},
        )
        self.assertEqual(
            no_event_metadata.returncode, 0, no_event_metadata.stderr
        )

    def test_issue_31_release_commit_must_be_on_main(self):
        with tempfile.TemporaryDirectory() as directory:
            base = Path(directory)
            remote = base / "remote.git"
            repo = base / "repo"
            run(["git", "init", "--bare", "-q", str(remote)])
            repo.mkdir()
            run(["git", "init", "-q", "-b", "main"], cwd=repo)
            run(["git", "config", "user.email", "test@example.com"], cwd=repo)
            run(["git", "config", "user.name", "Regression Test"], cwd=repo)
            (repo / "file").write_text("main\n")
            run(["git", "add", "file"], cwd=repo)
            run(["git", "commit", "-qm", "main"], cwd=repo)
            main_commit = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
            run(["git", "remote", "add", "origin", str(remote)], cwd=repo)
            run(["git", "push", "-qu", "origin", "main"], cwd=repo)

            run(["git", "switch", "-qc", "feature/change"], cwd=repo)
            (repo / "feature").write_text("feature\n")
            run(["git", "add", "feature"], cwd=repo)
            run(["git", "commit", "-qm", "feature"], cwd=repo)
            feature_commit = run(["git", "rev-parse", "HEAD"], cwd=repo).stdout.strip()
            run(["git", "push", "-qu", "origin", "feature/change"], cwd=repo)

            script = ROOT / "scripts/validate-release-branch.sh"
            accepted = run(
                ["bash", str(script)],
                cwd=repo,
                env={"INPUT_COMMIT_SHA": main_commit},
            )
            self.assertEqual(accepted.returncode, 0, accepted.stderr)
            rejected = run(
                ["bash", str(script)],
                cwd=repo,
                env={"INPUT_COMMIT_SHA": feature_commit},
            )
            self.assertNotEqual(rejected.returncode, 0)

    def mock_gh(self, directory):
        executable = directory / "gh"
        executable.write_text(
            f"""#!{os.sys.executable}
import json
import os
import sys

args = sys.argv[1:]
with open(os.environ["GH_CALL_LOG"], "a", encoding="utf-8") as log:
    log.write(json.dumps(args) + "\\n")
if args[:2] == ["issue", "list"] or args[:2] == ["label", "list"]:
    if os.environ.get("GH_FAIL_LIST") == "true":
        raise SystemExit(1)
    if args[:2] == ["issue", "list"]:
        print(os.environ.get("GH_ISSUE_NUMBER", ""))
    else:
        print(os.environ.get("GH_LABELS", "[]"))
elif os.environ.get("GH_FAIL_MUTATION") == "true":
    raise SystemExit(1)
"""
        )
        executable.chmod(0o755)
        return executable

    def action_env(self, directory, **extra):
        self.mock_gh(directory)
        log = directory / "gh-calls.jsonl"
        return {
            "PATH": f"{directory}{os.pathsep}{os.environ['PATH']}",
            "GH_CALL_LOG": str(log),
            **extra,
        }, log

    def test_issue_88_label_sync_updates_configured_and_removes_stale(self):
        action = ROOT / "actions/maintenance-label-management/action.yml"
        script = action_run_block(action, "Synchronize labels")
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            csv_file = temp / "labels.csv"
            csv_file.write_text(
                "category;name;color;description\n"
                "Type;bug;D73A4A;A bug\n"
                "Status;ready;5319E7;Ready\n"
            )
            env, log = self.action_env(
                temp,
                CSV_FILE=str(csv_file),
                REPOSITORY="owner/repo",
                GH_TOKEN="",
                GH_LABELS=json.dumps([{"name": "bug"}, {"name": "obsolete"}]),
            )
            result = run(["bash", "-e", "-c", script], env=env)
            self.assertEqual(result.returncode, 0, result.stderr)
            calls = [json.loads(line) for line in log.read_text().splitlines()]
            self.assertTrue(
                any(call[:3] == ["label", "create", "--color"] for call in calls)
            )
            self.assertIn(
                [
                    "label",
                    "delete",
                    "--repo",
                    "owner/repo",
                    "--yes",
                    "--",
                    "obsolete",
                ],
                calls,
            )

    def test_issue_88_invalid_csv_fails_before_changing_labels(self):
        action = ROOT / "actions/maintenance-label-management/action.yml"
        script = action_run_block(action, "Synchronize labels")
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            csv_file = temp / "labels.csv"
            csv_file.write_text(
                "category;name;color;description\nType;bug;invalid;Bug\n"
            )
            env, log = self.action_env(
                temp,
                CSV_FILE=str(csv_file),
                REPOSITORY="owner/repo",
                GH_TOKEN="test-token",
                GH_LABELS="[]",
            )
            result = run(["bash", "-e", "-c", script], env=env)
            self.assertNotEqual(result.returncode, 0)
            self.assertFalse(log.exists())

    def test_issue_60_link_issue_mutations_and_disabled_issues_fail_softly(self):
        action = ROOT / "actions/quality-link-check/action.yml"
        scenarios = (
            ("Create or update issue", "", "GH_FAIL_MUTATION"),
            ("Create or update issue", "42", "GH_FAIL_MUTATION"),
            ("Close existing issue", "42", "GH_FAIL_MUTATION"),
            ("Create or update issue", "", "GH_FAIL_LIST"),
            ("Close existing issue", "", "GH_FAIL_LIST"),
        )
        for step, issue_number, failure in scenarios:
            with self.subTest(
                step=step, issue_number=issue_number, failure=failure
            ):
                script = action_run_block(action, step)
                with tempfile.TemporaryDirectory() as directory:
                    temp = Path(directory)
                    env, _ = self.action_env(
                        temp,
                        ISSUE_TITLE="Broken links",
                        ISSUE_LABEL="dead-link",
                        REPORT_FILE=str(temp / "report.md"),
                        GH_ISSUE_NUMBER=issue_number,
                        **{failure: "true"},
                    )
                    result = run(["bash", "-e", "-c", script], env=env)
                    self.assertEqual(result.returncode, 0, result.stderr)


if __name__ == "__main__":
    unittest.main()
