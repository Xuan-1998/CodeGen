import sys

n, m = map(int, input().split())
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = i == 0 or i == n - 1
    if i < n:
        dp[i][1] = 1

for j in range(m + 1):
    dp[0][j] = j == 0 or j == m - 1
    if j < m:
        dp[1][j] = (n - 1) % (10**8+7)

for i in range(2, n + 1):
    for j in range(1, m + 1):
        if i < n:
            dp[i][j] = ((2 * i) > n or j == m - 1) and 1
        else:
            dp[i][j] = (dp[2 * i % n][j - 1]) * n

for _ in range(n - 1, -1, -1):
    for __ in range(m - 1, -1, -1):
        print((dp[_][_]) % (10**8+7))
