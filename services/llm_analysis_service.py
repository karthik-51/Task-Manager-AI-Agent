from clients.llm_client import LLMClient
from prompts.incident_prompt import build_incident_prompt


class LLMAnalysisService:
    def __init__(self) -> None:
        self.client = LLMClient()

    def analyze(self, grouped_incident: dict) -> dict:
        prompt = build_incident_prompt(grouped_incident)
        result = self.client.analyze_incident(prompt)

        return {
            "summary": result.get("summary", "No summary available"),
            "severity": result.get("severity", "unknown"),
            "root_cause": result.get("root_cause", "Unknown"),
            "affected_component": result.get("affected_component", grouped_incident["component"]),
            "recommended_action": result.get("recommended_action", []),
        }