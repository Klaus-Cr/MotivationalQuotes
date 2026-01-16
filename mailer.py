from smtplib import SMTP, SMTPException
from email.message import EmailMessage
from logger import Logger


class EMailClient():
    """
    The class EmailClient is responsible for sending E-Mails
    It is using the logger object to log information about success
    or error situations.
    """

    def __init__(self, logger: Logger, host: str, port: int, user: str, password: str):
        self.logger = logger
        self.host = host
        self.port = port
        self.user = user
        self.password = password


    def send_email(self, from_addr: str, to_addr: str, subject: str, content: str):
        msg = EmailMessage()
        msg["From"] = from_addr
        msg["To"] = to_addr
        msg["Subject"] = subject
        msg.set_content(content)
        try:
            with SMTP(host=self.host, port=self.port) as smtp:
                smtp.ehlo()
                smtp.starttls()
                smtp.login(user=self.user, password=self.password)
                smtp.send_message(msg=msg)

            self.logger.write_log("Email was send successful")

        except SMTPException as error:
            # HINT: f-strings require Python >= 3.6
            self.logger.write_log(f"SMTP error: {error}",self.logger.ERROR)

        except Exception as error:
            # HINT: f-strings require Python >= 3.6
            self.logger.write_log(f"General error: {error}",self.logger.ERROR)

