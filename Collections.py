#Lists

#Python has dynamic list types so there can be multiple types of data in a Python list

inventory = ["Sword", "Food", "Boots", "Hearthstone", "Armor", "Bedroll"]
# Lists are dynamic in size, you can add and remove items freely

inventory[0] = "Knife"
# This will modify the list at position 0 and changing the value already there to the new value

print(inventory)
# Expected : ["Knife", "Food", "Boots", "Hearthstone", "Armor", "Bedroll"]

print(len(inventory))
# This will return the length of the given collection - base 1
# Expected : 6

print(max(inventory))
# Knife ?
# Knife has the highest alphabetical value

print(min(inventory))
# Armor ?
# Armor has the lowest aplphabetical value

# Only the first letter is considered for Alphabetic Values

inventory.append("Flint and Tinder")
# Append is a method attached to the list class and has to be called on an instance of list itself
# Append will add a value directly to the end of the list
print(inventory)
# Expected : ["Knife", "Food", "Boots", "Hearthstone", "Armor", "Bedroll", "Flint and Tinder"]

inventory.insert(0, "Sword")
# Insert takes in a location and a value and inserts the value at the location
# this will move everything over so this will not replace any values at the location
#   if the location already has a value
print(inventory)
# Expected : ["Sword", "Knife", "Food", "Boots", "Hearthstone", "Armor", "Bedroll", "Flint and Tinder"] 

inventory.pop()
# Pop removes the last value in the list
print(inventory)
# Expected : ["Sword", "Knife", "Food", "Boots", "Hearthstone", "Armor", "Bedroll"]

inventory.remove("Sword")
# Remove a value from the list, it is not taking in a location
print(inventory)
# Expected : ["Knife", "Food", "Boots", "Hearthstone", "Armor", "Bedroll"]

inventory.clear()
# This will clear the list entirely
# this is the same functionality as list_name = []
print(inventory)
# Expected : []