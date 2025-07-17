monthly_income = 5000
monthly_expenses = 4000
difference = monthly_income - monthly_expenses
print(f"Your monthly savings are: {difference}")
annual_interest_rate = 5  # Annual interest rate in percentage
projected_savings = (difference * 12) + (difference * 12 * annual_interest_rate / 100)
print(f"Your projected savings after one year are: {projected_savings} including interest.")    
