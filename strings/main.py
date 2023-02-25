# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

goal_0 = 32
scorer_name0 = "Ruud Gullit"
goal_1 = 54
scorer_name1 = "Marco van Basten"
scorers = scorer_name0 + " " + str(goal_0) + ", " + scorer_name1 + " " + str(
    goal_1)
report = f"{scorer_name0}" + " scored in the " + f"{goal_0}nd minute "
report = report + f"{scorer_name1}" + " scored in the " + f"{goal_1}th minute"
print(report)

player = "Ruud Gullit"
first_name = player[player.find("Ruud"):player.find(" Gullit")]
print(first_name)
last_name_len = player.find(player[-1]) - player.find("Gullit") + 1
print(last_name_len)
name_short = player[0] + "."
print(name_short)
first_name_len = len(first_name)

chant = ""
for i in range(first_name_len):
    chant = chant + first_name + "!"

good_chant = chant[-1] != ' '
