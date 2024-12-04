def XMAS(a,b,c,d,e):
    if a == "M" and b == "S" and c == "A" and d == "M" and e =="S":
        return True
    elif a == "S" and b == "M" and c == "A" and d == "S" and e =="M":
        return True
    elif a == "S" and b == "S" and c == "A" and d == "M" and e =="M":
        return True
    elif a == "M" and b == "M" and c == "A" and d == "S" and e =="S":
        return True
    else:
        return False

f = open("AdventOfCode/Day 4/input.txt", "r")

# Define a matrix
y = len(f.readlines())
matrix = [[] for y in range(y)] 

f = open("AdventOfCode/Day 4/input.txt", "r")

y = 0

for l in f:
    l.replace("\n","")
    matrix[y] = list(l)
    y+=1

# Start the count
count = 0

# Search over every possible square that fits (up direction)
for y in range(len(matrix)-2):
    for x in range(len(matrix[0])-3):
        if XMAS(matrix[y][x], matrix[y][x+2], matrix[y+1][x+1], matrix[y+2][x], matrix[y+2][x+2]):
            count += 1
           
print("Total Count = ", count)