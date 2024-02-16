is_game_over = False
num_lives = 5
percent_health = 0.5
player_name = 'Mammoth'

#Arithmatic Operators
health = 50
health = health + 20
new_health = health + 20
#one is modifying the base value of health and assigning it ot 70
#the other is storing the result in a new variable

xPos = 5
print(xPos % 2)
print(xPos // 2)
# % will return the remainder
# // will discard the remainder
print(xPos ** 2)
# ** is an exponent
print(xPos)

#expected
#1
#2
#25
#5

first_name = "Alex"
last_name = "Erdenberger"
full_name = last_name + " " + first_name
print(full_name)
#expected Erdenberger Alex   


#Assignment Operators

health = 50
health += 20
# exactly the same as: health = health + 20
health -= 50
# exactly the same as: health = health - 50
# assignment operators can be combined with any of the arithmatic operators

name = "Alex"
name += " Erdenberger"
print(name)

# subtracting strings doesn't really makes sense
# not a lot of the other arithmatic operators works with strings

# Comparison Operators
# > >= < <= == !=
# return true or false based on the comparison
# values that are compared will remain unchanged
result = 5 > 2
print(result)
print(type(result))
# expected
# true
# bool
print(5 == 2)
print(5 != health)
# expected
# false
# true

# Doubles and Floats should be able to be compared freely
print(5.0 == 5)
# expected : True

print(True == False)
# expected : false

print(first_name == last_name)
# expected : false

print("a" == "A")
# expected : false
# Strings are case sensitive so although both have the letter "A" their both different characters

print("a" > "b")
# expected : false
# Python can compare the greater than and less than between letters
# The comparison is based off of position in the alphabet
# a is at position 0, b is at position 1, 1 > 0, so therefore, a is not greater than b, false

print(5 > False)
# Expected : true
# False and True have numeric values
# Stated before : False = 0 and True = 1

print(5 > True)
# Expected: True
# This gets a little weird because anything greater than 0 evaluates to true
# Python seems to be resolving this statement from left to right
# Converting the True into an integer to comare to the integer on the left half of the statement
# True = 1, 5 > 1, therefore True

# Logical Operators
# not and or
# not - reverses a boolean value
# or - either side needs to be true for a true statement
# and - both sides need to be true for a true statement

is_game_over = False
is_game_over = not is_game_over
print(is_game_over)
# Expected : True (not False -> True)
health = 0
lives = 0
print(health <= 0 and lives <= 0)
# Expected : True
# health = 0, 0 <= 0, True. lives = 0, 0 <= 0, True. True and True. True
lives = 1
print(health <= 0 and lives <= 0)
# Expected : False
print(health <= 0 or lives <= 0)
# Expected : True