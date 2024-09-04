# p. 107

# functions we've used
# print - accepts a parameter and doesn't return anything
print("Hello")

# int - accepts a parameter and returns a value of type int
one_str = "1"
one_int = int(one_str)

# print() - accepts no arguments/parameters
print()

# a function we write that accepts no parms and doesn't return anything
def print_welcome():
    print("Welcome to the chapter 4 demonstrations app!")
    print()
    
print_welcome()

# a function that accepts one parameter and no return
def print_welcome(message):
    print(message)
    print()
    
print_welcome("Wow Functions are so rad!")
#print_welcome()

# function accepts 2 arguments, returns a value
# computer the miles per gallon, given miles driven and gallons
def calc_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg

print(f"mpg: {calc_miles_per_gallon(100, 25)}")
prius_miles = 350
prius_gallons = 8

print(f"Prius mpg: {calc_miles_per_gallon(prius_miles, prius_gallons)}")

mpg1 = calc_miles_per_gallon(250, 4)

