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


getfile = open('c:/users/ted/VSCode/AoC2022/Day10/input.txt', 'r').read().splitlines()

cycle = 0
x = 1
total = 0
display = []
row = ""

queued_change = []
file_index = 0
execute_cycles = 1
while file_index < len(getfile) or len(queued_change) > 0:
    cycle = cycle + 1

    if len(row) in range(x-1,x+2):
        row = row + "#"
    else:
        row = row + "."

    if len(row) == 40:
        display.append(row)
        row = ""
        
    if file_index < len(getfile):
        i = getfile[file_index]
    else:
        i = "NULL"
    if i[0:4] == "addx":
        instruction, change = i.split(" ")
        change = int(change)
        queued_change.append(0)
        queued_change.append(change)
    elif i[0:4] == "noop":
#        print("noop-----")
        queued_change.append(0)

#    print(queued_change)
    if (cycle -20) % 40 == 0:
        total = total + cycle * x
    if len(queued_change) > 0:
            x = x + queued_change[0]
            queued_change = queued_change[1:]
#    print("end:",cycle,x)
    file_index = file_index + 1


print(total)
for i in display:
    print(i)
