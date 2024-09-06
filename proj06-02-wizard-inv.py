from console import validate_int_within_range, validate_menu_option

# global variables
items = ["wooden staff", "wizard hat", "cloth shoes"]

def main():
    print("Welcome to the Wizard Inventory App!")
    
    commands = ["show", "grab", "edit", "drop", "exit"]
    
    command = ""
    while command != "exit":
        display_menu()
        command = validate_menu_option("Command: ", commands)
        
        if command == "show":
            show_items()
        elif command == "grab":
            grab_item()
        elif command == "edit":
            edit_item()
        elif command == "drop":
            drop_item()
    print("Bye")

def show_items():
    print("\nShow All Items")
    for item_nbr in range(len(items)):
        print(f"{item_nbr + 1}. {items[item_nbr]}")
    
def grab_item():
    # * limit to 4 items total
    print("\nGrab/Add an Item")
    if len(items) >= 4:
        print("Too many items. Please drop one first.")
    else:
        new_item_name = input("Name: ")
        items.append(new_item_name)
        print(f"{new_item_name} was added.")
    
def edit_item():
    # prompt for 'item_nbr' and 'updated_name', update item
    print("\nEdit an Item")
    item_nbr = validate_int_within_range("Item Number: ", 1, len(items))
    updated_name = input("Updated Name: ")
    items[item_nbr - 1] = updated_name
    print(f"Item number {item_nbr} was updated.")
    
def drop_item():
    # prompt for 'item_nbr' and remove item
    print("\nDrop/Remove an Item")
    if len(items) == 0:
        print("No items in inventory. Please grab one first")
    else:
        item_nbr = validate_int_within_range("Item Number: ", 1, len(items))
        deleted_item = items.pop(item_nbr - 1)
        print(f"{deleted_item} was removed.")

def display_menu():
    print("\nCOMMAND MENU:")
    print("show - show all items")
    print("grab - add an item")
    print("edit - edit an item")
    print("drop - remove an item")
    print("exit - exit program\n")
    
if __name__ == "__main__":
    main()