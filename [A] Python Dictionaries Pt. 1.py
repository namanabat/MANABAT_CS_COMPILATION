# Creating a profile for a superhero
hero = {
   "name" : "Iron Man",
   "power_level" : 9000,
   "has_suit" : True
}

# print(hero)

# Alternatively, you can use the dict() constructor
villain = dict(name = "Thanos", power_level = 18000, has_suit = False)
print(villain)

# Creating empty dictionaries
# hero = { }
# hero = dict()

# Accessing items
# Option 1: Using square brackets
print(hero["name"])

# Option 2: get() method
# Prevents an error if the key does not exist
print(hero.get("name"))

# Changing an existing value
hero["power_level"] = 9500 # He leveled up

# Adding a new key-value pair
hero["color"] = "Red" # New key value pair added
# print(hero)

# Remove Items
# Option 1: del keyword
del hero["color"]
# print(hero)

# Option 2: pop() method
hero.pop("has_suit")
# print(hero)

# Option 3: popitem() method
# popitem() removes the last inserted item
hero.popitem()
# print(hero)

# To clear the whole dictionary
hero.clear()

# keys() return a list of all the keys in the dictionary
print(villain.keys())

# values() return a list of all the values in the dictionary
print(villain.values())

# items() return each item in the dictionary, as tuples in a list
print(villain.items())
