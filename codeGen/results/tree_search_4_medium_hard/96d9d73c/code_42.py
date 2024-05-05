def partition_possible(A):
    N, K, M = A[0], A[1], A[2]
    A = A[3:]

    dp = [[[False] * (M + 1) for _ in range(K + 1)] for _ in range(N + 1)]

    for i in range(N + 1):
        for j in range(min(i, K) + 1):
            dp[i][j][0] = True

    for i in range(1, N + 1):
        for j in range(1, min(i, K) + 1):
            if A[i - 1] - A[0] > M or i < K:
                dp[i][j][M] = False
            else:
                for k in range(j - 1, 0, -1):
                    if dp[i - k][k - 1][M] and A[i - 1] - A[i - k - 1] <= M:
                        dp[i][j][M] = True
                        break

    return dp[N][K-1][M]
