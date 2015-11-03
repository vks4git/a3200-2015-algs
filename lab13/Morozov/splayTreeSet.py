__author__ = 'vks'


class Set:
    def add(self, item):
        pass

    def remove(self, item):
        pass

    def contains(self, item):
        pass

    def __iter__(self):
        pass


class Node:
    def __init__(self, key, parent):
        self.key = key
        self.parent = parent
        self.left = None
        self.right = None


class SplayTree(Set):
    """
    An implementation of Set interface.
     Uses Splay tree to perform add(), remove() and contains() operations in amortized logarithmic time.
     Short description of the algorithm:
        Splay tree is a self-balancing BST, which uses some heuristics to achieve high performance.
        Each contains(x) call makes x the root using several left and|or right rotations. Thus, next contains(x) call
        will perform very fast. As a result, the most often accessed keys will be stored closer to the root.

        Adding an element works like in a simple BST, but with call to splay() on added element.

        To remove an element algorithm makes it the root, then splits the tree in two: one contains elements that are
        less than x, the other contains those that are greater. Then these trees are merged. Merge operation finds the
        maximum in the left tree and makes the right tree its right child.

        The iterator performs an ascending order traversal and adds elements into a queue, then iterates through it.
    """

    def __init__(self):
        """Create an empty tree."""
        self.__root = None

    def __rotate(self, node):
        """Rotate the edge between node and its parent."""
        parent = node.parent
        node.parent = parent.parent
        if parent.parent is not None:
            if parent.key < parent.parent.key:
                parent.parent.left = node
            else:
                parent.parent.right = node
        parent.parent = node
        if node.key < parent.key:
            parent.left = node.right
            if parent.left is not None:
                parent.left.parent = parent
            node.right = parent
        else:
            parent.right = node.left
            if parent.right is not None:
                parent.right.parent = parent
            node.left = parent
        return node

    def __splay(self, node):
        """Splay the node."""
        if node.parent is None:
            return node
        if node.parent.parent is None:
            return self.__rotate(node)
        node = self.__rotate(node)
        return self.__splay(self.__rotate(node))

    def __find(self, key):
        """Find a key in the tree and splay it. If there is no such key, return the closest one."""
        current = self.__root
        while current is not None:
            if current.key == key:
                self.__root = self.__splay(current)
                return True, self.__root
            if current.key > key:
                if current.left is None:
                    return False, current
                current = current.left
            else:
                if current.right is None:
                    return False, current
                current = current.right
        return False, current

    def __split(self, key):
        """Split the tree into two, left should contain elements less than key, right should contain the others."""
        result, node = self.__find(key)
        node = self.__splay(node)
        self.__root = node
        if not result:
            if node.key > key:
                left = node.left
                if left is not None:
                    left.parent = None
                node.left = None
                return left, node
            else:
                right = node.right
                if right is not None:
                    right.parent = None
                node.right = None
                return node, right
        else:
            left = node.left
            right = node.right
            if left is not None:
                left.parent = None
            if right is not None:
                right.parent = None
            return left, right

    def __merge(self, left, right):
        """Merge two trees, making the root of the right tree right child of the left tree's max element."""
        if left is None:
            return right
        if right is None:
            return left
        while left.right is not None:
            left = left.right
        left = self.__splay(left)
        left.right = right
        if right is not None:
            right.parent = left
        return left

    def __order_traversal(self, node, queue):
        """Make an ascending order traversal through the tree, adding elements into queue."""
        if node.left is not None:
            self.__order_traversal(node.left, queue)
        queue.append(node.key)
        if node.right is not None:
            self.__order_traversal(node.right, queue)

    def add(self, item):
        """Add element to the set."""
        if self.__root is None:
            self.__root = Node(item, None)
            return
        left, right = self.__split(item)
        self.__root = Node(item, None)
        self.__root.left = left
        self.__root.right = right
        if left is not None:
            left.parent = self.__root
        if right is not None:
            right.parent = self.__root

    def remove(self, item):
        """Remove item from set. If there is no such item, leave set unmodified."""
        result, node = self.__find(item)
        if not result:
            return None
        left = self.__root.left
        right = self.__root.right
        if left is not None:
            left.parent = None
        if right is not None:
            right.parent = None
        self.__root = self.__merge(left, right)
        return item

    def contains(self, item):
        """Check if set contains item."""
        result, node = self.__find(item)
        return result

    def __iter__(self):
        """Iterate through set elements."""
        if self.__root is None:
            return
        queue = []
        self.__order_traversal(self.__root, queue)
        for i in queue:
            yield i
