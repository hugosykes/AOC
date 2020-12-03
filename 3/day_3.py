def solve():
    lines = []
    for line in open("input.txt", "r").readlines():
        big_line = line.replace("\n", "")
        lines.append([big_line[i] for i in range(len(big_line))])

    x, y, count_of_trees = 0, 0, 0
    while y < len(lines):
        if lines[y][x % len(lines[1])] == '#':
            count_of_trees += 1
        x += 3
        y += 1
    return count_of_trees


def solve_part_2(list_of_slopes):
    lines = []
    for line in open("input.txt", "r").readlines():
        big_line = line.replace("\n", "")
        lines.append([big_line[i] for i in range(len(big_line))])

    count = 1
    for slope in list_of_slopes:
        x_crement, y_crement = slope
        x, y, count_of_trees = 0, 0, 0
        while y < len(lines):
            if lines[y][x % len(lines[1])] == '#':
                count_of_trees += 1
            x += x_crement
            y += y_crement
        count *= count_of_trees
    return count


if __name__ == '__main__':
    print(solve())
    print(solve_part_2([(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]))
