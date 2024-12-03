import numpy as np

def safe(x):
    IsSafe = 1
    
    for i in range(len(x)-1):
        if abs(x[i+1] - x[i])>3:
            IsSafe = 0
            break
        
        if not all(i < j for i, j in zip(x, x[1:])):  
            if not all(i > j for i, j in zip(x, x[1:])):
                IsSafe = 0
        
    return IsSafe

def safe_dampener(x):
    IsSafe = 0
    
    if safe(x):
        IsSafe = 1
    else:
        for i in range(len(x)):
            temp = x[:]
            temp.pop(i)
            xx = temp
            if safe(xx):
                IsSafe = 1
                break
    
    return IsSafe
            

f = open("AdventOfCode/Day 2/input.txt", "r")

report = []

for l in f:
    report.append(list(map(int, (l.split(" ")))))
    
safe_reports = 0
safe_dampener_reports = 0

for r in report:
    safe_reports += safe(r)
    safe_dampener_reports += safe_dampener(r)
    
print("Safe Reports: ", safe_reports)
print("Safe Dampened Reports: ", safe_dampener_reports)