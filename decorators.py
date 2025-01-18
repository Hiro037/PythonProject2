from functools import wraps

def log(filename: str = None):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f"{func.__name__} ok\n"
                _write_log(log_message, filename)
                return result
            except Exception as e:
                log_message = (f"{func.__name__} error: {type(e).__name__}. "
                               f"Inputs: {args}, {kwargs}\n")
                _write_log(log_message, filename)
                raise
        return wrapper
    return decorator

def _write_log(log_message: str, filename: str = None):
    if filename:
        with open(filename, "a") as file:
            file.write(log_message)
    else:
        print(log_message)
