import os

from copy import copy


def jump_recursive(maze, current_idx=0, jump_counter=0):
    """This does not work for large inputs, will have to do an iterative function instead"""
    offset = maze[current_idx]
    position = current_idx
    new_idx = position + offset

    maze[current_idx] = maze[current_idx] + 1
    current_idx = new_idx
    jump_counter += 1

    if current_idx < len(maze):
        jump_counter, current_idx = jump_recursive(maze, current_idx, jump_counter)

    return jump_counter, current_idx


def jump(maze, special_jump=False):
    # We do a copy here because we want to re-use the original maze for printing the second half.
    maze = copy(maze)
    current_idx = 0
    jump_counter = 0

    while True:
        offset = maze[current_idx]
        new_idx = current_idx + offset

        if special_jump and offset >= 3:
            maze[current_idx] = maze[current_idx] - 1
        else:
            maze[current_idx] = maze[current_idx] + 1

        current_idx = new_idx
        jump_counter += 1

        if current_idx < 0 or current_idx >= len(maze):
            break

    return jump_counter


def main():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        maze = f.read().splitlines()
        maze = map(int, maze)

    print "Day 05, Half 01: {}".format(jump(maze))
    print "Day 05, Half 02: {}".format(jump(maze, special_jump=True))


def test_maze():
    assert jump([0, 3, 0, 1, -3]) == 5


def test_maze_with_decrease_by_1_if_offset_3_or_more():
    assert jump([0, 3, 0, 1, -3], special_jump=True) == 10


if __name__ == '__main__':
    main()
