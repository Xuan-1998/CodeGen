def maximal_similarity(A, B):
    n = len(A)
    m = len(B)

    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[0][i][j] = max(i, j) - (4 * min(i, j))
            else:
                if A[i - 1] == B[j - 1]:
                    dp[1][i][j] = dp[1][i - 1][j - 1] + 1
                else:
                    dp[1][i][j] = max(dp[0][i - 1][j], dp[0][i][j - 1])

    return dp[1][n][m]
