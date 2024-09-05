from conversion import feet_to_meters, meters_to_feet
def main():
    display_title()
    
    choice = "y"
    while choice == "y":
        display_menu()
        menu_option = input("Select a conversion (a/b): ").lower()
        
        if menu_option == "a":
            feet = float(input("Enter feet: "))
            meters = feet_to_meters(feet)
            print(f"{round(meters,2)} Meters\n")
        elif menu_option == "b":
            meters = float(input("Enter meters: "))
            feet = meters_to_feet(meters)
            print(f"{round(feet,2)} Feet\n")

        choice = input("Would you like to perform another conversion (y/n)? ").lower()
    
    print("Bye")

def display_menu():
    print("Conversions Menu:")
    print("a. Feet to Meters")
    print("b. Meters to Feet")
    
def display_title():
    print("Feet and Meters Converter\n")
    
if __name__ == "__main__":
    main()