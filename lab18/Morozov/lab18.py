from sys import stdin, stdout

__author__ = 'vks'


def symbol_compare(s1, s2, i, j):
    if s1[j - 1] != s2[i - 1]:
        return 1
    return 0


def check_transposition(s1, s2, i, j):
    if i <= 1:
        return False
    if j <= 1:
        return False
    if s2[i - 2] != s1[j - 1]:
        return False
    if s2[i - 1] != s1[j - 2]:
        return False
    return True


def damerau_levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    length1 = len(s1)
    length2 = len(s2)
    if min(length1, length2) == 0:
        return max(length1, length2)
    length1 += 1
    length2 += 1
    inf = 2 ** 256
    fst = [inf for i in range(length1)]
    snd = [i for i in range(length1)]
    current = [0 for i in range(length1)]
    for i in range(1, length2):
        current[0] = i
        for j in range(1, length1):
            deletion = snd[j] + 1
            insertion = current[j - 1] + 1
            mismatch = snd[j - 1] + symbol_compare(s1, s2, i, j)
            swap = (fst[j - 2] + 1) if check_transposition(s1, s2, i, j) else inf
            current[j] = min(deletion, insertion, mismatch, swap)
        fst = [k for k in snd]
        snd = [k for k in current]
    return current[length1 - 1]


if __name__ == "__main__":
    s1 = stdin.readline().split("\n")[0]
    s2 = stdin.readline().split("\n")[0]
    stdout.write(str(damerau_levenshtein_distance(s1, s2)) + "\n")
