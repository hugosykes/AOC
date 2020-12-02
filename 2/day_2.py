def solve_part_one():
    valid = 0
    for line in open("day_2_input.txt", "r").readlines():
        condition, letter, password = line.split(" ")
        letter = letter.replace(":", "")
        minimum, maximum = condition.split("-")
        if int(minimum) <= password.count(letter) <= int(maximum):
            valid += 1
    print(valid)


def solve_part_two():
    valid = 0
    for line in open("day_2_input.txt", "r").readlines():
        condition, letter, password = line.split(" ")
        letter = letter.replace(":", "")
        minimum, maximum = condition.split("-")
        if password[int(minimum) - 1] == letter or password[int(maximum) - 1] == letter:
            if not (password[int(minimum) - 1] == letter and password[int(maximum) - 1] == letter):
                valid += 1
    print(valid)


if __name__ == '__main__':
    solve_part_one()
    solve_part_two()
