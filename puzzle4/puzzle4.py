import re

def part_one():
    passports = 0
    with open('input.txt') as f:
        text = [parse(fields) for fields in f.read().split('\n\n')]
        for x in range(len(text)):
            if 'byr' in text[x].keys() and 'iyr' in text[x].keys() and 'eyr' in text[x].keys() and 'hgt' in text[x].keys() and 'hcl' in text[x].keys() and 'ecl' in text[x].keys() and 'pid' in text[x].keys():
                passports += 1
    return passports

def part_two():
    passports = 0
    with open('input.txt') as f:
        text = [parse(fields) for fields in f.read().split('\n\n')]
        for x in range(len(text)):
            if 'byr' in text[x].keys() and 'iyr' in text[x].keys() and 'eyr' in text[x].keys() and 'hgt' in text[x].keys() and 'hcl' in text[x].keys() and 'ecl' in text[x].keys() and 'pid' in text[x].keys():
                # y = re.search("[0-9]{4}", text[x]['byr'])
                if (int(text[x]['byr']) >= 1920 and int(text[x]['byr']) <= 2002):
                    # y = re.search("[0-9]{4}", text[x]['iyr'])
                    if(int(text[x]['iyr']) >= 2010 and int(text[x]['iyr']) <= 2020):
                        # y = re.search("[0-9]{4}", text[x]['eyr'])
                        if(int(text[x]['eyr']) >= 2020 and int(text[x]['eyr']) <= 2030):
                            y = check_valid_height(text[x]['hgt'])
                            if y:
                                y = re.search("#[0-9|a-f]{6}", text[x]['hcl'])
                                if(y):
                                    y = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
                                    if text[x]['ecl'] in y:
                                        y = re.search("^[0-9]{9}$", text[x]['pid'])
                                        if y:
                                            passports += 1
    return passports

def check_valid_height(text):
    hgt_len = len(text) - 2
    if text[-2:] == 'cm':
        if int(text[:hgt_len]) >= 150 and int(text[:hgt_len]) <= 193:
            return True
    elif text[-2:] == 'in':
        if int(text[:hgt_len]) >= 59 and int(text[:hgt_len]) <= 76:
            return True
    return False

def parse(data):
    return dict(field.split(':') for field in data.split())

print("part one:", part_one())
print("part two:", part_two())