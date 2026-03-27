def build_incident_prompt(incident: dict) -> str:
    matched_logs = "\n".join(incident.get("matched_logs", [])[:10])

    return f"""
Analyze this production incident and return ONLY valid JSON.

Incident metadata:
- source_kind: {incident.get('source_kind')}
- component: {incident.get('component')}
- rule_name: {incident.get('rule_name')}
- source_file: {incident.get('source_file')}
- host: {incident.get('host')}
- timestamp: {incident.get('timestamp')}
- match_count: {incident.get('match_count')}

Matched logs:
{matched_logs}

Return JSON with exactly these keys:
summary
severity
root_cause
affected_component
recommended_action

Rules:
- summary: short paragraph
- severity: one of low, medium, high, critical
- root_cause: short explanation
- affected_component: string
- recommended_action: array of strings
"""