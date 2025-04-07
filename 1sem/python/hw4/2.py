def check_arguments(*arg_types):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args):
            if len(args) < len(arg_types):
                raise TypeError("Ожидалось не более {} аргументов.".format(len(arg_types)))
            for i in range(len(arg_types)):
                if not isinstance(args[i], arg_types[i]):
                    raise TypeError(f"Аргумент по индексу {i} имеет неверный тип.")
                return func(*args)
            return wrapper
        return decorator
