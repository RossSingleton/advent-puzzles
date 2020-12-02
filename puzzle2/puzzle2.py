def main():
    f = readFile('input.txt')
    part_1_final = 0
    part_2_final = 0

    for x in f:
        split_dict1 = x.split(": ")
        criteria = split_dict1[0]
        password = split_dict1[1]
        split_dict2 = criteria.split(" ")
        num_range = split_dict2[0]
        char = split_dict2[1]
        split_dict3 = num_range.split("-")
        low_num = int(split_dict3[0])
        high_num = int(split_dict3[1])

        count = 0
        for y in password:
            if y == char:
                count = count + 1
        if count >= low_num and count <= high_num:
            part_1_final = part_1_final + 1

        if (bool(password[low_num - 1] == char) ^ bool(password[high_num - 1] == char)):
            part_2_final = part_2_final + 1

    print("part 1:", part_1_final)
    print("part 2:", part_2_final)

def readFile(fileName):
    with open(fileName, 'r') as stream:
        passwords = stream.read().splitlines()

    return passwords

main()