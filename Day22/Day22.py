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



Pos = collections.namedtuple("Pos", "r c f h")

start_time = time.time()
heading = 1

SIDE_SIZE = 50

    
map, directions = open('c:/users/ted/VSCode/AoC2022/Day22/input.txt', 'r').read().split("\n\n")

#print(map)
#print(directions)

map = map.splitlines()

height = len(map)
width = len(map[2])

if width < 50:
    SIDE_SIZE = 4

for i in range(height):
    map[i] = map[i].ljust(width," ")
    print(map[i] + "|")

print(height,width)

part1 = False

start = map[0].index(".")
print(start)

position = Pos(0, start, 1, 0)

def change_heading(p : Pos, change):
    heading = p.h
    if change == "L":
        heading = (heading - 1) % 4
    elif change == "R":
        heading = (heading + 1) % 4
    return Pos(p.r, p.c, p.f, heading)  

def handle_flat_void(r, c, h):
    poschange = [[0,1],[1,0],[0,-1],[-1,0]]
#    print("void")

    diff = poschange[h]
    while map[r][c] == " ":
        r, c = (r + diff[0]) % height, (c + diff[1]) % width
    return r,c


#   1 2
#   3
# 5 4
# 6

# 1L = 5L x 
# 5L = 1L x
# 1U = 6L x
# 6L = 1U x
# 2U = 6D x
# 6D = 2U x
# 2R = 4R
# 4R = 2R 
# 2D = 3R x
# 3R = 2D x
# 4D = 6R x
# 6R = 4D x
# 5U = 3L x
# 3L = 5U x



examined = {}


def handle_cube_void(r, c, h):



    not_examined = False


    new_r, new_c, new_h = r, c, h

    r_div, r_mod = divmod(r, SIDE_SIZE)
    c_div, c_mod = divmod(c, SIDE_SIZE)
    str1 = str(r_div) + "," + str(c_div) + "," + str(h)
    if str1 not in list(examined.keys()):
        not_examined = True
        print("Tipping over edge from (%d, %d) %d" % (r, c, h))
        print("row_div_mod: (%d, %d)   col_div_mod: (%d, %d)" % (r_div, r_mod, c_div, c_mod))
    if [r_div, c_div] in [[0,2],[2,1]] and h == 1:  # down from 2 or 4
        new_c = c_div * SIDE_SIZE - 1
        new_r = c_mod + (r_div + 1) * SIDE_SIZE
        new_h = 2
    elif [r_div, c_div] in [[1,1],[3,0]] and h == 0:  # right from 3 or 6
        new_c = r_mod + (c_div + 1) * SIDE_SIZE
        new_r = r_div * SIDE_SIZE - 1
        new_h = 3
    elif [r_div, c_div] in [[2,0]] and h == 3:  # up from 5
        new_c = (c_div + 1) * SIDE_SIZE
        new_r = (r_div - 1) * SIDE_SIZE + c_mod
        new_h = 0
    elif [r_div, c_div] in [[1,1]] and h == 2:   # Left from 3
        new_r = (r_div + 1) * SIDE_SIZE
        new_c = r_mod
        new_h = 1
    elif [r_div, c_div] in [[0,1]] and h == 2:  # Left from 1
        new_c = 0
        new_r = 3 * SIDE_SIZE - 1 - r_mod
        new_h = 0
    elif [r_div, c_div] in [[2,0]] and h == 2:  # Left from 5
        new_c = SIDE_SIZE
        new_r = SIDE_SIZE - 1 - r_mod
        new_h = 0
    elif [r_div, c_div] in [[0,1]] and h == 3:  # Up from 1  (to 6L)
        new_c = 0
        new_r = c_mod + SIDE_SIZE * 3
        new_h = 0
    elif [r_div, c_div] in [[3,0]] and h == 2 : # Left from 6 to 1U
        new_r = 0
        new_c = r_mod + SIDE_SIZE
        new_h = 1
    elif [r_div, c_div] in [[0,2]] and h == 3: # Up from 2 (to 6D)
        new_r = SIDE_SIZE * 4 - 1
        new_c = c_mod
        new_h = h
    elif [r_div, c_div] in [[3,0]] and h == 1:  # Down from 6 (to 2U)
        new_r = 0
        new_c = c_mod + SIDE_SIZE * 2
        new_h = h
    elif [r_div, c_div] in [[0,2]] and h == 0: # Right from 2 to Right 4
        new_c = SIDE_SIZE * 2 - 1
        new_r = SIDE_SIZE * 3 - 1 - r_mod
        new_h = 2
    elif [r_div, c_div] in [[2,1]] and h == 0: # Right from 4 to Right 2
        new_c = SIDE_SIZE * 3 - 1
        new_r = SIDE_SIZE - 1 - r_mod
        new_h = 2

    if not_examined:
        print("New position (%d, %d) %d" % (new_r, new_c, new_h))
        examined[str1] = True



    return new_r, new_c, new_h, not_examined
    

def print_map():
    cnt = 0
    for x in map:
        print(x)   


def change_position(p, steps):
    need_to_print = False
    print("change position:",p,steps)
    poschange = [[0,1],[1,0],[0,-1],[-1,0]]
    indicators = ">v<^"
    steps = int(steps)
    diff = poschange[p.h]
#    print(diff)
    r, c, f, h = p
    new_h = h
    for x in range(steps):
        new_r = (r + diff[0]) % height
        new_c = (c + diff[1]) % width
#        print(new_c)
#        print(map[new_r])
        tipped = False
        if map[new_r][new_c] == " ":
            if part1:
                new_r, new_c = handle_flat_void(new_r, new_c, h)
                new_h = h
            else:
                print(" about to tip (%d, %d) %d" % (r, c, h))
                print(" because %s at (%d, %d)" % (map[new_r][new_c], new_r, new_c))
                new_r, new_c, new_h, need_to_print = handle_cube_void(r, c, h)
                diff = poschange[new_h]
                tipped = True
            print(" (%d, %d) %d" % (new_r, new_c, new_h))

#        print(new_r, new_c, new_h, map[new_r][new_c])
        if map[new_r][new_c] == "#":
            new_r, new_c, new_h = r, c, h
            break

        indicator = indicators[new_h]
#        print(indicator)
        line = map[new_r]
        line = line[:new_c] + indicator + line[new_c+1:]
        map[new_r] = line

        if need_to_print:
            need_to_print = False
            print_map()



        r, c, h = new_r, new_c, new_h
#        print(" (%d, %d) %d" % (r,c,h))

    new_p = Pos(r, c, f, h)
#    print(new_p)
    return new_p

    


res = re.finditer(r"\d+|[LR]",directions)
for i in res:
    next = i.group()
    print(next)
    if next == "L" or next == "R":
        position = change_heading(position,next)

    else:
        position = change_position(position, next)

cnt = 0
for x in map:
    if cnt % 10 == 0:
        print("%03d      |         |         |         |       50|         |         |         |         |      100|" % cnt)
#        print("123456789 123456789 123456789 123456789 123456789 123456789 123456789 123456788 123456789 123456789 ")
    cnt = cnt  + 1
    print(x)


print(1000*(position.r + 1) + 4 * (position.c + 1) + position.h)
    
