# Prompt user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on the type of operation using match case
result = 0
error_message = "Cannot divide by zero."

match operation:
    case '+':
        result = num1 + num2
    case '-':
        result = num1 - num2
    case '*':
        result = num1 * num2
    case '/':
        if num2 == 0:
            print(error_message)
        else:
            result = num1 / num2
            print(f"The result is {result}.")
    case _:
        print(f"Invalid operation '{operation}'. Please choose from '+', '-', '*', '/'.")

# Print the result for addition, subtraction, and multiplication
if operation in {'+', '-', '*'}:
    print(f"The result is {result}.")
