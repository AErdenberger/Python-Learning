is_game_over = False
num_lives = 5
percent_health = 0.5
player_name = 'Mammoth'

#str() takes the value stored in whatever is passed in and converts it into a string
#anything can be converted into a string
str_num_lives = str(num_lives)
print(type(str_num_lives))
print(type(num_lives))
#expected:
#String
#Integer

#0 is considered a false
#1 is considered a true
#basically anything else when convereted to a boolean is true as well
print(bool(0))
print(bool(1))
print(bool(2))
print(bool(0.1))
print(bool(player_name))
#expected
#False
#True
#True
#True
#True

#When converting to an integer SOME things are allowed, others aren't
#print(int("fdsadfasdf"))
#expected error
print(int("56"))
#expected 56
print(int(0.5))
#expected 0
#Python just 'chops off' the decimal
print(int(False))
print(int(True))
#expected
#0
#1
#the reverse of converting 0 and 1 into booleans

#floats work similarly with restrictions to integers
print(float("1"))
print(float(0.5))
print(float(False))
print(float(True))
#expected
#1.0
#0.5
#0.0
#1.0