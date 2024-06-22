"""Module contains a solution to the task: engineering calculator."""
import operator
operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '**': operator.pow
}


def parse_expression(expression):
    """Function parses the entered expression into numbers and operators."""
    parts = expression.split()
    numbers = []
    operators = []

    for part in parts:
        if part.isnumeric():
            numbers.append(float(part))
        elif part in operations:
            operators.append(part)
        else:
            raise ValueError(f"Invalid expression format: {expression}")
    return numbers, operators


def calculate(numbers, operators):
    """Function evaluates the result of the expression."""
    if len(numbers) != len(operators) + 1:
        raise ValueError("Invalid expression format")
    result = numbers[0]
    for i, v in enumerate(operators):
        operation = operations[v]
        result = operation(result, numbers[i + 1])
    return result


def main():
    """Function of entering an expression and "exit" to exit the calculator
    also works with exceptions."""
    print("Enter the expression you want to calculate."
          "Enter 'exit' if you want to exit.")
    while True:
        try:
            user_input = input("~ ")
            if user_input.lower() == 'exit':
                print("Program completed.")
                break

            numbers, operators = parse_expression(user_input)
            result = calculate(numbers, operators)
            print(f"Result: {result}")

        except ValueError as e:
            print(f"Error: {e}")
        except ZeroDivisionError:
            print("Error: Can't divide by 0.")


if __name__ == "__main__":
    main()
