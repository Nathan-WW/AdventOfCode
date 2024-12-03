import re

# Open file and set up variables
f = open("AdventOfCode/Day 3/input.txt", "r")

mul_list = []

# Use a regular expression to create an array with all the correct multiplies
for l in f:
    mul_l = re.findall("mul\([0-9]*,[0-9]*\)", l)
    for m in mul_l:
        mul_list.append(m)
    
# Do the multiplication
total = 0

for m in mul_list:
    nums = ((m.split("("))[1]).split(",")
    total += int(nums[0])*int(nums[1].replace(")",""))

print("Total Sum = ", total)