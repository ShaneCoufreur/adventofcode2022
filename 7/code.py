# Advent of code Year 2022 Day 5 solution
# Author = Shane Coufreur
# Date = December 2022
from time import time

from collections import defaultdict
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


def parse():
    pass

@timer
def solve1():
    filesystem = defaultdict(int)
    path = Path('/')
    for line in input:
        if line.startswith("$ cd"):
            dirname = line[5:]
            path = (path / dirname).resolve()
        elif line.startswith("$ ls"):
            pass 
        elif line.startswith("dir"):
            pass
        else:
            size, name = line.split(" ")
            size = int(size)
            filesystem[path] += size
            for parent in path.parents:
                filesystem[parent] += size
    return sum( size for size in filesystem.values() if size <= 100000 )


@timer
def solve2():
    filesystem = defaultdict(int)
    path = Path('/')
    for line in input:
        if line.startswith("$ cd"):
            dirname = line[5:]
            path = (path / dirname).resolve()
        elif line.startswith("$ ls"):
            pass 
        elif line.startswith("dir"):
            pass
        else:
            size, name = line.split(" ")
            size = int(size)
            filesystem[path] += size
            for parent in path.parents:
                filesystem[parent] += size

    unused_space = filesystem[Path("/").resolve()]
    required = 30_000_000 - ( 70_000_000 - unused_space)

    return min(v for v in filesystem.values() if v >= required)

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))