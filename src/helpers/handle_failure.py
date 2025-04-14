from re import match


def handle_failure(on_error: callable):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                if match(".*404.*", str(e)):
                    return on_error(404)

                if match(".*403.*", str(e)):
                    return on_error(403)

                return on_error(500)

        return wrapper

    return decorator
