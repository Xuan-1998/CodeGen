def can_partition(A):
    N, K, M = len(A), min(len(A) // 10, 1000), max(1, min(M, 1000000))
    dp = [[False] * (K+1) for _ in range(N+1)]

    dp[0][0] = True

    for i in range(1, N+1):
        for j in range(min(j+1, i//K), -1, -1):
            if all(A[p-1]-A[0] <= M for p in range(i)):
                dp[i][j] = or_(any(dp[p][k] and k < j for p in range(i)) or dp[i-1][0], True)
            else:
                dp[i][j] = False

    return dp[N][K]
