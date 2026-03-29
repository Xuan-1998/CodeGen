def find_lcs_length(A, B):
    m = len(A)
    n = len(B)
    
    # Create a 2D array to store the lengths of LCS
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill up the dp table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # The length of the LCS is stored in the bottom-right corner
    return dp[m][n]
