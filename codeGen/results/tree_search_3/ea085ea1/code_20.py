def max_common_substrings(str1, str2):
    n = len(str1)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    # Initialize the base case: 0 common substrings when both strings are empty.
    for i in range(n + 1):
        dp[i][0] = dp[0][i] = 0
    
    for length in range(1, n + 1):
        for i in range(n - length + 1):
            j = i + length
            for k in range(i, j + 1):
                # Check if the substring str1[i:k+1] is present in str2.
                if str1[i:k+1] in str2:
                    dp[j][j] = max(dp[j][j], dp[k-1][k-1] + 1)
    
    return dp[n][n]

str1, str2 = input().split()
print(max_common_substrings(str1, str2))
