from sys import stdin, stdout
from math import log2, floor

__author__ = 'vks'


class SegmentTree:
    def __init__(self, array):
        length = len(array)
        size = 2 ** (floor(log2(length)) + 1)
        self.__tree = [(-1, -1) for i in range(size - 1)]
        self.__lo = size - 1
        self.__hi = 2 * size - 1
        for i in array:
            self.__tree.append(i)
        for i in range(length, size):
            self.__tree.append((2 ** 256, -1))
        self.__borders = [() for i in range(2 * size - 1)]
        self.__borders[0] = (0, size - 1)
        self.__build_tree()

    def get_min(self, left, right, index=0):
        lo = self.__borders[index][0]
        hi = self.__borders[index][1]
        if left == lo and right == hi:
            return self.__tree[index]
        med = (lo + hi) // 2
        if left > med:
            return self.get_min(left, right, 2 * (index + 1))
        if right <= med:
            return self.get_min(left, right, 2 * (index + 1) - 1)
        l = self.get_min(left, med, 2 * (index + 1) - 1)
        r = self.get_min(med + 1, right, 2 * (index + 1))
        if l[0] < r[0]:
            return l
        return r

    def __build_tree(self, index=0):
        if self.__tree[index][0] == -1:
            lo = self.__borders[index][0]
            hi = self.__borders[index][1]
            med = (lo + hi) // 2
            self.__borders[2 * (index + 1) - 1] = (lo, med)
            self.__borders[2 * (index + 1)] = (med + 1, hi)
            left = self.__build_tree(2 * (index + 1) - 1)
            right = self.__build_tree(2 * (index + 1))
            if left[0] < right[0]:
                self.__tree[index] = left
            else:
                self.__tree[index] = right
        return self.__tree[index]


class Tree:
    def __init__(self, size, adjacent, root):
        self.__size = size
        self.__list = [[] for i in range(size)]
        self.__depths = []
        self.__visited = {}
        for (v1, v2) in adjacent:
            self.__list[v1].append(v2)
            self.__list[v2].append(v1)
        self.__dfs(root)
        self.__st = SegmentTree(self.__depths)

    def lca(self, v1, v2):
        v1 = self.__visited[v1]
        v2 = self.__visited[v2]
        if v1 > v2:
            v1, v2 = v2, v1
        min = self.__st.get_min(v1, v2)
        return min[1]

    def __dfs(self, v, parent=None, depth=0):
        self.__depths.append((depth, v))
        self.__visited[v] = len(self.__depths) - 1
        for child in self.__list[v]:
            if child is not parent:
                self.__dfs(child, v, depth + 1)
                self.__depths.append((depth, v))


if __name__ == "__main__":
    n = int(stdin.readline())
    root = int(stdin.readline())
    adjacent = []
    for i in range(n - 1):
        v1, v2 = stdin.readline().split()
        adjacent.append((int(v1), int(v2)))
    tree = Tree(n, adjacent, root)
    for line in stdin.readlines():
        v1, v2 = line.split()
        stdout.write(str(tree.lca(int(v1), int(v2))) + "\n")
