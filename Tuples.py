# Tuples are immutable
# "They are data stored for one time use"

# Tuples are great places to store multiple types of data
item = ("Health Kit", 4)
name = item[0]
quantity = item[1]
print(name)
print(quantity)

# item[1] = 10
# expected : error
# Tuples are immutable and cannot be changed

item = ("Knife", 1)
# We're not modifying the Item tuple, instead we are reassigning the item variable to a different Tuple

print(item.count("Knife"))
# expected : 1

print(item.index(1))
# expected : 1
# A little confusing in this context: we're looking for the value not the thing at location 1

print(len(item))
# print(max(item))
# print(min(item))
# These are all valid methods to call on Tuples, however for this context min and max will not work
#       Because we are comparing an int to a str
