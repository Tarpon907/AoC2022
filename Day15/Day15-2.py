import matplotlib.pylab as plt
import numpy as np
import re
import time
import itertools
import string
import collections
import math
import functools


start_time = time.time()

getfile = open('c:/users/ted/VSCode/AoC2022/Day15/floyduk.txt', 'r').read().splitlines()


#TARGET_ROW, OFFSET, MAX, ARRAY_SIZE = 10, 10, 40, 40
#MAX = 20
MAX = 4_000_000
#MAX, CHUNK_SIZE = 4_000_000, 97_561

inputs = []
for i in getfile:
    m = re.search(r"Sensor at x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)",i)

#    print(i)
    s_x = int(m.group(1))
    s_y = int(m.group(2))
    b_x = int(m.group(3))
    b_y = int(m.group(4))
#    print("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d" % (s_x,s_y,b_x,b_y))
    distance = abs(s_x - b_x) + abs(s_y - b_y)

    inputs.append([s_x,s_y,b_x,b_y,distance])

print(inputs)



def check_neighbors_of_scanner(s_x, s_y, distance):

    min_x = max(0, s_x - distance)
    max_x = min(MAX, s_x + distance)
    min_y = max(0, s_y - distance)
    max_y = min(MAX, s_y + distance)

    for x in range(min_x, max_x + 1):
        x_diff = abs(s_x - x)
        y_diff = abs(distance - x_diff)
        
#        print("  distance: %d, x_diff: %d, y_diff: %d" %(distance,x_diff,y_diff))
        y = s_y - y_diff
        clear = False
        if y >= 0:
#            print("\tchecking location (%d,%d)" % (x,y))
            clear = check_if_location_clear(x,y)
            if clear:
                return x,y
        y = s_y + y_diff
        if y <= MAX and not clear:
#            print("\tchecking location (%d,%d)" %(x,y))
            clear = check_if_location_clear(x,y)
            if clear:
                return x, y
    return -1,-1

def check_if_location_clear(x,y):
    clear = True
    for input in inputs:
        s_x, s_y, b_x, b_y,distance = input
        diff_x = abs(s_x - x)
        diff_y = abs(s_y - y)
        if diff_x + diff_y <= distance:
#            print("\t\twithin range of scanner (%d,%d)" % (s_x,s_y))
            return False
    print("------ (%d,%d) does not seem to be in range of any scanners" % (x,y))
    return True


for input in inputs:
        s_x, s_y, b_x, b_y,distance = input
#        print("checking locations %d away from scanner at (%d,%d)" % (distance + 1, s_x, s_y))
        x,y = check_neighbors_of_scanner(s_x, s_y, distance + 1)
        if x != -1:
            print(4_000_000 * x + y)
            print("execution time (in ms): ",(time.time()-start_time)*1000) 
            exit()









