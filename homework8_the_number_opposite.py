"""Module providing a function printing python version."""
enter_n = int(input("Enter the number of n: "))
number1 = int(input("Enter first number: "))


def find_opposite_number(n, first_number):
    """Find opposite number."""
    number_of_values = n // 2
    opposite_number = first_number + number_of_values
    if opposite_number > n:
        opposite_number = opposite_number - n
    return opposite_number


print(f"Your answer: {find_opposite_number(enter_n, number1)}")
