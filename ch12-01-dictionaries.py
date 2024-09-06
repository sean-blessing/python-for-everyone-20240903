print("Welcome to the Dictionaries App!")

us_states = {
    "OH": "Ohio",
    "IN": "Indiana",
    "VA": "Virginia",
    "TX": "Texas",
    "CO": "Colorado"
}

print(f"us_states dictionary = {us_states}")

print("getting values out of the dictionary:")
state_abv = input("State (abbreviation)? ")
if state_abv in us_states:
    print(f"state ({state_abv}): {us_states[state_abv]}")
else:
    print(f"{state_abv} does not exist!")

print("Add an entry to the dictionary:")
us_states["AK"] = "Alaska"

print(f"us_states: {us_states}")

print("using the get method to retrieve a value: ")
print(f"CO: {us_states.get("CO")}")

print("Delete an entry from the dictionary:")
state_deleted = us_states.pop("CO")
print(f"CO removed: {us_states}")

print("="*20)
print("keys, items, values")
print(f"keys: {us_states.keys()}")
print(f"values: {us_states.values()}")
print(f"items: {us_states.items()}")

print("unpacking a tuple as it loops through all keys/values")
for abbv, name in us_states.items():
    print(f"{abbv}: {name}")
    
print("sorted - unpacking a tuple as it loops through all keys/values")
for abbv, name in sorted(us_states.items()):
    print(f"{abbv}: {name}")
print("Bye")