def max_similarity_score(A, B):
    n = len(A)
    m = len(B)

    # Initialize dp array with 0s
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    # Base case: If either string is empty, the maximum similarity score is 0.
    for i in range(n + 1):
        dp[i][0] = -i
    for j in range(m + 1):
        dp[0][j] = -j

    # Fill up dp array using dynamic programming
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 4
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) - (i + j)

    # Return the maximum similarity score found so far.
    return dp[n][m]

A = input().strip()
B = input().strip()
print(max_similarity_score(A, B))
