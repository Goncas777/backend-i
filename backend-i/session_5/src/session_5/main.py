import time
import logging


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def log_calls(func):
    """A decorator that logs function call details."""
    def wrapper(*args, **kwargs):
        start = time.time()
        logger.info(f"Calling {func.__name__} with args: {args} kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.info(f"{func.__name__} returned: {result}")
        end = time.time()
        logger.info(f"Time -> {end-start:.7f} seconds")
        return result
    return wrapper

@log_calls
def add(a, b):
    return a + b

print("Result of add:", add(3, 4))
