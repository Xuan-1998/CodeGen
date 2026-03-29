import sys
input = lambda: [int(x) for x in input().split()]
n, *ps = input()
dp = [[0] * (n + 1) for _ in range(n + 1)]
dp[0][1] = 1

for i in range(2, n + 1):
    for j in range(i + 1):
        if dp[i - 1][j]:
            dp[i][j] += dp[i - 1][j]
        if j != i and dp[i - 1][ps[0]]:
            dp[i][j] = (dp[i][j] + dp[i - 1][ps[0]]) % (10**9 + 7)
    ps.pop(0)

print((dp[n][n + 1]) % (10**9 + 7))
