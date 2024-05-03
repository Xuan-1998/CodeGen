def max_distance(commands, n):
    dp = [[0] * (n + 1) for _ in range(len(commands) + 1)]

    for i in range(1, len(commands) + 1):
        for j in range(1, min(i, n) + 1):
            if commands[i - 1] == 'F':
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + 1)
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[-1][-1]

# Example usage
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
