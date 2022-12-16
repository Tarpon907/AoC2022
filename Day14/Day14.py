import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string
import collections
import math
import functools

getfile = open('c:/users/ted/VSCode/AoC2022/Day14/input.txt', 'r').read().splitlines()

cave = np.zeros((1000,300),dtype=int)

highest_y = 0
for line in getfile:
    coords = re.findall("(\d+),(\d+)",line)
    for i in range(len(coords) - 1):
        start, end = coords[i], coords[i+1]
        if start[0] == end[0]:
            x = int(start[0])
            y_start = int(start[1])
            y_end = int(end[1])
            if y_end < y_start:
                y_end, y_start = y_start, y_end
            highest_y = max(highest_y,y_end)
            for y in range(y_start,y_end+1):
                print(x,y)
                cave[x][y] = 2
        else:
            y = int(start[1])
            highest_y = max(highest_y,y)
            x_start = int(start[0])
            x_end = int(end[0])
            if x_end < x_start:
                x_end, x_start = x_start, x_end
            for x in range(x_start,x_end+1):
                cave[x][y] = 2

print(highest_y)
for x in range(1000):
    cave[x][highest_y + 2] = 3

def print_cave():

    for y in range(0,15):
        for x in range(480,520):
            print(cave[x][y],end="")
        print("")
    print("")

abyss = False
plugged = False
grains = 0
while not abyss and not plugged:
#    print_cave()
    grains = grains + 1
    x = 500
    y = 0
    stopped = False
    while not stopped and not abyss and not plugged:
        if cave[x][y+1] == 0:
            y = y + 1
            continue
        if cave[x-1][y+1] == 0:
            y = y + 1
            x = x - 1
            continue
        if cave[x+1][y+1] == 0:
            y = y + 1
            x = x + 1
            continue
        cave[x][y] = 1
        if cave[500][0] != 0:
            plugged = True

        stopped = True

print(grains)

    





