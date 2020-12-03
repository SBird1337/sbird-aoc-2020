#!/bin/python3
import os
import itertools

numbers = []
with open("day1/input12.txt", 'r') as f:
    for line in f.readlines():
        if line != None:
            numbers.append(int(line))

for tup in itertools.combinations(numbers, 2):
    if tup[0] + tup[1] == 2020:
        print(tup[0]*tup[1])
        break