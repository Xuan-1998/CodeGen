def max_distance(commands, n):
    # Initialize a table to store the maximum distances for each subproblem
    dp = [[0] * (len(commands) + 1) for _ in range(n + 1)]

    # Fill up the table using dynamic programming
    for i in range(1, len(commands) + 1):
        for j in range(min(i, n) + 1):
            if commands[i - 1] == "T":
                dp[j][i] = max(dp[j - 1][i - 1], dp[j][i - 1])
            elif commands[i - 1] == "F":
                dp[j][i] = dp[j][i - 1] + 1

    # Return the maximum distance for the original problem
    return dp[n][len(commands)]

# Example usage:
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
