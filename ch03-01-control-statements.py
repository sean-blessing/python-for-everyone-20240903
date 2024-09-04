# p. 67 boolean expressions

# light_color = input("What's the stoplight color? ").lower()

# print(f"red? {light_color == 'red'}")
# print(f"yellow? {light_color == 'yellow'}")
# print(f"green? {light_color == 'green'}")

# if light_color == "red":
#     print(f"Light color is red - stop!")
# elif light_color == "yellow":
#     print("Light color is yellow - slow down!")
# elif light_color == "green":
#     print("Light color is green - go!")
# else:
#     print("Invalid light color")

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
# age = 37
# city = "Chicago"

# # over 35 and living in Chicago?
# if age >= 35 and city == "Chicago":
#     print("Yep, over 35 in Chi-town")
    
# # under 30 or living in Chicago?
# if age < 30 or city == "Chicago":
#     print("under thirty or chicago")
    
# p. 75 convert numeric to letter grade
# numeric_grade = int(input("Enter numeric grade: "))

# # convert to letter grade on the following scale:
# # A >= 90, B >= 80, C >= 70, D >= 60, F below 60
# # assume 0 <= numeric_grade <= 100
# letter_grade = "F"
# if numeric_grade >= 90:
#     letter_grade = "A"
# elif numeric_grade >= 80:
#     letter_grade = "B"
# elif numeric_grade >= 70:
#     letter_grade = "C"
# elif numeric_grade >= 60:
#     letter_grade = "D"

# print(f"numeric: {numeric_grade}, letter: {letter_grade}")

# combine an AND and OR in one IF statement
# Determine a discount based on:
# 1) Customer type: Retail (R) or Corporate (C)
#    - C: 5%
#    - R: 0%
# 2) Invoice Total - Retail customers
#    - 500: 2%
#    - 1500: 4%
# customer_type = input("Customer Type (C/R): ").lower()
# invoice_total = float(input("Invoice Total? "))

# if customer_type == "c":
#     discount_pct = .05
# elif customer_type == "r":
#     if invoice_total >= 1500:
#         discount_pct = .04
#     elif invoice_total >= 500:
#         discount_pct = .02
#     else:
#         discount_pct = 0.0
    
# if invoice_total >= 500 and invoice_total < 1500:
#     discount_pct = .02
# elif invoice_total >= 1500:
#     discount_pct = .04
# else :
#     discount_pct = 0.0
    

# Simplified discount %
# if a customer is C OR if invoice total >= 1000, offer a 5% discount
# discount_pct = 0.0
# if customer_type == 'C' or invoice_total >= 1000:
#     discount_pct = .05

# another discount scenario
# if a customer is C OR (if invoice total >= 1000 AND customer is R), 5% discount

# choice = "y"

# while loop ends if customer type is anything other than 'c' or 'r'
# customer_type = 'r'

# #while customer_type == 'r' or customer_type == 'c':
# while True:
#     customer_type = input("Customer Type (C/R): ").lower()
#     if customer_type != 'r' and customer_type != 'c':
#         # end the loop
#         break
#     else:
#         invoice_total = float(input("Invoice Total? "))
#         discount_pct = 0.0
#         if customer_type == 'c' or (invoice_total >= 1000 and customer_type == 'r'):
#             discount_pct = .05

#         print(f"customer_type: {customer_type}")
#         print(f"invoice_total: {invoice_total}")
#         print(f"discount_pct:  {discount_pct}")
#         #choice = input("Continue (y/n)? ").lower()


# tomorrow (Weds) - add while loop to test this further
# p. 85 while loop
# while choice == "y"

# print("Testing a while loop...")
# choice = "y"

# while choice == "y":
#     print("In the while loop...")
#     choice = input("Continue (y/n)? ").lower()


# while True

# p. 87 - for loop in range
# range demos
# print(f"range(5): {range(5)}")
# for i in range(5):
#     print(i, end=" ")
# print("\n================")
# print(f"range(1,5): {range(1,5)}")
# for i in range(1,5):
#     print(i, end=" ")
# print("\n================")
# print(f"range(1,7): {range(1,7)}")
# for i in range(1,7):
#     print(i, end=" ")
# print("\n================")
# # 0 to 20, even numbers
# print(f"range(0,21,2): {range(0,21,2)}")
# for i in range(0,21,2):
#     print(i, end=" ")
# print("\n================")
# # 50 to 0, by 5
# print(f"range(50,-1,-5): {range(50,-1,-5)}")
# for i in range(50,-1,-5):
#     print(i, end=" ")
# print("\n================")

# # 0 to 20, but calculate a sum along the way
# sum = 0
# print(f"range(0,21): {range(0, 21)}")
# for i in range(0,21):
#     sum += i
#     print(f"i={i} sum={sum}")
# print("\n================")

# p. 89 - break/ continue

# p. 93 - walrus operator - new to me!
# an infinite while loop to process user data
# print("Enter -1 to quit.")
# print("-----------------")
# while True:
#     score = input("Enter score: ")
#     if score == "-1":
#         break
#     print(f"You entered: {score}")
# print("Bye")

# same thing w/ walrus operator
print("Enter -1 to quit.")
print("-----------------")
while (score := input("Enter score: ")) != "-1":
    print(f"You entered: {score}")
print("Bye")
