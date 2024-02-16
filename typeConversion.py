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