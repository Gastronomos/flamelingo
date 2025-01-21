import logging
import smtplib
import traceback
from dataclasses import dataclass
from email import utils as email_utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from api.src.constants import DEFAULT_SENDMAIL_SUBJECT

logger = logging.getLogger("uvicorn.info")


@dataclass
class Email:
    host: str
    port: int
    user: str
    password: str
    address: str

    def is_enabled(self):
        return self.host and self.port and self.user and self.password and self.address

    def __str__(self) -> str:
        return f"{self.user}:{self.password}@{self.host}:{self.port}?email={self.address}&mode={self.mode}"

    def init_smtp_server(self):  # pragma: no cover
        server = smtplib.SMTP(host=self.host, port=self.port, timeout=5)
        server.starttls()
        return server

    def check_ping(self):  # pragma: no cover
        dsn = str(self)
        if not self.is_enabled():
            logger.info("Checking ping failed: some parameters empty")
            return False
        try:
            with self.init_smtp_server() as server:
                server.login(self.user, self.password)
                server.verify(self.address)
            logger.info(f"Checking ping successful for {dsn}")
            return True
        except OSError:
            logger.info(f"Checking ping error for {dsn}\n{traceback.format_exc()}")
            return False

    def send_mail(self, where, text, subject=DEFAULT_SENDMAIL_SUBJECT, use_html_templates=False):  # pragma: no cover
        if not where:
            return
        message_obj = MIMEMultipart()
        message_obj["Subject"] = subject
        message_obj["From"] = self.address
        message_obj["To"] = where
        message_obj["Date"] = email_utils.formatdate()
        message_obj.attach(MIMEText(text, "html" if use_html_templates else "plain"))
        message = message_obj.as_string()
        with self.init_smtp_server() as server:
            server.login(self.user, self.password)
            server.sendmail(self.address, where, message)
