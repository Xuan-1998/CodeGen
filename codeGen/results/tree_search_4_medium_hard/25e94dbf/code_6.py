===BEGIN SOLUTION===
from collections import defaultdict

def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(2)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0:
                dp[0][j] = [0] * (m + 1)
            elif j == 0:
                dp[1][j] = [0] * (m + 1)

    for i in range(1, m + 1):
        for j in range(1, min(i, n) + 1):
            if commands[i - 1] == 'T':
                dp[1][j] = max(dp[0][j - 1], dp[1][j - 1])
            else:
                dp[1][j] = max(dp[1][j - 1], dp[0][j - 1] + 1)

    return dp[1][n]

commands = input().strip()
n = int(input())
print(max_distance(list(commands), n))
