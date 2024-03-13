import logging
from logging.handlers import RotatingFileHandler

def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(filename='app.log', maxBytes=1000000, backupCount=5)
    handler.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger