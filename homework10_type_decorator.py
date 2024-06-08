"""Module contains a solution to the task: type decorator."""


def typed(type1):
    """Function takes decorator arguments."""
    def decorator(func):
        """Function accepts the function to be decorated."""
        def wrapper(*args):
            """Function change type of arguments and execute main function."""
            new_args = []
            for arg in args:
                new_args.append(type1(arg))
            return func(*new_args)
        return wrapper
    return decorator


@typed(str)
def add_str(a, b):
    """Function sums arguments."""
    return a + b


@typed(int)
def add_int(a, b, c):
    """Function sums arguments."""
    return a + b + c


@typed(float)
def add_float(a, b, c):
    """Function sums arguments."""
    return a + b + c


assert add_str("3", 5) == "35", ("Function with arguments '3' and 5"
                                 " returned not a '35' result.")
assert add_str(5, 5) == "55", ("Function with arguments "
                               "returned unexpected result.")
assert add_str('a', 'b') == 'ab', ("Function with arguments "
                                   "returned unexpected result.")
assert add_int(5, 6, 7) == 18, ("Function with arguments "
                                "returned unexpected result.")
assert add_float(0.1, 0.2, 0.4) == 0.7000000000000001, ("Function"
                                                        " with arguments "
                                                        "returned unexpected "
                                                        "result.")
