from turtle import end_fill
import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string

start_time = time.time()

getfile = open('c:/users/ted/VSCode/AoC2022/Day6/input.txt', 'r').read()



for i in range(3,len(getfile)):
    x = set(getfile[i-4:i])
    if len(x) == 4:
        print(i)
        break
    
for i in range(13,len(getfile)):
    x = set(getfile[i-14:i])
    if len(x) == 14:
        print(i)
        break


print("execution time (in ms): ",(time.time()-start_time)*1000) 
