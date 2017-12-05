def parse_input(filepath):
    with open(filepath) as f:
        captcha = list(f.read().strip())
        captcha = map(int, captcha)

    return captcha


def solve_captcha(captcha, steps=1):
    pre_sum = []
    for idx, value in enumerate(captcha):
        if idx + steps >= len(captcha):
            next_value = captcha[steps - (len(captcha) - idx)]
        else:
            next_value = captcha[idx + steps]

        if value == next_value:
            pre_sum.append(value)

    return sum(pre_sum)


def main():
    captcha = parse_input('input.txt')
    print "Day 1, Part 1: {}".format(solve_captcha(captcha))
    print "Day 1, Part 2: {}".format(solve_captcha(captcha, len(captcha) / 2))


def test_step_1_case_1():
    captcha = map(int, list('1122'))
    assert solve_captcha(captcha) == 3


def test_step_1_case_2():
    captcha = map(int, list('1111'))
    assert solve_captcha(captcha) == 4


def test_step_1_case_3():
    captcha = map(int, list('1234'))
    assert solve_captcha(captcha) == 0


def test_step_1_case_4():
    captcha = map(int, list('91212129'))
    assert solve_captcha(captcha) == 9


def test_step_x_case_1():
    captcha = map(int, list('1212'))
    steps = len(captcha) / 2
    assert solve_captcha(captcha, steps) == 6


def test_step_x_case_2():
    captcha = map(int, list('1221'))
    steps = len(captcha) / 2
    assert solve_captcha(captcha, steps) == 0


def test_step_x_case_3():
    captcha = map(int, list('123425'))
    steps = len(captcha) / 2
    assert solve_captcha(captcha, steps) == 4


def test_step_x_case_4():
    captcha = map(int, list('12131415'))
    steps = len(captcha) / 2
    assert solve_captcha(captcha, steps) == 4


if __name__ == '__main__':
    main()
