import csv

print("Welcome to CSV Files App!")

FILE_NAME = './files/movies.csv'
with open(FILE_NAME, newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        print(f"{row[0]}, {row[1]}")

# writing to a CSV... actors(firstName, lastName, birthDate)
# Marlon Brando (4/3/24), Hugh Jackman (10/12/68), Harrison Ford (7/13/42), Salma Hayek (9/2/66), Emma Watson (4/15/90),
# Samuel L. Jackson 12/21/48
# a 2 dimensional List (List of Lists) of actor info

actors = [
    ["Marlon", "Brando", 1924],
    ["Hugh", "Jackman", 1968],
    ["Harrison", "Ford", 1942],
    ["Samuel L", "Jackson", 1948],
    ["Salma", "Hayek", 1966],
    ["Emma", "Watson", 1990]
]

# write actors to a csv
with open("./files/actors.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(actors)








print("Bye")