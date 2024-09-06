from actor import Actor

def main():
    print("Welcome to the classes app!")
    
    actor1 = Actor("Marlon", "Brando", 1924)
    actor2 = Actor("Hugh", "Jackman", 1968)
    actor3 = Actor("Emma", "Watson", 1990)
    
    print(f"actor1: {actor1}")
    
    actors = [actor1, actor2, actor3]
    
    print(f"actor1 firstName: {actor1.firstName}")
    
    for actor in actors:
        print(actor.getDetails())
    

    print("Bye")

if __name__ == "__main__":
    main()