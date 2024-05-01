import sys

n, m = map(int, input().split())

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        if i < j:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = min((dp[k][j] + dp[i][l]) for k in range(i) for l in range(j))

print(dp[n][m])
