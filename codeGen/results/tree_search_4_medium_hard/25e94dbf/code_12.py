def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for k in range(n + 1):
            if commands[i - 1] == 'F':
                dp[i][k] = max(dp[i - 1][k - 1] + 1, dp[i - 1][k])
            elif commands[i - 1] == 'T':
                dp[i][k] = max(dp[i - 1][k - 1] + 1, dp[i - 1][k])

    return dp[m][n]

# Example usage:
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
