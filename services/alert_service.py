from typing import Dict


def build_email_subject(incident: Dict) -> str:
    severity = incident.get("severity", "unknown").upper()
    component = incident.get("affected_component", incident.get("component", "unknown"))
    return f"[{severity}] {component} incident detected"


def build_email_body(incident: Dict) -> str:
    recommendations = incident.get("recommended_action", [])
    recommendation_text = "\n".join(
        [f"{idx + 1}. {item}" for idx, item in enumerate(recommendations)]
    ) or "1. Review logs in OpenSearch Dashboards"

    return f"""Incident Summary
{incident.get('summary', 'No summary available')}

Severity:
{incident.get('severity', 'unknown')}

Affected Component:
{incident.get('affected_component', incident.get('component', 'unknown'))}

Rule:
{incident.get('rule_name', 'unknown')}

Source:
{incident.get('source_kind', 'unknown')}

Host:
{incident.get('host', 'unknown')}

Source File:
{incident.get('source_file', 'unknown')}

Time:
{incident.get('timestamp', 'unknown')}

Match Count:
{incident.get('match_count', 0)}

Likely Root Cause:
{incident.get('root_cause', 'Unknown')}

Recommended Actions:
{recommendation_text}
"""