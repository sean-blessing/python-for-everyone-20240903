# p. 67 boolean expressions

light_color = input("What's the stoplight color? ").lower()

print(f"red? {light_color == 'red'}")
print(f"yellow? {light_color == 'yellow'}")
print(f"green? {light_color == 'green'}")

if light_color == "red":
    print(f"Light color is red - stop!")
elif light_color == "yellow":
    print("Light color is yellow - slow down!")
elif light_color == "green":
    print("Light color is green - go!")
else:
    print("Invalid light color")

# number = int(input("Enter a whole number: "))
# print(f"{number} % 2 == 0? {number % 2 == 0}")
# # even number? An even number has no remainder when divided by 2
# if number % 2 == 0:
#     print("Even Number!")
# else:
#     print("Odd Number!")
  
# p. 69 Logical Operators
# AND, OR, NOT
# example from book
age = 37
city = "Chicago"

# over 35 and living in Chicago?
if age >= 35 and city == "Chicago":
    print("Yep, over 35 in Chi-town")
    
# under 30 or living in Chicago?
if age < 30 or city == "Chicago":
    print("under thirty or chicago")
    
# p. 75 convert numeric to letter grade
numeric_grade = int(input("Enter numeric grade: "))

# convert to letter grade on the following scale:
# A >= 90, B >= 80, C >= 70, D >= 60, F below 60
# assume 0 <= numeric_grade <= 100
letter_grade = "F"
if numeric_grade >= 90:
    letter_grade = "A"
elif numeric_grade >= 80:
    letter_grade = "B"
elif numeric_grade >= 70:
    letter_grade = "C"
elif numeric_grade >= 60:
    letter_grade = "D"

print(f"numeric: {numeric_grade}, letter: {letter_grade}")

# tomorrow (Weds) - add while loop to test this further