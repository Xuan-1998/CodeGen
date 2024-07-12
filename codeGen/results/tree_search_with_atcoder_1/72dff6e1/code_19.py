python
     dp[i][j] = sum(dp[i-1][k] for all k such that the sequence remains valid after adding j)
     
