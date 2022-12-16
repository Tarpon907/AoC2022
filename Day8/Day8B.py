from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string


start_time = time.time()


getfile = open('c:/users/ted/VSCode/AoC2022/Day8/input.txt', 'r').read().splitlines()

height = len(getfile)
width = len(getfile[0])

print (width,height)

highest_scenic = 0
for i in range(len(getfile)):
    for j in range(len(getfile[0])):
        treeheight = getfile[i][j]
 #       print("(",i,",",j,") - ",treeheight," - ",end="")
        visible = True
        k = i - 1
        scenic = 0
        while k > -1 and visible:
            scenic = scenic + 1
#            print (k,j)
            if getfile[k][j] >= treeheight:
                visible = False
            k = k - 1
        dir_scenic = 0
        visible = True
        k = i + 1
        while k < height and visible:
            dir_scenic = dir_scenic + 1
#            print(k,j)
            if getfile[k][j] >= treeheight:
                visible = False
            k = k + 1
        scenic = scenic * dir_scenic
        k = j - 1
        dir_scenic = 0
        visible = True
        while k > -1 and visible:
            dir_scenic = dir_scenic + 1
#            print(i,k)
            if getfile[i][k] >= treeheight:
                visible = False
            k = k - 1
        scenic = scenic * dir_scenic
        k = j + 1
        dir_scenic = 0
        visible = True
        while k < width and visible:
            dir_scenic = dir_scenic + 1
#            print(i,k)
            if getfile[i][k] >= treeheight:
                visible = False
            k = k + 1
        scenic = scenic * dir_scenic

        highest_scenic = max(scenic, highest_scenic)



print(highest_scenic)

            
            

            
        
        


print("execution time (in ms): ",(time.time()-start_time)*1000) 
