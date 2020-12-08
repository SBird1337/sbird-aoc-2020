#!/bin/env python3

import os

def count_bags(bags, name):
    return 1 + sum(n * count_bags(bags, b) for n,b in bags[name])

bags = {}
with open('day7/input12.txt', 'r') as f:
    for line in f.readlines():
        name = line.split(' bags ')[0]
        contained = line.split(' contain ')[1].split(', ')
        contained[len(contained)-1] = contained[len(contained)-1].replace('.\n', '').replace('.', '')
        tuples = []
        for bag in contained:
            if bag.startswith('no'):
                break
            count = bag.split(' ')[0]
            bag = bag.replace(f'{count} ', '').replace(' bags', '').replace(' bag', '')
            tuples.append((int(count), bag))
        bags[name] = tuples
    print(count_bags(bags, 'shiny gold')-1)
        