__author__ = 'vks'


class Set:
    def add(self, value):
        pass

    def check(self, value):
        pass

    def iterate(self):
        pass


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None


class BST(Set):

    def __init__(self):
        self._root = None
        self._size = 0

    def add(self, value):
        if self._root is None:
            self._root = Node(value, None)
            self._size += 1
            return
        current = self._root
        parent = None
        while current is not None:
            parent = current
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return
        self._size += 1
        current = Node(value, parent)
        if value < parent.value:
            parent.left = current
        elif value > parent.value:
            parent.right = current

    def check(self, value):
        current = self._root
        while current is not None:
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                return True
        return False

    def successor(self, elem):
        if elem.right is not None:
            elem = elem.right
            while elem.left is not None:
                elem = elem.left
            return elem
        else:
            while elem.parent is not None and elem is elem.parent.right:
                elem = elem.parent
            return elem.parent

    def iterate(self):
        minimum = self._root
        if minimum is None:
            return
        while minimum.left is not None:
            minimum = minimum.left
        current = Node(0, minimum)
        current.parent = minimum
        for i in range(self._size):
            current = self.successor(current)
            yield current.value

    def __iter__(self):
        return self.iterate()
