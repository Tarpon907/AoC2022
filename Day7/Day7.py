from __future__ import annotations
import matplotlib.pylab as plt
import numpy as np
import re
import time
from itertools import permutations
import string


start_time = time.time()

class Directory:
    def __init__(self,name, parent : Directory = None):
        self.name = name
        self.subdirs = dict()
        self.files = dict()
        self.parent = parent
        self.size = int(0)
    
    def add_subdir(self,subdir):
        if subdir in self.subdirs:
            return
        newsubdir = Directory(subdir,self)
        self.subdirs[subdir] = newsubdir

    def add_file(self,file,size):
        if file in self.files:
            return
        self.files[file]=size

    def get_subdir(self,subdir):
        return self.subdirs[subdir]

    def get_parentdir(self):
        return self.parent

    def get_dirname(self):
        return self.name

    def get_dirsize(self):
        return self.size

    def calculate_size(self) -> int:
        for i in self.subdirs.keys():
            self.size = self.size + self.subdirs[i].calculate_size()
        for f in self.files.keys():
            self.size = self.size + int(self.files[f])
        return self.size

    def get_total_size_under_cap(self,cap = 100000):
        total = 0
        for i in self.subdirs.keys():
            total = total + self.subdirs[i].get_total_size_under_cap()
        if self.size < cap:
            total = total + self.get_dirsize()
        return total
            
    def find_smallest_greater_than(self, needed : int):

        smallest = 70000000

        for i in self.subdirs.keys():
            subdir_smallest = self.subdirs[i].find_smallest_greater_than(needed)
            if subdir_smallest < smallest:
                smallest = subdir_smallest
        if self.get_dirsize() > needed and self.get_dirsize() < smallest:
            if smallest != 70000000:
                print("smallest is now directory", self.get_dirname(), " with size ", self.getdirsize())
            smallest = self.get_dirsize()
        if smallest != 70000000:
            print(self.get_dirname(), needed, smallest)
        return smallest


        




        if self.get_dirsize() > needed and self.get_dirsize() < smallest:
            smallest = self.get_dirsize()

        return smallest

    def build_dir_string(self, indent : int = 0) -> str:
        foo = 0
        mystring = "".ljust(indent)
        mystring = mystring +  "- " + self.name
        mystring = mystring + " (SIZE = " + str(self.size) + ")\n"
        for i in self.subdirs.keys():
            mystring = mystring + str(self.subdirs[i].build_dir_string(indent + 2))
        for i in self.files.keys():
            mystring = mystring + "".ljust(indent+2) + "- "
            mystring = mystring + i + " (file, size = " + self.files[i] + ")\n"
        return mystring

    def __str__(self):
        return self.build_dir_string()
        


    




getfile = open('c:/users/ted/VSCode/AoC2022/Day7/input.txt', 'r').read().splitlines()

filesystem  = Directory("/")
pointer = filesystem
lineindex = 0
for line in getfile:
#    print(line)
    if line[:4] == '$ cd':
        print ("cd ",end = "")
        if line[5] == "/":
            print ("/")
            pointer = filesystem
        elif line[5:7] == "..":
            print (".. to ", end = "")
            pointer = pointer.get_parentdir()
            print(pointer.get_dirname())

        else:
            subdir = line[5:]
            print ("to subdir", subdir)
            pointer = pointer.get_subdir(subdir)
    elif line[:4] == '$ ls':
        continue
    elif line[:4] == "dir ":
        pointer.add_subdir(line[4:])
    else:
        size, name = line.split(" ")
        pointer.add_file(name,size)


filesystem.calculate_size()
#print(filesystem)

fulldisk = 70000000
unused = fulldisk - filesystem.get_dirsize()
needed = 30000000 - unused

#print("fulldisk", fulldisk, "getdirsize", filesystem.get_dirsize(), "unused", unused, "neeeded", needed)

print(filesystem.find_smallest_greater_than(needed))






print("execution time (in ms): ",(time.time()-start_time)*1000) 
