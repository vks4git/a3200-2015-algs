import unittest
from splayTreeSet import SplayTree
from random import randint

__author__ = 'vks'


class TestSplayTree(unittest.TestCase):
    def test_empty(self):
        st = SplayTree()
        self.assertFalse(st.contains(0))

    def test_add(self):
        st = SplayTree()
        st.add(5)
        st.add(6)
        self.assertFalse(st.contains(0))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(6))
        st.add(0)
        self.assertTrue(st.contains(0))
        self.assertTrue(st.contains(6))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(0))
        st.add(1)
        st.add(3)
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(0))
        self.assertTrue(st.contains(1))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(3))

    def test_medium_add(self):
        st = SplayTree()
        array = [4, 8, 15, 16, 23, 42, 1, 1, 2, 3, 5, 8, 13, 1, 4, 9, 16, 25, 36, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29,
                 31, 4, 2, 3, 5, 11, 12]
        for i in range(len(array)):
            st.add(array[i])
            if i > 3:
                for j in range(5):
                    ind = randint(0, i - 1)
                    self.assertTrue(st.contains(array[ind]))

    def test_big_add(self):
        st = SplayTree()
        array = [randint(-10000, 10000) for i in range(100000)]
        for i in range(len(array)):
            st.add(array[i])
            if i > 3:
                for j in range(10):
                    ind = randint(0, i - 1)
                    self.assertTrue(st.contains(array[ind]))

    def test_remove(self):
        st = SplayTree()
        st.add(5)
        st.add(6)
        self.assertFalse(st.contains(0))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(6))
        st.add(0)
        self.assertTrue(st.contains(0))
        st.remove(6)
        self.assertFalse(st.contains(6))
        self.assertTrue(st.contains(5))
        self.assertTrue(st.contains(0))

    def test_medium_remove(self):
        st = SplayTree()
        st.add(9)
        st.add(1)
        st.add(5)
        st.add(8)
        st.add(3)
        st.add(2)
        st.add(7)
        st.add(4)
        st.add(6)
        for i in range(1, 9):
            st.remove(i)
            self.assertFalse(st.contains(i))
            self.assertTrue(st.contains(i + 1))
            self.assertFalse(st.contains(i - 1))
            st.add(i)
            self.assertTrue(st.contains(i))
            self.assertTrue(st.contains(i + 1))
            self.assertFalse(st.contains(i - 1))
            st.remove(i)

    def test_big_remove(self):
        st = SplayTree()
        array = [i for i in range(100000)]
        removed = []
        for i in range(len(array)):
            ind = randint(0, len(array) - 1)
            array[i], array[ind] = array[ind], array[i]
        for i in array:
            st.add(i)
        for i in range(len(array)):
            st.remove(array[i])
            removed.append(array[i])
            if i > 3:
                for j in range(10):
                    ind = randint(0, len(removed) - 1)
                    self.assertFalse(st.contains(removed[ind]))

    def test_contains_on_empty_set(self):
        st = SplayTree()
        for i in range(10000):
            self.assertFalse(st.contains(randint(-10000, 10000)))

    def test_remove_on_empty_set(self):
        st = SplayTree()
        for i in range(10000):
            st.remove(randint(-10000, 10000))

    def test_remove_elements_not_in_set(self):
        st = SplayTree()
        for i in range(1000):
            st.add(i)
        for i in range(1001, 10000):
            st.remove(i)
        for i in range(1000):
            self.assertTrue(st.contains(i))

    # be patient, it may take several minutes to pass this test
    # At the beginning the set is filled with randomly shuffled ints, then at each iteration one int is removed,
    # at each fifth iteration three ints are restored. Also some checks are performed
    def test_big_combined(self):
        st = SplayTree()
        array = [i for i in range(100000)]
        removed = []
        for i in range(len(array)):
            ind = randint(0, len(array) - 1)
            array[i], array[ind] = array[ind], array[i]
        for i in array:
            st.add(i)
        for i in range(100000):
            st.remove(array[i])
            removed.append(array[i])
            if i > 3:
                for j in range(10):
                    ind = randint(0, len(removed) - 1)
                    self.assertFalse(st.contains(removed[ind]))
            if i < len(array) - 4:
                for j in range(10):
                    ind = randint(i + 2, len(array) - 2)
                    self.assertTrue(st.contains(array[ind]))
                    self.assertTrue(st.contains(array[ind + 1]))
                    self.assertTrue(st.contains(array[ind]))
                    self.assertTrue(st.contains(array[ind + 1]))
                    self.assertTrue(st.contains(array[ind - 1]))
                    self.assertTrue(st.contains(array[ind + 1]))
                    self.assertTrue(st.contains(array[ind]))
            if i > 0 and i % 5 == 0:
                for j in range(3):
                    ind = randint(0, len(removed) - 1)
                    num = removed[ind]
                    removed.remove(num)
                    array.append(num)
                    st.add(num)

    def test_iterator_on_empty_set(self):
        st = SplayTree()
        array = [i for i in st]
        self.assertEqual(array, [])

    def test_iterator(self):
        st = SplayTree()
        st.add(9)
        st.add(1)
        st.add(5)
        st.add(8)
        st.add(3)
        st.add(2)
        st.add(7)
        st.add(4)
        st.add(6)
        ptr = 1
        for i in st:
            self.assertEqual(i, ptr)
            ptr += 1

    def test_big_iterator(self):
        st = SplayTree()
        array = [i for i in range(100000)]
        for i in range(len(array)):
            ind = randint(0, len(array) - 1)
            array[i], array[ind] = array[ind], array[i]
        for i in array:
            st.add(i)
        ptr = 0
        for i in st:
            self.assertEqual(i, ptr)
            ptr += 1

    def test_nested_iterators(self):
        st = SplayTree()
        array = [i for i in range(100)]
        for i in range(len(array)):
            ind = randint(0, len(array) - 1)
            array[i], array[ind] = array[ind], array[i]
        for i in array:
            st.add(i)
        a = 0
        b = 0
        c = 0
        for i in st:
            for j in st:
                for k in st:
                    self.assertEqual(a, i)
                    self.assertEqual(b, j)
                    self.assertEqual(c, k)
                    c += 1
                b += 1
                c = 0
            a += 1
            b = 0
