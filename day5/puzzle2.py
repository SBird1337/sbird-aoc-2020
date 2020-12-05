#!/bin/env python3

def search_seat(spec):
    seat = 0
    q = 512
    for char in spec:
        if char == 'B' or char == 'R':
            seat = seat | q
        q = q >> 1
    return seat

seats = []
with open('day5/input12.txt', 'r') as f:
    for line in f.readlines():
        seats.append(search_seat(line))

candidates = [x for x in range(1,1024) if x not in seats and x > 69 and x < 939]
print(candidates[0])