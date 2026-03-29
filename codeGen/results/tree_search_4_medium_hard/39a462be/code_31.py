def maximal_similarity():
    A = input().strip()
    B = input().strip()

    n, m = len(A), len(B)

    dp = [[[0] * (m + 1) for _ in range(n + 1)] for _ in range(2)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if A[i - 1] == B[j - 1]:
                dp[0][i][j] = dp[1][i - 1][j - 1] + 1
            else:
                dp[0][i][j] = max(dp[1][i - 1][j], dp[1][i][j - 1])

    lcs_length = dp[0][n][m]
    return (4 * lcs_length) - (n + m)

print(maximal_similarity())
