# Advent of code Year 2022 Day 5 solution
# Author = Shane Coufreur
# Date = December 2022
from time import time

from pathlib import Path

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

grid = []
max_x = 0
def parse():
    global grid, max_x, max_y
    grid = [[int(c) for c in line] for line in input]
    max_x = len(grid[0])
    max_y = len(grid)

@timer
def solve1():
    visible = 0
    parse()
    for y in range(max_y):
        for x in range(max_x):
            if y == 0 or x == 0 or y == max_y-1 or x == max_x-1:
               visible += 1 
            else:
                row = grid[y]
                col = [row[x] for row in grid]
                val = grid[y][x]

                if max(row[:x]) < val or max(row[x+1:]) < val or max(col[:y]) < val or max(col[y+1:]) < val:
                    visible += 1

    return visible


@timer
def solve2():
    parse()
    max_score = 0
    for y in range(max_y):
        for x in range(max_x):
            score = 0
            score = 1

            t = 0
            for i in range(x - 1, -1, -1):
                t += 1
                if grid[y][i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(x + 1, max_x):
                t += 1
                if grid[y][i] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y - 1, -1, -1):
                t += 1
                if grid[i][x] >= grid[y][x]:
                    break
            score *= t

            t = 0
            for i in range(y + 1, max_y):
                t += 1
                if grid[i][x] >= grid[y][x]:
                    break
            score *= t

            max_score = max(max_score, score)

    return max_score

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))