print("Welcome to File Output!")

# outfile = open("test.txt", "w")
# outfile.write("Test")
# outfile.close()

# print("Write file to files folder...")
# outfile = open("./files/test2.txt", "w")
# outfile.write("Another test, in the files folder")
# outfile.close()

# print("Write out some names")
# NAMES_FILE = './files/names.txt'
# with open(NAMES_FILE, "w") as file:
#     file.write("Haby\n")
#     file.write("Aruna\n")
#     file.write("Alyssa\n")
#     file.write("Renaldo\n")

print("Write out some movies")
FILE_NAME = './files/movies.txt'
with open(FILE_NAME, "w") as movies_file:
    # write Star Wars movie
    movies_file.write("Star Wars Episode IV: A New Hope\t")
    movies_file.write("1977\t")
    movies_file.write("PG\t")
    movies_file.write("George Lucas\n")
    # write Creed movie
    movies_file.write("Creed\t2015\tPG-13\tRyan Coogler\n")
    
print("Bye")