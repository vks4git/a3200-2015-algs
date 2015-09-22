# coding=UTF-8
import sys
import random

__author__ = 'vks'


# Dijkstra 3-way partitioning + random pivot
def split(array, left, right):
    index = random.randint(left, right)
    array[left], array[index] = array[index], array[left]
    x = array[left]
    less = left
    greater = right
    j = left
    while j <= greater:
        if array[j] < x:
            array[less], array[j] = array[j], array[less]
            less += 1
            j += 1
        elif array[j] > x:
            array[greater], array[j] = array[j], array[greater]
            greater -= 1
        else:
            j += 1
    return less, greater


def sort(array, left, right):
    if left < right:
        less, greater = split(array, left, right)
        sort(array, left, less - 1)
        sort(array, greater + 1, right)


def qsort(array):
    left = 0
    right = len(array) - 1
    sort(array, left, right)


a = [int(s) for s in sys.stdin.readline().split()]
qsort(a)
for i in a:
    sys.stdout.write(str(i) + ' ')
