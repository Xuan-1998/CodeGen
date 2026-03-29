def can_partition(A):
    N = len(A)
    K = int(input())
    M = int(input())

    dp = [[False] * (K + 1) for _ in range(N + 1)]

    # Base case: It's always possible to partition the empty array into one partition
    dp[0][1] = True

    for i in range(1, N + 1):
        for j in range(1, min(i, K) + 1):
            if (i - K >= 0 and dp[i - K][j - 1]):
                max_val = max(A[i - K:i])
                min_val = min(A[i - K:i])
                if max_val - min_val <= M:
                    dp[i][j] = True
            elif j == 1:
                dp[i][j] = True

    return dp[N][K]
