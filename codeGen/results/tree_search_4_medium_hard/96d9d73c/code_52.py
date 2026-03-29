def can_partition(arr):
    N, K, M = len(arr), 0, 0
    dp = [[False] * (K + 1) for _ in range(N + 1)]

    for i in range(1, N + 1):
        for j in range(1, min(i // M + 1, K) + 1):
            if (i == 1 or arr[i - 1] - arr[i - 2] <= M) and dp[i - 1][min(j - 1, ceil((i - 1) / M) + 1)]:
                dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[N][K]
