===BEGIN SOLUTION===
from collections import defaultdict
mod = 10**9 + 7

n = int(input())
m = list(map(int, input().split()))
dp = [[0] * (max(m) + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(i + 1):
        if m[i - 1] < i and j > 0:
            dp[i][j] += dp[m[i - 1]][j - 1]
        dp[i][j] %= mod
        if m[i - 1] >= i:
            dp[i][j] += dp[m[i - 1]][j]
            dp[i][j] %= mod

print(dp[n][max(m)])
