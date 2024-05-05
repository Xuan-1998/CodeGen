dp[i][j] = min(dp[k][j] + 1 for k in ancestors(i)) + |j - l_i|
