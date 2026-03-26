import time
from typing import Dict, Set, Tuple

from analyzers.formatter import build_email_body, build_email_subject
from clients.smtp_client import SMTPClient
from config.settings import Settings
from utils.logger import get_logger


class AlertService:
    def __init__(self) -> None:
        self.smtp_client = SMTPClient()
        self.logger = get_logger("alert_service")
        self.sent_cache: Set[Tuple[str, str, str]] = set()
        self.last_sent_time: Dict[Tuple[str, str, str], float] = {}

    def _cache_key(self, incident: Dict) -> Tuple[str, str, str]:
        return (
            incident["rule_name"],
            incident["component"],
            incident["message"][:120],
        )

    def should_send(self, incident: Dict) -> bool:
        key = self._cache_key(incident)
        now = time.time()
        last_sent = self.last_sent_time.get(key)

        if last_sent is None:
            return True

        return (now - last_sent) >= Settings.ALERT_COOLDOWN_SECONDS

    def send_alert(self, incident: Dict) -> None:
        key = self._cache_key(incident)

        if not self.should_send(incident):
            self.logger.info("Skipping duplicate alert within cooldown window")
            return

        subject = build_email_subject(incident)
        body = build_email_body(incident)

        self.smtp_client.send_email(subject, body)
        self.last_sent_time[key] = time.time()
        self.logger.info("Alert email sent successfully")