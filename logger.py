import logging
import sys
from logtail import LogtailHandler
import os

token = os.environ.get('LOGGING_TOKEN')

logger = logging.getLogger()

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s"
)

stream_handler = logging.StreamHandler(sys.stdout)
file_handler = logging.FileHandler('app.log')
beter_stack_handler = LogtailHandler(source_token=token)

stream_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.handlers = [stream_handler, file_handler, beter_stack_handler]

logger.setLevel(logging.INFO)