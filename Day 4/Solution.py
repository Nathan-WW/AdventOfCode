def XMAS(a,b,c,d):
    if a == "X" and b == "M" and c == "A" and d == "S":
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

# Check straight horizontal
for y in range(len(matrix)):
    for x in range(len(matrix[0])-4):
        if XMAS(matrix[y][x], matrix[y][x+1], matrix[y][x+2], matrix[y][x+3]):
            count += 1
            
# Check reverse horizontal
for y in range(len(matrix)):
    for x in range(len(matrix[0])-4):
        if XMAS(matrix[y][x+3], matrix[y][x+2], matrix[y][x+1], matrix[y][x]):
            count += 1

# Check straight down
for x in range(len(matrix)):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y][x], matrix[y+1][x], matrix[y+2][x], matrix[y+3][x]):
            count += 1
            
# Check reverse down
for x in range(len(matrix)):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y+3][x], matrix[y+2][x], matrix[y+1][x], matrix[y][x]):
            count += 1

# Check diag up NE /
for x in range(len(matrix)-3):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y+3][x], matrix[y+2][x+1], matrix[y+1][x+2], matrix[y][x+3]):
            count += 1

# Check diag up SE \
for x in range(len(matrix)-3):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y+3][x+3], matrix[y+2][x+2], matrix[y+1][x+1], matrix[y][x]):
            count += 1
    
# Check diag down NE /
for x in range(len(matrix)-3):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y][x+3], matrix[y+1][x+2], matrix[y+2][x+1], matrix[y+3][x]):
            count += 1

# Check diag down SE \
for x in range(len(matrix)-3):
    for y in range(len(matrix[0])-4):
        if XMAS(matrix[y][x], matrix[y+1][x+1], matrix[y+2][x+2], matrix[y+3][x+3]):
            count += 1

print("Total Count = ", count)