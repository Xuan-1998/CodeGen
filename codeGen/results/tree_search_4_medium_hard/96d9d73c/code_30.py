def partition_possible(n, k, m, arr):
    dp = [[False] * (k + 1) for _ in range(n + 1)]

    dp[0][0] = True

    for i in range(1, n + 1):
        for j in range(1, min(i + 1, k) + 1):
            if dp[i - 1][j]:
                max_val = max(arr[:i])
                min_val = min(arr[i:])
                if abs(max_val - min_val) <= m:
                    dp[i][j] = True
            else:
                dp[i][j] = False

    return dp[n][k]
