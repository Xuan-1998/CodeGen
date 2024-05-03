def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * (n + 1) for _ in range(2)] for _ in range(m + 1)]
    
    dp[0][0][0] = 0
    
    for i in range(m + 1):
        for j in range(min(i, n) + 1):
            if i == 0:
                continue
            
            if commands[i - 1] == 'F':
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][0] + 1)
                
                if j > 0 and i > 0:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][1])
            elif commands[i - 1] == 'T' and j > 0:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j - 1][0])
                dp[i][j][1] = 0
            
    return max(max(dp[m][k][0] for k in range(n + 1)) for _ in range(2))
