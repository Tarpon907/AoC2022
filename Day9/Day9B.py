from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string
import collections

Point = collections.namedtuple("Point", "x y")

start_time = time.time()

ROPE_LENGTH = 10

getfile = open('c:/users/ted/VSCode/AoC2022/Day9/input1.txt', 'r').read().splitlines()


section_x = [0] * ROPE_LENGTH
section_y = [0] * ROPE_LENGTH

visited_coords = dict()
visited_coords[section_x[ROPE_LENGTH-1],section_y[ROPE_LENGTH-1]] = 1

def move_head(direction : str):
#    print("move head:", direction)
    global section_x, section_y

    if direction == "U":
        section_y[0] = section_y[0] - 1
    elif direction == "D":
        section_y[0] = section_y[0] + 1
    elif direction == "R":
        section_x[0] = section_x[0] + 1
    else:
        section_x[0] = section_x[0] - 1


def move_next_knot(index : int = 1):
    global section_x, section_y, ROPE_LENGTH
    if index == ROPE_LENGTH:
        return

    prev_index = index - 1
    if abs(section_x[index] - section_x[prev_index]) > 1:
        if section_x[prev_index] - section_x[index] > 1:
            section_x[index] = section_x[prev_index] - 1
        else:
            section_x[index] = section_x[prev_index] + 1

        if section_y[index] > section_y[prev_index]:
            section_y[index] = section_y[index] - 1
        elif section_y[index] < section_y[prev_index]:
            section_y[index] = section_y[index] + 1
    
    if abs(section_y[index] - section_y[prev_index]) > 1:
        if section_y[prev_index] - section_y[index] > 1:
            section_y[index] = section_y[prev_index] - 1
        else:
            section_y[index] = section_y[prev_index] + 1

        if section_x[index] > section_x[prev_index]:
            section_x[index] = section_x[index] - 1
        elif section_x[index] < section_x[prev_index]:
            section_x[index] = section_x[index] + 1

    move_next_knot(index+1)



for line in getfile:
    y_change = 0
    x_change = 0
    direction, count = line.split(" ")

    i = 0
    while i < int(count):
        move_head(direction)
        move_next_knot()
        i = i + 1
        visited_coords[section_x[ROPE_LENGTH - 1],section_y[ROPE_LENGTH - 1]] = 1
#    for j in range(ROPE_LENGTH):
#        print(j,": (",section_x[j],section_y[j],")")



#print(visited_coords.keys())
print(len(visited_coords.keys()))

       


print("execution time (in ms): ",(time.time()-start_time)*1000) 
