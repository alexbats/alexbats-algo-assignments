# python plan_matches.py graph_file

import sys

input_file = sys.argv[1]
valid_day_to_play = dict()
matches_array = []
try:
    input_file = open(input_file, 'r')
    for line_str in input_file:
        line_str = line_str.strip()
        players = line_str.split()
        matches_array.append([players[0], players[1], -1])
        valid_day_to_play[players[0]] = -1
        valid_day_to_play[players[1]] = -1

except IOError:
    print("The input file doesn't exist.")
    sys.exit(1)

input_file.close()

for match in matches_array:

    if match[0] > match[1]:
        temp = match[0]
        match[0] = match[1]
        match[1] = temp

matches_planed = False
day_to_play = 0
while not matches_planed:

    for match in matches_array:
        player1_valid_day_to_play = valid_day_to_play[match[0]]
        player2_valid_day_to_play = valid_day_to_play[match[1]]
        max_day_to_play = max(player1_valid_day_to_play, player2_valid_day_to_play)
        if max_day_to_play < day_to_play and match[2] == -1:
            valid_day_to_play[match[0]] = day_to_play
            valid_day_to_play[match[1]] = day_to_play
            match[2] = day_to_play

    matches_planed = True
    for match in matches_array:
        if match[2] == -1:
            matches_planed = False
            break

    day_to_play += 1

matches_array.sort(key=lambda x: (x[0], x[1]))

for match in matches_array:
    print "(" + match[0] + ", " + match[1] + ") " + str(match[2])