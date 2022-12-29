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
import heapq
import random

start_time = time.time()

MAX_MINUTE = 32

robot_types = ["geode_robot", "obs_robot", "clay_robot", "ore_robot"]
resource_types = ["geode", "obs", "clay", "ore"]


input = open('c:/users/ted/VSCode/AoC2022/Day19/input.txt', 'r').read().splitlines()

def produce_for_minutes(inv, minutes):
      next_inv = copy.deepcopy(inv)
      next_inv["ore"] += next_inv["ore_robot"] * minutes
      next_inv["clay"] += next_inv["clay_robot"] * minutes
      next_inv["obs"] += next_inv["obs_robot"] * minutes
#      next_inv["geode"] += next_inv["geode_robot"]
      return next_inv

def convert_inventory_to_string(minute,i):
    istr = "%d,%d,%d,%d,%d,%d,%d" % (minute, i["ore"],i["ore_robot"],i["clay"],i["clay_robot"],i["obs"],i["obs_robot"])
    return istr

def create_heap_index(inv):
#    index  = 1000 - inv["ore_robot"]
#    index += 10000 - inv["ore"] * 100
#    index += 100000 - inv["clay_robot"] * 1000
#    index += 1000000 - (inv["clay"] * 10000)
#    index += 10000000 - (inv["obs_robot"] * 100000)
#    index += 100000000 - (inv["obs"] * 1000000)
#    index += 1000000000 - (inv["geode"] * 10000000)

    index = -100 * inv["geode"] - inv["obs"]
#    print(index)
    return index



def max_if_cheat(inv, minute):
    clay_r = inv["clay_robot"]
    clay = inv["clay"]
    obs_r = inv["obs_robot"]
    obs = inv["obs"]
    geode_r = 0
    produce = 0
    for i in range(minute + 1, MAX_MINUTE-1):
        clay = clay + clay_r
        clay_r = clay_r + 1
        obs = obs + obs_r
        if costs["obs_clay"] <= clay:
            clay = clay - costs["obs_clay"]
            obs_r = obs_r + 1
        if costs["geode_obs"] <= obs:
            obs = obs - costs["geode_obs"]
            geode_r = geode_r + 1
            produce = produce + MAX_MINUTE - i

    return produce



p2total = 1
total = 0
    


for id, bp in enumerate(input[0:3]):
    inventory = {}
    inventory = {"ore_robot" : 0,
              "ore" : 0,
              "clay_robot" : 0,
              "clay" : 0,
              "obs_robot" : 0,
              "obs" : 0,
              "geode_robot" : 0,
              "geode" : 0}
    
    

    m = re.search(r"Blueprint (\d+): Each ore robot costs (\d+) ore. Each clay robot costs (\d+) ore. Each obsidian robot costs (\d+) ore and (\d+) clay. Each geode robot costs (\d+) ore and (\d+) obsidian.", bp)
    blueprint = m.group(1)
    costs = {"ore_ore" : int(m.group(2)),
          "clay_ore" : int(m.group(3)),
          "obs_ore" : int(m.group(4)),
          "obs_clay" : int(m.group(5)),
          "geode_ore" : int(m.group(6)),
          "geode_obs" : int(m.group(7))}


    max_ore = max(costs["ore_ore"],costs["clay_ore"])
    max_ore = max(max_ore, costs["obs_ore"])
    max_ore = max(max_ore, costs["geode_ore"])
    costs["max_ore"] = max_ore
#    print(costs,inventory)


    inventory["ore"] = costs["ore_ore"]

    queue = []
    visited = []
    best = 0
    best_str = ""
    found = False

    tiebreaker = itertools.count()

    heapq.heappush(queue, (0,0, next(tiebreaker),["ore_robot", inventory, 0, 0, ""]))
    maxqueue = 1
#    queue.append(["ore_robot", inventory, 0, 0, ""])   # robot, current inventory, build minute, produced so far

    while queue:


        maxqueue = max(maxqueue,len(queue))
        index, nm, tie, build = queue.pop(0)
#        print(index)
        if build in visited:
            continue
        visited.append(build)
        robot_type, inv, build_minute, produced, history = build

        new_inv = copy.deepcopy(inv)

        match robot_type:
            case "ore_robot":
                new_inv["ore"] -= costs["ore_ore"]
            case "clay_robot":
                new_inv["ore"] -= costs["clay_ore"]
            case "obs_robot":
                new_inv["ore"] -= costs["obs_ore"]
                new_inv["clay"] -= costs["obs_clay"]
            case "geode_robot":
                new_inv["ore"] -= costs["geode_ore"]
                new_inv["obs"] -= costs["geode_obs"]
                produced = produced + MAX_MINUTE - build_minute
                new_inv["geode"] = produced
                mystr = mystr + "(produces %d)" % (MAX_MINUTE - build_minute)

        new_inv = produce_for_minutes(new_inv, 1)

        new_inv[robot_type] += 1

        invstr = convert_inventory_to_string(MAX_MINUTE - build_minute, new_inv)

        mystr = "%s - minute %d, build %s" % (invstr,build_minute, robot_type) 

        if invstr == "10,6,3,6,5,4,3":
            true = True
        if invstr == "9,6,3,11,6,7,3":
            true = True
        if invstr == "8,6,3,9,6,10,4":
            true = True
        if invstr == "7,6,3,7,6,14,5":
            true = True
        if invstr == "6,6,3,13,6,7,5":
            true = True
        if invstr == "5,6,3,11,6,12,6":
            true = True
        if invstr == "4,6,3,17,6,6,6":
            true = True



        history = history + "\n" + mystr
        if produced > best:
            best = produced
            best_str = history
        else:
            if produced + max_if_cheat(new_inv, build_minute) < best:
                continue

        if new_inv["obs_robot"] > 0:
            time_to_geode_obs = max(0,math.ceil((costs["geode_obs"] - new_inv["obs"])/new_inv["obs_robot"]))
            time_to_geode_ore = max(0,math.ceil((costs["geode_ore"] - new_inv["ore"])/new_inv["ore_robot"]))
            time_to_geode = max(time_to_geode_obs, time_to_geode_ore)
            if build_minute + 1 + time_to_geode < MAX_MINUTE:
                next_inv = produce_for_minutes(new_inv, time_to_geode)
                new_minute = build_minute + 1 + time_to_geode
                next_build = ["geode_robot", next_inv, new_minute, produced, history]
                heapq.heappush(queue,(create_heap_index(next_inv), -new_minute, next(tiebreaker), next_build))
        if new_inv["clay_robot"] > 0 and new_inv["obs_robot"] < costs["geode_obs"]:
            time_to_obs_clay = max(0, math.ceil((costs["obs_clay"] - new_inv["clay"])/new_inv["clay_robot"]))
            time_to_obs_ore = max(0,math.ceil((costs["obs_ore"] - new_inv["ore"])/new_inv["ore_robot"]))
            time_to_obs = max(time_to_obs_clay, time_to_obs_ore)
            if build_minute + 1 + time_to_obs < MAX_MINUTE - 1:
                next_inv = produce_for_minutes(new_inv, time_to_obs)
                new_minute = build_minute + 1 + time_to_obs
                next_build = ["obs_robot", next_inv, new_minute, produced, history]
                heapq.heappush(queue,(create_heap_index(next_inv), -new_minute, next(tiebreaker), next_build))
        if new_inv["clay_robot"] < costs["obs_clay"]:
            time_to_clay = max(0,math.ceil((costs["clay_ore"] - new_inv["ore"])/new_inv["ore_robot"]))
            if build_minute + 1 + time_to_clay < MAX_MINUTE - 2:
                next_inv = produce_for_minutes(new_inv, time_to_clay)
                new_minute = build_minute + 1 + time_to_clay
                next_build = ["clay_robot", next_inv, new_minute, produced, history]
                heapq.heappush(queue,(create_heap_index(next_inv), - new_minute, next(tiebreaker), next_build))
        if new_inv["ore_robot"] < costs["max_ore"]:
            time_to_ore = max(0,math.ceil((costs["ore_ore"] - new_inv["ore"])/new_inv["ore_robot"]))
            if build_minute + 1 + time_to_ore < MAX_MINUTE - 1:
                next_inv = produce_for_minutes(new_inv, time_to_ore)
                new_minute = build_minute + 1 + time_to_ore
                next_build = ["ore_robot", next_inv, new_minute, produced, history]
                heapq.heappush(queue,(create_heap_index(next_inv),-new_minute, next(tiebreaker), next_build))

#    print(best_str)
    print("blueprint %d, best %d, quality: %d" % (id + 1, best, (id + 1 )*best))
    total = total + (id + 1) * best
    print("max queue size", maxqueue)
    p2total = p2total * best
    print("p2total:",p2total)

print(total)

        

        


print("execution time (in ms): ",(time.time()-start_time)*1000) 




