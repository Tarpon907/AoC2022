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





