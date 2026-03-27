from collections import defaultdict
from typing import Dict, List, Tuple


class IncidentGrouper:
    def group(self, incidents: List[Dict]) -> List[Dict]:
        grouped: Dict[Tuple[str, str, str, str], List[Dict]] = defaultdict(list)

        for incident in incidents:
            key = (
                incident["source_kind"],
                incident["rule_name"],
                incident["component"],
                incident["source_file"],
            )
            grouped[key].append(incident)

        grouped_incidents: List[Dict] = []

        for _, items in grouped.items():
            first = items[0]
            grouped_incidents.append(
                {
                    "source_kind": first["source_kind"],
                    "rule_name": first["rule_name"],
                    "component": first["component"],
                    "source_file": first["source_file"],
                    "host": first["host"],
                    "timestamp": first["timestamp"],
                    "match_count": len(items),
                    "matched_logs": [item["message"] for item in items[:20]],
                }
            )

        return grouped_incidents