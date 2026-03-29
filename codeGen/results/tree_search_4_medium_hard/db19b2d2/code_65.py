import sys

n, m, h = map(int, input().split())
s = list(map(int, input().split()))

dp = [[0.0 for _ in range(m)] for _ in range(n)]

for i in range(m):
    if i == h:
        dp[0][i] = 1
    else:
        dp[0][i] = 0

s_total = sum(s)
for i in range(1, n):
    for j in range(m):
        if j == h:
            dp[i][j] = 1 - (sum(s[:j] + s[j+1:]) / s_total)**(n-i)
        else:
            dp[i][j] = 0
print(dp[-1][h])
