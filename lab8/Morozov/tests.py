import unittest
from queue import parse_line, MaxElementQueue

__author__ = 'vks'


class TestQueue(unittest.TestCase):
    def _grade(self, given_in, expected_out, queue):
        size = len(given_in)
        for i in range(size):
            self.assertEqual(parse_line(given_in[i], queue), expected_out[i])

    def test_empty(self):
        queue = MaxElementQueue()
        strings = ["pop", "max", "pop", "max"]
        ans = ["empty", "empty", "empty", "empty"]
        self._grade(strings, ans, queue)

    def test_without_pop(self):
        queue = MaxElementQueue()
        strings = []
        ans = []
        for i in range(1, 11):
            strings.append("push " + str(i))
            strings.append("max")
            ans.append("ok")
            ans.append(str(i))
        for i in range(10, 0, -1):
            strings.append("push " + str(i))
            strings.append("max")
            ans.append("ok")
            ans.append("10")
        self._grade(strings, ans, queue)

    def test_tricky_input(self):
        queue = MaxElementQueue()
        strings = []
        ans = []
        strings.append("max")
        ans.append("empty")
        for i in range(10, 0, -1):
            strings.append("push " + str(i))
            strings.append("max")
            ans.append("ok")
            ans.append("10")
        for i in range(10, 1, -1):
            strings.append("pop")
            strings.append("max")
            ans.append(str(i))
            ans.append(str(i - 1))
        strings.append("pop")
        strings.append("max")
        ans.append("1")
        ans.append("empty")
        self._grade(strings, ans, queue)

    def test_manual(self):
        queue = MaxElementQueue()
        strings = ["push 4", "push 8", "push 15", "push 16", "push 23", "push 42", "pop", "pop", "max", "pop", "push 1",
                   "push 1", "push 2", "push 3", "push 5", "push 8", "push 13", "pop", "max", "push 10000", "max",
                   "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop", "pop",
                   "max", "pop", "push 45", "max", "push 326", "pop", "max"]
        ans = ["ok", "ok", "ok", "ok", "ok", "ok", "4", "8", "42", "15", "ok", "ok", "ok", "ok", "ok", "ok", "ok", "16",
               "42", "ok", "10000", "23", "42", "1", "1", "2", "3", "5", "8", "13", "10000", "empty", "empty", "empty",
               "empty", "empty", "empty", "ok", "45", "ok", "45", "326"]
        self._grade(strings, ans, queue)
