from functools import lru_cache
import sys

n = int(input())
m = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][0] = 1

for i in range(1, n + 1):
    for j in range(i + 1):
        if m[j - 1] == i:
            dp[i][j] = (sum(dp[x][i - 1] for x in range(j)) % (10 ** 9 + 7))
        else:
            dp[i][j] = sum(dp[x][i - 1] * ((x < j) or (m[j - 1] == i)) for x in range(j)) % (10 ** 9 + 7)

print(dp[n][n])
