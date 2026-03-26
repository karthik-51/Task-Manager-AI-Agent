from typing import Dict


def build_email_subject(incident: Dict) -> str:
    return f"[{incident['severity'].upper()}] {incident['component']} issue detected"


def build_email_body(incident: Dict) -> str:
    return f"""Incident Summary
A log pattern matched one of the AI agent monitoring rules.

Severity:
{incident['severity']}

Component:
{incident['component']}

Rule:
{incident['rule_name']}

Source:
{incident['source_kind']}

Host:
{incident['host']}

Time:
{incident['timestamp']}

Source File:
{incident['source_file']}

Detected Message:
{incident['message']}

Recommended Next Checks:
1. Review the recent logs in OpenSearch Dashboards
2. Check the affected container or Jenkins stage
3. Verify environment variables, connectivity, and recent deployment changes
"""