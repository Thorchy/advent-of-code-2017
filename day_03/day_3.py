from math import sqrt

PUZZLE_INPUT = 277678
BASE_VALUE = 1


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


def find_distance(first, second):
    x1, y1 = coord(first)
    x2, y2 = coord(second)
    return abs(x2 - x1) + abs(y2 - y1)


print find_distance(BASE_VALUE, PUZZLE_INPUT)
