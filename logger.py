import logging
from pathlib import Path

class Logger():
    """
    The Logger class initializes the logging and opens the file which is passed as
    an argument As well as writing in the log and closing it. If init went wrong
    it raises an exeption for the caller
    """
    INFO = logging.INFO
    WARNING = logging.WARNING
    ERROR = logging.ERROR

    def __init__(self, folder_filename: Path):
        try:
            logging.basicConfig(
            filename=folder_filename,
            level=logging.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s"
            )
        except Exception as e:
            raise RuntimeError("Logger initialzing went wrong!") from e


    def write_log(self, message: str, level: int = logging.INFO) -> None:
        logging.log(level, message)


    def close_log(self):
        logging.shutdown()

