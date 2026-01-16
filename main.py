from mailer import EMailClient
from logger import Logger
import json
from random import choice

from config import (LOGGING, SMTP_USER, SUBJECT, SMTP_PORT,
                    SMTP_HOST, SMTP_PASSWORD, FROM_ADDR, TO_ADDR, QUOTES)

def main() -> None:
    """
    Application entry point for sending motivational quotes

    The module is intended to be executed as the main entry point,
    either directly or via `python -m`.
    """
    msg = ""

    try:
        logger = Logger(LOGGING)
    except RuntimeError:
        exit(1)

    try:
        with open(file=QUOTES, mode="r", encoding="UTF-8") as fp:
            data = json.load(fp)
    except Exception as e:
        logger.write_log(str(e),logger.ERROR)
        logger.close_log()
        exit(1)
    else:
        text = choice(data)
        # HINT: f-strings require Python >= 3.6
        msg = f"{text["quote"]}\nAuthor: {text["author"]}"

    email_client = EMailClient(logger,SMTP_HOST,
                               SMTP_PORT, SMTP_USER,
                               SMTP_PASSWORD
                               )

    email_client.send_email(from_addr=FROM_ADDR,
                            to_addr=TO_ADDR,
                            subject=SUBJECT,
                            content=msg
                            )

    logger.close_log()


if __name__ == "__main__":
    main()
