inventory = {"Knife":1, "Health Kit": 3, "Wood": 5}
# Key : Value pairs are seperated by a colon
# In a dictionary, the key and value pairs are the elements in the dictionary
# the values in this case are the integers
# the keys are how we access those values and in this case are Strings

print(inventory["Knife"])
# in this case we are grabbing the value associated with the key "Knife"
# expected : 1

inventory["Gold"] = 50
# This will create a new key:value pair in the dictionary and
#       "insert it at the end" (order doesn't matter in dictionaries)

print(inventory)
# expected:
# {"Knife":1, "Health Kit":1, "Wood":5, "Gold":50}

print(inventory.get("Silver"))
# expected : none
# This is preferable to just explicitly calling inventory[KEY_THAT_DOES_NOT_EXIST] because this method
#       will return an error


inventory.keys()
inventory.values()
# These return ITERABLE structures of keys or values
# Iterables ACT like lists but AREN'T LISTS you'll have to convert them

inventory.pop("Knife")
# This will removethe key AND the value

print(len(inventory))
print(min(inventory))
print(max(inventory))

# length is number of pairs
# min and max returns keys not values (that's weird.)