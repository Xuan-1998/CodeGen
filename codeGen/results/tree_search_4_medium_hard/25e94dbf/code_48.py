def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    dp[0][0] = 0

    for i in range(1, m + 1):
        for j in range(n + 1):
            if commands[i - 1] == 'T':
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = dp[i - 1][j] - 1

    return dp[m][n]

# Example usage
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
