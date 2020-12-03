import os

def is_tree_at(line, col, mod, map):
    col = col % mod
    return map[line][col]

map = []
with open('day3/input12.txt', 'r') as f:
    for line in f.readlines():
        map.append([c == '#' for c in line])

mod = len(map[0])-1
bottom = len(map)

current_line = 0
current_column = 0
trees = 0

while current_line < bottom:
    if is_tree_at(current_line, current_column, mod, map):
        trees = trees+1
    current_line = current_line+1
    current_column = current_column+3

print(trees)
