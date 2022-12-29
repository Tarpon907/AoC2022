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


MAX_MINUTE = 24

part1 = False

ENC_KEY = 1 if part1 else 811589153
HOW_MANY = 1 if part1 else 10





start_time = time.time()
    
encrypted = [int(x) * ENC_KEY for x in open('c:/users/ted/VSCode/AoC2022/Day20/input.txt', 'r').read().splitlines()]



decrypted = list(range(len(encrypted)))

#print(getfile.count(0))

def decrypted_index(encrypted_index):
    return decrypted.index(encrypted_index)

def encrypted_value(decrypted_index):
    decrypted_index = decrypted_index % len(decrypted)
    return encrypted[decrypted[decrypted_index]]

for j in range(HOW_MANY):

    for i in range(len(encrypted)):

        d_index = decrypted_index(i)
    #    print("moving:",i)
        new_index = d_index + encrypted[i]
    #    print(decrypted)
        decrypted = decrypted[:d_index] + decrypted[d_index+1:]   
    #    decrypted.remove(i)
        new_index = new_index % len(decrypted) 
    #    print(decrypted)
        decrypted = decrypted[:new_index] + [i] + decrypted[new_index:]
    #    print(decrypted)

z_index = encrypted.index(0)
d_index = decrypted_index(z_index)
print(z_index)
x = encrypted_value(d_index + 1000)
y = encrypted_value(d_index + 2000)
z = encrypted_value(d_index + 3000)

print(x,y,z)
print(x+y+z)


print("execution time (in ms): ",(time.time()-start_time)*1000) 
