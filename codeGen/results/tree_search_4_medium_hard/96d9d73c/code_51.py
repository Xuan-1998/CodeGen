def canPartitionIntoKParts(A, K, M):
    N = len(A)
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, min(K, ceil(i/M)) + 1):
            if A[i-1] - A[i-2] > M:
                dp[i][j] = False
            elif i >= K and (dp[i-1][min(j-1, ceil((i-1)/M)+1)] or dp[i-1][j]):
                dp[i][j] = True

    return dp[N][K]

N, K, M = map(int, input().split())
A = list(map(int, input().split()))
print(canPartitionIntoKParts(A, K, M))
