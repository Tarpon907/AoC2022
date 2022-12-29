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


getfile = open('c:/users/ted/VSCode/AoC2022/Day9/input1.txt', 'r').read().splitlines()


tail_x = 0
tail_y = 0
head_x = 0
head_y = 0

visited_coords = dict()
visited_coords[tail_x,tail_y] = 1

print(visited_coords)

for line in getfile:
    y_change = 0
    x_change = 0
    direction, count = line.split(" ")
    if direction == "U":
        y_change = -1
    elif direction == "D":
        y_change = 1
    elif direction == "L":
        x_change = -1
    else:
        x_change = 1

    i = 0
    while i < int(count):
        head_x = head_x + x_change
        head_y = head_y + y_change
        if abs(head_x - tail_x) > 1:
            if head_x - tail_x == 2:
                tail_x = head_x - 1
            else:
                tail_x = head_x + 1
            if tail_y != head_y:
                tail_y = head_y
        elif abs(head_y - tail_y) > 1:
            if head_y - tail_y == 2:
                tail_y = head_y - 1
            else:
                tail_y = head_y + 1
            if tail_x != head_x:
                tail_x = head_x
        visited_coords[tail_x,tail_y] = 1
        i = i + 1

    
print(len(visited_coords.keys()))

       


print("execution time (in ms): ",(time.time()-start_time)*1000) 
