from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string
import collections
import math

Point = collections.namedtuple("Point", "x y")

start_time = time.time()



class Monkey:
    
    def __init__(self,monkeystring):
        monkeylines = monkeystring.splitlines()
        self.id = int(monkeylines[0].split()[1][:-1])

        self.items = [int(i) for i in monkeylines[1].split(':')[1].split(", ")]

        m = re.search(r"Operation: new = old (.*)",monkeylines[2])
        self.operation = m.group(1)

        self.test = int(monkeylines[3].split()[3])
        self.true = int(monkeylines[4].split()[5])
        self.false = int(monkeylines[5].split()[5])
        self.count = 0

        
    def __str__(self):
        string = str(self.id) + ": "
        for i in self.items:
            string = string + str(i) + ", "
        string = string[:-2]
        string = string + "\noperation: " + self.operation
        string = string + "\ntest: " + str(self.test)
        string = string + "\ntrue: " + str(self.true)
        string = string + "\nfalse: " + str(self.false)
        string = string + "\ncount: " + str(self.count)
        return string

    def get_items(self):
        return self.items

    def do_operation(self,current_item):
 #       print("op: ", self.operation[0],self.operation[2:])
        if self.operation[0] == "+":
            current_item = current_item + int(self.operation[2:])
        elif self.operation[0] == "*":
            if self.operation[2:] == "old":
                product = current_item
            else:
                product = int(self.operation[2:])
            current_item = current_item * product

        return current_item

    def test_item(self,item):
        if item % self.test == 0:
            return self.true
        else:
            return self.false

    def get_test(self):
        return self.test

    def add_item(self, item):
        self.items.append(item)

    def process_monkey(self, monkey_data , LCM):

        for i in range(len(self.items)):
            current_item = self.items.pop(0)
#            print("popped:",current_item,self.items)
            new_item = self.do_operation(current_item)
#            print(new_item, "% LCM = ", end="")
            new_item = new_item % LCM
#            print(new_item)

            target = self.test_item(new_item)

#            print("tossing item ", new_item, "to monkey",target)
            monkey_data[target].add_item(new_item)

            self.count = self.count + 1
            
    def get_count(self):
        return self.count

    def print_count(self):
        print("Monkey ",self.id,"inspected items ",self.count,"times.")

monkey_data = []

getfile = open('c:/users/ted/VSCode/AoC2022/Day11/input.txt', 'r').read().split("\n\n")


for monkey in getfile:
    monkeylines = monkey.splitlines()
    newmonkey = Monkey(monkey)
    print(newmonkey)
    monkey_data.append(newmonkey)

LCM = math.prod([monkey.get_test() for monkey in monkey_data])

for round in range(10000):
    for index in range(len(monkey_data)):
#        print (round, index)

        monkey_data[index].process_monkey(monkey_data,LCM)

#        for i in monkey_data:
#            print(i)

    if (round+1) in [1,20,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]:
        print("== After round ",round+1," ==")
        for index in range(len(monkey_data)):
            monkey_data[index].print_count()



highest = 0
second = 0

for i in monkey_data:
    val = i.get_count()
    if val > highest:
        second = highest
        highest = val
    elif val > second:
        second = val

print(highest,second)
print (highest*second)

#print(monkey_data)


