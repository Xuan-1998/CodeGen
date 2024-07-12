python
   dp[i] = max(dp[i-1] - a[i], a[i] - dp[i-1])
   
