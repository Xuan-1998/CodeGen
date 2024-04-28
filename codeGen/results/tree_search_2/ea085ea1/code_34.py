def common_substrings(str1, str2):
    N = len(str1)
    M = len(str2)
    
    # Initialize a 3D DP table to store the count of common non-overlapping substrings ending at each position.
    dp = [[[0] * (M+1) for _ in range(N+1)] for _ in range(2)]
    
    # Fill up the DP table using dynamic programming and memoization.
    for i in range(1, N+1):
        for j in range(i):
            for k in range(1, M+1):
                for l in range(k):
                    if str1[j:i] == str2[l:k]:
                        dp[0][i][k] = max(dp[0][i][k], dp[0][j][l]+1)
    
    # Return the maximum count of common non-overlapping substrings.
    return max(max(row) for row in dp[0])

# Receive inputs from standard input and print your answer to standard output.
str1, str2 = [input() for _ in range(2)]
print(common_substrings(str1, str2))
