import { execFileSync, spawnSync } from 'node:child_process';
import { readFileSync, mkdtempSync, writeFileSync, rmSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';

const packageJson = JSON.parse(readFileSync(new URL('../package.json', import.meta.url), 'utf8'));
const version = packageJson.version;

if (!/^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$/.test(version)) {
  throw new Error(`Invalid package version: ${version}`);
}

const tag = `v${version}`;
const majorTag = `v${version.split('.')[0]}`;
const head = execFileSync('git', ['rev-parse', 'HEAD'], { encoding: 'utf8' }).trim();
execFileSync('git', ['fetch', '--force', '--tags', 'origin'], { stdio: 'inherit' });

const existingTag = spawnSync(
  'git',
  ['rev-parse', '--verify', `refs/tags/${tag}^{commit}`],
  { encoding: 'utf8', stdio: ['ignore', 'pipe', 'ignore'] },
);
if (existingTag.error) {
  throw existingTag.error;
}

let releaseCommit;
if (existingTag.status === 0) {
  releaseCommit = existingTag.stdout.trim();
} else {
  execFileSync('git', ['tag', tag, 'HEAD'], { stdio: 'inherit' });
  execFileSync('git', ['push', 'origin', `refs/tags/${tag}`], { stdio: 'inherit' });
  releaseCommit = head;
}

execFileSync('git', ['tag', '--force', majorTag, tag], { stdio: 'inherit' });
execFileSync('git', ['push', 'origin', '--force', `refs/tags/${majorTag}`], { stdio: 'inherit' });

if (releaseCommit !== head) {
  console.log(`${tag} already exists; no release is needed for this commit.`);
  process.exit(0);
}

const changelog = readFileSync(new URL('../CHANGELOG.md', import.meta.url), 'utf8').split(/\r?\n/);
const heading = `## ${version}`;
const start = changelog.indexOf(heading);
if (start === -1) {
  throw new Error(`CHANGELOG.md has no Changesets entry for ${version}`);
}

const end = changelog.findIndex((line, index) => index > start && line.startsWith('## '));
const entry = changelog.slice(start, end === -1 ? undefined : end).join('\n').trim();
if (entry === heading) {
  throw new Error(`CHANGELOG.md entry for ${version} is empty`);
}

const tempDir = mkdtempSync(join(tmpdir(), 'ci-platform-release-'));
try {
  const notesFile = join(tempDir, 'release-notes.md');
  writeFileSync(notesFile, `${entry}\n`);
  const release = spawnSync('gh', ['release', 'view', tag], { stdio: 'ignore' });
  if (release.status !== 0) {
    execFileSync('gh', ['release', 'create', tag, '--title', tag, '--notes-file', notesFile], {
      stdio: 'inherit',
    });
  }
} finally {
  rmSync(tempDir, { recursive: true, force: true });
}
