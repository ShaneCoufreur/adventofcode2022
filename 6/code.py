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
        #print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func  


datastream = ''

def parse():
    global datastream
    datastream = input[0]

@timer
def solve1():
    parse()
    for i in range(3, len(datastream)):
        slice = datastream[i-3:i+1]
        if len(slice) == len(set(slice)):
            return i+1

@timer
def solve2():
    parse()
    for i in range(13, len(datastream)):
        slice = datastream[i-13:i+1]
        if len(slice) == len(set(slice)):
            return i+1

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"test1input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"test2input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"test3input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"test4input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))