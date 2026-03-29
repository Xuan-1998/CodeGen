def canPartition(A):
    N, K, M = len(A), sum(1 for x in A if x >= K) + 1, max(A)
    dp = [[[False] * (M + 1) for _ in range(K)] for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(min(i, K)):
            if j == 0:
                dp[i][j][A[0]] = True
            else:
                for k in range(M + 1):
                    dp[i][j][k] |= (dp[i - 1][min(j - 1, K - 1)][max(0, k - M)] and A[i - 1] <= k)
    return dp[N][K][M]
