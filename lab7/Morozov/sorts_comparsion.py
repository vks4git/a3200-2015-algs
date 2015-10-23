from generators import *
from time import time
import pylab
import sys

__author__ = 'vks'

root = "/"
parts = __file__.split('/')
for i in range(1, len(parts) - 3):
    root += parts[i] + '/'

sys.path.append(root + "lab4/Morozov/")
sys.path.append(root + "lab5/Morozov/")
sys.path.append(root + "lab6/Morozov/")
from mergesort import merge_sort
from radix_sort import radix_sort
from qsort import qsort


def grade(sort_func, array_generator, size):
    millis = 0.0
    for i in range(5):
        array = array_generator(size)
        t1 = time()
        sort_func(array)
        t2 = time()
        millis += t2 - t1
    millis /= 5.0
    return millis


sort_functions = {"Quick sort": qsort,
                  "Merge sort": merge_sort,
                  "Radix sort": radix_sort,
                  "Built-in sort": sorted}

generators = {"Array of random ints from [-1e6, 1e6]": positive_and_negative_array,
              "Array of random ints from [0, 1e4]": positive_array,
              "Array with some sorted subarrays": partially_sorted_array,
              "Already sorted array": ascending_sorted_array,
              "Descending sorted array": descending_sorted_array,
              "Array with the only distinct element": unique_number_array}

if __name__ == "__main__":

    sizes = [100 + 100000 * i for i in range(11)]
    current = 1

    for gen_name, gen in generators.items():
        pylab.subplot(2, 3, current)
        pylab.xlabel("size, elements")
        pylab.ylabel("time, sec")
        print("Now passing: %s" % gen_name)
        for func_name, func in sort_functions.items():
            millis = []
            for size in sizes:
                millis.append(grade(func, gen, size))
                print("\tUsing %s on array of size %s" % (func_name, size))
            print("\t***\n\n")
            pylab.plot(sizes, millis, label=func_name)
        pylab.title(gen_name)
        pylab.legend(loc='upper left', title="Sorts")
        current += 1

    pylab.show()
