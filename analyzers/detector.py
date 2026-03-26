from typing import Any, Dict, List, Optional

from analyzers.rules import DOCKER_RULES, JENKINS_RULES


class IncidentDetector:
    @staticmethod
    def _extract_message(source: Dict[str, Any]) -> str:
        parts = []

        for key in ["log", "message", "msg"]:
            value = source.get(key)
            if isinstance(value, str) and value.strip():
                parts.append(value.strip())

        if not parts:
            parts.append(str(source))

        return " | ".join(parts)

    def _match_rules(self, message: str, rules: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        lowered = message.lower()

        for rule in rules:
            if any(pattern.lower() in lowered for pattern in rule["patterns"]):
                return rule

        return None

    def detect_from_source(self, source: Dict[str, Any], source_kind: str) -> Optional[Dict[str, Any]]:
        message = self._extract_message(source)

        rules = DOCKER_RULES if source_kind == "docker" else JENKINS_RULES
        matched_rule = self._match_rules(message, rules)

        if not matched_rule:
            return None

        return {
            "rule_name": matched_rule["name"],
            "severity": matched_rule["severity"],
            "component": matched_rule["component"],
            "message": message,
            "timestamp": source.get("@timestamp", "unknown"),
            "host": source.get("host", "unknown"),
            "source_file": source.get("source_file", "unknown"),
            "source_kind": source_kind,
        }