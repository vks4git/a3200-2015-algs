__author__ = 'vks'

inf = 2 ** 64


def merge(array, l_pointer, mid_pointer, r_pointer):
    global inf
    n1 = mid_pointer - l_pointer
    n2 = r_pointer - mid_pointer
    left = [array[l_pointer + i] for i in range(n1)]
    right = [array[mid_pointer + i] for i in range(n2)]
    left.append(inf)
    right.append(inf)
    ptr1 = 0
    ptr2 = 0
    for ind in range(l_pointer, r_pointer):
        if left[ptr1] <= right[ptr2]:
            array[ind] = left[ptr1]
            ptr1 += 1
        else:
            array[ind] = right[ptr2]
            ptr2 += 1


def insertion_sort(array, l, r):
    for i in range(l, r + 1):
        j = i - 1
        while j >= l and array[j] > array[j + 1]:
            array[j], array[j + 1] = array[j + 1], array[j]
            j -= 1


def sort(array, l, r, threshold):
    if r - l <= threshold:
        insertion_sort(array, l, r)
    else:
        mid = (l + r) // 2
        sort(array, l, mid, threshold)
        sort(array, mid, r, threshold)
        merge(array, l, mid, r)


def merge_sort(array):
    lo = 0
    hi = len(array) - 1
    sort(array, lo, hi, 10)
