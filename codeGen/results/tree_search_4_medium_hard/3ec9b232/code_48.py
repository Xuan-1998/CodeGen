import sys

MOD = 10**9 + 7

n = int(input())
m = list(map(int, input().split()))

dp = [[0] * (n+1) for _ in range(n+1)]

for i in range(n+1):
    dp[i][0] = 1

for i in range(1, n+1):
    for j in range(1, min(i, n)+1):
        if m[i-1] == i:
            dp[i][j] += dp[i-1][j-1]
        else:
            dp[i][j] += sum(dp[i-1][k] for k in range(j+1))
        dp[i][j] %= MOD

print(dp[n][0])
