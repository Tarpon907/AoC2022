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


start_time = time.time()

getfile = open('c:/users/ted/VSCode/AoC2022/Day16/input.txt', 'r').read().splitlines()


openable = []
inputs = {}
for i in getfile:
    m = re.search(r"Valve (..) has flow rate=(\d+); tunnels? leads? to valves? (.*)",i)

    adjacent = m.group(3)

    id, rate, adjacent_list = m.group(1), int(m.group(2)), adjacent.split(", ")
#    inputs[m.group(1)] = [m.group(2),adjacent.split(", ")]
    inputs[id] = {"rate" : rate, "adjacent" : adjacent_list}

    if rate != 0:
        openable.append(id)
#    print(inputs)

new_graph = {}

for i in inputs:
    visited = []
    queue = []




def find_distances_to_real_neighbors():
    important_valves = []
    for i in inputs.keys():
        room_data = inputs[i]
        if i == 'AA' or room_data["rate"] != 0:
            important_valves.append(i)

    print(important_valves)

    for i in important_valves:
        room_data = inputs[i]
        new_data = {"rate" : room_data["rate"],
                    "neighbors" : {}}
        new_graph[i] = new_data

    print(new_graph)


    important_pairs = list(itertools.combinations(important_valves,2))
    
    print(important_pairs)

    for start, dest in important_pairs:
        visited = []
        queue = []

        if dest == 'AA':
            continue

        visited.append(start)
        neighbors = inputs[start]["adjacent"]
#        print(neighbors)
        for neighbor in neighbors:
            queue.append([neighbor,1])

        done = False
        while not done:
#            print(queue)
            m, length = queue.pop(0)
            if m == dest:
                done = True
#                print("found path from %s to %s of length %d" % (start,dest,length))

            room_data = inputs[m]
            neighbors = room_data["adjacent"]
            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.append(neighbor)
                    queue.append([neighbor,length + 1])

#                   print(queue)


#        print("distance from %s to %s is %d" % (start,dest,length))

        new_graph[start]["neighbors"][dest] = length
        if start != 'AA':
            new_graph[dest]["neighbors"][start] = length
#        start_neighbors = start_data["neighbors"]
#        start_neighbors.append([dest,length])

            




find_distances_to_real_neighbors()

print(new_graph)


valves = list(new_graph.keys())
valves.sort()
valves.pop(0)
print(valves)

highest_pressure = 0

part2 = True



def open_and_move(id, TOTAL_TIME, minute = 1, is_elephant = False, visited_list = []):



    if minute > TOTAL_TIME:
        return 0, ""

        
    neighbors = new_graph[id]["neighbors"]
    rate = new_graph[id]["rate"]

    my_string = "== Minute %d ==\n" % minute
    if is_elephant:
        my_string = my_string + "ELEPHANT"
    my_string = my_string + "in room %s\n" % id
    my_string = my_string + "release rate = %d\n" % rate

    new_visited = copy.deepcopy(visited_list)

 
    
    released_pressure = 0
    next_minute = minute
    if id != 'AA':
        next_minute = next_minute + 1
        new_visited.append(id)

    released_pressure = (TOTAL_TIME+1 - next_minute) * rate

    my_string = my_string + "releasing %d pressure over %d minutes\n\n" % (released_pressure, TOTAL_TIME+1-next_minute)

    highest_pressure = 0






    best_child_string = ""
    for i in list(neighbors.keys()):
        if i == 'AA':
            continue

        if i in new_visited:
            continue
        child_pressure, child_string = open_and_move(i, TOTAL_TIME, next_minute + neighbors[i], is_elephant, new_visited)
        if child_pressure > highest_pressure:
            highest_pressure = child_pressure
            best_child_string = child_string
    if not is_elephant:    
        child_pressure, child_string = open_and_move('AA', TOTAL_TIME, 1, True, new_visited)
        if child_pressure > highest_pressure:
            highest_pressure = child_pressure
            best_child_string = child_string
        

    released_pressure = released_pressure + highest_pressure

    my_string = my_string + best_child_string

    return released_pressure, my_string

if not part2:
    best, string = open_and_move('AA',30)
else:
    best, string = open_and_move('AA',26)


#print(string)
print(best)


print("execution time (in ms): ",(time.time()-start_time)*1000) 
