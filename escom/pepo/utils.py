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
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        logger.debug(" Running %s, execution time: %s", func.__name__, end - start)
        return result

    return wrapper