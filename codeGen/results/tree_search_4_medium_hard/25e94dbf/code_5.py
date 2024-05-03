def max_distance(commands, n):
    dp = [[0 for _ in range(n+1)] for _ in range(len(commands)+1)]
    
    for j in range(n+1):
        dp[0][j] = 0
    
    for i in range(1, len(commands)+1):
        cmd = commands[i-1]
        if cmd == 'F':
            dp[i][n] = max(dp[i-1][n], dp[i-1][n-1] + 1)
        elif cmd == 'T':
            dp[i][n] = -dp[i-1][n]
    
    return dp[-1][-1]

# Example usage:
commands = input().strip()
n = int(input())
print(max_distance(commands, n))
