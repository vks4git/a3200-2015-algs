__author__ = 'vks'


class QuickWeightedUF:
    def __init__(self, size):
        self.__parents = [i for i in range(size)]
        self.__weights = [1 for i in range(size)]

    def same_set(self, u, v):
        return self.__root(u) == self.__root(v)

    def union(self, u, v):
        if self.same_set(u, v):
            return
        root_u = self.__root(u)
        root_v = self.__root(v)
        if self.__weights[root_u] > self.__weights[root_v]:
            self.__parents[root_v] = root_u
            self.__weights[root_u] += self.__weights[root_v]
        else:
            self.__parents[root_u] = root_v
            self.__weights[root_v] += self.__weights[root_u]

    def __root(self, v):
        if v == self.__parents[v]:
            return v
        self.__parents[v] = self.__root(self.__parents[v])
        return self.__parents[v]
