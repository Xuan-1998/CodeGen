def max_distance(commands, n):
    m = len(commands)
    dp = [[[0] * 2 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(1, m+1):
        for j in range(1, min(i, n)+1):
            if commands[i-1] == 'F':
                dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1])
                dp[i][j][1] = dp[i-1][j][1] + 1
            else:
                if j > i // 2:  # this is an overestimation, but it's correct
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1])
                    dp[i][j][1] = min(j, m) // 2 + (i % 2)
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j-1][1])
                    dp[i][j][1] = i // 2
    return dp[m][n][1]
