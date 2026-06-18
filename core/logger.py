import logging
import os


LOG_DIR = "logs"
LOG_FILE = "api_tests.log"

os.makedirs(LOG_DIR, exist_ok=True)

logger = logging.getLogger("api_logger")
logger.setLevel(logging.INFO)

if not logger.handlers:
    file_handler = logging.FileHandler(
        filename=os.path.join(LOG_DIR, LOG_FILE),
        mode="a",
        encoding="utf-8"
    )

    console_handler = logging.StreamHandler()

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )

    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)