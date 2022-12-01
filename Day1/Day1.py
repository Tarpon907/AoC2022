from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

start_time = time.time()

backpack = open('c:/users/ted/VSCode/AoC2022/Day1/input.txt', 'r').read().split('\n\n')



sums = []
 
for i in backpack:
    sums.append(sum(map(int,i.splitlines())))

sums.sort()

print("A:",sums[-1])
print("B",sum(map(int,sums[-3:])))


