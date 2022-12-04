# Advent of code Year 2022 Day 4 solution
# Author = Shane Coufreur
# Date = December 2022
p1 = []
def parse():
    global p1
    p1 = []
    for l in input:
        elf1, elf2 = [l for l in l.split(",")]
        e1 = elf1.split("-")
        e2 = elf2.split("-")
        p1.append( ((int(e1[0]),int(e1[1])), (int(e2[0]),int(e2[1])))   )

def solve1():
    parse()
    overlap = []
    for e1, e2 in p1:
        s1 = set([i for i in range(e1[0], e1[1]+1)])
        s2 = set([i for i in range(e2[0], e2[1]+1)])
        o = s1.intersection(s2)

        #print(s1, s2, o, len(s1), len(s2), len(o))
        if len(o) == len(s1) or len(o) == len(s2):
            overlap.append(o)
            
    return len(overlap)
    
def solve2():
    parse()
    overlap = []
    for e1, e2 in p1:
        s1 = set([i for i in range(e1[0], e1[1]+1)])
        s2 = set([i for i in range(e2[0], e2[1]+1)])
        o = s1.intersection(s2)

        #print(s1, s2, o, len(s1), len(s2), len(o))
        if len(o) > 0:
            overlap.append(o)
            
    return len(overlap)

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))