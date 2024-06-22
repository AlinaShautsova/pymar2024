"""Module contains a solution to the task: calculator."""


def calculator(expression):
    """Function evaluates the result of an expression and
    deals with exceptions."""
    try:
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Error: you can't divide by zero."
    except SyntaxError:
        return "Error: invalid expression format."


def main():
    """Function to enter an expression and show the results calculations."""
    print("Enter the expression you want to calculate . Enter "
          "'exit' if you want to exit.")
    while True:
        user_input = input("~ ")
        if user_input.lower() == 'exit':
            print("Program completed.")
            break
        result = calculator(user_input)
        print(f"Result: {result}")


if __name__ == "__main__":
    main()
