from GraphInterface import WeightedGraph
import unittest

__author__ = 'vks'


class Tests(unittest.TestCase):
    def test_single(self):
        graph = WeightedGraph()
        graph.add_vertex(0)
        self.assertEqual(graph.paths(0), [[0]])

    def test_2ver_1edge(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 1, 2)
        self.assertEqual(graph.paths(0), [[0], [0, 1]])
        self.assertEqual(graph.paths(1), [[], [1]])

    def test_small_graph(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 1, 2)
        graph.add_direct_link(0, 2, 1)
        graph.add_direct_link(0, 5, 8)
        graph.add_direct_link(1, 2, 3)
        graph.add_direct_link(2, 3, 1)
        graph.add_direct_link(2, 4, 2)
        graph.add_direct_link(3, 6, 3)
        graph.add_direct_link(4, 5, 7)
        graph.add_direct_link(5, 6, 2)
        self.assertEqual(graph.paths(0), [[0], [0, 1], [0, 2], [0, 2, 3], [0, 2, 4], [0, 5], [0, 2, 3, 6]])
        self.assertEqual(graph.paths(6), [[], [], [], [], [], [], [6]])
        self.assertEqual(graph.paths(3), [[], [], [], [3], [], [], [3, 6]])
        self.assertEqual(graph.paths(2), [[], [], [2], [2, 3], [2, 4], [2, 4, 5], [2, 3, 6]])

    def test_not_connected_graph(self):
        graph = WeightedGraph()
        graph.add_direct_link(0, 1, 2)
        graph.add_direct_link(0, 2, 1)
        graph.add_direct_link(0, 5, 8)
        graph.add_direct_link(1, 2, 3)
        graph.add_direct_link(2, 3, 1)
        graph.add_direct_link(2, 4, 2)
        graph.add_direct_link(3, 6, 3)
        graph.add_direct_link(4, 5, 7)
        graph.add_direct_link(5, 6, 2)
        graph.add_direct_link(7, 8, 2)
        graph.add_direct_link(7, 9, 3)
        graph.add_direct_link(8, 10, 1)
        graph.add_direct_link(9, 10, 2)
        graph.add_direct_link(10, 7, 1)
        self.assertEqual(graph.paths(6), [[], [], [], [], [], [], [6], [], [], [], []])
        self.assertEqual(graph.paths(7), [[], [], [], [], [], [], [], [7], [7, 8], [7, 9], [7, 8, 10]])

