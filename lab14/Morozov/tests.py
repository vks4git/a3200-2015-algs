import unittest
from Graph import Graph

__author__ = 'vks'


class TestGraph(unittest.TestCase):
    def test_empty(self):
        graph = Graph()
        self.assertEqual(graph.topological_sort(), [])

    def test_cycle(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(3, 1)
        self.assertEqual(graph.topological_sort(), None)

    def test_cycle_with_isolated_points(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_vertex(6)
        graph.add_vertex(7)
        graph.add_directed_link(2, 3)
        graph.add_vertex(1)
        graph.add_directed_link(6, 4)
        graph.add_directed_link(3, 1)
        graph.add_directed_link(3, 4)
        self.assertEqual(graph.topological_sort(), None)

    def test_two_connected_components(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(3, 1)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(5, 6)
        graph.add_directed_link(6, 4)
        self.assertEqual(graph.topological_sort(), None)

    def test_many_connected_components_with_cycle(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(1, 4)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(5, 6)
        graph.add_directed_link(7, 5)
        graph.add_directed_link(7, 9)
        graph.add_directed_link(11, 12)
        graph.add_directed_link(13, 12)
        graph.add_directed_link(11, 15)
        graph.add_directed_link(15, 16)
        graph.add_directed_link(15, 17)
        graph.add_directed_link(17, 10)
        graph.add_directed_link(10, 11)
        graph.add_directed_link(10, 17)
        self.assertEqual(graph.topological_sort(), None)

    def test_DAG_sort(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(2, 3)
        self.assertEqual(graph.topological_sort(), [1, 2, 3, 4, 5])

    def test_not_connected_DAG_sort(self):
        graph = Graph()
        graph.add_directed_link(1, 2)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(2, 4)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(4, 5)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(6, 7)
        graph.add_directed_link(6, 8)
        graph.add_directed_link(7, 9)
        graph.add_directed_link(8, 9)
        graph.add_directed_link(9, 10)
        graph.add_directed_link(7, 8)
        ans1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        ans2 = [6, 7, 8, 9, 10, 1, 2, 3, 4, 5]
        arr = graph.topological_sort()
        match1 = True
        match2 = True
        for i in range(10):
            match1 = match1 or (arr[i] == ans1[i])
        for i in range(10):
            match2 = match2 or (arr[i] == ans2[i])
        self.assertTrue(match1 or match2)
