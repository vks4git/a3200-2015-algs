import unittest
from random import randint
from bst import BST

__author__ = 'vks'


class TestBST(unittest.TestCase):
    def random_shuffle(self, array):
        for i in range(len(array)):
            ind = randint(0, len(array) - 1)
            array[i], array[ind] = array[ind], array[i]
        return array

    def grade(self, array):
        bst = BST()
        for i in array:
            bst.add(i)
        array = sorted(array)
        ptr = 0
        for i in bst:
            self.assertEqual(i, array[ptr])
            ptr += 1

    def test_empty(self):
        self.grade([])

    def test_trivial(self):
        self.grade([1])

    def test_ascending(self):
        self.grade([1, 2, 3, 4, 5, 6, 7])

    def test_descending(self):
        self.grade([7, 6, 5, 4, 3, 2, 1])

    def test_small_balanced(self):
        self.grade([2, 1, 3])

    def test_balanced_tree(self):
        self.grade([5, 3, 7, 2, 4, 6, 8])

    def test_big_balanced_tree(self):
        self.grade([8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15])

    def test_big_unbalanced(self):
        self.grade(
            [100, 50, 51, 52, 53, 54, 55, 56, 57, 49, 48, 30, 31, 32, 33, 34, 200, 199, 198, 197, 196, 195, 194, 193,
             192, 191, 190])

    def test_random(self):
        array = [i for i in range(1000)]
        array = self.random_shuffle(array)
        self.grade(array)

    def test_big_random(self):
        array = [i for i in range(100000)]
        array = self.random_shuffle(array)
        self.grade(array)
