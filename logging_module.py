"""Module logging for homework22."""
import logging


def setup_logging():
    """Set up logging function."""
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s')
    file_handler = logging.FileHandler('robot.log')
    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    logger = logging.getLogger(__name__)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger
