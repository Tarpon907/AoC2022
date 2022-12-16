import scipy as sp
import matplotlib.pylab as plt
import numpy as np
import re
import time

alphabet = "abcdefghijklmnopqrstuvwxyz"
start_time = time.time()

lines = open('c:/users/ted/vscode/AoC2022/Day12/input.txt', 'r').readlines()

height = len(lines)
width = len(lines[0].strip())

elevation = np.ndarray((height,width),dtype=int)
dijkstra = np.full((height,width),fill_value=1000000000000)
minmatrix = np.full((height,width),fill_value=1000000000000)
visited = np.full((height,width),fill_value=False)
total_nodes = width * height


for i in range(len(lines)):
    line = lines[i].strip()
    for j in range(len(line)):
        if line[j] == "S":
            start_coords = [i,j]
            elevation[i][j] = 0
        elif line[j] == "E":
            end_coords = [i,j]
            elevation[i][j] = 25
        else:
            elevation[i][j] = alphabet.index(line[j])
#        unvisited.append([i,j])
#print (elevation)




def visit(i,j):
#    print(dijkstra)
#    print("visiting: ",i,j)
    cur_height = elevation[i][j]
    neighbor_steps = [1000000000001] * 4
    neighbor_dir = [[-1,0],[1,0],[0,-1],[0,1]]
    if i > 0:
        if elevation[i-1][j] <= cur_height + 1:
            neighbor_steps[0] = 1
    if i < height-1:
        if elevation[i+1][j] <= cur_height + 1:
            neighbor_steps[1] = 1
    if j > 0:
        if elevation[i][j-1] <= cur_height + 1:
            neighbor_steps[2] = 1
    if j < width-1:
        if elevation[i][j+1] <= cur_height + 1:
            neighbor_steps[3] = 1
#    print (neighbor_steps)
   

    while len(neighbor_steps) > 0:
#        print(neighbor_steps)
        min_neighbor_steps = min(neighbor_steps)
#        print("min",min_neighbor_steps)
        if min_neighbor_steps == 1000000000001:
            break
        index = neighbor_steps.index(min_neighbor_steps)
#        print("index",index)
        neighbor_i = i + neighbor_dir[index][0]
        neighbor_j = j + neighbor_dir[index][1]
#        print("checking neighbor at: ",neighbor_i, neighbor_j)
#        print(visited)
        if not visited[neighbor_i][neighbor_j]:
            dijkstra[neighbor_i][neighbor_j] = min(dijkstra[i][j] + 1,dijkstra[neighbor_i][neighbor_j])
#            print("d:",dijkstra[neighbor_i][neighbor_j])
            minmatrix[neighbor_i][neighbor_j] = dijkstra[neighbor_i,neighbor_j]
        neighbor_steps.pop(index)
        neighbor_dir.pop(index)
#        print(dijkstra)
    visited[i][j] = True
#    unvisited.remove([i,j])
    minmatrix[i][j] = 1000000000001;

    return

shortest_hike = 1000000000001
for map_index in range(total_nodes):
    map_r = int(map_index / width)
    map_c = map_index % width

#    if map_c == 0:
#        print(shortest_hike, lines[map_r].strip())
#    print("%2d at %3d,%3d" % (elevation[map_r][map_c],map_r,map_c))
    if elevation[map_r][map_c] != 0:
        continue

    dijkstra[map_r][map_c] = 0

map_r, map_c = start_coords
visit(map_r,map_c)


total_visited = 1
    #print("[0,0]: ", dijkstra[0][0])

while total_visited < total_nodes:
    min_i = 0
    min_j = 0
    min_val = 1000000000000
#    for point in unvisited:
#        i, j = point
#        if dijkstra[i][j] < min_val and visited[i][j] == False:
#                min_val = dijkstra[i][j]
#                min_i = i
#                min_j = j
#    print("minmatrix: ", minmatrix)
    index = np.argmin(minmatrix)

    i = int(index / width)
    j = index % width
    if i == end_coords[0] and j == end_coords[1]:
        break
#    print("argmin index:", index, "coirelates to: ", i, j)
    visit(i, j)
    total_visited += 1
#    if dijkstra[0][0] != 0:
#        print (dijkstra)
#        print ("visiting: ",i,j)

shortest_hike = min(shortest_hike,dijkstra[end_coords[0],end_coords[1]])
print(shortest_hike, dijkstra[end_coords[0],end_coords[1]])







print("execution time (in ms): ",(time.time()-start_time)*1000) 
