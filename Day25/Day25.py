import matplotlib.pylab as plt
import numpy as np
import scipy as sp
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
from scipy import ndimage


start_time = time.time()

numbers = "=-012"

decimal = []

snafu = ["0", "1", "2", "1=", "1-"]


input = open('c:/users/ted/VSCode/AoC2022/Day25/input.txt', 'r').read().splitlines()

def carry_the_one(str1):
    last_digit = str1[-1]
    last_val = numbers.index(last_digit) - 2
    if last_val == 2:
        return carry_the_one(str1[:-1]) + "="
    else:
        last_val = last_val + 1
        return str1[:-1] + str(numbers[last_val + 2])



def convert_to_SNAFU(dec):


    if dec == 0:
        return "0"

    str1 = "00"

    power = int(math.log(dec,5))

    last = False
    while power >= 0:

        if power > 0:
            d, m = divmod(dec,int(5 ** power))
        else:
            d, m = dec, 0

        power = power - 1


        new_digit = snafu[d]
        if d <= 2:
            lsd = numbers.index(str1[-1])
            lsd = numbers[d + lsd - 2]
            str1 = str1 + new_digit
        else:
            str1 = carry_the_one(str1) + new_digit[-1]

        dec = m




    return str1




total = 0
for line in input:
    chars = [*line]
    print(chars)

    val = 0
    for char in chars:
        val = val * 5
        val = val + numbers.index(char) - 2
    decimal.append(val)
    total = total + val

print(total)
print(decimal)

decimal.append(total)
for i in decimal:

    print(i, "===", convert_to_SNAFU(i).lstrip("0"))

