# arithmetic_operation.py

def perform_operation(num1, num2, operation)
    """
    Performs basic arithmetic operations on two numbers.

    Parameters:
    - num1 (float): The first number
    - num2 (float): The second number
    - operation (string): The operation to perform ('add', 'subtract', 'multiply', 'divide')


    Returns:
    - float: Result of the arithmetic operation
    """

    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero!"
        else:
            return num1 / num2
    else:
        return "Error: unsupported operation!"


# This script defines a function perform_operation that handles arithmetic operations based on user input.
# It includes handling for division by zero and returns appropriate messages or values.
