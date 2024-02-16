#variables just need a name and a value
#types are interpreted
#you CAN explicity make a type if you want

#best practice to use snake_case with variables in Python

#booleans
is_game_over = False
print(is_game_over)
#expected False

is_game_over = True
print(is_game_over)
#expected True

is_game_over = 5 > 6
print(is_game_over)
#expected False

#numerical
num_lives = 5
print(num_lives)
#expected 5

percent_health = 0.5
print(percent_health)
#expected 0.5

#String
#Strings are in-between either '' or ""

player_name = "Nimish"
#just like in other languages, strings are case-sensitive
print(player_name)
#expected Nimish
player_name = 'Mammoth'
print(player_name)
#expected Nimish

print(type(is_game_over))
print(type(num_lives))
print(type(percent_health))
print(type(player_name))

#expected:
#boolean
#integer
#float
#String

#Types are dynamic in Python
num_lives = "5"
print(type(num_lives))
#expected String