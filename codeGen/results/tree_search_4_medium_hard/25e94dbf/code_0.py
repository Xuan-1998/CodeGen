def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * (n + 1) for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        for j in range(min(i, n), -1, -1):
            if commands[i-1] == 'F':
                dp[j][i][k] = max(dp[j][i-1][k], dp[j-1][i-1][k+1] + 1)
            else:
                dp[j][i][k] = max(dp[j][i-1][k], dp[j][i-1][k-1])
    
    return dp[-1][-1][-1]

# Example usage
n = int(input())
commands = input()
print(max_distance(commands, n))
