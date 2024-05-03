import sys

def max_distance(commands, n):
    m, n = len(commands), n
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, min(i, n) + 1):
            if commands[i - 1] == 'F':
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])

    return dp[m][n]

# Example usage:
commands = "FFF"  # or any other string of commands
n = 2  # or any other value for n

print(max_distance(commands, n))
