import unittest
import random
from radix_sort import radix_sort

__author__ = 'vks'


class TestRadixSort(unittest.TestCase):
    def check_sorted(self, array):
        if len(array) == 0:
            return True
        prev = array[0]
        for i in array:
            if i < prev:
                return False
            prev = i
        return True

    def test_empty(self):
        arr = []
        res = radix_sort(arr)
        expected = []
        self.assertEqual(expected, res)

    def test_trivial(self):
        arr = [1]
        res = radix_sort(arr)
        expected = [1]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_trivial_2(self):
        arr = [123456789]
        res = radix_sort(arr)
        expected = [123456789]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_trivial_3(self):
        arr = [0]
        res = radix_sort(arr)
        expected = [0]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_equal_length_ints(self):
        arr = [random.randint(1000, 9999) for i in range(1000)]
        res = radix_sort(arr)
        self.assertTrue(self.check_sorted(res))

    def test_different_length_ints(self):
        arr = [random.randint(0, 1000000) for i in range(1000)]
        res = radix_sort(arr)
        self.assertTrue(self.check_sorted(res))

    def test_long_array(self):
        arr = [random.randint(0, 1000000) for i in range(200000)]
        res = radix_sort(arr)
        self.assertTrue(self.check_sorted(res))

    def test_single_negative(self):
        arr = [-1]
        res = radix_sort(arr)
        expected = [-1]
        self.assertFalse(not res)
        self.assertEqual(expected, res)

    def test_multiple_negative(self):
        arr = [random.randint(-1000000, -1) for i in range(1000)]
        res = radix_sort(arr)
        self.assertTrue(self.check_sorted(res))

    def test_random_input(self):
        arr = [random.randint(-1000000, 1000000) for i in range(100000)]
        res = radix_sort(arr)
        self.assertTrue(self.check_sorted(res))
