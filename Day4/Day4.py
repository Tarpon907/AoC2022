from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string

start_time = time.time()

lines = open('c:/users/ted/VSCode/AoC2022/Day4/input.txt', 'r').read().splitlines()


a = 0
b = 0
for line in lines:

    m = re.search(r"(\d+)-(\d+),(\d+)-(\d+)",line)
    e1 = set(range(int(m.group(1)),int(m.group(2))+1))
    e2 = set(range(int(m.group(3)),int(m.group(4))+1))
    if e1.issubset(e2) or e2.issubset(e1):
        a = a + 1
    if e1 & e2:
        b = b + 1
 
print(a,b)

print("execution time (in ms): ",(time.time()-start_time)*1000) 
