def max_distance(commands, n):
    if n == 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(len(commands) + 1)]

    for i in range(1, len(commands) + 1):
        dp[i][0] = dp[i-1][0]
        for k in range(1, min(i, n) + 1):
            if commands[i-1] == 'F':
                dp[i][k] = max(dp[i-1][k], dp[i-1][max(0, k-1)] + 1)
            elif commands[i-1] == 'T':
                dp[i][k] = max(dp[i-1][k], dp[i-1][max(0, k-1)] - 1)
            else:
                # Handle edge case where command[i] is neither 'T' nor 'F'
                pass

    return dp[-1][-1]

# Example usage
commands = input()
n = int(input())
print(max_distance(commands, n))
