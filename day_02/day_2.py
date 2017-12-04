import csv

LARGEST_SMALLEST = False
with open('input.txt') as f:
    csv_reader = csv.reader(f, delimiter='\t')

    checksum = 0

    if LARGEST_SMALLEST:
        # Create checksum with the largest - smallest integer
        for row in csv_reader:
            row = map(int, row)
            largest = max(row)
            smallest = min(row)
            difference = largest - smallest
            checksum += difference

    else:
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

    print checksum
