# finance_calculator.py

# Prompt the user for their monthly income and total monthly expenses
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate the monthly savings
monthly_savings = monthly_income - monthly_expenses

# Calculate the projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the results
print(f"Your monthly savings are ${monthly_savings}.")
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
