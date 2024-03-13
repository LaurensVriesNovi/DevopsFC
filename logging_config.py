import logging
from logging.handlers import RotatingFileHandler
import re
def setup_logging():
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(filename='app.log', maxBytes=1000000, backupCount=5)
    handler.setLevel(logging.INFO)

    # Define a custom filter to log only 400 and 500 status code messages
    class StatusCodeFilter(logging.Filter):
        def filter(self, record):
            message = record.getMessage()
            return re.search(r' (4|5)\d\d ', message) is not None

    # Add the filter to the handler
    handler.addFilter(StatusCodeFilter())

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logger.addHandler(handler)

    return logger