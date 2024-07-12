python
     dp[i][j] = max(dp[i+1][j] - a[i], dp[i][j-1] - a[j])
     
