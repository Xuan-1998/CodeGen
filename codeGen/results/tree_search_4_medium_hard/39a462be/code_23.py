def max_similarity_score(A, B):
    n = len(A)
    m = len(B)
    
    # Initialize the 2D DP table
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    # Handle edge cases
    if n == 0:
        return m
    if m == 0:
        return n
    
    # Fill the DP table using memoization and recursion
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 4
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    # Return the maximum similarity score
    return dp[n][m]

# Read input from stdin
A = input()
B = input()

# Calculate and print the result
result = max_similarity_score(A, B)
print(result)

