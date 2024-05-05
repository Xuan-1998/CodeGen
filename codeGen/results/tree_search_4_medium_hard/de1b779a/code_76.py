import sys

n, m, c0, d0 = map(int, input().split())
d = [0] + list(map(int, input().split()))
p = [0] + list(map(int, input().split()))

dp = [[-1 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = max(dp[i-c0][0], 0)

for j in range(1, m+1):
    dp[0][j] = -1

for i in range(1, n+1):
    for j in range(1, m+1):
        if d[j] >= c0 and p[j] + d[i-c0] > 0:
            dp[i][j] = max(dp[i-c0][j-1] + p[j], dp[i][j-1])
        else:
            dp[i][j] = dp[i][j-1]

print(max(0, dp[-1][-1]))
