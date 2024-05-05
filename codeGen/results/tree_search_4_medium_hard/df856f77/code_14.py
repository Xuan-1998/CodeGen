def min_operations(N, M, A):
    dp = [[0] * (M + 1) for _ in range(N + 1)]

    for i in range(N + 1):
        dp[i][0] = i

    for i in range(1, N + 1):
        for j in range(1, M + 1):
            if A[j - 1] > A[j]:
                dp[i][j] = min(dp[k][M] + 1 for k in range(i)) or 1
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[N][M]

N, M = map(int, input().split())
A = list(map(int, input().split()))
print(min_operations(N, M, A))
