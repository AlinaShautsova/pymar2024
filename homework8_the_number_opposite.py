"""Module providing a function printing python version."""

n = int(input("Enter the number of n: "))
first_number = int(input("Enter first number: "))
number_of_values = (n // 2)

opposite_number = first_number + number_of_values
if opposite_number > n:
    opposite_number = opposite_number - n
print(f"Your answer: {opposite_number}")
