import sys

n, m = map(int, input().split())
dp = [[0] * m for _ in range(n+1)]
for i in range(1, n+1):
    s, x = map(int, input().split())
    dp[i][s-1] = 1
for i in range(2, n+1):
    for j in range(m):
        if j > 0:
            dp[i][j] += min(dp[i-1][k] + (1 if k != j else 0) for k in range(j))
        if j < m-1:
            dp[i][j] = min(dp[i-1][k] + (1 if k == j+1 else 0) for k in range(j, m))
print(min(dp[-1]))
