from fastapi import Request
from logger import logger  # Importeer je logger
import time

async def log_middleware(request: Request, call_next):
    start_time = time.time()

    response = await call_next(request)

    process_time = time.time() - start_time

    log_dict = {
        'url': request.url.path,
        'method': request.method,
        'process_time': process_time,
        'status_code': response.status_code
    }

    if 400 <= log_dict['status_code'] < 500:
        logger.warning(log_dict['status_code'], extra=log_dict)
    elif 500 <= log_dict['status_code'] < 600:
        logger.error(log_dict['status_code'], extra=log_dict)
    elif process_time > 1.0:
        logger.warning('Duurt lang', extra=log_dict)

    return response