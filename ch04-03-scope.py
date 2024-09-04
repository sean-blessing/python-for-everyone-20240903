def define_variables():
    # a and b are local to this function
    a = 5
    b = 6
    print(f"In define_variables function")
    print(f"a = {a}")
    print(f"b = {b}")

c = 7
d = 8

print(f"c = {c}")
print(f"d = {d}")

# print(f"a = {a}") - no access to 'a'

def new_function():
    print("In new_function")

    print(f"c = {c}")
    print(f"d = {d}")

def main():
    # don't do this!
    global d
    d = "abc" # overwrites previous definition 

# constant
MONTHS_IN_YEAR = 12

main()