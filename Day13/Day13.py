from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string
import collections
import math
import functools

Point = collections.namedtuple("Point", "x y")

start_time = time.time()
part_3 = False
part_2 = True
part_1 = False

getfile = open('c:/users/ted/VSCode/AoC2022/Day13/input.txt', 'r').read().split("\n\n")

all_packets = [[[6]],[[2]]]
left_packets = [[6]]
right_packets = [[2]]

for group in getfile:
    left_packet, right_packet = [eval(x) for x in group.splitlines()]
    left_packets.append(left_packet)
    right_packets.append(right_packet)
    all_packets.append(left_packet)
    all_packets.append(right_packet)

#print(all_packets)

if len(left_packets) != len(right_packets):
    print("PACKETS DON'T MATCH")
    exit()

def compare_ints(left : int, right : int):
#    print("comparing ints left(%d) and right(%d)" % (left, right))
    if left < right:
#        print("\tcorrect order and done")
        return True, True  # correct order and done
    if left > right:
#        print("\twrong order and done")

        return False, True # wrong order, done
    else: 
#        print("\tcorrect order and NOT done")

        return True, False # correct_order but not done

def cmp_lists(left : list, right : list):
    correct, done = compare_lists(left_packet, right_packet)
    if correct:
        return -1
    else:
        return 1

def parent_compare_lists(left_packet : list, right_packet : list):
    correct, done = compare_lists(left_packet, right_packet)

    return correct

def compare_lists(left_packet : list, right_packet : list):
#    print("compare: ", left_packet, right_packet)
    left_index = 0
    right_index = 0
    correct_order = True
    done = False
    left_done = right_done = False
#    print("comparing lists:", left_packet, right_packet)
    while correct_order and not done:
        if left_index >= len(left_packet):
#            print("\nleft list is done")
            left_done = True
        if right_index >= len(right_packet):
#            print("\nright list is done")
            right_done = True
        if left_done and not right_done:
#            print("\t\tcorrect order and done")
            return True, True  # correct_order and done
        if right_done and not left_done:
#            print("\t\tWRONG order and done")
            return False, True # incorrect_order and done
        if right_done and left_done:
#            print("\t\tcorrect order but NOT done (equal)")
            return True, False # correct_order so far but not done


        left = left_packet[left_index]
        right = right_packet[right_index]
#        print(left,right)
        if type(left) == int and type(right) == int:
            correct_order, done = compare_ints(left,right)
            if not done:
                left_index = left_index + 1
                right_index = right_index + 1
            continue

        if type(left) == list and type(right) == list:
            correct_order, done = compare_lists(left, right)
            if not done:
                left_index = left_index + 1
                right_index = right_index + 1
                continue

        if type(left) == int and type(right) == list:
            new_left = [left]
#            print("\tconverting (left) int %d to list " % left, new_left)
            correct_order, done = compare_lists(new_left,right)
            if not done:
                left_index = left_index + 1
                right_index = right_index + 1

        if type(left) == list and type(right) == int:
            new_right = [right]
#            print("\tconverting (right) int %d to list " % right, new_right)
            correct_order, done = compare_lists(left,new_right)
            if not done:
                left_index = left_index + 1
                right_index = right_index + 1

    return correct_order, done


if part_2:
    for i in range(len(all_packets)):
        for j in range(len(all_packets)):
            if i == j:
                continue
            left = all_packets[i]
            right = all_packets[j]
#            print(left,right)
            result = parent_compare_lists(left,right)
#            print(result)
            if not result:
                all_packets[i] , all_packets[j] = all_packets[j] , all_packets[i]
#            print(all_packets)



    print(all_packets)  
    all_packets.reverse()
    for i in all_packets:
        print(i)

    foo = all_packets.index([[2]])+1
    bar = all_packets.index([[6]])+1
    print(foo*bar)


if part_1:
    sum = 0
    for i in range(len(left_packets)):
            left_packet = left_packets[i]
            right_packet = right_packets[i]
            correct, done = compare_lists(left_packet,right_packet)
            if correct:
                print(i, "is in correct order")
                sum = sum + i
            else:
                print(i, "is in the WRONG order")

    print(sum)
