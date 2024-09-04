    
def calc_miles_per_gallon(miles_driven, gallons):
    mpg = miles_driven / gallons
    mpg = round(mpg, 1)
    return mpg

def print_welcome(message="Welcome! Glad you are here!"):
    print("=" * len(message))
    print(message)
    print("=" * len(message) + "\n")

def main():
    print_welcome("Hello, welcome to the main function app!!!")
    print_welcome()
    # print a variety of mpgs by car
    print(f"mpg: {calc_miles_per_gallon(100, 25)}")
    print(f"mpg: {calc_miles_per_gallon(125, 4)}")
    print(f"mpg: {calc_miles_per_gallon(280, 12)}")
    
if __name__ == "__main__":
    main()