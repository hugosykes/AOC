import re


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

    passenger_field_lists = [
        [field for field in passenger.split(" ") if "cid" not in field] for passenger in passengers
    ]
    valid_count = 0
    for field_list in passenger_field_lists:
        if len(field_list) == 7:
            valid_count += 1

    return valid_count


def validate(field_list):
    for field in field_list:
        if field[0] == 'byr':
            if not (1920 <= int(field[1]) <= 2002):
                return False

        if field[0] == 'iyr':
            if not (2010 <= int(field[1]) <= 2020):
                return False

        if field[0] == 'eyr':
            if not (2020 <= int(field[1]) <= 2030):
                return False

        if field[0] == 'hgt':
            if field[1][-2:] == "cm":
                if not (150 <= int(field[1][:-2]) <= 193):
                    return False
            elif field[1][-2:] == "in":
                if not (59 <= int(field[1][:-2]) <= 76):
                    return False
            else:
                return False

        if field[0] == 'hcl':
            if not (re.search("#[0-9a-f]{6}", field[1]) and len(field[1]) == 7):
                return False

        if field[0] == 'ecl':
            if field[1] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                return False

        if field[0] == 'pid':
            if not (re.search("[0-9]{9}", field[1]) and len(field[1]) == 9):
                return False

    return True


def solve_part_2():
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

    passenger_field_lists = [
        [field.split(":") for field in passenger.split(" ") if "cid" not in field] for passenger in passengers
    ]

    valid_count = 0
    for field_list in passenger_field_lists:
        if len(field_list) == 7 and validate(field_list):
            valid_count += 1

    return valid_count


if __name__ == '__main__':
    print(solve())
    print(solve_part_2())
