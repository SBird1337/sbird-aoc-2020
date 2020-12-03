import os
import re

content = ''
with open("day2/input12.txt", 'r') as f:
    content = f.read()

valid = 0

for match in re.findall(r'(\d+)-(\d+)\s*([aA-zZ]):\s*([aZ-zZ]+)', content):
    min = int(match[0])
    max = int(match[1])
    char = match[2]
    password = match[3]
    count = password.count(char)
    if (count >= min and count <= max):
        valid = valid+1
    
print(valid)