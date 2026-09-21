import logging
from pathlib import Path


def setup_logger(name, log_file=None, level=logging.DEBUG):
    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.propagate = False

    if log_file is None:
        log_file = Path(__file__).with_name("server.log")
    if logger.handlers:
        return logger

    file_handler = logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger