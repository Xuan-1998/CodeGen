def max_similarity(A, B):
    m, n = len(A), len(B)
    dp = [[[0] * 1005 for _ in range(1005)] for _ in range(2)]

    for k in range(2):
        for i in range(n + 1):
            for j in range(m + 1):
                if i == 0 and j == 0:
                    dp[k][i][j] = n + m - 4 * min(n, m)
                elif i == 0:
                    dp[k][i][j] = dp[k][i][j-1] - 4
                elif j == 0:
                    dp[k][i][j] = dp[k][i-1][j] - 4
                else:
                    if A[i-1] == B[j-1]:
                        dp[k][i][j] = dp[k][i-1][j-1] + 4
                    else:
                        dp[k][i][j] = max(dp[k][i-1][j], dp[k][i][j-1])

    return max(max(row) for row in dp[1])
