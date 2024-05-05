import sys

def solve():
    t = input()
    n = int(input())
    strings = [input() for _ in range(n)]

    dp = [[(None, 0, False)] * (n + 1) for _ in range(len(t))]

    for i in range(1, len(t)):
        for j in range(1, min(i + 1, n + 1)):
            if any(s in t[i - k:i] for s in strings[:j]):
                dp[i][j] = (strings[j - 1], i - len(strings[j - 1]) + 1, True)
            else:
                dp[i][j] = min((dp[k][j - 1][0], k) for k in range(j))

    m = sum(1 for x, y, _ in dp if y != 0)

    print(m)
    for i in range(len(t)):
        if dp[i][n].index(y) != n:
            print(dp[i][n])

solve()
