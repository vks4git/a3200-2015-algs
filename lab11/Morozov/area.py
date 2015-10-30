from sys import stdin, stdout

__author__ = 'vks'


def area(arg):
    if len(arg) < 3:
        return 0
    peak = arg[0]
    ans = 0
    current = 0
    for i in range(1, len(arg)):
        if arg[i] < peak:
            current += (peak - arg[i])
        else:
            if current > ans:
                ans = current
            current = 0
            peak = arg[i]
    return ans


def histogram(arg):
    a1 = area(arg)
    arg.reverse()
    a2 = area(arg)
    return max(a1, a2)


if __name__ == "__main__":
    array = [int(i) for i in stdin.readline().split()]
    stdout.write(str(histogram(array)) + "\n")
