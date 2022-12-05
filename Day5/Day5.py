from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string

start_time = time.time()

getfile = open('c:/users/ted/VSCode/AoC2022/Day5/input.txt', 'r').read().split("\n\n")

setup = getfile[0]
lines = getfile[1].splitlines()


stacks = []

for i in range(9):
    stacks.append([])

for i in setup.splitlines():
    if i[1] == '1':
        continue
    m = re.search(r"(...) (...) (...) (...) (...) (...) (...) (...) (...)",i)
    for j in range(9):
        block = m.group(j+1)
        if block[0] == "[":
            stacks[j].append(block)
            
for j in range(9):
    stacks[j].reverse()

#print(stacks)

stackA = []
stackB = []
for stack in stacks:
    stackA.append(stack.copy())
    stackB.append(stack.copy())

for i in lines:
    m = re.search(r"move (\d+) from (\d+) to (\d+)",i)
    howmany, origin, destination = int(m.group(1)), int(m.group(2)), int(m.group(3))

    foo = []
    bar = []
    for j in range(howmany):
        foo.append(stackA[origin-1].pop())
        bar.append(stackB[origin-1].pop())

    foo.reverse()

    for j in range(howmany):
        stackA[destination-1].append(foo.pop())
        stackB[destination-1].append(bar.pop())
    


for i in range(9):
    print(stackA[i][-1][1],end="")
print()
for i in range(9):
    print(stackB[i][-1][1],end="")
print()

print("execution time (in ms): ",(time.time()-start_time)*1000) 
