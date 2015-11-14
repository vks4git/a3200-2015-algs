import heapq

__author__ = 'vks'


class GraphInterface:
    def add_vertex(self, v):
        pass

    def add_direct_link(self, v1, v2, weight):
        pass

    def paths(self, w):
        pass


class Vertex:
    def __init__(self, index):
        self.index = index
        self.distance = 0
        self.adjacent = set()
        self.previous = None

    def __lt__(self, other):
        return self.distance < other.distance


class WeightedGraph(GraphInterface):
    def __init__(self):
        self.__V = []
        self.__max = -1
        self.__inf = 2 ** 256

    def add_vertex(self, v):
        if v > self.__max:
            for i in range(self.__max + 1, v + 1):
                self.__V.append(Vertex(i))

    def add_direct_link(self, v1, v2, weight):
        self.add_vertex(v1)
        self.add_vertex(v2)
        self.__V[v1].adjacent.add((Vertex(v2), weight))

    def paths(self, w):
        self.__dijkstra(w)
        ans = []
        for v in self.__V:
            path = []
            while v is not None:
                path.append(v.index)
                v = v.previous
            path.reverse()
            ans += [path]
        return ans

    def __dijkstra(self, w):
        self.__V[w].distance = 0
        pq = []
        passed = []
        for v in self.__V:
            v.distance = self.__inf
        self.__V[w].distance = 0
        for v in self.__V:
            heapq.heappush(pq, v)
        while len(pq) > 0:
            u = heapq.heappop(pq)
            passed.append(u)
            for v in u.adjacent:
                weight = v[1]
                v = v[0]
                if v.distance > u.distance + weight:
                    v.distance = u.distance + weight
                    v.previous = u
                    heapq.heapify(pq)
