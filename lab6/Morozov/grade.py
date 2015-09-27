import radix_sort
import sys

__author__ = 'vks'

elements = [int(i) for i in sys.stdin.readline().split()]
elements = radix_sort.radix_sort(elements)
for i in elements:
    sys.stdout.write(str(i) + ' ')
