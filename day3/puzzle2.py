import os

def is_tree_at(line, col, mod, map):
    col = col % mod
    return map[line][col]

def check_slope(right, down, bottom, mod, map):
    current_line = 0
    current_column = 0
    trees = 0
    while current_line < bottom:
        if is_tree_at(current_line, current_column, mod, map):
            trees = trees+1
        current_line = current_line + down
        current_column = current_column + right
    return trees

map = []
with open('day3/input12.txt', 'r') as f:
    for line in f.readlines():
        map.append([c == '#' for c in line])

mod = len(map[0])-1
bottom = len(map)

result = check_slope(1,1, bottom, mod, map) * check_slope(3,1, bottom, mod, map) * check_slope(5,1, bottom, mod, map) * check_slope(7,1, bottom, mod, map) * check_slope(1,2, bottom, mod, map)
print(result)
