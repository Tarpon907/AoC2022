from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string

s = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
start_time = time.time()

rucksacks = open('c:/users/ted/VSCode/AoC2022/Day3/input.txt', 'r').read().split("\n")

rucksacks = rucksacks[:-1]
score = 0

for rucksack in rucksacks:
    comp1 = rucksack[:int(len(rucksack)/2)]
    comp2 = rucksack[int(len(rucksack)/2):]

    comp1 = ''.join(sorted(comp1))
    comp2 = ''.join(sorted(comp2))

#    print(rucksack, comp1, comp2)
    dupe = ''
    i = 0
    while i < len(comp1) and dupe == '':
        j = 0
        while j < len(comp2) and dupe == '':
            if comp1[i] == comp2[j]:
                dupe = comp1[i]
            j = j + 1
        i = i + 1
#    print(dupe)
    thisscore = s.find(dupe) + 1
#    print(thisscore)
    score = score + thisscore

print(score)

score = 0
h = 0
while h < len(rucksacks):
    line1 = rucksacks[h]
    line2 = rucksacks[h+1]
    line3 = rucksacks[h+2]
    h = h + 3
    print(line1,line2,line3)

    line1 = ''.join(sorted(line1))
    line2 = ''.join(sorted(line2))
    line3 = ''.join(sorted(line3))

    i = 0
    dupe = ''
    while i < len(line1) and dupe == '':
        j = 0
        while j < len(line2) and dupe == '':
            if line1[i] != line2[j]:
                j = j + 1
                continue
            k = 0
            while k < len(line3) and dupe == '':
                if line1[i] == line2[j] and line2[j] == line3[k]:
                    dupe = line1[i]
                    print(dupe)
                k = k + 1
            j = j + 1
        i = i + 1
    thisscore = s.find(dupe) + 1
    score = score + thisscore

print(score)





