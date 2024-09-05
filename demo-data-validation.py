def get_int_exc(prompt):
    valid_entry = False
    whole_nbr = 0
    while not valid_entry:
        try:
            whole_nbr = int(input(prompt))
            valid_entry = True
        except:
            print("Invalid entry. Enter a whole number.")
    return whole_nbr  

def get_int_dv(prompt):
    valid_entry = False
    whole_nbr = 0
    while not valid_entry:
        whole_nbr = input(prompt)
        if whole_nbr.isdigit():
            whole_nbr = int(whole_nbr)
            valid_entry = True
        else:
            print("Invalid entry. Enter a whole number.")
    return whole_nbr

def main():
    print("Welcome to the number validator app!")
    
    print("Use Exception Handling to Validate:")
    nbr1 = get_int_exc("Enter first whole #: ")
    print(f"You entered {nbr1}")

    print("Use Data Validation to Validate:")
    nbr2 = get_int_dv("Enter second whole #: ")
    print(f"You entered {nbr2}")
    
    print("Bye")
    
if __name__ == "__main__":
    main()