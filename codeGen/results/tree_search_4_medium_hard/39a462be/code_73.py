def get_max_similarity_score(A, B):
    m = len(A)
    n = len(B)

    # Initialize a 2D array to store the maximum similarity score
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill up the base case values
    for i in range(m + 1):
        dp[i][0] = -i
    for j in range(n + 1):
        dp[0][j] = -j

    # Calculate the maximum similarity score using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = max(dp[i - 1][j - 1] + 4, dp[i - 1][j], dp[i][j - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the maximum value in the dp array
    return dp[m][n]

A = input().strip()
B = input().strip()

print(get_max_similarity_score(A, B))
