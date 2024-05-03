def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * 2 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(m + 1):
        for j in range(1, min(i + 1, n) + 1):
            if commands[i - 1] == 'F':
                dp[i][j]['T'] = dp[i - 1][j - 1]['T'] + 1
                dp[i][j]['F'] = dp[i - 1][j - 1]['F']
            else:
                dp[i][j]['T'] = max(dp[i - 1][j - 1]['T'], dp[i - 1][j]['T'])
                dp[i][j]['F'] = min(dp[i - 1][j - 1]['F'], dp[i - 1][j]['F'])

    return dp[m][n]['T']

# Example usage:
commands = 'TTFF'
n = 2
print(max_distance(commands, n))  # Output: 3
