import matplotlib.pylab as plt
import numpy as np
import re
import time
import itertools
import string
import collections
import math
import functools
import copy
import operator
import sys


start_time = time.time()

def num_free_sides(array, index, empty_val = 0):
    x,y,z = index
    difference = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    count = 0
    for i in difference:
        if x+i[0] < 0 or y+i[1] < 0 or z+i[2] < 0:
            continue
        if x+i[0] > 24 or y+i[1] > 24 or z+i[2] > 24:
            continue
        foo = array[x + i[0]][y + i[1]][z + i[2]]
#        print("(%d, %d, %d) " % (x + i[0], y + i[1], z + i[2]),foo)
        if foo == empty_val:
            count = count + 1

    return count

def get_empty_neighbors(array,index):
    x,y,z = index
    difference = [[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]]
    empty_neighbor_list = []
    for i in difference:
        if x+i[0] < 0 or y+i[1] < 0 or z+i[2] < 0:
            continue
        if x+i[0] > 24 or y+i[1] > 24 or z+i[2] > 24:
            continue
        if array[x+i[0]][y+i[1]][z+i[2]] == 0:
            empty_neighbor_list.append([x+i[0],y+i[1],z+i[2]])
    return empty_neighbor_list

    

Pos = collections.namedtuple("Pos", "r c")

getfile = open('c:/users/ted/VSCode/AoC2022/Day18/input.txt', 'r').read().splitlines()

obsidian = np.zeros((25,25,25),dtype = int)


total = 0
for i in getfile:
    x,y,z = [int(x) + 1 for x in list(i.split(","))]
    obsidian[x][y][z] = 1

for i in list(np.transpose(obsidian.nonzero())):
#    print(num_free_sides(obsidian, i))
    total = total + num_free_sides(obsidian, i)
print(total)


queue = [[0,0,0]]
visited = []
while len(queue) != 0:
    visit = queue.pop(0)
    x,y,z = visit
#    print("visit: ", visit)
    obsidian[x][y][z] = 2
    visited.append(visit)
    for j in get_empty_neighbors(obsidian,visit):
        if not j in visited and not j in queue:
            queue.append(j)
#    print(queue)

total = 0
for i in list(np.transpose(np.where(obsidian == 1))):
#    print(num_free_sides(obsidian, i, 2))
    total = total + num_free_sides(obsidian, i, 2)
print(total)




