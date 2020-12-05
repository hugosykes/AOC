def resolve_column_or_row(column_or_row, is_row):
    if is_row:
        range_length = 129
    else:
        range_length = 9

    start_range = [i for i in range(1, range_length)]

    for letter in column_or_row:
        new_length = int(len(start_range) / 2)
        if letter == "F" or letter == "L":
            start_range = start_range[:new_length]
        elif letter == "B" or letter == "R":
            start_range = start_range[new_length:]
    return start_range[0] - 1


def solve():
    lines = []
    for l in open("input.txt"):
        line = l.rstrip("\n")
        lines.append((line[:7], line[7:]))

    resolved = [(resolve_column_or_row(line[0], True), resolve_column_or_row(line[1], False)) for line in lines]
    return max([r[0] * 8 + r[1] for r in resolved])


def solve_part_2():
    lines = []
    for l in open("input.txt"):
        line = l.rstrip("\n")
        lines.append((line[:7], line[7:]))

    resolved = [(resolve_column_or_row(line[0], True), resolve_column_or_row(line[1], False)) for line in lines]
    seat_ids = [r[0] * 8 + r[1] for r in resolved]
    print([_id for _id in list(range(1024)) if _id not in seat_ids])


if __name__ == '__main__':
    print(solve())
    print(solve_part_2())
