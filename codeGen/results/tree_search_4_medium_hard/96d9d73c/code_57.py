def can_partition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    min_val = min(A)
    max_val = max(A)

    for i in range(K + 1):
        dp[0][i] = True

    for i in range(1, N + 1):
        if A[i - 1] >= min_val and A[i - 1] <= max_val:
            if A[i - 1] - M < min_val:
                dp[i][K] = False
            else:
                dp[i][K] = True

    return dp[N][K]
