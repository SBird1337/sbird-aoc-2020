#!/bin/env python3
import os
groups = []

with open('day6/input12.txt', 'r') as f:
    for group in f.read().split('\n\n'):
        group = group.replace('\n', '')
        groups.append(len("".join(set(group))))

print(sum(groups))