#!/bin/python3
import random
abc = ['A','B','C']
xyz = ['X','Y','Z']
seed = 939482
random.seed(seed)

output = open('largeinput.txt', 'w')

for i in range(100_000_000):
    first = random.randrange(3)
    second = random.randrange(3)
    #print(abc[first] + " "+ xyz[second])
    output.write(abc[first]+" "+xyz[second]+"\nl")

output.close()