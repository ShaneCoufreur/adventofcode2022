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

def parse():
    global instructions
    instructions = [l for l in input]

@timer
def solve1():
    parse()
    i = 1
    s = []
    X = 1
    for ins in instructions:
        cmd = ins.split(" ")

        if cmd[0] == "noop":
            i += 1
            if i in [20, 60, 100, 140, 180, 220]:
                s.append((i, X, i*X))
        elif cmd[0] == "addx":
            c = int(cmd[1])

            i += 1
            if i in [20, 60, 100, 140, 180, 220]:
                s.append((i, X, i*X))
            X += c
            i += 1
            if i in [20, 60, 100, 140, 180, 220]:
                s.append((i, X, i*X))
    # print(s)
    return sum( map(lambda t: t[0] * t[1], s) )

@timer
def solve2():
    parse()

    i = 0
    output = []

    X = 1
    sprite = [ X-1, X, X+1 ]
    
    for ins in instructions:
        cmd = ins.split(" ")
        r = False
        if cmd[0] == "noop":
            if i%40 in sprite:
                r = True
            i+=1

            output.append( "#" if r else "." )
        elif cmd[0] == "addx":
            c = int(cmd[1])

            r = False
            print( i%40, sprite)
            if i%40 in sprite:
                r = True
            i +=1

            output.append( "#" if r else "." )
            X += c
            
            r = False
            print( i%40, sprite)
            if i%40 in sprite:
                r = True
            i +=1

            output.append( "#" if r else "." )

            sprite = [ X-1, X, X+1 ]
            
    s = ""
    for ind, c in enumerate(output):
        if ind % 40 == 0:
            s+= "\n"
        s += c
    print(s)


with open((__file__.rstrip("code.py")+"test2input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
   input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))