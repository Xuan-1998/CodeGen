import sys

# Read input from stdin
n, commands = map(int, input().split())
commands = list(commands)

# Initialize DP array
dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1 if commands[i - 1] == 'F' else 2

for length in range(3, n + 1):
    for i in range(n - length + 1):
        j = i + length
        if commands[i] == commands[j]:
            dp[i][j] = dp[i + 1][j - 1] + (1 if commands[i] == 'F' else 2)
        elif commands[i] == 'T':
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

# Print the maximum distance from the starting point to the ending point
print(max(map(max, dp)))
