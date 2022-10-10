# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
goal_0 = 32
player_0 = 'Ruud Gullit'
goal_1 = 54
player_1 = 'Marco van Basten'
scorers = player_0 +' '+ str(goal_0)+', '+player_1+' '+str(goal_1)
report = f'{player_0} scored in the {goal_0}nd minute\n{player_1} scored in the {goal_1}th minute'
player = 'Ronald Koeman'
first_name = player[:player.find(' ')]
last_name = player[player.find(' ')+1:]
last_name_len = len(last_name)
name_short = player[0] +'. '+last_name
chant = (first_name+ '! ')*(len(first_name)-1)+first_name+'!'
good_chant = chant[-1] != ' '

