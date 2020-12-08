#!/bin/env python3

import os

def contains_bag(bags, name, bag):
        for t in bags[bag]:
            if t[1] == name:
                return True
        return any(map(lambda t: contains_bag(bags, name, t[1]), bags[bag]))

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
    count = 0
    for bag in bags:
        if contains_bag(bags, "shiny gold", bag):
            count = count + 1
    print(count)
        