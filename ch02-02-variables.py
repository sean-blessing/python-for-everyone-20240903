# declare some variables
# p. 35
# camelCase, spinal-case, PascalCase or TitleCase are other naming conventions
# snake_case - preferred naming convention
first_name = "Bob"
last_name = "Marley"
middle_name = "Nesta"
full_name = first_name + ' ' + middle_name + " " + last_name

print(full_name)

# buying a mouse pad for each student
product = "mouse pad"
quantity = 13
price = 8.99
total_cost = quantity * price

# print a summary of this purchase
print("I need " + str(quantity) + " " + product + "(s). ")
print("Total cost: $" + str(total_cost))

# defining two variables on one line - not recommended
a = 5; b = 7

print('-- page 39 math --')
a = 25
b = 4

print(a / b)
print(a // b)
print(a % b)

a = 5
b = 8
c = a + b

# formatted print
print(f"c = {c}")

# compound assignment operator
# c+=a is the same as c = c + a
c += a
print(f"c = {c}")

count = 0
# increment count by 1
count += 1
print(f"count = {count}")


# p. 47 escape sequences
# new line \n
print("This is line 1\nThis is line 2")
print("col1\tcol2\tcol3")
print("The book title is \"Lord of the Rings\".")
print("folder structure is: c:\\repos\\python-for-everyone!")

# implicit line continuation:
print("Name: "+ first_name + "\n" +
      "Age: " + str(43))

print(f"Name: {first_name}\n"
      f"Age: {45}")

# p. 51 sep and end arguments
print("abc",end="")
print("def")

print(1,2,3,4)
print(1,2,3,4, sep="!")

# p.53 input() function
# get user's name from the console
name = input("Enter your name: ")
print(f"You entered: {name}")

# float() and int() functions
price = input("Enter price: ")
price = float(price)
qty = input("Enter quantity: ")
qty = int(qty)

print(f"price * qty = {price * qty}")

age = int(input("What's your age? "))

#round() function
miles_driven = 150
gallons_used = 5.875

mpg = miles_driven / gallons_used
mpg = round(mpg, 2)

print(f"mpg = {mpg}")






