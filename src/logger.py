import logging
from src.config import LOG_LEVEL


def setup_logger():
    logging.basicConfig(level=LOG_LEVEL,
        format="%(asctime)s | %(levelname)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
