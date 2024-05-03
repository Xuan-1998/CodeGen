def max_distance(commands, n):
    m, k = len(commands), n + 1
    dp = [[0] * (k + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(min(i, k) + 1):
            if commands[i - 1] == 'F':
                dp[i][j] = dp[i - 1][j - 1] + 1
            elif commands[i - 1] == 'T' and j > 0:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1])
            else:
                dp[i][j] = 0

    return dp[m][k]

# Example usage
commands = input()
n = int(input())
print(max_distance(commands, n))
