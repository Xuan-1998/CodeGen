import sys

n = int(input())
m = list(map(int, input().split()))

dp = [[0] * n for _ in range(n)]
dp[0][0] = 1

for i in range(1, n):
    for j in range(i+1):
        if m[j] < m[i]:
            dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % (10**9 + 7)
        else:
            dp[i][j] = dp[i-1][j]

print((dp[n-1][n-1] + dp[n-1][0]) % (10**9 + 7))
