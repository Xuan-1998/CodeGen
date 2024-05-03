import sys

n = int(input())
commands = input().strip()
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(min(i, n) + 1):
        if commands[i - 1] == 'T':
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][max(0, j - 1)] + 1)
        elif commands[i - 1] == 'F':
            dp[i][j] = dp[i - 1][j] + 1

print(max(max(row) for row in dp))
