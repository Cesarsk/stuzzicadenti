#!/usr/bin/env python3
import sys
from pathlib import Path
import yaml

POLICY_PATH = Path('.kiki/auto-jira.yaml')

REQUIRED_TOP_LEVEL = [
    'version', 'enabled', 'jira', 'github', 'execution', 'gitIsolation',
    'qualityGates', 'blockedPolicy', 'failurePolicy'
]

REQUIRED_STATUS_KEYS = ['todo', 'inProgress', 'review']
REQUIRED_PR_SECTION_KEYS = [
    'required', 'requireDescription', 'enforceTemplateSections', 'requiredSections'
]


def fail(msg: str) -> None:
    print(f'POLICY_INVALID: {msg}')
    sys.exit(1)


def main() -> None:
    if not POLICY_PATH.exists():
        fail(f'missing {POLICY_PATH}')

    data = yaml.safe_load(POLICY_PATH.read_text())
    if not isinstance(data, dict):
        fail('policy root must be a map/object')

    for key in REQUIRED_TOP_LEVEL:
        if key not in data:
            fail(f'missing top-level key: {key}')

    jira = data.get('jira', {})
    statuses = jira.get('statuses', {})
    for key in REQUIRED_STATUS_KEYS:
        value = statuses.get(key)
        if not isinstance(value, str) or not value.strip():
            fail(f'jira.statuses.{key} must be a non-empty string')

    pick_jql = jira.get('pickJql')
    if not isinstance(pick_jql, str) or 'ORDER BY' not in pick_jql.upper():
        fail('jira.pickJql must be deterministic and include ORDER BY')

    pr = data.get('github', {}).get('pr', {})
    for key in REQUIRED_PR_SECTION_KEYS:
        if key not in pr:
            fail(f'github.pr missing key: {key}')

    required_sections = pr.get('requiredSections', [])
    if not isinstance(required_sections, list) or not required_sections:
        fail('github.pr.requiredSections must be a non-empty list')

    git_iso = data.get('gitIsolation', {})
    if git_iso.get('mode') != 'worktree-per-ticket':
        fail('gitIsolation.mode must be worktree-per-ticket')
    if not git_iso.get('oneTicketPerWorktree', False):
        fail('gitIsolation.oneTicketPerWorktree must be true')

    print('POLICY_OK')


if __name__ == '__main__':
    main()
