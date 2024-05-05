import sys

mod = 998244353

n = int(sys.stdin.readline())

dp = [[0] * (n + 2) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i-1] = 1

for j in range(1, n + 1):
    for i in range(j - 1, -1, -1):
        if i % 2 == 0:
            dp[i][j-1] += dp[i+1][j-1]
        else:
            dp[i][j-1] += dp[i+1][j]

print(dp[0][n].mod(mod))
