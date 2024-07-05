import sys
from math import gcd

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    inf = float('inf')
    dp = [[inf]*n for _ in range(n)]
    one_cnt = a.count(1)
    if one_cnt > 0:
        return n - one_cnt

    g = [[0]*n for _ in range(n)]
    for i in range(n):
        g[i][i] = a[i]
        for j in range(i+1, n):
            g[i][j] = gcd(g[i][j-1], a[j])

    for i in range(n):
        if g[i][i] == 1:
            dp[i][i] = 1
        for j in range(i+1, n):
            if g[i][j] == 1:
                dp[i][j] = 1
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])

    if dp[0][n-1] == inf:
        return -1
    else:
        return dp[0][n-1] + n - 1

print(solve())

