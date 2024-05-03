def max_distance(commands, n):
    dp = [[[0] * 2 for _ in range(n+1)] for _ in range(len(commands)+1)]

    for i in range(1, len(commands)+1):
        command_i = commands[i-1]
        if command_i == 'T':
            # Update direction
            dp[i][n]['F'] = max(dp[i-1][n-1]['T'], dp[i-1][n]['F'])
            dp[i][n]['T'] = max(dp[i-1][n-1]['F'], dp[i-1][n]['T'])
        elif command_i == 'F':
            # Increase distance traveled
            dp[i][n]['F'] += 1
            dp[i][n]['T'] = dp[i-1][n]['F']

    return max(dp[-1][n]['F'], dp[-1][n]['T'])

# Example usage:
commands = ['F', 'T', 'F', 'F', 'T']
n = 2

result = max_distance(commands, n)
print(result)  # Output: maximum distance reachable
