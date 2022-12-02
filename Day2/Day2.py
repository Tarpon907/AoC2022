from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string


start_time = time.time()

cheatsheet = open('c:/users/ted/VSCode/AoC2022/Day2/input.txt', 'r').read().split("\n")

score = 0
for line in cheatsheet:
    if len(line) < 2:
        continue
    win = False
    tie = False
    opp_play = line[0]
    my_play = line[2]
    opp_index = string.ascii_uppercase.index(opp_play) - string.ascii_uppercase.index('A')
    my_play_index = string.ascii_uppercase.index(my_play) - string.ascii_uppercase.index('X')
    winner_index = (opp_index + 1) % 3
    loser_index = (opp_index - 1) % 3
    tie_index = (opp_index)

    my_play_value = my_play_index + 1

    if my_play_index == tie_index:
        roundscore = my_play_value + 3
    elif my_play_index == winner_index:
        roundscore = my_play_value + 6
    else:
        roundscore = my_play_value

    score = score + roundscore
#    print(opp_play, my_play, "(", my_play_value, "+",
#          roundscore-my_play_value, ")", roundscore, score)

print(score)
       
print("execution time (in ms): ",(time.time()-start_time)*1000) 