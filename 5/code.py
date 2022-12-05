# Advent of code Year 2022 Day 5 solution
# Author = Shane Coufreur
# Date = December 2022

containers = []
instructions = []
def parse():
    global containers, instructions
    stacks, instructions = input.split("\n\n")
    stacks = stacks.split("\n")
    instructions = instructions.split("\n")

    containers, maxStacks, charsPerStack = [], max([int(x) for x in stacks[-1].split("   ")]), 4

    for stackNumber in range(maxStacks):
        column, index = [], stackNumber * charsPerStack + 1
        for line in range(len(stacks) - 1):
            if stacks[line][index] != " ": column.append(stacks[line][index])
        containers.append(column)
    return containers

def solve1():
    parse()
    global instructions, containers
    for instruction in instructions:
        _, n, _, f, _, t = instruction.split(" ")

        for _ in range(int(n)):
            tmp, containers[int(f)-1] = containers[int(f)-1][0], containers[int(f)-1][1:]
            containers[int(t)-1] = [tmp] + containers[int(t)-1]
    
    return "".join([c[0] for c in containers])

def solve2():
    parse()
    global instructions, containers
    for instruction in instructions:
        _, n, _, f, _, t = instruction.split(" ")

        tmp, containers[int(f)-1] = containers[int(f)-1][:int(n)], containers[int(f)-1][int(n):]
        containers[int(t)-1] = tmp + containers[int(t)-1]
    
    return "".join([c[0] for c in containers])

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = input_file.read()
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = input_file.read()
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))