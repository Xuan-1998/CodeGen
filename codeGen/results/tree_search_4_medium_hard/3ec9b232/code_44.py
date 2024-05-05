import sys

n = int(input())
M = list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][0] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if M[j - 1] <= i:
            dp[i][j] = (dp[i][j - 1] + dp[i - 1][j - 1]) % (10**9 + 7)
        else:
            break

print(dp[n][n])
