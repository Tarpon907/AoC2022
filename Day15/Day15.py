import matplotlib.pylab as plt
import numpy as np
import re
import time
import itertools
import string
import collections
import math
import functools

getfile = open('c:/users/ted/VSCode/AoC2022/Day15/input.txt', 'r').read().splitlines()

start_time = time.time()

TARGET_ROW, OFFSET, MAX, ARRAY_SIZE = 10, 10, 40, 40
#MAX = 20, 7
TARGET_ROW, OFFSET, MAX, ARRAY_SIZE = 2_000_000, 1_000_000, 4_000_000, 12_000_000

row = np.zeros(ARRAY_SIZE,dtype = int)
inputs = []
for i in getfile:
    m = re.search(r"Sensor at x=(-?\d+), y=(-?\d+):.*x=(-?\d+), y=(-?\d+)",i)

#    print(i)
    s_x = int(m.group(1))
    s_y = int(m.group(2))
    b_x = int(m.group(3))
    b_y = int(m.group(4))
#    print("Sensor at x=%d, y=%d: closest beacon is at x=%d, y=%d" % (s_x,s_y,b_x,b_y))

    inputs.append([s_x,s_y,b_x,b_y])

print(inputs)

def eliminate_possible(possible, range):

    start_x, end_x = range
    for stretch in possible:
        if end_x < stretch[0]:
            return

        elif start_x <= stretch[0] and end_x >= stretch[1]:
            possible.remove(stretch)


        elif start_x > stretch[0] and end_x < stretch[1]:
            anustart = stretch[0]
            stretch[0] = end_x + 1
            loc = possible.index(stretch)
            possible.insert(loc,[anustart, start_x - 1])

        elif end_x >= stretch[0] and end_x < stretch[1]:
            stretch[0] = end_x + 1
        
        elif start_x > stretch[0] and start_x <= stretch[1]:
            stretch[1] = start_x - 1

def check_line(TARGET_ROW):

    for input in inputs:
        s_x, s_y, b_x, b_y = input

        distance = abs(s_x - b_x) + abs(s_y - b_y)



#       print("Beacon at %d,%d -- distance %d" % (b_x, b_y, distance))
        delta_y = abs(s_y - TARGET_ROW)
        if delta_y > distance:
#            print("delta Y (%d) is greater than distance (%d).  No contribution" % (delta_y, distance))
            continue
#       print("distance: %d, delta_y: %d"%  (distance, delta_y))

        start_x = s_x - abs(distance - delta_y) + OFFSET
        end_x = s_x + abs(distance - delta_y)  + OFFSET # inclusive

#        start_x = max(start_x, 0)
#        end_x = min(end_x,MAX)
#        print("(%d,%d) beacon, delta_y (%d) means (%d) beacons from (%d,%d) - (%d,%d)" % (b_x,b_y,delta_y,(end_x-start_x+1),start_x,TARGET_ROW,end_x,TARGET_ROW))

#        print("eliminationg from %d to %d" % (start_x,end_x))

        for i in range(start_x, end_x + 1):
            row[i] = 1

    for input in inputs:
        s_x, s_y, b_x, b_y = input
        if b_y == TARGET_ROW:
            row[b_x + OFFSET] = 0




def process_input(sector,sector_data):
    for input in inputs:
        s_x, s_y, b_x, b_y = input

        distance = abs(s_x - b_x) + abs(s_y - b_y)



#       print("Beacon at %d,%d -- distance %d" % (b_x, b_y, distance))
        delta_y = abs(s_y - TARGET_ROW)
        if delta_y > distance:
#            print("delta Y (%d) is greater than distance (%d).  No contribution" % (delta_y, distance))
            continue
#       print("distance: %d, delta_y: %d"%  (distance, delta_y))

        start_x = s_x - abs(distance - delta_y) + OFFSET
        end_x = s_x + abs(distance - delta_y)  + OFFSET # inclusive

        start_x = max(start_x, 0)
        end_x = min(end_x,MAX)
#        print("(%d,%d) beacon, delta_y (%d) means (%d) beacons from (%d,%d) - (%d,%d)" % (b_x,b_y,delta_y,(end_x-start_x+1),start_x,TARGET_ROW,end_x,TARGET_ROW))

#        print("eliminationg from %d to %d" % (start_x,end_x))




check_line(TARGET_ROW)
print(row,row.sum())



print("execution time (in ms): ",(time.time()-start_time)*1000) 




