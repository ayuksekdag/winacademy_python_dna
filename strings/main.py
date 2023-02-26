# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goal_0 = 32
scorer_name_0 = "Ruud Gullit"
goal_1 = 54
scorer_name_1 = "Marco van Basten"
scorers = f"{scorer_name_0} {goal_0}, {scorer_name_1} {goal_1}"
print(scorers)
report = f"{scorer_name_0} scored in the {goal_0}nd minute\n{scorer_name_1} scored in the {goal_1}th minute"
print(report)

player = "Ruud Gullit"
find_space_index = player.find(" ")
first_name = player[0:find_space_index]
print(first_name)
first_name_len = len(first_name)
print(first_name_len)
last_name = player[find_space_index + 1:]
print(last_name)
last_name_len = len(last_name)
print(last_name_len)
name_short = player[0] + ". " + last_name
print(name_short)

chant = ""
for i in range(first_name_len):
    if i == 0:
        chant = chant + first_name + "!"
    else:
        chant = chant + " " + first_name + "!"
print(chant)

good_chant = chant[-1] != ' '
