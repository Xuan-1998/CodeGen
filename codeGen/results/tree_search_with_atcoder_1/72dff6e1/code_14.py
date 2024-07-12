python
       dp[i][j] = dp[i][j-1] + (dp[i-1][j-1] * min(A[j-1], i)) % 998244353
       
