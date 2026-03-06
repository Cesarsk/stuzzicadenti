#!/usr/bin/env python3
import argparse
import base64
import json
import os
import re
import sys
from pathlib import Path
from urllib.request import Request, urlopen
import yaml

ROOT = Path(__file__).resolve().parent.parent
POLICY_PATH = ROOT / '.kiki' / 'auto-jira.yaml'


def fail(msg: str) -> None:
    print(f'RUN_ABORTED: {msg}')
    sys.exit(1)


def jira_request(base_url: str, email: str, token: str, method: str, path: str, payload=None):
    auth = base64.b64encode(f'{email}:{token}'.encode()).decode()
    data = None
    headers = {
        'Authorization': f'Basic {auth}',
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    if payload is not None:
        data = json.dumps(payload).encode()
    req = Request(base_url + path, data=data, headers=headers, method=method)
    with urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


def slugify(text: str) -> str:
    s = re.sub(r'[^a-zA-Z0-9]+', '-', text.strip().lower()).strip('-')
    return s[:50] or 'ticket'


def main():
    parser = argparse.ArgumentParser(description='Deterministic Jira ticket selector (fail-closed).')
    parser.add_argument('--dry-run', action='store_true', help='Only plan actions, do not transition or comment.')
    args = parser.parse_args()

    if not POLICY_PATH.exists():
        fail('policy file missing')

    policy = yaml.safe_load(POLICY_PATH.read_text())
    if not policy.get('enabled', False):
        fail('policy disabled')

    jira = policy['jira']
    github = policy['github']

    base_url = jira['baseUrl']
    email = os.getenv('JIRA_EMAIL', '').strip()
    token = os.getenv('JIRA_API_TOKEN', '').strip()
    if not email or not token:
        fail('missing JIRA_EMAIL/JIRA_API_TOKEN env vars')

    query = {
        'jql': jira['pickJql'],
        'maxResults': policy['execution'].get('maxTicketsPerRun', 1),
        'fields': ['summary', 'status', 'issuetype', 'labels', 'description']
    }
    result = jira_request(base_url, email, token, 'POST', '/rest/api/3/search/jql', query)
    issues = result.get('issues', [])
    if not issues:
        print('NO_ELIGIBLE_TICKETS')
        return

    issue = issues[0]
    key = issue['key']
    fields = issue['fields']
    summary = fields.get('summary', '')
    issue_type = fields.get('issuetype', {}).get('name')
    labels = set(fields.get('labels') or [])

    allowed_types = set(policy['execution'].get('allowedIssueTypes', []))
    if issue_type not in allowed_types:
        fail(f'{key} type {issue_type} not allowed')

    needed_label = jira['labels']['eligibility']
    if needed_label not in labels:
        fail(f'{key} missing required label {needed_label}')

    branch_template = github['branchNameTemplate']
    branch_type = github.get('allowedBranchTypes', ['chore'])[0]
    branch = (branch_template
              .replace('{type}', branch_type)
              .replace('{issueKey}', key)
              .replace('{slug}', slugify(summary)))

    print('PLAN')
    print(f'- issue: {key} :: {summary}')
    print(f'- currentStatus: {fields.get("status", {}).get("name")}')
    print(f'- nextStatus: {jira["statuses"]["inProgress"]}')
    print(f'- branch: {branch}')
    print(f'- worktreeMode: {policy["gitIsolation"]["mode"]}')

    if args.dry_run:
        print('DRY_RUN_ONLY')
        return

    print('READY_FOR_IMPLEMENTATION')
    print('NOTE: transition/commit/PR steps should be executed by your implementation worker.')


if __name__ == '__main__':
    main()
