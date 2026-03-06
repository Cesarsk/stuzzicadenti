#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f .kiki/auto-jira.yaml ]]; then
  echo "ERROR: .kiki/auto-jira.yaml missing"
  exit 1
fi

python3 .kiki/validate_policy.py

if [[ -z "${JIRA_EMAIL:-}" || -z "${JIRA_API_TOKEN:-}" ]]; then
  echo "ERROR: JIRA_EMAIL and JIRA_API_TOKEN are required"
  exit 1
fi

python3 .kiki/run_ticket.py "$@"
