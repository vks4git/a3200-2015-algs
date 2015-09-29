from random import randint

__author__ = 'vks'


# generate an array of random elements, each is repeated with probability 0.03
def generate_random_array(lo, hi, size):
    ans = [randint(lo, hi) for i in range(size)]
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[randint(0, i)] = ans[i - 1]
    return ans


def positive_and_negative_array(size):
    return generate_random_array(-1000000, 1000000, size)


def positive_array(size):
    return generate_random_array(0, 10000, size)


def partially_sorted_array(size):
    hi = 10000
    ans = [0 for i in range(size)]
    ans[0] = randint(0, hi)
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[i] = ans[i - 1]
        else:
            ans[i] = (ans[i - 1] + randint(0, hi)) % hi
    return ans


def ascending_sorted_array(size):
    ans = [0 for i in range(size)]
    ans[0] = randint(0, 10000)
    for i in range(1, size):
        if randint(0, 1000000) < 30000:
            ans[i] = ans[i - 1]
        else:
            ans[i] = ans[i - 1] + randint(0, (10000 - ans[i - 1]) // 10)
    return ans


def descending_sorted_array(size):
    ans = ascending_sorted_array(size)
    ans.reverse()
    return ans


def unique_number_array(size):
    num = randint(-1000000, 1000000)
    return [num for i in range(size)]
