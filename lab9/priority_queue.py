import sys

__author__ = 'vks'


class MinPQ:
    def __init__(self, count):
        self._arr = [0]
        self._size = 0
        self._k = count
        self._positive_inf = 2 ** 256

    def add(self, elem):
        self._arr.append(elem)
        self._size += 1
        ptr = self._size
        while ptr > 1:
            if self._arr[ptr] < self._arr[ptr // 2]:
                self._arr[ptr], self._arr[ptr // 2] = self._arr[ptr // 2], self._arr[ptr]
                ptr //= 2
            else:
                break
        if self._size > self._k:
            self._delete_head()

    def _delete_head(self):
        self._arr[1], self._arr[self._size] = self._arr[self._size], self._arr[1]
        self._arr.pop()
        self._size -= 1
        ptr = 1
        while ptr < self._size:
            left = self._positive_inf
            right = self._positive_inf
            if 2 * ptr <= self._size:
                left = self._arr[2 * ptr]
            if 2 * ptr + 1 <= self._size:
                right = self._arr[2 * ptr + 1]
            if self._arr[ptr] > min(left, right):
                if left < right:
                    self._arr[ptr], self._arr[2 * ptr] = self._arr[2 * ptr], self._arr[ptr]
                    ptr *= 2
                else:
                    self._arr[ptr], self._arr[2 * ptr + 1] = self._arr[2 * ptr + 1], self._arr[ptr]
                    ptr = 2 * ptr + 1
            else:
                break

    def get_max(self):
        return self._arr[1:]


if __name__ == "__main__":
    k = int(sys.stdin.readline())
    pq = MinPQ(k)
    for i in sys.stdin.readline().split():
        pq.add(int(i))
    for i in pq.get_max():
        sys.stdout.write(str(i) + ' ')
