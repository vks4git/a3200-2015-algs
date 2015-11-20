import unittest
from tree import Tree

__author__ = 'vks'


class Tester(unittest.TestCase):
    def test_example(self):
        n = 8
        root = 2
        adjacent = [(0, 6), (3, 6), (6, 2), (4, 2), (1, 4), (5, 1), (7, 1)]
        tree = Tree(n, adjacent, root)
        self.assertEqual(tree.lca(0, 7), 2)
        self.assertEqual(tree.lca(5, 1), 1)
        self.assertEqual(tree.lca(1, 5), 1)
        self.assertEqual(tree.lca(0, 3), 6)

    def test_2_vertices(self):
        n = 2
        root = 1
        adjacent = [(0, 1)]
        tree = Tree(n, adjacent, root)
        self.assertEqual(tree.lca(0, 1), 1)
        self.assertEqual(tree.lca(1, 0), 1)
        self.assertEqual(tree.lca(0, 0), 0)
        self.assertEqual(tree.lca(1, 1), 1)

    def test_tiny(self):
        n = 6
        root = 0
        adjacent = [(0, 1), (0, 5), (1, 2), (1, 4), (2, 3)]
        tree = Tree(n, adjacent, root)
        self.assertEqual(tree.lca(0, 0), 0)
        self.assertEqual(tree.lca(1, 1), 1)
        self.assertEqual(tree.lca(3, 2), 2)
        self.assertEqual(tree.lca(1, 5), 0)
        self.assertEqual(tree.lca(3, 4), 1)
        self.assertEqual(tree.lca(3, 5), 0)

    def test_small(self):
        n = 20
        root = 7
        adjacent = [(7, 5), (7, 13), (7, 11), (11, 4), (11, 19), (4, 6), (4, 0), (4, 1), (4, 3), (13, 15), (13, 14),
                    (15, 16), (16, 17), (16, 18), (5, 2), (2, 8), (8, 9), (8, 12), (8, 10)]
        tree = Tree(n, adjacent, root)
        self.assertEqual(tree.lca(5, 13), 7)
        self.assertEqual(tree.lca(6, 19), 11)
        self.assertEqual(tree.lca(6, 12), 7)
        self.assertEqual(tree.lca(15, 10), 7)
        self.assertEqual(tree.lca(18, 14), 13)
        self.assertEqual(tree.lca(14, 2), 7)
        self.assertEqual(tree.lca(3, 19), 11)
        self.assertEqual(tree.lca(18, 15), 15)
        self.assertEqual(tree.lca(10, 2), 2)
