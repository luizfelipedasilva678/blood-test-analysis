def handle_failure(on_error: callable):
    def decorator(func):
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                return on_error(e)

        return wrapper

    return decorator
