def max_common_substrings(str1, str2):
    n = len(str1)
    m = len(str2)
    
    # Create a 2D array to store the lengths of common suffixes for each substring
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    max_length = 0
    
    # Iterate over both strings using a sliding window approach
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])
    
    return max_length

