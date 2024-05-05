def can_partition(A):
    N = len(A)
    K = int(input())  # number of partitions
    M = int(input())  # maximum absolute difference

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(min(K, i), 0, -1):  # start from the maximum possible number of partitions
            if j == 1:
                dp[i][j] = True
            elif dp[i - 1][j - 1]:
                if all(abs(A[i - 1] - x) <= M for x in A[:i]):
                    dp[i][j] = True

    return dp[N][K]
