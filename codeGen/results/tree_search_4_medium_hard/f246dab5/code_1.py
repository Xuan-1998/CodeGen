dp = [[0 for _ in range(141)] for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = float('inf')
    
    for j in range(1, min(i + 1, 140) + 1):
        if j <= i:
            dp[i][j] = min(dp[i][j], (i - j + 1) * 20)
        
        elif j >= 90:
            dp[i][j] = min(dp[i][j], dp[i - 1][min(139, j)] + 120)
        
        else:
            dp[i][j] = min(dp[i][j], dp[i - 1][min(89, j)] + 50)

print(dp[n][0])
