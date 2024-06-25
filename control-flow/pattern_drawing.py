# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Draw the pattern
row = 1
while row <= size:
    # Print '*' for each column in the current row
    for column in range(size):
        print("*", end="")
    # Move to the next line after printing each row
    print()
    row += 1
