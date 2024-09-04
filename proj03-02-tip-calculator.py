print("Welcome to the tip calculator app!\n")

# get input
cost_of_meal = float(input("Cost of meal: "))

# biz logic
# display output
# loop through the tip percentages: 15%, 20%, 25%
for pct in range(15,26,5):
    # calculate and print values:
    tip_amount = cost_of_meal * (pct / 100)
    total_amount = cost_of_meal + tip_amount
    # round results to 2 decimal places
    print()
    print(f"{pct}%")
    print(f"Tip Amount:   {round(tip_amount, 2)}")
    print(f"Total Amount: {round(total_amount, 2)}")

print("Bye")