from conversion import feet_to_meters, meters_to_feet
def main():
    display_title()
    
    choice = "y"
    while choice == "y":
        display_menu()
        menu_option = input("Select a conversion (a/b): ").lower()
        
        if menu_option == "a":
            feet = get_float("Enter feet: ")
            meters = feet_to_meters(feet)
            print(f"{round(meters,2)} Meters\n")
        elif menu_option == "b":
            meters = get_float("Enter meters: ")
            feet = meters_to_feet(meters)
            print(f"{round(feet,2)} Feet\n")

        choice = input("Would you like to perform another conversion (y/n)? ").lower()
    
    print("Bye")

def get_float(prompt):
    valid_entry = False
    float_nbr = 0.0
    while not valid_entry:
        try:
            float_nbr = float(input(prompt))
            valid_entry = True
        except:
            print("Invalid entry. Enter a valid float number.")
    return float_nbr    
    
def display_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    
def display_title():
    print("Feet and Meters Converter\n")
    
if __name__ == "__main__":
    main()