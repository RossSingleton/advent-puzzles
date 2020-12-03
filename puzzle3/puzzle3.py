def count_trees(right, down):
    trees = 0
    with open('input.txt') as f:
        text = f.read().splitlines()
        for x, lines in enumerate(text[::down]):
            trees += lines[(x * right) % len(lines)] == "#"
    return trees

def part_two():
    slope1 = count_trees(1, 1)
    slope2 = count_trees(3, 1)
    slope3 = count_trees(5, 1)
    slope4 = count_trees(7, 1)
    slope5 = count_trees(1, 2)

    result = slope1 * slope2 * slope3 * slope4 * slope5
    return result

print("part 1:", count_trees(1, 2))
print("part 2:", part_two())