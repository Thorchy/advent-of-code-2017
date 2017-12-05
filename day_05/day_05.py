import os


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


def jump(maze):
    current_idx = 0
    jump_counter = 0

    while True:
        offset = maze[current_idx]
        position = current_idx
        new_idx = position + offset

        maze[current_idx] = maze[current_idx] + 1
        current_idx = new_idx
        jump_counter += 1

        if current_idx >= len(maze):
            break

    return jump_counter


def main():
    filepath = os.path.join(os.path.dirname(__file__), 'input.txt')
    with open(filepath) as f:
        maze = f.read().splitlines()
        maze = map(int, maze)

    print "Day 05, Half 01: {}".format(jump(maze))


def test_maze():
    assert jump([0, 3, 0, 1, -3]) == 5


if __name__ == '__main__':
    main()
