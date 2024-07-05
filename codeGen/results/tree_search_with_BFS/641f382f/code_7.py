import math
import sys

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

n = int(input().strip())
a = list(map(int, input().strip().split()))

INF = 1 << 30
dp = [[INF]*n for _ in range(n)]
next = [[0]*n for _ in range(n)]

for i in range(n):
    if a[i] == 1:
        print(1)
        sys.exit(0)

for i in range(n):
    dp[i][i] = 1
    next[i][i] = a[i]

for length in range(1, n):
    for i in range(n-length):
        j = i + length
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k+1][j])
        next[i][j] = gcd(next[i][j-1], a[j])
        if next[i][j] == 1:
            dp[i][j] = 1

ans = min(dp[i][n-i-2] for i in range(n-1))
if ans >= INF:
    print(-1)
else:
    print(ans + n - 1)

