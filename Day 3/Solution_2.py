import re

# Open file and set up variables
f = open("AdventOfCode/Day 3/input.txt", "r")

mul_list = []

# Remove where the don't conditional statements stop the multiplication
text = f.read()
found_all_donts = False

while not found_all_donts:
    dnt = text.find("don't()")
    
    if dnt == -1:
        found_all_donts = True
    else:
        if text[dnt:].find("do()") == -1:
           text = text[:(dnt-1)]
        else:
            do = text[dnt:].find("do()")+dnt
            text = text[:(dnt)]+text[do+4:]
        
    

# Use a regular expression to create an array with all the correct multiplies
mul_l = re.findall("mul\([0-9]*,[0-9]*\)", text)
for m in mul_l:
    mul_list.append(m)
    
# Do the multiplication
total = 0

for m in mul_list:
    nums = ((m.split("("))[1]).split(",")
    total += int(nums[0])*int(nums[1].replace(")",""))

print("Total Sum = ", total)