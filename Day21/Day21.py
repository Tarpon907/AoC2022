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

REP_VAL = "6969696969"

operations = "+-*/"
inverse_ops = "-+/*"




value = {}
input = open('c:/users/ted/VSCode/AoC2022/Day21/input.txt', 'r').read().splitlines()

def get_value(monkey):
    global value
    val_string = value[monkey]
    if not any(c for c in val_string if c.islower()):
        return val_string
    else:
#        print(val_string)
        m = re.search(r"([a-z][a-z][a-z][a-z]) ([\+\-\*\/]) ([a-z][a-z][a-z][a-z])",val_string)
        left, op, right = [m.group(1), m.group(2), m.group(3)]

        left_rep = get_value(left)
        right_rep = get_value(right)

        new_val = eval(left_rep + op + right_rep)
#        print(new_val)
        return(str(new_val))


def check_for_humn_in_tree(monkey):
    global value
    if monkey == "humn":
        return True
    val_string = value[monkey]
#    print(val_string)
    if any(c for c in val_string if c.islower()):
        m = re.search(r"([a-z][a-z][a-z][a-z]) ([\+\-\*\/]) ([a-z][a-z][a-z][a-z])",val_string)
        left, op, right = [m.group(1), m.group(2), m.group(3)]
        return check_for_humn_in_tree(left) or check_for_humn_in_tree(right)
    else:
        return False


def split_var_and_constant(string):
    m = re.search(r"([a-z][a-z][a-z][a-z]) ([\+\-\*\/]) ([a-z][a-z][a-z][a-z])",string)
    left, op, right = [m.group(1), m.group(2), m.group(3)]
    if check_for_humn_in_tree(left):
        left_val = "NO"
        human_string = left
        right_val = get_value(right)
    else:
        right_val = "NO"
        human_string = right
        left_val = get_value(left)
    return [left_val, human_string, right_val, op]



def solve(monkey_side, known):
    global value
#    print(monkey_side)
    left, var, right, op = split_var_and_constant(monkey_side)

    inv_op = inverse_ops[operations.find(op)]
    if left == "NO":
        evalstr = str(known) + inv_op + right
    elif right == "NO":
        if op == "+" or op == "*":
            evalstr = str(known) + inv_op + left
        if op == "-" or op == "/":
            evalstr = left + op + str(known)
    known = eval(evalstr)

    if var == "humn":
        return known
    else:
        return solve(value[var], known)
        







value = {}
for i in input:
    my_key, data = i.split(": ")
    value[my_key] = data

print(int(float(get_value("root"))))


left_side, right_side = value["root"].split(" + ")

print("Left has human?", check_for_humn_in_tree(left_side))
print("Right has human?", check_for_humn_in_tree(right_side))

right_val = get_value(right_side)

print(int(float(solve(value[left_side], right_val))))
