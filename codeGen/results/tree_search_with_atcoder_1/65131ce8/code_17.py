     dp[i][j] = sum(dp[k][m] * dp[i-1-k][j-1-m] for all valid k, m)
     
