import logging
import sys
from logtail import LogtailHandler
import os

token = os.environ.get('LOGGING_TOKEN')

logger = logging.getLogger()

formatter = logging.Formatter(
    fmt="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

stream_handler = logging.StreamHandler(sys.stdout)
better_stack_handler = LogtailHandler(source_token=token)

stream_handler.setFormatter(formatter)
better_stack_handler.setFormatter(formatter)

logger.handlers = [stream_handler, better_stack_handler]

logger.setLevel(logging.INFO)