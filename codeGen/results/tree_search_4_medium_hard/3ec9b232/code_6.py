import sys
from collections import defaultdict

n = int(input())
M = list(map(int, input().split()))
mod = 10**9 + 7

dp = [[0] * (len(M) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1
    for j in range(len(M)):
        if M[j - 1] > M[len(M) - i]:
            break
        dp[i][j] = (dp[i][j] + sum(dp[i - 1][x] for x in range(j))) % mod

print(sum(dp[n]) % mod)
