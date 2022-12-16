from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string
import collections

start_time = time.time()

ROPE_LENGTH = 10

getfile = open('c:/users/ted/VSCode/AoC2022/Day9/input1.txt', 'r').read().splitlines()

knot = dict(x=[0]*ROPE_LENGTH, y=[0]*ROPE_LENGTH)

visited_coords = dict()
visited_coords[knot['x'][ROPE_LENGTH-1],knot['y'][ROPE_LENGTH-1]] = 1

def move_head(direction : str):
    global knot

    if direction == "U":
        knot['y'][0] = knot['y'][0] - 1
    elif direction == "D":
        knot['y'][0] = knot['y'][0] + 1
    elif direction == "R":
        knot['x'][0] = knot['x'][0] + 1
    else:
        knot['x'][0] = knot['x'][0] - 1


def move_next_knot(index : int = 1):
    global knot, ROPE_LENGTH
    if index == ROPE_LENGTH:
        return

    prev_index = index - 1
    if abs(knot['x'][index] - knot['x'][prev_index]) > 1:
        if knot['x'][prev_index] - knot['x'][index] > 1:
            knot['x'][index] = knot['x'][prev_index] - 1
        else:
            knot['x'][index] = knot['x'][prev_index] + 1

        if knot['y'][index] > knot['y'][prev_index]:
            knot['y'][index] = knot['y'][index] - 1
        elif knot['y'][index] < knot['y'][prev_index]:
            knot['y'][index] = knot['y'][index] + 1
    
    if abs(knot['y'][index] - knot['y'][prev_index]) > 1:
        if knot['y'][prev_index] - knot['y'][index] > 1:
            knot['y'][index] = knot['y'][prev_index] - 1
        else:
            knot['y'][index] = knot['y'][prev_index] + 1

        if knot['x'][index] > knot['x'][prev_index]:
            knot['x'][index] = knot['x'][index] - 1
        elif knot['x'][index] < knot['x'][prev_index]:
            knot['x'][index] = knot['x'][index] + 1

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
        visited_coords[knot['x'][ROPE_LENGTH - 1],knot['y'][ROPE_LENGTH - 1]] = 1


print(len(visited_coords.keys()))

       


print("execution time (in ms): ",(time.time()-start_time)*1000) 
