print("Welcome to Exception Handling")

whole_number = 0
while True:
    try:
        whole_number = int(input("Enter a whole number: "))
        break
    except ValueError as ve:
        print("Error. Please enter a whole number.")
        #print(ve)

print(f"You entered: {whole_number}")

float_number = 0.0
valid_entry = False
while not valid_entry:
    try:
        float_number = float(input("Enter a float number: "))
        valid_entry = True
    except Exception:
        print("Error: Please enter a float number.")
print(f"You entered: {float_number}")

print("Bye")