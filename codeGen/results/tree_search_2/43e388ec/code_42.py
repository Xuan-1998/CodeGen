import sys

MOD = 10**9 + 7

a, b = [int(x) for x in input().split()]
n = 314159

dp = [[0] * 32 for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = b % MOD
    for j in range(31, -1, -1):
        if i > 0:
            dp[i][j] = (a & (1 << j)) ^ ((b >> j) % MOD)
        else:
            dp[i][j] = (dp[i][j+1] | (1 << j)) if j < 31 and a & (1 << j) else 0

ans = sum(dp[i][0] for i in range(n+1))
print(ans % MOD)
