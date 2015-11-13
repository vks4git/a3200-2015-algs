__author__ = 'vks'


class GraphInterface:
    def add_vertex(self, v):
        pass

    def add_directed_link(self, v1, v2):
        pass

    def topological_sort(self):
        pass


class Graph(GraphInterface):
    def __init__(self):
        self.__map = {}
        self.__unseen = 0
        self.__visited = 1
        self.__closed = 2

    def add_vertex(self, v):
        if v not in self.__map.keys():
            self.__map[v] = []

    def add_directed_link(self, v1, v2):
        if v1 not in self.__map.keys():
            self.__map[v1] = []
        if v2 not in self.__map.keys():
            self.__map[v2] = []
        if v2 not in self.__map[v1]:
            self.__map[v1].append(v2)

    def topological_sort(self):
        if self.__has_cycle():
            return None
        stack = []
        state_map = {}
        for v in self.__map.keys():
            state_map[v] = self.__unseen
        for v in self.__map.keys():
            if state_map[v] == self.__unseen:
                self.__dfs2(v, state_map, stack)
                stack.append(v)
        stack.reverse()
        return stack

    def __dfs1(self, vertex, state_map):
        result = False
        for v in self.__map[vertex]:
            if state_map[v] == self.__unseen:
                state_map[v] = self.__visited
                result = result or self.__dfs1(v, state_map)
                state_map[v] = self.__closed
            elif state_map[v] == self.__visited:
                return True
        return result

    def __dfs2(self, vertex, state_map, list):
        for v in self.__map[vertex]:
            if state_map[v] == self.__unseen:
                state_map[v] = self.__visited
                self.__dfs2(v, state_map, list)
                list.append(v)

    def __has_cycle(self):
        state_map = {}
        for v in self.__map.keys():
            state_map[v] = self.__unseen
        for v in self.__map.keys():
            if state_map[v] == self.__unseen:
                result = self.__dfs1(v, state_map)
                if result:
                    return True
        return False
