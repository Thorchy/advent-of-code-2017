with open('input.txt') as f:
    captcha = list(f.read().strip())
    captcha = map(int, captcha)

# Challenge with next digit
pre_sum = []
for idx, value in enumerate(captcha):
    if idx == len(captcha) - 1:
        next_value = captcha[0]
    else:
        next_value = captcha[idx + 1]

    if value == next_value:
        pre_sum.append(value)

print 'Half 1: {}'.format(sum(pre_sum))


# Challenge with digit x steps ahead
pre_sum = []
steps = len(captcha) / 2
for idx, value in enumerate(captcha):
    if idx + steps >= len(captcha):
        next_value = captcha[steps - (len(captcha) - idx)]
    else:
        next_value = captcha[idx + steps]

    if value == next_value:
        pre_sum.append(value)

print 'Half 2: {}'.format(sum(pre_sum))
