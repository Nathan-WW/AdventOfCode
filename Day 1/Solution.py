import numpy as np

f = open("AdventOfCode/Day 1/input.txt", "r")

l_arr = []
r_arr = []

for l in f:
    l_arr.append(int(l.split("   ")[0]))
    r_arr.append(int(l.split("   ")[1]))

l_arr.sort()
r_arr.sort()

dists = []
sim = 0

for i in range(len(l_arr)):
    dists.append(abs(l_arr[i]-r_arr[i]))
    n = 0
    for j in range(len(r_arr)):
        if l_arr[i] == r_arr[j]:
            n += 1
    sim += l_arr[i]*n
    
print(sum(dists))
print (sim)
