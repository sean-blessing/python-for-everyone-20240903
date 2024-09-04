print("=" * 80)
print("Shipping Calculator")
print("=" * 80)

choice = "y"

while choice == "y":
    while True:
        cost_of_items = float(input("Cost of items ordered: "))
        if cost_of_items < 0:
            print("Entry must be 0 or greater. Please try again.")
            continue
        else:
            shipping_cost = 0.0
            if cost_of_items < 30:
                shipping_cost = 5.95
            elif cost_of_items < 50:
                shipping_cost = 7.95
            elif cost_of_items < 75:
                shipping_cost = 9.95
            total_cost = round((cost_of_items + shipping_cost), 2)
            print(f"Shipping Cost:       {shipping_cost}")
            print(f"Total Cost:          {total_cost}")
            print()
            # prompt continue
            choice = input("Continue (y/n)? ")
            print("=" * 80)
            break

print("Bye")