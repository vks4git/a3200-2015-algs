__author__ = 'vks'


# get i-th digit of a number
def ith_digit(number, i):
    return (number % (10 ** (i + 1))) // (10 ** i)


# count sort by digits at k-th position
def count_sort(a, b, k):
    digits = [0 for i in range(10)]
    for i in a:
        index = ith_digit(i, k)
        digits[index] += 1
    for i in range(1, 10):
        digits[i] += digits[i - 1]
    for i in range(len(a) - 1, -1, -1):
        index = ith_digit(a[i], k)
        b[digits[index] - 1] = a[i]
        digits[index] -= 1


def digits_count(num):
    count = 0
    while num > 0:
        count += 1
        num //= 10
    return count


def radix_sort(array):
    if len(array) == 0:
        return array
    min_number = min(array)
    for i in range(len(array)):
        array[i] -= min_number
    # shifting array to [0, n]
    max_length = digits_count(max(array))
    b = [0 for i in range(len(array))]
    for i in range(max_length + 1):
        count_sort(array, b, i)
        array, b = b, array
    # shifting array back
    for i in range(len(array)):
        array[i] += min_number
    return array
