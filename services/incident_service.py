from datetime import datetime, timezone

from clients.opensearch_client import OpenSearchClient
from config.settings import Settings


class IncidentService:
    def __init__(self) -> None:
        self.client = OpenSearchClient()

    def store_incident(self, incident_document: dict) -> None:
        payload = dict(incident_document)
        payload["stored_at"] = datetime.now(timezone.utc).isoformat()

        self.client.index_document(
            index_name=Settings.OPENSEARCH_INCIDENT_INDEX,
            document=payload,
        )