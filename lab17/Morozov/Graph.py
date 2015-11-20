from QuickWeightedUnionFind import QuickWeightedUF

__author__ = 'vks'


class Graph:
    def add_vertex(self, v):
        pass

    def add_direct_link(self, v1, v2, weight):
        pass

    def get_links(self, v):
        pass

    def min_tree(self):
        pass


class Edge:
    def __init__(self, v1, v2, weight):
        self.v1 = v1
        self.v2 = v2
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


class WeightedGraph(Graph):
    def __init__(self):
        self.__adjacency_list = []
        self.__size = 0
        self.__edges = []

    def add_vertex(self, v):
        if v >= self.__size:
            for i in range(self.__size, v + 1):
                self.__adjacency_list.append([])
            self.__size = v + 1

    def add_direct_link(self, v1, v2, weight):
        edge = Edge(v1, v2, weight)
        self.__edges.append(edge)
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.__adjacency_list[v1].append(edge)
        self.__adjacency_list[v2].append(edge)

    def get_links(self, v):
        self.add_vertex(v)
        adjacent = []
        for e in self.__adjacency_list[v]:
            if e.v1 == v:
                adjacent.append(e.v2)
            else:
                adjacent.append(e.v1)
        return adjacent

    def min_tree(self):
        graph = WeightedGraph()
        quick_uf = QuickWeightedUF(self.__size)
        self.__edges.sort()
        for e in self.__edges:
            if not quick_uf.same_set(e.v1, e.v2):
                quick_uf.union(e.v1, e.v2)
                graph.add_direct_link(e.v1, e.v2, e.weight)
        return graph
