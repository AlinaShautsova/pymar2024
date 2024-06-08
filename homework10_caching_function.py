"""Module contains a solution to the task: caching function."""


def cache(func):
    """Caches the results of a function call and returns the cached
    value on repeated calls with the same arguments."""
    storing_cached_values = {}

    def wrapper(*args):
        """Checks whether the result of a function call
        with the given arguments is already cached."""
        if args not in storing_cached_values:
            answer = func(*args)
            storing_cached_values[args] = answer
        else:
            answer = storing_cached_values[args]
        return answer
    return wrapper


@cache
def fibonacci(n):
    """Calculating Fibonacci sequence for a given number n."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print(fibonacci(5))
print(fibonacci(10))
print(fibonacci(5))
