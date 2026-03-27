import os
from dotenv import load_dotenv

load_dotenv()


def _to_bool(value: str, default: bool = False) -> bool:
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "y", "on"}


class Settings:
    OPENSEARCH_HOST = os.getenv("OPENSEARCH_HOST", "localhost")
    OPENSEARCH_PORT = int(os.getenv("OPENSEARCH_PORT", "9200"))
    OPENSEARCH_USER = os.getenv("OPENSEARCH_USER", "admin")
    OPENSEARCH_PASSWORD = os.getenv("OPENSEARCH_PASSWORD", "")
    OPENSEARCH_USE_SSL = _to_bool(os.getenv("OPENSEARCH_USE_SSL"), True)
    OPENSEARCH_VERIFY_CERTS = _to_bool(os.getenv("OPENSEARCH_VERIFY_CERTS"), False)

    OPENSEARCH_DOCKER_INDEX = os.getenv("OPENSEARCH_DOCKER_INDEX", "task-deploy-docker-*")
    OPENSEARCH_JENKINS_INDEX = os.getenv("OPENSEARCH_JENKINS_INDEX", "jenkins-logs-*")
    OPENSEARCH_INCIDENT_INDEX = os.getenv("OPENSEARCH_INCIDENT_INDEX", "ai-agent-incidents")

    SMTP_HOST = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER = os.getenv("SMTP_USER", "")
    SMTP_PASSWORD = os.getenv("SMTP_PASSWORD", "")
    ALERT_FROM = os.getenv("ALERT_FROM", SMTP_USER)
    ALERT_TO = [e.strip() for e in os.getenv("ALERT_TO", "").split(",") if e.strip()]

    POLL_INTERVAL_SECONDS = int(os.getenv("POLL_INTERVAL_SECONDS", "60"))
    LOG_FETCH_SIZE = int(os.getenv("LOG_FETCH_SIZE", "100"))
    LOG_LOOKBACK_MINUTES = int(os.getenv("LOG_LOOKBACK_MINUTES", "5"))
    ALERT_COOLDOWN_SECONDS = int(os.getenv("ALERT_COOLDOWN_SECONDS", "1800"))

    OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
    OLLAMA_TIMEOUT_SECONDS = int(os.getenv("OLLAMA_TIMEOUT_SECONDS", "60"))
    OLLAMA_KEEP_ALIVE = os.getenv("OLLAMA_KEEP_ALIVE", "10m")