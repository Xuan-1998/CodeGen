def is_possible_partitioning(n, k, m, A):
    dp = [[False for _ in range(k+1)] for _ in range(n+1)]

    for i in range(1, n+1):
        if i < k:
            continue
        max_val = max(A[i-k:i])
        min_val = min(A[i-k:i])
        if abs(max_val-min_val) <= m:
            dp[i][k-1] = True

        for j in range(k-2, -1, -1):
            if not (dp[i-1][j-1]):
                continue
            max_val = max(A[i-j:i])
            min_val = min(A[i-j:i])
            if abs(max_val-min_val) <= m:
                dp[i][j] = True

    return any(dp[n].values())
