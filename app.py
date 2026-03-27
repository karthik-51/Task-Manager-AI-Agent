import time
from typing import Dict, List

from analyzers.detector import IncidentDetector
from analyzers.incident_grouper import IncidentGrouper
from services.alert_service import AlertService
from services.incident_service import IncidentService
from services.llm_analysis_service import LLMAnalysisService
from services.log_service import LogService


class MonitoringAgent:
    def __init__(self) -> None:
        self.log_service = LogService()
        self.detector = IncidentDetector()
        self.grouper = IncidentGrouper()
        self.alert_service = AlertService()
        self.incident_service = IncidentService()
        self.llm_service = LLMAnalysisService()

    def _detect_incidents(self, hits: List[Dict], source_kind: str) -> List[Dict]:
        incidents = []

        for hit in hits:
            source = hit.get("_source", {})
            incident = self.detector.detect_from_source(source, source_kind=source_kind)
            if incident:
                incidents.append(incident)

        return incidents

    def _process_grouped_incidents(self, grouped_incidents: List[Dict]) -> None:
        print(f"[INFO] Unique grouped incidents: {len(grouped_incidents)}")

        for grouped_incident in grouped_incidents:
            print(
                f"[ALERT] Grouped incident detected | "
                f"source={grouped_incident['source_kind']} | "
                f"component={grouped_incident['component']} | "
                f"rule={grouped_incident['rule_name']} | "
                f"file={grouped_incident['source_file']}"
            )

            try:
                llm_result = self.llm_service.analyze(grouped_incident)
                analyzed_incident = {**grouped_incident, **llm_result}

                self.incident_service.store_incident(analyzed_incident)

                was_sent = self.alert_service.send_alert(analyzed_incident)
                if was_sent:
                    print("[INFO] Alert email sent")
                else:
                    print("[INFO] Duplicate alert skipped")

            except Exception as exc:
                print(f"[ERROR] Failed to process grouped incident: {exc}")

    def run_once(self) -> None:
        try:
            if not self.log_service.client.ping():
                print("[ERROR] OpenSearch ping failed")
                return
        except Exception as exc:
            print(f"[ERROR] OpenSearch health check failed: {exc}")
            return

        print("[INFO] Fetching recent docker logs...")
        docker_hits = self.log_service.get_docker_logs()
        print(f"[INFO] Docker logs fetched: {len(docker_hits)}")
        docker_incidents = self._detect_incidents(docker_hits, source_kind="docker")
        print(f"[INFO] Docker matched incidents: {len(docker_incidents)}")
        grouped_docker = self.grouper.group(docker_incidents)
        self._process_grouped_incidents(grouped_docker)

        print("[INFO] Fetching recent Jenkins logs...")
        jenkins_hits = self.log_service.get_jenkins_logs()
        print(f"[INFO] Jenkins logs fetched: {len(jenkins_hits)}")
        jenkins_incidents = self._detect_incidents(jenkins_hits, source_kind="jenkins")
        print(f"[INFO] Jenkins matched incidents: {len(jenkins_incidents)}")
        grouped_jenkins = self.grouper.group(jenkins_incidents)
        self._process_grouped_incidents(grouped_jenkins)

    def run_forever(self) -> None:
        print("[INFO] AI monitoring agent started")

        while True:
            try:
                self.run_once()
            except Exception as exc:
                print(f"[ERROR] Monitoring cycle failed: {exc}")

            time.sleep(60)

if __name__ == "__main__":
    agent = MonitoringAgent()
    agent.run_forever()
