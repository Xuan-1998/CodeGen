import sys

n = int(input())  # number of commands that can be modified
m = int(input())  # total number of commands
commands = input()  # list of turtle commands (T or F)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(min(i, n) + 1):
        if commands[i - 1] == 'F':
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] - 1)

print(dp[m][n])
