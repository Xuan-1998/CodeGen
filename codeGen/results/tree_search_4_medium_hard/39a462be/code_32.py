def max_similarity_score(A, B):
    n, m = len(A), len(B)
    dp = [[[0] * (max(n, m) + 1) for _ in range(m + 1)] for _ in range(n + 1)]

    # Base case: edge cases
    dp[0][0][0] = 0

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[i][j][0] = max(dp[i - 1][j - 1][0], dp[i - 1][j - 1][1]) + 1
            else:
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i][j - 1][0])

    # Update state with LCS and similarity score from previous state
    for k in range(1, min(n, m) + 1):
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                dp[i][j][k] = max(dp[i - 1][j - 1][k], dp[i][j][k - 1]) + (4 * k - n - m)

    return dp[n][m][-1]
