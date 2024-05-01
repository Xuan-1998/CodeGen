dp[i][j] = (dp[i-1][j-1] and ((s[i-2] == 'A' && s[j-2] == 'B') || (s[i-2] == 'B' && s[j-2] == 'A'))) or dp[i-1][j]
