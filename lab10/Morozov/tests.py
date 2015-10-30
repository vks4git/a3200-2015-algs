import unittest
from pythagoras import triplets, remove_duplicates
from random import randint

__author__ = 'vks'


class TestPythagoras(unittest.TestCase):
    def grade(self, array):
        copy = [i ** 2 for i in array]
        copy = remove_duplicates(copy)
        expected = 0
        for i in range(len(copy)):
            for j in range(i + 1, len(copy)):
                for k in range(j + 1, len(copy)):
                    if copy[i] + copy[j] == copy[k]:
                        expected += 1
        ans = triplets(array)
        self.assertEqual(ans, expected)

    def test_empty(self):
        self.grade([])

    def test_one_elem(self):
        self.grade([1])

    def test_one_negative(self):
        self.grade([-123456789])

    def test_pair(self):
        self.grade([123, 456])

    def test_pair2(self):
        self.grade([346, -4625])

    def test_trivial(self):
        self.grade([3, 4, 5])

    def test_duplicates(self):
        self.grade([3, 4, 3, 3, 5, 4, 4, 5, 3, 4, 5, 5, 4, 3])

    def test_nontrivial(self):
        self.grade([1, 2, 3, 4, 5, 6, 7, 8])

    def test_negative(self):
        # no triplets but (3, 4, 5)
        self.grade([-1, 2, -3, 4, -5, 6, -7, 8])

    def test_negative_duplicates(self):
        # no triplets but (3, 4, 5)
        self.grade([-2, 2, 5, -1, 7, 1, 1, -3, 8, 0, 1, -5, 3, 4, -6, -8, -9, 0, -2])

    def test_multi_triplets(self):
        self.grade([3, 4, 5, 6, 8, 10, 12, 13])

    def test_large_set(self):
        self.grade([3, 4, 5, 6, 8, 10, 5, 12, 13, 9, 12, 15, 8, 15, 17, 12, 16, 20, 15, 20, 25,
                    7, 24, 25, 10, 24, 26, 20, 21, 29, 18, 24, 30, 16, 30, 34, 21, 28, 35, 12, 35, 37,
                    15, 36, 39, 24, 32, 40, 9, 40, 41, 14, 48, 50, 30, 40, 50])

    def test_random_set(self):
        array = [randint(-10000, 10000) for i in range(100)]
        self.grade(array)

    def test_huge_random_set(self):
        array = [randint(-10000, 10000) for i in range(1000)]
        self.grade(array)