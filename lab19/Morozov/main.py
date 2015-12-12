from sys import stdin, stdout

__author__ = 'vks'


def palindrome(s):
    length = len(s)
    if length == 0:
        return ""
    dp = [[0 for i in range(length)] for i in range(length)]
    for i in range(length):
        dp[i][i] = 1
    for i in range(length - 2, -1, -1):
        for j in range(i + 1, length):
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) if s[i] != s[j] else dp[i + 1][j - 1] + 2
    ans = ""
    i = 0
    j = length - 1
    middle = ""
    while i <= j:
        if s[i] == s[j]:
            if i == j:
                middle += s[i]
            else:
                ans += s[i]
            i += 1
            j -= 1
        else:
            if dp[i + 1][j] > dp[i][j - 1]:
                i += 1
            else:
                j -= 1
    ans += middle + ans[::-1]
    return ans


if __name__ == "__main__":
    s = stdin.readline()
    stdout.write(palindrome(s) + "\n")
