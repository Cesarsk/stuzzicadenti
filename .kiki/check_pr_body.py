#!/usr/bin/env python3
import os
import sys
from pathlib import Path
import yaml

POLICY_PATH = Path('.kiki/auto-jira.yaml')


def fail(msg: str) -> None:
    print(f'PR_BODY_INVALID: {msg}')
    sys.exit(1)


def main() -> None:
    if not POLICY_PATH.exists():
        fail('missing policy file')

    policy = yaml.safe_load(POLICY_PATH.read_text())
    required_sections = policy.get('github', {}).get('pr', {}).get('requiredSections', [])
    if not required_sections:
        fail('no required sections configured in policy')

    body = os.getenv('PR_BODY', '')
    if not body.strip():
        fail('PR body is empty')

    missing = [s for s in required_sections if s not in body]
    if missing:
        fail('missing required section(s): ' + ', '.join(missing))

    print('PR_BODY_OK')


if __name__ == '__main__':
    main()
