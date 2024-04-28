def max_common_substrings(str1, str2):
    N = len(str1)
    
    # Initialize a 2D DP array with zeros
    dp = [[0] * (N + 1) for _ in range(N + 1)]
    
    # Fill the DP table using dynamic programming
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The maximum number of common non-overlapping substrings is stored in the bottom-right corner of the DP table
    return dp[-1][-1]

str1 = input().strip()
str2 = input().strip()

print(max_common_substrings(str1, str2))
