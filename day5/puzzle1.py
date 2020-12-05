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

print(max(seats))