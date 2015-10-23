import sys

__author__ = 'vks'


class QsortMax:
    def __init__(self, array, k):
        self._arr = array
        self._k = k
        self._ans = []

    def _median(self, left, right):
        arg = [self._arr[i] for i in range(left, right)]
        while len(arg) >= 6:
            buf = []
            ans = []
            for i in range(len(arg)):
                if (i + 1) % 6 != 0:
                    buf.append(arg[i])
                else:
                    buf = sorted(buf)
                    ans.append(buf[2])
                    buf = []
            if len(buf) != 0:
                buf = sorted(buf)
                ans.append(buf[len(buf) // 2])
            arg = ans
        buf = sorted(arg)
        return buf[len(buf) // 2]

    def split(self, left, right):
        x = self._median(left, right + 1)
        less = left
        greater = right
        j = left
        while j <= greater:
            if self._arr[j] < x:
                self._arr[less], self._arr[j] = self._arr[j], self._arr[less]
                less += 1
                j += 1
            elif self._arr[j] > x:
                self._arr[greater], self._arr[j] = self._arr[j], self._arr[greater]
                greater -= 1
            else:
                j += 1
        return greater, less

    def _build_max(self, left, right):
        if self._k == 0:
            return
        if right < left:
            return
        hi, lo = self.split(left, right - 1)
        elems = right - self._k
        if lo <= elems <= hi:
            for i in range(elems, right):
                self._ans.append(self._arr[i])
            return
        elif elems > hi:
            self._build_max(hi + 1, right)
        else:
            for i in range(lo, right):
                self._ans.append(self._arr[i])
            self._k -= (right - lo)
            self._build_max(left, lo)

    def get_max(self):
        self._build_max(0, len(self._arr))
        return self._ans


if __name__ == "__main__":
    k = int(sys.stdin.readline())
    array = [int(i) for i in sys.stdin.readline().split()]
    qsort_max = QsortMax(array, k)
    for i in qsort_max.get_max():
        sys.stdout.write(str(i) + ' ')
