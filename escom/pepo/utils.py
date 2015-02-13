__author__ = 'alberto'

import time
from functools import wraps
from config import logger


def measure_time(func):
    """
    Decorator that reports the execution time.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info("Running %s", func.__name__)
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.info("Execution time: %s", end - start)
        return result

    return wrapper