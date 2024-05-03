===BEGIN CODE===
def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        if commands[i - 1] == 'F':
            dp[i][j] = dp[i - 1][j] + 1
        else:
            for k in range(min(i, j) + 1):
                dp[i][j] = max(dp[i][j], 2 * dp[i - 1][k])

    return dp[m][n]

commands = input().split()
n = int(input())
print(max_distance(commands, n))
