from typing import Dict, List

from clients.opensearch_client import OpenSearchClient
from config.settings import Settings


class LogService:
    def __init__(self) -> None:
        self.client = OpenSearchClient()

    def get_docker_logs(self) -> List[Dict]:
        return self.client.search_recent_logs(
            index_pattern=Settings.OPENSEARCH_DOCKER_INDEX,
            size=Settings.LOG_FETCH_SIZE,
            minutes=Settings.LOG_LOOKBACK_MINUTES,
        )

    def get_jenkins_logs(self) -> List[Dict]:
        return self.client.search_recent_logs(
            index_pattern=Settings.OPENSEARCH_JENKINS_INDEX,
            size=Settings.LOG_FETCH_SIZE,
            minutes=Settings.LOG_LOOKBACK_MINUTES,
        )