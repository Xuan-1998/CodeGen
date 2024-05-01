def max_common_substrings(str1, str2):
    N = len(str1)
    
    # Create a 2D table to store the maximum number of common non-overlapping substrings
    dp = [[0] * (N+1) for _ in range(N+1)]
    
    # Fill the dp table in top-down manner
    for i in range(1, N+1):
        for j in range(1, N+1):
            if str1[i-1] == str2[j-1]:
                # If characters at current positions match, extend the common substring
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                # If characters don't match, find maximum number of common substrings from left or right
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    
    return dp[N][N]
