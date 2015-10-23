import sys

__author__ = 'vks'


class Queue:
    def pop(self):
        pass

    def push(self, item):
        pass

    def size(self):
        pass


class Stack(Queue):
    def __init__(self):
        self._arr = []

    def push(self, a):
        self._arr.append(a)

    def pop(self):
        return self._arr.pop()

    def size(self):
        return len(self._arr)


class MaxElementQueue(Queue):
    def __init__(self):
        self._negative_inf = - (2 ** 128)
        self._stack1 = Stack()
        self._stack2 = Stack()
        self._max_stack = []
        self._max1 = self._negative_inf
        self._max_stack.append(self._negative_inf)
        self._size = 0

    def push(self, item):
        self._stack1.push(item)
        if item > self._max1:
            self._max1 = item
        self._size += 1

    def pop(self):
        if self._stack2.size() == 0:
            length = self._stack1.size()
            local_max = self._negative_inf
            self._max1 = self._negative_inf
            for i in range(length):
                item = self._stack1.pop()
                self._stack2.push(item)
                if item > local_max:
                    local_max = item
                self._max_stack.append(local_max)
        self._size -= 1
        self._max_stack.pop()
        return self._stack2.pop()

    def size(self):
        return self._size

    def max(self):
        index = len(self._max_stack) - 1
        return max(self._max1, self._max_stack[index])


def parse_line(string, max_element_queue):
    string = string.split("\n")[0]
    if string == "max":
        if max_element_queue.size() > 0:
            return str(max_element_queue.max())
        return "empty"
    elif string == "pop":
        if max_element_queue.size() > 0:
            return str(max_element_queue.pop())
        return "empty"
    op, val = string.split()
    max_element_queue.push(int(val))
    return "ok"


if __name__ == "__main__":
    queue = MaxElementQueue()
    for line in sys.stdin:
        print(parse_line(line, queue))
