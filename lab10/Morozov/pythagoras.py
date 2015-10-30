from sys import stdin, stdout

__author__ = 'vks'


def find(array, target):
    lo = 0
    hi = len(array) - 1
    count = 0
    while lo <= hi:
        if lo == target:
            lo += 1
        if hi == target:
            hi -= 1
        if array[lo] + array[hi] == array[target]:
            count += 1
        if array[lo] + array[hi] > array[target]:
            hi -= 1
        else:
            lo += 1
    return count


def remove_duplicates(array):
    if len(array) == 0:
        return []
    array = sorted(array)
    prev = array[0]
    ans = [prev]
    for i in range(len(array)):
        if array[i] == prev:
            continue
        prev = array[i]
        ans.append(prev)
    return ans


def triplets(array):
    n = len(array)
    if n < 3:
        return 0
    squares = [i ** 2 for i in array]
    squares = remove_duplicates(squares)
    count = 0
    for i in range(len(squares)):
        count += find(squares, i)
    return count


if __name__ == "__main__":
    numbers = [int(i) for i in stdin.readline().split()]
    stdout.write(str(triplets(numbers)) + "\n")
