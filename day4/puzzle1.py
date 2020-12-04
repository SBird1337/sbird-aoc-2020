import os

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

passports = [[]]
with open('day4/input12.txt', 'r') as f:
    for line in f.readlines():
        if line == '\n':
            passports.append([])
        else:
            for entry in line.split(' '):
                passports[len(passports)-1].append(entry)

valid = 0

for passport in passports:
    entry_dict = {}
    for entry in passport:
        entry_dict[entry[0:3]] = entry[4:].replace('\n','')

    current_valid = True

    for req in required_fields:
        if not req in entry_dict:
            current_valid = False
            break
    
    if current_valid:
        valid = valid+1

print(valid)
