from datetime import datetime


def solve():
    start_time = datetime.now()
    numbers = []
    for line in open("day_1_input.txt", "r").readlines():
        numbers.append(int(line))

    def loop(n1, num_list, minimum):
        for n2 in num_list:

            if n2 + minimum > 2020:
                continue

            for n3 in num_list:
                if n1 + n2 + n3 == 2020:
                    return n1 * n2 * n3

    for _n1 in numbers:
        looped = loop(n1=_n1, num_list=numbers, minimum=min(*numbers))
        if looped:
            return looped, datetime.now() - start_time
        else:
            numbers.remove(_n1)


if __name__ == '__main__':
    print(solve())
