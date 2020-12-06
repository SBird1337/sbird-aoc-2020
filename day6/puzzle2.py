#!/bin/env python3
import os
groups = []

with open('day6/input12.txt', 'r') as f:
    for group in f.read().split('\n\n'):
        group_answers = []
        for person in group.split("\n"):
            group_answers.append(set(person))
        groups.append(len(set.intersection(*group_answers)))

print(sum(groups))