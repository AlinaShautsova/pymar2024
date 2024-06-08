"""Module contains a solution to the task: 'Return number'."""


def result_of_function_is_number(func):
    """Check if the function result is a number."""
    def wrapper(*args, **kwargs):
        """Display an error message, if function result is not a number"""
        result = func(*args, **kwargs)
        if not isinstance(result, (int, float)):
            print(f"Error: This is {result} not a number")
            return result
        else:
            return result
    return wrapper


@result_of_function_is_number
def checking(a):
    return a


@result_of_function_is_number
def checking2(word):
    return f"Hello, {word}!"


print(checking(1))
print(checking('4'))
result_of_checking2 = checking2('World')
print(result_of_checking2)

assert checking(1) == 1, ("Function with argument (1) returned unexpected "
                          "result.")
assert checking('4') == '4', ("Function with argument ('4') returned "
                              "unexpected result.")
assert checking2('World') == 'Hello, World!', ("Function with argument"
                                               " ('Hello, World!') returned "
                                               "unexpected result.")
