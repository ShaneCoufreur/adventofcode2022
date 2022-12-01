# Advent of code Year 2022 Day 1 solution
# Author = Shane Coufreur
# Date = December 2022

elfs = []
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.readlines()

    data = []
    for inp in input:
        if inp == "\n":
            elfs.append(data)
            data = []
        else:
            data.append(int(inp))
    
    elfs.append(data)
    
    #print(elfs)

def solve1():
    sorted = [sum(value) for value in elfs]
    sorted.sort()
    return sorted[-1:][0]

def solve2():
    sorted = [sum(value) for value in elfs]
    sorted.sort()
    return sum(sorted[-3:])

print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))
