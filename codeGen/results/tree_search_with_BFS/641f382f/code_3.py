import sys
from math import gcd

def solve():
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    INF = float('inf')

    dp = [[INF]*n for _ in range(n)]
    g = [[0]*n for _ in range(n)]

    for i in range(n):
        g[i][i] = a[i]
        if a[i] == 1:
            dp[i][i] = 0

    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i + length - 1
            g[i][j] = gcd(g[i][j-1], a[j])
            if g[i][j] == 1:
                dp[i][j] = 0
            else:
                for k in range(i, j):
                    dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j] + 1)

    if dp[0][n-1] == INF:
        print(-1)
    else:
        print(dp[0][n-1])

solve()

