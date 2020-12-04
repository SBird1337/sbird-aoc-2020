import os

eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def validate_entry(key, value):
    if key == 'byr':
        if len(value) != 4:
            return False
        if not value.isnumeric():
            return False
        return int(value) >= 1920 and int(value) <= 2002
    elif key == 'iyr':
        if len(value) != 4:
            return False
        if not value.isnumeric():
            return False
        return int(value) >= 2010 and int(value) <= 2020
    elif key == 'eyr':
        if len(value) != 4:
            return False
        if not value.isnumeric():
            return False
        return int(value) >= 2020 and int(value) <= 2030
    elif key == 'hgt':
        number = value[0:-2]
        ext = value[-2:]
        if not number.isnumeric():
            return False
        number = int(number)
        if ext == 'cm':
            return number >= 150 and number <=193
        if ext == 'in':
            return number >= 59 and number <=76
        return False
    elif key == 'hcl':
        if value[0:1] != '#':
            return False
        if len(value[1:]) != 6:
            return False
        try:
            int(value[1:], 16)
            return True
        except:
            return False
    elif key == 'ecl':
        return value in eye_colors
    elif key == 'pid':
        return len(value) == 9 and value.isnumeric()
    else:
        return True

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
        if not validate_entry(req, entry_dict[req]):
            current_valid = False
            break
    
    if current_valid:
        valid = valid+1

print(valid)
