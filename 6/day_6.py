def solve():
    lines = []
    for line in open("input.txt"):
        lines.append(line.rstrip("\n"))

    passengers = []
    tmp_line = ""
    for line in lines:
        if line == "":
            passengers.append(tmp_line)
            tmp_line = ""
        else:
            if tmp_line == "":
                tmp_line += line
            else:
                tmp_line += f" {line}"

    print(sum([len(set(passenger.replace(" ", ""))) for passenger in passengers]))


def count_common_strings(list_of_strings):
    first_one = list_of_strings[0]
    count = 0
    for str_1 in first_one:
        if all([str_1 in str_2 for str_2 in list_of_strings[1:]]):
            count += 1
    return count


def solve_part_two():
    lines = []
    for line in open("input.txt"):
        lines.append(line.rstrip("\n"))

    groups = []
    tmp_line = ""
    for line in lines:
        if line == "":
            groups.append(tmp_line)
            tmp_line = ""
        else:
            if tmp_line == "":
                tmp_line += line
            else:
                tmp_line += f" {line}"
    list_of_groups = [group.split(" ") for group in groups]
    return sum(
        [
            count_common_strings(group)
            for group
            in list_of_groups
        ]
    )


if __name__ == '__main__':
    # solve()
    print(solve_part_two())
