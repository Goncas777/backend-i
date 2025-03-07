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


"so consegui fazer a parte do user, nao consegui a do caching"


users = ["Goncalo","Goncas","Guilhermina"]

@log_calls
def userverify(user):
    if user in users:
        return "Log in with success"
    else:
        return "User doesnt exist"

print(userverify("goncalo"))

