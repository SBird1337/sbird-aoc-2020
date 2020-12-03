import os
import re

content = ''
with open("day2/input12.txt", 'r') as f:
    content = f.read()

valid = 0

for match in re.findall(r'(\d+)-(\d+)\s*([aA-zZ]):\s*([aZ-zZ]+)', content):
    first = int(match[0])
    second = int(match[1])
    char = match[2]
    password = match[3]
    matches = 0
    if password[first-1] == char:
        matches = matches + 1
    if password[second-1] == char:
        matches = matches + 1
    if matches == 1:
        valid = valid + 1
    
print(valid)