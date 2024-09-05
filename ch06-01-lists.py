def main():
    print("Welcome to the Lists App")
    
    # # list of strings - names
    # names = ["Chuck", "Haby", "Tanya", "Kyle", "Claudia", "Nadine",
    #          "Renaldo", "Alyssa", "Myron", "Aruna", "Charlie"]
    
    # loop_thru_names(names)
    # # Lili, John
    # # names[11] = "Lili" -> error, no position 11
    # names.append("Lili")
    # names.append("Sean")
    # names.append("John")
    
    # loop_thru_names(names)
    
    # print(f"Person in 10th index position: {names[10]}")
    
    # # remove "Sean"
    # names.pop(12)
    # print("idx 12 removed")
    # loop_thru_names(names)
    
    # print("insert 'test' in 8th position...")
    # names.insert(8, "Test")
    # loop_thru_names(names)
    
    # print(f"Does 'Tanya' exist in the list? {"Tanya" in names}")
    # print(f"Does 'Sean' exist in the list? {"Sean" in names}")
    
    # numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # # foreach loop
    # for nbr in numbers:
    #     print(nbr)
    
    # # In Python we can create a list of multiple types
    # stuff = [1, "one", 1.1]
    # print(stuff)
    
    # print("--- loop through numbers, multiplying each by 3 ---")
    # for n in numbers:
    #     t = n * 3
    #     print(f"n: {n}, t: {t}")
    
    # print("--- List of toys ---")
    # toys = ["Doll", "choo choo train", "stuffed animal", "bouncy ball"]
    # print("list of toys, starting w/ # 1")
    # for idx in range(len(toys)):
    #     print(f"{idx + 1}: {toys[idx]}")
        
    # print("=== Sort the list of toys, alphabetically ===")
    # toys.sort()
    # print(f"toys: {toys}")
    # print("** Casing matters! Let's fix that...")
    # toys.sort(key=str.lower)
    # print(f"toys sorted again: {toys}")
    
    # numbers = [5, 75, -12, 246, 11, 0]
    # print(f"numbers: {numbers}")
    # print(f"numbers max: {max(numbers)}")
    # print(f"numbers min: {min(numbers)}")
    
    # print("slices...")
    # print(f"numbers[1:4]: {numbers[1:4]}")
    # print(f"numbers[:3]: {numbers[:3]}")
    # print(f"numbers[2:]: {numbers[2:]}")
    
    # print("List comprehension")
    # numbers = [1, 2, 3, 4, 5, 6]
    # print(f"numbers: {numbers}")
    # print("+ new list of even-squares - sqared version of the even #s")
    # # w/ for loop
    # even_squares = []
    # for n in numbers:
    #     if n % 2 == 0:
    #         even_squares.append(n * n)
    # print(f"even_squares: {even_squares}")
    
    # print("do it again w/ list comprehension...")
    # even_squares = [n * n for n in numbers if n % 2 == 0]
    
    print("=== tuples ===")
    print("defining a Movie without a tuple:")
    title = "Star Wars"
    year = 1977
    rating = "PG"
    director = "George Lucas"
    
    print("define a tuple to represent a movie...")
    star_wars_tuple = (title, year, rating, director)
    
    title = "Creed"
    year = 2015
    rating = "PG-13"
    director = "Ryan Coogler"
    run_time = 133
    
    creed_tuple = (title, year, rating, director, run_time)
    
    print(f"star wars tuple: {star_wars_tuple}")
    print(f"creed tuple: {creed_tuple}")
    
    print(f"creed_tuple[2]: {creed_tuple[2]}")
    print(f"creed_tuple title: {creed_tuple[0]}")
    
        
        
    print("Bye")
    
def loop_thru_names(names):    
    # loop through names w/ for in range:
    for i in range(len(names)):
        print(f"name({i}): {names[i]}", end=" ")
    print("\n" + ("+" * 30))
    
if __name__ == "__main__":
    main()