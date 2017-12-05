import csv
import os

LARGEST_SMALLEST = False


def largest_smallest(filepath):
    with open(filepath) as f:
        csv_reader = csv.reader(f, delimiter='\t')

        checksum = 0

        # Create checksum with the largest - smallest integer
        for row in csv_reader:
            row = map(int, row)
            largest = max(row)
            smallest = min(row)
            difference = largest - smallest
            checksum += difference

        return checksum


def divide_whole(filepath):
    with open(filepath) as f:
        csv_reader = csv.reader(f, delimiter='\t')

        checksum = 0
        # Create checksum by dividing the 2 integers that divide whole
        for row in csv_reader:
            row = map(int, row)
            number_1 = None
            number_2 = None
            for x in row:
                first = True
                for y in row:
                    if x == y and first:
                        first = False
                        continue
                    if x % y == 0:
                        number_1 = x
                        number_2 = y

            checksum += number_1 / number_2

        return checksum


def main():
    print "Day 2, Half 1: {}".format(largest_smallest(os.path.join(os.path.dirname(__file__), 'input.txt')))
    print "Day 2, Half 2: {}".format(divide_whole(os.path.join(os.path.dirname(__file__), 'input.txt')))


def test_largest_smallest():
    assert largest_smallest(os.path.join(os.path.dirname(__file__), 'test_input_01.txt')) == 18


def test_divide_whole():
    assert divide_whole(os.path.join(os.path.dirname(__file__), 'test_input_02.txt')) == 9


if __name__ == '__main__':
    main()
