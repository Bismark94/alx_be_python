# finance_calculator.py

# Prompt user for monthly income and expenses
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = float(input("Enter your monthly income: ")) - float(input("Enter your total monthly expenses: "))


# Project annual savings with 5% simple interest
annual_savings = monthly_savings * 12 * (1 + 0.05)

# Display results
print(f"Your monthly savings are ${monthly_savings:.2f}.")
print(f"Projected savings after one year, with interest, is: ${annual_savings:.2f}.")
