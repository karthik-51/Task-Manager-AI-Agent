from opensearchpy import OpenSearch
from config.settings import Settings


class OpenSearchClient:
    def __init__(self) -> None:
        self.client = OpenSearch(
            hosts=[
                {
                    "host": Settings.OPENSEARCH_HOST,
                    "port": Settings.OPENSEARCH_PORT,
                }
            ],
            http_auth=(Settings.OPENSEARCH_USER, Settings.OPENSEARCH_PASSWORD),
            use_ssl=Settings.OPENSEARCH_USE_SSL,
            verify_certs=Settings.OPENSEARCH_VERIFY_CERTS,
            ssl_assert_hostname=False,
            ssl_show_warn=False,
        )

    def ping(self) -> bool:
        return self.client.ping()

    def search_recent_logs(self, index_pattern: str, size: int = 100):
        query = {
            "size": size,
            "sort": [{"@timestamp": {"order": "desc"}}],
            "query": {
                "bool": {
                    "filter": [
                        {
                            "range": {
                                "@timestamp": {
                                    "gte": "now-10m",
                                    "lte": "now"
                                }
                            }
                        }
                    ]
                }
            }
        }

        response = self.client.search(index=index_pattern, body=query)
        return response.get("hits", {}).get("hits", [])