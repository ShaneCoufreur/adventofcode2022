# Advent of code Year 2022 Day 5 solution
# Author = Shane Coufreur
# Date = December 2022
from time import time
  
def timer(func):
    # This function shows the execution time of 
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func  


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

@timer
def solve1():
    parse()
    global instructions, containers
    for i, instruction in enumerate(instructions):
        _, n, _, f, _, t = instruction.split(" ")
        if i % (len(instructions) / 10000) == 0:
            pass
            #print( f"Handling {i} of {len(instructions)} instructions.")
        tmp, containers[int(f)-1] = containers[int(f)-1][:int(n)], containers[int(f)-1][int(n):]
        tmp.reverse()
        tmp += containers[int(t)-1]
        containers[int(t)-1] = tmp
    
    return "".join([c[0] for c in containers])

@timer
def solve2():
    parse()
    global instructions, containers
    for i, instruction in enumerate(instructions):
        _, n, _, f, _, t = instruction.split(" ")
        if i % (len(instructions) / 10000) == 0:
            pass
            #print( f"Handling {i} of {len(instructions)} instructions.")

        tmp, containers[int(f)-1] = containers[int(f)-1][:int(n)], containers[int(f)-1][int(n):]
        #containers[int(t)-1] = tmp + containers[int(t)-1]
        tmp += containers[int(t)-1]
        containers[int(t)-1] = tmp
    
    return "".join([c[0] for c in containers])

# with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
#     input = input_file.read()
# print("Part One : "+ str(solve1()))
# print("Part Two : "+ str(solve2()))

# with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
#    input = input_file.read()
# print("Part One : "+ str(solve1()))
# print("Part Two : "+ str(solve2()))

# with open((__file__.rstrip("code.py")+"largeinput.txt"), 'r') as input_file:
#    input = input_file.read()
# print("Part One : "+ str(solve1()))
# print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"hugeinput.txt"), 'r') as input_file:
   input = input_file.read()
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))