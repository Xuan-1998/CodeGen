def max_distance(commands, n):
    m = len(commands)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        if commands[i - 1] == "F":
            dp[i][0] = dp[i - 1][0]
            for j in range(n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1] + 1)
        else:
            dp[i][0] = dp[i - 1][n]
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]


# Example usage
commands = input()
n = int(input())
print(max_distance(commands, n))
