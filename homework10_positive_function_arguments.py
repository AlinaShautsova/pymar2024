"""Module contains a solution to the task: positive function arguments."""


def validate_arguments(func):
    """Validate arguments."""
    def wrapper(*args):
        """Check variable is a number or not, and positive or not."""
        for arg in args:
            if not isinstance(arg, (int, float)) or arg <= 0:
                raise ValueError(f"{arg} variable is not a number "
                                 f"or not positive.")
        return func(*args)
    return wrapper


@validate_arguments
def enter_numbers(a, b):
    """Sum up the variables"""
    return a + b


print(enter_numbers(1, 2))
print(enter_numbers(2, -7))
