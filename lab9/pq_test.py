import unittest
from random import randint
from priority_queue import MinPQ

__author__ = 'vks'


class TestPQ(unittest.TestCase):
    def grade(self, array, k):
        pq = MinPQ(k)
        for i in array:
            pq.add(i)
        array = sorted(array)
        array.reverse()
        ans = sorted(pq.get_max())
        ans.reverse()
        for i in range(k):
            self.assertEqual(array[i], ans[i])
        self.assertEqual(len(ans), k)

    def test_empty(self):
        self.grade([], 0)

    def test_one_element(self):
        self.grade([1], 1)

    def test_equal_elem(self):
        self.grade([1, 1, 1, 1], 2)

    def test_equal_elem2(self):
        self.grade([1, 1, 1, 1], 4)

    def test_equal_elem3(self):
        self.grade([1, 1, 1, 1], 0)

    def test_zero_k(self):
        arr = [randint(-1000, 1000) for i in range(10000)]
        self.grade(arr, 0)

    def test_small_random(self):
        arr = [randint(-1000, 1000) for i in range(1000)]
        self.grade(arr, 5)

    def test_big_random(self):
        arr = [randint(-1000, 1000) for i in range(1000000)]
        self.grade(arr, 5)

    def test_small_random2(self):
        arr = [randint(-1000, 1000) for i in range(1000)]
        self.grade(arr, 1000)

    def test_big_random2(self):
        arr = [randint(-1000, 1000) for i in range(1000000)]
        self.grade(arr, 1000000)

    def test_some_random_inputs(self):
        for i in range(200):
            n = randint(0, 10000)
            k = randint(0, n)
            arr = [randint(-1000000, 1000000) for j in range(n)]
            self.grade(arr, k)
