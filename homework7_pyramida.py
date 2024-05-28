"""Module providing a function printing python version."""


def print_pyramid(a):
    for i in range(a):
        spaces = ' ' * (a - i - 1)
        stars = '*' * (2 * i + 1)
        print(spaces + stars + spaces)


n = int(input("Какое количество n Вы хотите: "))
print_pyramid(n)
