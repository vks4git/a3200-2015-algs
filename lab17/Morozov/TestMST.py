from QuickWeightedUnionFind import QuickWeightedUF
from Graph import WeightedGraph
from unittest import TestCase
from random import randint

__author__ = 'vks'


class Tests(TestCase):
    def test_union_find_tiny(self):
        quick_uf = QuickWeightedUF(5)
        self.assertFalse(quick_uf.same_set(0, 1))
        self.assertFalse(quick_uf.same_set(1, 2))
        self.assertFalse(quick_uf.same_set(1, 3))
        self.assertFalse(quick_uf.same_set(2, 3))
        self.assertFalse(quick_uf.same_set(2, 1))
        self.assertFalse(quick_uf.same_set(1, 2))
        self.assertFalse(quick_uf.same_set(0, 4))
        self.assertFalse(quick_uf.same_set(1, 4))
        quick_uf.union(2, 4)
        self.assertFalse(quick_uf.same_set(0, 1))
        self.assertFalse(quick_uf.same_set(1, 2))
        self.assertFalse(quick_uf.same_set(1, 3))
        self.assertFalse(quick_uf.same_set(2, 3))
        self.assertFalse(quick_uf.same_set(2, 1))
        self.assertFalse(quick_uf.same_set(1, 2))
        self.assertFalse(quick_uf.same_set(0, 4))
        self.assertFalse(quick_uf.same_set(1, 4))
        self.assertTrue(quick_uf.same_set(2, 4))

    def test_union_find_small(self):
        quick_uf = QuickWeightedUF(20)
        self.assertFalse(quick_uf.same_set(0, 8))
        self.assertFalse(quick_uf.same_set(5, 16))
        self.assertFalse(quick_uf.same_set(19, 2))
        self.assertFalse(quick_uf.same_set(3, 13))
        self.assertFalse(quick_uf.same_set(4, 5))
        self.assertFalse(quick_uf.same_set(7, 6))
        self.assertTrue(quick_uf.same_set(7, 7))
        quick_uf.union(0, 1)
        quick_uf.union(1, 2)
        quick_uf.union(3, 2)
        self.assertTrue(quick_uf.same_set(0, 2))
        self.assertTrue(quick_uf.same_set(0, 3))
        self.assertTrue(quick_uf.same_set(1, 3))
        self.assertTrue(quick_uf.same_set(2, 3))
        self.assertFalse(quick_uf.same_set(0, 8))
        self.assertFalse(quick_uf.same_set(5, 16))
        self.assertFalse(quick_uf.same_set(19, 2))
        self.assertFalse(quick_uf.same_set(3, 13))
        self.assertFalse(quick_uf.same_set(4, 5))
        self.assertFalse(quick_uf.same_set(7, 6))
        self.assertTrue(quick_uf.same_set(7, 7))

    def test_union_find_medium(self):
        quick_uf = QuickWeightedUF(1000)
        arr1 = [i for i in range(500)]
        arr2 = [i for i in range(500, 1000)]
        for i in range(500):
            for j in range(10):
                quick_uf.union(arr1[randint(0, 499)], arr1[i])
            quick_uf.union(0, i)
        for i in range(500, 1000):
            for j in range(10):
                quick_uf.union(arr2[randint(0, 499)], arr2[i - 500])
            quick_uf.union(500, i)
        for i in range(500):
            self.assertFalse(quick_uf.same_set(arr1[i], arr2[i]))
            self.assertTrue(quick_uf.same_set(randint(0, 499), randint(0, 499)))
            self.assertTrue(quick_uf.same_set(randint(500, 999), randint(500, 999)))

    def test_union_find_huge(self):
        quick_uf = QuickWeightedUF(1000000)
        arr1 = [i for i in range(250000)]
        arr2 = [i for i in range(250000, 500000)]
        arr3 = [i for i in range(500000, 750000)]
        arr4 = [i for i in range(750000, 1000000)]
        for i in range(250000):
            quick_uf.union(arr1[i], arr1[randint(0, 249999)])
            quick_uf.union(arr1[i], arr1[0])
            quick_uf.union(arr2[i], arr2[randint(0, 249999)])
            quick_uf.union(arr2[i], arr2[0])
            quick_uf.union(arr3[i], arr3[randint(0, 249999)])
            quick_uf.union(arr3[i], arr3[0])
            quick_uf.union(arr4[i], arr4[randint(0, 249999)])
            quick_uf.union(arr4[i], arr4[0])
        for i in range(250000):
            self.assertTrue(quick_uf.same_set(i, randint(0, 249999)))
            self.assertFalse(quick_uf.same_set(i, randint(250000, 999999)))
            self.assertFalse(quick_uf.same_set(i, randint(250000, 999999)))
            self.assertTrue(quick_uf.same_set(i + 250000, randint(250000, 499999)))
            self.assertTrue(quick_uf.same_set(i + 500000, randint(500000, 749999)))
            self.assertFalse(quick_uf.same_set(i + 250000, randint(500000, 999999)))
            self.assertTrue(quick_uf.same_set(i + 750000, randint(750000, 999999)))

    def test_get_links_tiny(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 1, 50)
        graph.add_direct_link(1, 2, 34)
        graph.add_direct_link(1, 3, 42)
        graph.add_direct_link(4, 1, 24)
        links = sorted(graph.get_links(1))
        self.assertEqual(links, [0, 2, 3, 4])

    def test_get_links_small(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 5, 1)
        graph.add_direct_link(0, 1, 1)
        graph.add_direct_link(0, 2, 1)
        graph.add_direct_link(1, 5, 1)
        graph.add_direct_link(2, 5, 1)
        graph.add_direct_link(2, 3, 1)
        graph.add_direct_link(3, 4, 1)
        graph.add_direct_link(3, 5, 1)
        graph.add_direct_link(5, 6, 1)
        graph.add_direct_link(5, 7, 1)
        graph.add_direct_link(6, 9, 1)
        graph.add_direct_link(7, 11, 1)
        graph.add_direct_link(8, 9, 1)
        graph.add_direct_link(9, 10, 1)
        graph.add_direct_link(9, 11, 1)
        links = sorted(graph.get_links(1))
        self.assertEqual(links, [0, 5])
        links = sorted(graph.get_links(3))
        self.assertEqual(links, [2, 4, 5])
        links = sorted(graph.get_links(5))
        self.assertEqual(links, [0, 1, 2, 3, 6, 7])
        links = sorted(graph.get_links(11))
        self.assertEqual(links, [7, 9])

    def test_MST_tiny(self):
        graph = WeightedGraph()
        graph.add_direct_link(1, 3, 15)
        graph.add_direct_link(1, 2, 1)
        graph.add_direct_link(1, 4, 10)
        graph.add_direct_link(2, 4, 15)
        graph.add_direct_link(2, 3, 16)
        graph.add_direct_link(2, 0, 4)
        graph.add_direct_link(3, 0, 2)
        graph.add_direct_link(4, 0, 3)
        mst = graph.min_tree()
        self.assertEqual(sorted(mst.get_links(0)), [2, 3, 4])
        self.assertEqual(sorted(mst.get_links(1)), [2])
        self.assertEqual(sorted(mst.get_links(2)), [0, 1])
        self.assertEqual(sorted(mst.get_links(3)), [0])
        self.assertEqual(sorted(mst.get_links(4)), [0])

    def test_MST_small(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 1, 2)
        graph.add_direct_link(2, 1, 3)
        graph.add_direct_link(2, 5, 4)
        graph.add_direct_link(2, 4, 1)
        graph.add_direct_link(2, 6, 5)
        graph.add_direct_link(3, 7, 13)
        graph.add_direct_link(4, 7, 6)
        graph.add_direct_link(5, 8, 7)
        graph.add_direct_link(8, 9, 8)
        graph.add_direct_link(8, 10, 9)
        graph.add_direct_link(10, 11, 10)
        graph.add_direct_link(12, 11, 11)
        graph.add_direct_link(13, 11, 12)
        graph.add_direct_link(0, 11, 54)
        graph.add_direct_link(0, 12, 64)
        graph.add_direct_link(0, 7, 42)
        graph.add_direct_link(0, 2, 6)
        graph.add_direct_link(1, 3, 63)
        graph.add_direct_link(1, 9, 99)
        graph.add_direct_link(5, 6, 42)
        graph.add_direct_link(5, 9, 87)
        graph.add_direct_link(8, 12, 46)
        mst = graph.min_tree()
        self.assertEqual(sorted(mst.get_links(0)), [1])
        self.assertEqual(sorted(mst.get_links(1)), [0, 2])
        self.assertEqual(sorted(mst.get_links(2)), [1, 4, 5, 6])
        self.assertEqual(sorted(mst.get_links(3)), [7])
        self.assertEqual(sorted(mst.get_links(4)), [2, 7])
        self.assertEqual(sorted(mst.get_links(5)), [2, 8])
        self.assertEqual(sorted(mst.get_links(6)), [2])
        self.assertEqual(sorted(mst.get_links(7)), [3, 4])
        self.assertEqual(sorted(mst.get_links(8)), [5, 9, 10])
        self.assertEqual(sorted(mst.get_links(9)), [8])
        self.assertEqual(sorted(mst.get_links(10)), [8, 11])
        self.assertEqual(sorted(mst.get_links(11)), [10, 12, 13])
        self.assertEqual(sorted(mst.get_links(12)), [11])
        self.assertEqual(sorted(mst.get_links(13)), [11])
