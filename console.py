# This module represents helper functions for console IO
def print_welcome(message="Welcome! Glad you are here!"):
    print("=" * len(message))
    print(message)
    print(f"console.print_welcome().__name__: {__name__}")
    print("=" * len(message) + "\n")
    
def validate_int_within_range(prompt, min_val, max_val):
    nbr = 0
    valid_entry = False
    while not valid_entry:
        nbr = int(input(prompt))
        if nbr < min_val:
            print(f'Error: please enter value greater than or equal to {min_val}.')
            continue
        elif nbr > max_val:
            print(f'Error: please enter value less than or equal to {max_val}.')
            continue
        else:
            valid_entry = True
    return nbr

# user entry must equal str1 or str2, can't be empty, entries converted to lowercase
def validate_required_string(prompt, str1, str2):
    ret_str = ""
    valid_entry = False
    while not valid_entry:
        ret_str = input(prompt).lower()
        if ret_str == "":
            print("Entry is required. Try again")
            continue
        elif ret_str != str1 and ret_str != str2:
            print(f"Error: Entry must be either '{str1}' or '{str2}'. Try again.")
        else:
            valid_entry = True
    return ret_str

# user entry (command) must be in the list of acceptable commands
def validate_menu_option(prompt, commands):
    command = ""
    valid_entry = False
    while not valid_entry:
        command = input(prompt)
        if command in commands:
            valid_entry = True
        else:
            print("Invalid command. Please try again.")
    return command

def even_odd_check(number):
    if number % 2 == 0:
        print("This is an even number")
    else:
        print("This is an Odd number") 