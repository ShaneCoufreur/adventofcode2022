# Advent of code Year 2022 Day 3 solution
# Author = Shane Coufreur
# Date = December 2022

import string

#with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
#    input = [l.strip() for l in input_file.readlines()]

priorities = list(" ")
priorities += list(string.ascii_lowercase) + list(string.ascii_uppercase)

#print(priorities)

def solve1():
    matches = []
    for l in input:
        p1, p2 = l[:len(l)//2], l[len(l)//2:]

        for c in p1:
            if c in p2:
                matches.append(c)
                break

    return sum([priorities.index(m) for m in matches])
    
def solve2():
    matches = []
    grouplength = 3
    for g in range(len(input)//grouplength):
        for c in input[0+g*grouplength]:
            if c in input[1+g*grouplength] and c in input[2+g*grouplength]:
                matches.append(c)
                break
            
    return sum([priorities.index(m) for m in matches])

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))