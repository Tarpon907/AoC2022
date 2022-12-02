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

scores = []
#print(cheatsheet)

perm = permutations(["A","B","C"])

score = 0
for line in cheatsheet:
    if len(line) < 2:
        continue

    opp_play = line[0]
    opp_index = string.ascii_uppercase.index(opp_play) - string.ascii_uppercase.index('A')
    result = line[2]

    result_score = 0
    if result == 'Y':
        my_index = opp_index
        result_score = 3
    elif result == 'X':
        my_index = (opp_index - 1) % 3
    elif result == 'Z':
        my_index = (opp_index + 1) % 3
        result_score = 6
    my_play_value = my_index + 1

    roundscore = my_play_value + result_score


    score = score + roundscore
#    print(opp_index ,my_index,"(",my_play_value,"+",roundscore-my_play_value,")",roundscore,score)


print(score)
        
print("execution time (in ms): ",(time.time()-start_time)*1000) 