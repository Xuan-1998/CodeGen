def canPartition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    dp = [[False] * (M + 1) for _ in range(N + K + 1)]
    dp[0][0] = True

    max_val = max(A)
    min_val = min(A)

    for i in range(1, N + 1):
        for j in range(min(max_val - min_val, M), -1, -1):
            if A[i-1] <= min_val + j:
                dp[i][j] = (dp[i-1][j-1] or dp[i-1][j])
            else:
                break

    return dp[N][M]
