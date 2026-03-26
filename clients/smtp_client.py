import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from config.settings import Settings


class SMTPClient:
    def send_email(self, subject: str, body: str) -> None:
        if not Settings.ALERT_TO:
            raise ValueError("ALERT_TO is empty. Add recipient emails in .env")

        msg = MIMEMultipart()
        msg["From"] = Settings.ALERT_FROM
        msg["To"] = ", ".join(Settings.ALERT_TO)
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(Settings.SMTP_HOST, Settings.SMTP_PORT) as server:
            server.starttls()
            server.login(Settings.SMTP_USER, Settings.SMTP_PASSWORD)
            server.sendmail(Settings.ALERT_FROM, Settings.ALERT_TO, msg.as_string())