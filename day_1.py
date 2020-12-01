from datetime import datetime

i = 0


def solve():
    start_time = datetime.now()
    numbers = []
    for line in open("input.txt", "r").readlines():
        numbers.append(int(line))

    def loop_daddy(_n1, num_list):
        for n2 in num_list:
            for n3 in num_list:
                if _n1 + n2 + n3 == 2020:
                    return _n1 * n2 * n3

    for n1 in numbers:
        looped = loop_daddy(_n1=n1, num_list=numbers)
        if looped:
            return looped, datetime.now() - start_time


if __name__ == '__main__':
    print(solve())
