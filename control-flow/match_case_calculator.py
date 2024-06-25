# Prompt the  user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for the type of  operation
operation = input("Choose the operation (+, -, *, /): ")

# Perform calculation based on the type of operation using if-elif-else
result = 0
error_message = "Cannot divide by zero."

if operation == '+':
    result = num1 + num2
    print(f"The result is {result}.")
elif operation == '-':
    result = num1 - num2
    print(f"The result is {result}.")
elif operation == '*':
    result = num1 * num2
    print(f"The result is {result}.")
elif operation == '/':
    if num2 == 0:
        print(error_message)
    else:
        result = num1 / num2
        print(f"The result is {result}.")
else:
    print(f"Invalid operation '{operation}'. Please choose from '+', '-', '*', '/'.")
