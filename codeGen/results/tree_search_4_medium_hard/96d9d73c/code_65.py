def canPartition(K, M):
    N = int(input())
    A = list(map(int, input().split()))
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(min(i, K), 0, -1):
            if all(abs(A[k] - A[0]) <= M for k in range(j)):
                dp[i][j] = True
                break

    return 'YES' if any(dp[N][k] for k in range(1, K + 1)) else 'NO'
