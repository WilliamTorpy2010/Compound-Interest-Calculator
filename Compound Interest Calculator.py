"""
Compound Interest Calculator

Calculates monthly compound interest.

Created for EFDS practice project.
"""


print("==============================")
print(" Compound Interest Calculator ")
print("==============================")


# User inputs

initial_investment = float(
    input("Enter initial investment (£): ")
)

interest_rate = float(
    input("Enter annual interest rate (%): ")
)

years = int(
    input("Enter investment period (years): ")
)


# Compound interest calculation

monthly_interest_rate = (interest_rate / 100) / 12

number_of_months = years * 12

final_amount = initial_investment * (
    1 + monthly_interest_rate
) ** number_of_months


# Calculate profit

interest_earned = final_amount - initial_investment


# Output results

print("\n========== RESULTS ==========")

print(
    "Initial investment: £",
    round(initial_investment, 2)
)

print(
    "Interest rate:",
    interest_rate,
    "%"
)

print(
    "Investment period:",
    years,
    "years"
)

print(
    "Final value: £",
    round(final_amount, 2)
)

print(
    "Interest earned: £",
    round(interest_earned, 2)
)

print("=============================")
