import sys
from collections import defaultdict

n = int(input())
p = list(map(int, input().split()))
dp = [[float('inf')] * (n + 1) for _ in range(n + 1)]
dp[0][1] = 0

for i in range(2, n + 1):
    dp[i][i] = p[i - 1]
    if p[i - 1] > i:
        dp[i][p[i - 1]] = 0
    for j in range(i):
        if p[j] < i and (dp[j][p[j]] == float('inf') or dp[j][i] + 1 < dp[p[j]][i]):
            dp[i][j] = dp[j][p[j]] + 1

print((dp[0][n + 1]) % int(10**9 + 7))
