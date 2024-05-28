"""Module providing a function printing python version."""


def print_pyramid(a):
    """Print pyramid by amount of lines."""
    for i in range(a):
        spaces = ' ' * (a - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars + spaces)


n = int(input("What amount of n do you want: "))
print_pyramid(n)
