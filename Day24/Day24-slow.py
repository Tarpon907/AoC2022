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

Bliz = collections.namedtuple("Bliz", ["r", "c", "h"])

headings = ">v<^"


input = open('c:/users/ted/VSCode/AoC2022/Day24/input.txt', 'r').read().splitlines()

height = len(input)
width = len(input[0])

cavern_width = width - 2
cavern_height = height - 2

print(cavern_width, cavern_height)
#destination = [cavern_height, cavern_width - 1]

#print(destination)
raw_start = [-1,0]
start_space = [-1,0]
queue = [[-1, 0, 0, -1, 0, cavern_height, cavern_width - 1, ""]]

bliz_by_row = dict()
bliz_by_col = dict()
for x in range(cavern_height):
    bliz_by_row[x] = []
for x in range(cavern_width):
    bliz_by_col[x] = [] 

cycle_length = math.lcm(cavern_height, cavern_width)
print(cycle_length)

part = 1

r = -1
bliz_by_row[-1] = []
bliz_by_row[cavern_height] = []
for line in input:
#    print("row: ", r)



    for match in re.finditer(r"[>v<^]",line):
        h = headings.index(match.group(0))
        d, m = divmod(h, 2)
        c = match.start() - 1
#            print("col:", c)

        if m == 0:
            b = c - d*2j + 1j
#                print(b)
            bbr = bliz_by_row[r] if r in bliz_by_row.keys() else []
#                print(bbr)         
            bbr.append(b)
#                print(bbr)
            bliz_by_row[r] = bbr
        else:
            b = r - d*2j + 1j
#                print(b)
            
            bbc = bliz_by_col[c] if c in bliz_by_col.keys() else []
            bbc.append(b)
#                print(bbc)
            bliz_by_col[c] = bbc
    r = r + 1

#print("bbr:",bliz_by_row)
#print("bbc:",bliz_by_col)


visited = []

def print_map(row, column, minute):
    row, column, minute = int(row), int(column), int(minute)
    map = []
    for i in range(cavern_height + 2):
        line = "#" + "." * cavern_width + "#"
        map.append(line)
    map[0] = "#." + "#" * (cavern_width)
    map[cavern_height + 1] = "#" * (cavern_width) +".#"

    for r in range(cavern_height):
        bbr = bliz_by_row[r]
#        print(bbr)
        for bliz in bbr:
#            print(bliz)
            if bliz.imag == -1:
                char = "<"
            else:
                char = ">"
#            print(bliz.real, bliz.imag, minute)
            c = int(bliz.real + bliz.imag * minute) % cavern_width + 1
            foo = map[r+1][c]
            if foo != ".":
                if foo in ["v","^","<",">"]:
                    char = "2"
                else:
                    char = str(int(foo) + 1)
            map[r+1] = map[r+1][:c] + char + map[r+1][c+1:]

    for c in range(cavern_width):
        bbc = bliz_by_col[c]
        for bliz in bbc:
            if bliz.imag == -1:
                char = "^"
            else:
                char = "v"            
            r = int(bliz.real + bliz.imag * minute) % cavern_height + 1
            foo = map[r][c+1]
            if foo != ".":
                if foo in ["v","^","<",">"]:
                    char = "2"
                else:
                    char = str(int(foo) + 1)
            map[r] = map[r][:c+1] + char + map[r][c+2:]


    if map[row+1][column+1] != ".":
        print("ERROR: (%d,%d) occupied" % (row, column))   
    else:
        map[row+1] = map[row+1][:column+1] + "E" + map[row+1][column+2:]
 

    print("\nMINUTE",minute)
    for i in range(cavern_height + 2):
        print(map[i])



printed = False
while len(queue) > 0:
    visit = queue.pop(0)
    r,c,m, start_r, start_c, dest_r, dest_c, str1= visit
    destination = [dest_r, dest_c]
    start = [start_r, start_c]

#    print(visit)

    cycle_index = m % cycle_length
    visit = r, c, cycle_index
    if visit in visited:
        continue
    visited.append(visit)
    if m % 100 == 0:
        if not printed:
            printed = True
            print(visit)
    else:
        printed = False
    if [r,c] == destination:
#        print("at destination")
#        if part == 3 or part == 4:
        if part > 2:
#        print(str1)
            print(m)
            print("execution time (in ms): ",(time.time()-start_time)*1000) 
            break

    b_blocked = set()

    if [r+1,c] == destination:
#        print(str1)
#        print("here")
        str1 = str1 + "%d,%d,%d " % (r,c,m) + "DESTINATION "
        print(m+1)
        print("execution time (in ms): ",(time.time()-start_time)*1000) 
#        print(str1)
        queue = []
        visited = []
#        print("returning to %d, %d" % (start_r, start_c))
        queue.append([r+1,c, m+1, dest_r, dest_c, start_r, start_c, str1])
#        print(queue)
        part = part + 1
        if part == 2:
            continue
        if part == 4:
#            print(str1)
#            print(m+1)
            break

    if [r-1,c] == destination:
#        print(destination)
#        print("here 2")
        str1 = str1 + "%d,%d,%d " % (r,c,m) + "BACK_AT_START "
        print(m+1)
        print("execution time (in ms): ",(time.time()-start_time)*1000) 
        queue = []
        visited = []
        queue.append([r-1, c, m+1, dest_r, dest_c, start_r, start_c, str1])
#        print("back at start:", m+1)
#        print(str1)
        part = part + 1
        continue


    if [r,c] == start or [r,c] == destination:
        b_blocked.add((r,c+1))
        b_blocked.add((r,c-1))



    for new_x in range(-1,2):
        if r + new_x >= 0 and r + new_x < cavern_height:

            bbr = bliz_by_row[r + new_x]
#            print (bbr)
            if (c - (m + 1)) % cavern_width  +1j in bbr or (c + (m + 1)) % cavern_width -1j in bbr:
                b_blocked.add((r+new_x,c))

            if new_x == 0:
                if ((c+1) - (m + 1) ) % cavern_width  +1j in bbr or ((c+1) + (m + 1) ) % cavern_width -1j in bbr:
                    b_blocked.add((r+new_x,c+1))
                if ((c-1) - (m + 1) ) % cavern_width  +1j in bbr or ((c-1) + (m + 1) ) % cavern_width -1j in bbr:
                    b_blocked.add((r+new_x,c-1))
        else:
            b_blocked.add((r + new_x,c))


        if c + new_x >= 0 and c + new_x < cavern_width:
#            print(c+new_x)
            bbc = bliz_by_col[c + new_x]
            if (r - (m + 1)) % cavern_height +1j in bbc or (r + (m + 1)) % cavern_height  - 1j in bbc:
                b_blocked.add((r,c + new_x))
            if new_x == 0:
                if ((r+1) - (m + 1)) % cavern_height  +1j in bbc or ((r+1) + (m + 1)) % cavern_height - 1j in bbc:
                    b_blocked.add((r+1,c + new_x))
                if ((r-1) - (m + 1)) % cavern_height  +1j in bbc or ((r-1) + (m + 1)) % cavern_height  - 1j in bbc:
                    b_blocked.add((r-1,c + new_x))


        else:
            b_blocked.add((r,c + new_x))

    if [r,c] == start:
        b_blocked.remove((r,c))
        
#    print("[%d, %d, %d]:" % (r, c, m), end = "")
#    print("blocked: ", b_blocked)

    try_next = {(r - 1, c), (r, c), (r + 1, c), (r, c - 1), (r, c + 1)}
#    print("all otions:", try_next)
    try_next = try_next - b_blocked
#    if part == 2:
#        print("open:", try_next)

    str1 = str1 + "%d,%d,%d " % (r,c,m)

    for next in list(try_next):
        next = list(next)
        next.append(m + 1)
#        print(next, " ", end="")
        next.extend([start_r, start_c, dest_r, dest_c, str1])
        queue.append(next)

#    print()

for x in str1.split(" "):
    if x == "DESTINATION" or x == "BACK_AT_START":
        continue
#    r,c,m = x.split(",")
#    print(r,c,m)
#    print_map(r,c,m)
    

    
print("execution time (in ms): ",(time.time()-start_time)*1000) 
