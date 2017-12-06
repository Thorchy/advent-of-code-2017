from itertools import count
from math import sqrt

PUZZLE_INPUT = 277678


def coord(number):
    if number == 1:
        return 0, 0

    ring_number = int(sqrt(number - 1) - 1) // 2 + 1
    group, direction = divmod(number - (2 * ring_number - 1) ** 2 - 1, 2 * ring_number)
    return [
        (-ring_number + direction + 1, ring_number),
        (ring_number, ring_number - direction - 1),
        (ring_number - direction - 1, -ring_number),
        (-ring_number, -ring_number + direction + 1)
    ][group]


def find_distance(value, base_value=1):
    x1, y1 = coord(base_value)
    x2, y2 = coord(value)
    return abs(x2 - x1) + abs(y2 - y1)


def sum_spiral():
    a, i, j = {(0, 0): 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0, 1, 0), (0, 0, -1), (1, -1, 0), (1, 0, 1)]:
            for _ in range(s + ds):
                i += di
                j += dj
                a[i, j] = sum(a.get((k, l), 0) for k in range(i - 1, i + 2)
                              for l in range(j - 1, j + 2))
                yield a[i, j]


def part2(n):
    for x in sum_spiral():
        if x > n: return x


def main():
    print part2(PUZZLE_INPUT)
    print "Day 3, Half 1: {}".format(find_distance(PUZZLE_INPUT))
    print "Day 3, Half 2: {}".format('Not Yet Implemented')


def test_spiral_case_1():
    assert find_distance(1) == 0


def test_spiral_case_2():
    assert find_distance(12) == 3


def test_spiral_case_3():
    assert find_distance(23) == 2


def test_spiral_case_4():
    assert find_distance(1024) == 31


if __name__ == '__main__':
    main()
