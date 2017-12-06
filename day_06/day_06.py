import csv
import os

from copy import copy


def parse_input(filepath):
    with open(filepath) as f:
        csv_reader = csv.reader(f, delimiter='\t')
        memory_banks = list(csv_reader)[0]
        memory_banks = map(int, memory_banks)

    return memory_banks


def reallocate(memory_banks, return_loop_cycles=False):
    previous_states = []

    while memory_banks not in previous_states:
        previous_states.append(copy(memory_banks))
        idx = memory_banks.index(max(memory_banks))
        highest = memory_banks[idx]
        memory_banks[idx] = 0

        while highest > 0:
            idx += 1
            if idx >= len(memory_banks):
                idx = 0

            memory_banks[idx] += 1
            highest -= 1

    if return_loop_cycles:
        return reallocate(memory_banks, return_loop_cycles=False)

    return len(previous_states)


def main():
    filename = os.path.join(os.path.dirname(__file__), 'input.txt')
    memory_banks = parse_input(filename)
    print 'Day 06, Half 1: {}'.format(reallocate(memory_banks))
    print 'Day 06, Half 2: {}'.format(reallocate(memory_banks, True))


def test_reallocate():
    assert reallocate([0, 2, 7, 0]) == 5


def test_reallocate_cycles():
    assert reallocate([0, 2, 7, 0], True) == 4


if __name__ == '__main__':
    main()
