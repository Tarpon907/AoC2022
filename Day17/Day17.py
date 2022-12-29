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


Pos = collections.namedtuple("Pos", "r c")

getfile = open('c:/users/ted/VSCode/AoC2022/Day17/input.txt', 'r').read().strip()

print(getfile)
print(len(getfile))

cavern = np.zeros((8004,12),dtype = int)
vert = np.ones(8003,dtype = int)
floor = np.ones(12,dtype = int)
empty_row = np.zeros(12,dtype = int)
empty_row[0] = empty_row[8] = 1
cavern[8000] = floor
cavern[:8003,0] = vert
cavern[:8003,8] = vert
#print(cavern)

hash_multiplier = np.array([10000000,1000000,100000,10000,100,10,1],dtype=int)

rock = np.zeros((5,4,4), dtype = int)
rock[0] = [[1,1,1,1], \
            [0,0,0,0], \
            [0,0,0,0], \
            [0,0,0,0]]

rock[1] = [[0,1,0,0], \
            [1,1,1,0], \
            [0,1,0,0], \
            [0,0,0,0]]
            
rock[2] = [[0,0,1,0], \
            [0,0,1,0], \
            [1,1,1,0], \
            [0,0,0,0]]

rock[3] = [[1,0,0,0], \
            [1,0,0,0], \
            [1,0,0,0], \
            [1,0,0,0]]

rock[4] = [[1,1,0,0], \
            [1,1,0,0], \
            [0,0,0,0], \
            [0,0,0,0]]


def first_nonzero(arr, axis, invalid_val = -1):
    mask = arr!=0
    return np.where(mask.any(axis=axis),mask.argmax(axis=axis),invalid_val)

def get_countour_hash(cavern):

        cavern_no_walls = cavern[0:8000,1:8]
        non_zeroes = first_nonzero(cavern_no_walls, axis = 0, invalid_val = 8000)
        non_zeroes = non_zeroes * -1 + non_zeroes.max()
        return np.array2string(non_zeroes)




rock_shift = [3,1,1,0,2]
highest = 8000

rock_index = -1
rock_count = 0
instruction_index = 0
have_rock = False

rock_pos = Pos(8000,2)
height = 0
stop_rocks = 2022
shifts = 0
SHIFT_SIZE = 1000
CHUNK_SIZE = 500
lookup = {}
heights = {}
contour_hash = ""


while True:

#    if rock_count == stop_rocks and not have_rock:
#        break
    i_key = instruction_index
    instruction = getfile[instruction_index]
    instruction_index = instruction_index + 1
    if instruction_index == len(getfile):
        instruction_index = 0

    if not have_rock:
        highest = min(highest,rock_pos.r)
        height = 8000 - highest

        if highest < 8000 - SHIFT_SIZE - 100:
            new_cavern = cavern[8000-SHIFT_SIZE-CHUNK_SIZE:8000 - SHIFT_SIZE,1:8]
#            print(new_cavern[CHUNK_SIZE - 10:CHUNK_SIZE, :])
            clear_cavern = cavern[8000 - SHIFT_SIZE:8000,1:8]
            clear_cavern.fill(0)
            cavern[8000 - CHUNK_SIZE:8000,1:8] += new_cavern
            new_cavern.fill(0)
            shifts = shifts + 1
            highest = highest + SHIFT_SIZE
            height = 8000 - highest

#            print(cavern[7990:8004,0:12])

        rock_index = (rock_index + 1) % 5


        # need to change this so that the key is the rock_count and the value is what is currently "my_key" and 
        if rock_count != 0:

            my_key = i_key * 1000 + rock_index
            my_key = " ".join([str(i_key),str(rock_index),contour_hash])
            heights[rock_count] = height + shifts * SHIFT_SIZE
#            print(my_key)
            if my_key in list(lookup.keys()):
                print(my_key, height + shifts * SHIFT_SIZE)
                break

            if not rock_count % 10000:
                print(rock_count, height + shifts * SHIFT_SIZE, instruction_index - 1)
            val = [rock_count, height + shifts * SHIFT_SIZE]
            lookup[my_key] = rock_count


        have_rock = True
        start = highest - 5
        while np.array_equal(cavern[start],empty_row):
            start = start + 1
        start = start - 7 + rock_shift[rock_index]
        rock_pos = Pos(start,3)
            
        cavern[rock_pos.r:rock_pos.r+rock[rock_index].shape[0],
                rock_pos.c:rock_pos.c+rock[rock_index].shape[1]] += rock[rock_index]

        cavern_slice = cavern[rock_pos.r:rock_pos.r + 7,:]

#        print("NEW ROCK\n")
#        print(cavern_slice)

    if instruction == '>':
        new_pos = Pos(rock_pos.r, rock_pos.c + 1)
    else:
        # instruction == '<'
        new_pos = Pos(rock_pos.r, rock_pos.c - 1)

#    print(instruction)

    cavern_slice = cavern[rock_pos.r:rock_pos.r + 10,:]

#    if (rock_pos.r) > 7935 and rock_pos.r < 7945:
#        print(rock_pos.r)
#        print(cavern_slice)
#        print()


    cavern[rock_pos.r:rock_pos.r + rock[rock_index].shape[0],
            rock_pos.c:rock_pos.c + rock[rock_index].shape[1]] -= rock[rock_index]
    cavern[new_pos.r:new_pos.r+rock[rock_index].shape[0],
            new_pos.c:new_pos.c+rock[rock_index].shape[1]] += rock[rock_index]

    if np.any(cavern_slice > 1):
#        print("hit horizontal")
        cavern[rock_pos.r:rock_pos.r + rock[rock_index].shape[0],
                rock_pos.c:rock_pos.c + rock[rock_index].shape[1]] += rock[rock_index]
        cavern[new_pos.r:new_pos.r + rock[rock_index].shape[0],
                new_pos.c:new_pos.c + rock[rock_index].shape[1]] -= rock[rock_index]
    else:
        rock_pos = Pos(new_pos.r,new_pos.c)

    # drop

    new_pos = Pos(rock_pos.r + 1, rock_pos.c)

    cavern_slice = cavern[rock_pos.r:rock_pos.r + 10,:]


    cavern[rock_pos.r:rock_pos.r + rock[rock_index].shape[0],
            rock_pos.c:rock_pos.c + rock[rock_index].shape[1]] -= rock[rock_index]
    cavern[new_pos.r:new_pos.r+rock[rock_index].shape[0],
            new_pos.c:new_pos.c+rock[rock_index].shape[1]] += rock[rock_index]

    if np.any(cavern_slice > 1):
#        print("hit vertical")
        cavern[rock_pos.r:rock_pos.r + rock[rock_index].shape[0],
                rock_pos.c:rock_pos.c + rock[rock_index].shape[1]] += rock[rock_index]
        cavern[new_pos.r:new_pos.r+rock[rock_index].shape[0],
                new_pos.c:new_pos.c+rock[rock_index].shape[1]] -= rock[rock_index]
        have_rock = False
        rock_count = rock_count + 1
#        print(cavern_slice)

        contour_hash = get_countour_hash(cavern)

        

    else:
        rock_pos = Pos(new_pos.r,new_pos.c)


print("-------")

print(lookup)
print(my_key)
print (lookup[my_key])

first_rock_in_cycle = lookup[my_key]
rocks_in_cycle = rock_count - lookup[my_key]
cycle_height = heights[rock_count] - heights[first_rock_in_cycle]
height_at_cycle_start = heights[first_rock_in_cycle]

print("first in cycle:", first_rock_in_cycle)
print("rocks in cycle:", rocks_in_cycle)
print("cycle height:", cycle_height)
print("height_at_cycle_start:", heights[first_rock_in_cycle])

print(heights[lookup[my_key]])
print(heights[rock_count])

rocks = 1e12
rocks = rocks - first_rock_in_cycle
answer = height_at_cycle_start

multiplier, remainder = divmod(rocks,rocks_in_cycle)
print(multiplier, remainder)

answer = answer + multiplier * cycle_height
answer = answer + heights[remainder + first_rock_in_cycle] - heights[first_rock_in_cycle]
print(answer)


print("execution time (in ms): ",(time.time()-start_time)*1000) 

exit()
