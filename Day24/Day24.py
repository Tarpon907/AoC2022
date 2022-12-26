import matplotlib.pylab as plt
import numpy as np
import scipy as sp
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
from scipy import ndimage


start_time = time.time()

headings = ">v<^"

neighbors = np.array([[0,1,0],[1,1,1],[0,1,0]],dtype = bool)
#print(neighbors)


map = open('c:/users/ted/VSCode/AoC2022/Day24/input.txt', 'r').read().splitlines()

height = len(map) - 2
width = len(map[0]) - 2

bliz = np.zeros((4,height,width), dtype = bool)

elf = np.zeros((height,width), dtype = bool)




for r, line in enumerate(map):

    for m in re.finditer(r"[>v<^]",line):
        h = headings.index(m.group(0))
        c = m.start() - 1
        bliz[h][r-1][c] = True


part = 1
start = [-1,0]
minute = 0

def roll_blizzards(bliz):
#    print("east:\n",bliz[0]) 
    bliz[0] = np.roll(bliz[0], 1, axis = 1)
#    print("rolled:\n",bliz[0])
#    print("south:\n",bliz[1])
    bliz[1] = np.roll(bliz[1], 1, axis = 0)
#    print("rolled:\n",bliz[1])
#    print("west:\n",bliz[2])
    bliz[2] = np.roll(bliz[2], -1, axis = 1)
#    print("rolled:\n",bliz[2])
#    print("north:\n",bliz[3])
    bliz[3] = np.roll(bliz[3], -1, axis = 0)
#    print("rolled:\n",bliz[3])

    return bliz
    

while not elf[-1][-1]:
    minute = minute + 1

    bliz = roll_blizzards(bliz)

    elf = sp.ndimage.binary_dilation(elf, neighbors)
    elf[0][0] = True

    combined_blizzards = np.any(bliz, axis = 0)

    combined_blizzards = np.invert(combined_blizzards)

    elf = np.bitwise_and(elf,combined_blizzards)

minute = minute + 1
print ("part 1:", minute)

bliz = roll_blizzards(bliz)



elf = np.zeros((height,width), dtype = bool)

while not elf[0][0]:
    minute = minute + 1

    bliz = roll_blizzards(bliz)

    elf = sp.ndimage.binary_dilation(elf, neighbors)
    elf[-1][-1] = True

    combined_blizzards = np.any(bliz, axis = 0)

    combined_blizzards = np.invert(combined_blizzards)

    elf = np.bitwise_and(elf,combined_blizzards)    

minute = minute + 1

bliz = roll_blizzards(bliz)
elf = np.zeros((height,width), dtype = bool)

while not elf[-1][-1]:
    minute = minute + 1

    bliz = roll_blizzards(bliz)

    elf = sp.ndimage.binary_dilation(elf, neighbors)
    elf[0][0] = True

    combined_blizzards = np.any(bliz, axis = 0)

    combined_blizzards = np.invert(combined_blizzards)

    elf = np.bitwise_and(elf,combined_blizzards)

minute = minute + 1
print ("part 2:", minute)



    
print("execution time (in ms): ",(time.time()-start_time)*1000) 