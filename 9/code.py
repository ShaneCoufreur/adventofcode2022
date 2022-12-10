# Advent of code Year 2022 Day 5 solution
# Author = Shane Coufreur
# Date = December 2022
from time import time

from collections import defaultdict

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


instructions = []
def split_input(l):
    s = l.split(" ")
    return ( s[0], int(s[1]))

def parse():
    global instructions
    instructions = [split_input(l) for l in input]

def solve(n):
    knots = [[0,0] for i in range(10)]
    positions = [{(0,0)} for i in range(10)]
    movement = {'R': (1,0),
                'L': (-1,0),
                'U': (0,1),
                'D': (0,-1)}
    for instruction in instructions:
        for _ in range(instruction[1]):
            knots[0] = [knots[0][0]+movement[instruction[0]][0],knots[0][1]+movement[instruction[0]][1]]
            for j in range(1,10):
                taildiff = (knots[j-1][0]-knots[j][0])**2+(knots[j][1]-knots[j-1][1])**2
                if taildiff in [4,5,8]:
                    for i in [0,1]:
                        if knots[j-1][i] != knots[j][i]:
                            if knots[j-1][i] > knots[j][i]:
                                knots[j][i] += 1
                            else:
                                knots[j][i] -= 1
                    positions[j].add((knots[j][0],knots[j][1]))

    return len(positions[n])


@timer
def solve1():
    parse()
    return solve(1)

@timer
def solve2():
    parse()
    return solve(9)

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))

with open((__file__.rstrip("code.py")+"test2input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))