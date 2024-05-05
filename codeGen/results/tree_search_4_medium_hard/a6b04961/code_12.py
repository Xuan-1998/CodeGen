import sys

def read():
    return [int(x) for x in input().split()]

n, m = read()
dp = [[0] * 100001 for _ in range(n + 1)]
for i in range(m):
    u, v = read()
    for j in range(min(u,v), -1, -1):
        if dp[j][i]:
            dp[j+1][i+1] = max(dp[j+1][i+1], dp[j][i])
    dp[u][i+1] = max(dp[u][i+1], dp[u-1][i] + (u-v))
for i in range(1, n+1):
    for j in range(m+1):
        if j:
            dp[i][j] += dp[i-1][j]
print(max(dp[-1]))
