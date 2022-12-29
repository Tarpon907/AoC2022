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

map = open('c:/users/ted/VSCode/AoC2022/Day23/input.txt', 'r').read().splitlines()

directions = "NSWE"
dir_index = 0

neighbor_list = [[-1-1j, -1j, 1-1j],
                 [-1+1j, +1j, 1+1j],
                 [-1-1j, -1, -1+1j],
                 [1-1j, 1, 1+1j]]


elves = set()

for r in range(len(map)):
    for c in range(len(map[r])):
        if map[r][c] == "#":
            elves.add(c+r*1j)

print(elves)
moves = {}
stable = set()

part = 1

def print_map():
    min_x, max_x, min_y, max_y = 1e8, -1e8, 1e8, -1e8

    for elf in elves:
        x, y = elf.real, elf.imag
        min_x, max_x, min_y, max_y = min(min_x,int(x)), max(max_x,int(x)), min(min_y,int(y)), max(max_y,int(y))

    for y in range(min_y, max_y + 1):
        str1 = ""
        for x in range(min_x, max_x+ 1):
            if (x+y*1j) in elves:
                str1 = str1 + "#"
            else:
                str1 = str1 + "."
        print(str1)

    print((max_x - min_x + 1) * (max_y - min_y + 1) - len(elves))
            


i = 1
moved = True
while moved:
#    print(len(stable), len(elves))
    moved = False
    for elf in elves:
        if elf in stable:
            continue
        neighbor = False
        for index in range(4):
            for check in neighbor_list[index]:
                foo = elf + check
                if foo in elves:
                    neighbor = True
        if not neighbor:
#            print("Elf %d,%d has no neighbors.  Staying put" % (elf.real, elf.imag))
            stable.add(elf)
            continue

        cnt = 0
        found_dir = False
        while not found_dir and cnt < 4:
            neighbor = False
            index = (dir_index + cnt) % 4
            for check in neighbor_list[index]:
                foo = elf + check
#                print(elf, foo)
                if foo in elves:
#                    print("neighbor at %d,%d" % (foo.real, foo.imag))
                    neighbor = True

            if neighbor:
                cnt = cnt + 1
#                print(cnt)
            else:
                found_dir = True

        if found_dir:
            move = elf + neighbor_list[(dir_index + cnt) % 4][1]
            if move not in moves.keys():
#                print("elf at %d,%d might move to %d,%d" % (elf.real, elf.imag, move.real, move.imag))
                moves[move] = elf
            else:
                moves[move] = "CONFLICT"

#    print(moves)

#    print_map()
    for move in list(moves.keys()):
        if moves[move] != "CONFLICT":
            moved = True
            elves.remove(moves[move])
            elves.add(move)
            for a in range(-1,2):
                for b in range(-1,2):
                    check = move + (a + b*1j)
                    if check in stable:
                        stable.remove(check)
                        
        del moves[move]

    dir_index = (dir_index + 1) % 4

#    print(moves)
    moves = {}

#    print_map()

#    print(moved)
    if not moved:
        print(i)
    else:
        i = i + 1





print("execution time (in ms): ",(time.time()-start_time)*1000) 


#print(elves)


