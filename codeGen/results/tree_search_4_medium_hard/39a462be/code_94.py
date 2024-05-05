def max_similarity_score():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)
    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(max(n, m) + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            k = min(i, j)
            if A[i - 1] == B[j - 1]:
                dp[k][i][j] = max(dp[k - 1][i - 1][j - 1]) + 4
            else:
                dp[k][i][j] = max([dp[k - 1][i - 1][j], dp[k][i - 1][j], dp[k][i][j - 1]])

    return dp[n][m][0]

print(max_similarity_score())
