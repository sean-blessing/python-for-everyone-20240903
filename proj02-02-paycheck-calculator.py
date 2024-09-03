print("Welcome to the paycheck calculator app!\n")

# get user input
hours_worked = float(input("Hours worked:     "))
hourly_pay_rate = float(input("Hourly pay rate: "))

print()

# do biz logic - float types, round 2 decimal places:
gross_pay = round((hours_worked * hourly_pay_rate), 2)
tax_rate = 18
tax_amount = round((gross_pay * (tax_rate / 100)), 2)
take_home_pay = round((gross_pay - tax_amount), 2)

# print output:
print(f"Gross Pay:     {gross_pay}")
print(f"Tax Rate:      {tax_rate}%")
print(f"Tax Amount:    {tax_amount}")
print(f"Take Home Pay: {take_home_pay}")


print("bye")