print("Welcome to the File Reader App!")

# # loop and read each line of a file
# FILE_NAME = './files/names.txt'
# with open(FILE_NAME) as file:
#     for line in file:
#         print(line, end="")
#     print()

# print("read entire names.txt file as a string")
# with open(FILE_NAME) as file:
#     contents = file.read()
#     print(contents)

# print("read entire file as list")
# with open(FILE_NAME) as file:
#     names = file.readlines()
#     for name in names:
#         name = name.replace("\n", "")
#         print(f"name = {name}")

print("\nRead movies file into a list - each movie one long string, tab delimited")
FILE_NAME = "./files/movies.txt"
movies = []
with open(FILE_NAME) as file:
    for line in file:
        line = line.replace("\n", "")
        movies.append(line)    
print(f"movies = {movies}")

print("\nRead movies file into a list - convert each movie string into a Movie tuple")
movies = []
with open(FILE_NAME) as file:
    for line in file:
        line = line.replace("\n", "")
        movie_properties = line.split("\t")
        title = movie_properties[0]
        year = int(movie_properties[1])
        rating = movie_properties[2]
        director = movie_properties[3]
        movie = (title, year, rating, director)
        movies.append(movie)    
print("=== Movie Tuples ===")
for movie in movies:
    print(f"movie = {movie[0]} ({movie[1]}), rated {movie[2]}, directed by {movie[3]}")



print("Bye")