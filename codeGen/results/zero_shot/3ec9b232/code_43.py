import sys

n = int(input())
M = list(map(int, input().split()))
dp = [[0] * (max(M) + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(M[:i]), max(M[:i]) + 1):
        if M[:i].count(j) == 1:
            dp[i][j] = (dp[i-1][M[:i].index(j)] + dp[i-1][j]) % (10**9 + 7)
        else:
            dp[i][j] = dp[i-1][j]

print(dp[n][max(M)])
