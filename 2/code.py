# Advent of code Year 2022 Day 2 solution
# Author = Shane Coufreur
# Date = December 2022

rock = 1
paper = 2
scissors = 3

loss = 0
draw = 3
win = 6

def solve1():
    #print(input)
    # A = Rock, B = Paper, C = Scissors
    # X = Rock, Y = Paper, Z = Scissors
    draws = dict()
    draws[("A", "X")] = rock + draw
    draws[("A", "Y")] = paper + win
    draws[("A", "Z")] = scissors + loss
    draws[("B", "X")] = rock + loss
    draws[("B", "Y")] = paper + draw
    draws[("B", "Z")] = scissors + win
    draws[("C", "X")] = rock + win
    draws[("C", "Y")] = paper + loss
    draws[("C", "Z")] = scissors + draw

    sum = 0
    for round in input:
        sum += draws[ (round[0], round[1]) ]

    return sum
    
def solve2():
    # A = Rock, B = Paper, C = Scissors
    # X = loss, Y = draw, Z = Win
    draws = dict()
    draws[("A", "X")] = loss + scissors
    draws[("A", "Y")] = draw + rock
    draws[("A", "Z")] = win + paper
    draws[("B", "X")] = loss + rock
    draws[("B", "Y")] = draw + paper
    draws[("B", "Z")] = win + scissors
    draws[("C", "X")] = loss + paper
    draws[("C", "Y")] = draw + scissors
    draws[("C", "Z")] = win + rock

    sum = 0
    for round in input:
        sum += draws[ (round[0], round[1]) ]

    return sum

with open((__file__.rstrip("code.py")+"testinput.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = [l.strip() for l in input_file.readlines()]
print("Part One : "+ str(solve1()))
print("Part Two : "+ str(solve2()))