# p. 121
# import into module's default namespace
#import console

# import into a specified namespace
# giving module name an alias
#import console as cons

# import one function into the global namespace
#from console import print_welcome

# import all functions into global namespace (not recommended)
#from console import *

# import specific functions into global namespace (Sean's way)
from console import print_welcome, validate_int_within_range, validate_required_string
import sys

# prompt user for three whole numbers, print to console, then prompt to continue

def main():
    print_welcome("Welcome to the Modules application demo!")
    choice = "y"
    while choice == "y":
        nbr1 = validate_int_within_range("Enter Number 1 (within range 1 to 6): ", 1, 6)
        nbr2 = validate_int_within_range("Enter number 2 (within range 10 to 20): ", 10, 20)
        nbr3 = validate_int_within_range("Enter any positive number: ", 1, sys.maxsize)
        print(f"nbr1: {nbr1}")
        print(f"nbr2: {nbr2}")
        print(f"nbr3: {nbr3}")
        
        choice = validate_required_string("Continue (y/n)? ", "y", "n")
    print("Bye")
    
if __name__ == "__main__":
    main()