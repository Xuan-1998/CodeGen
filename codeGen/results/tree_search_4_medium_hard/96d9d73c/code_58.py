def canPartition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, min(i, K) + 1):
            if j == 1:
                dp[i][j] = True
            elif A[i-1] - M <= dp[i-1][j]:
                dp[i][j] = True

    return dp[N][K]
