def max_points(a):
    n = len(a)
    max_val = max(a)
    dp = [[0] * (max_val+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for k in range(max(a), 0, -1):
            if k+1 <= a[i]:
                dp[i][k] = max(dp[i-1][k+1] + (a[i]-k) if k+1 in a[:i] else 0,
                               dp[i-1][k-1] + (a[i]-k) if k-1 in a[:i] else 0)
            else:
                dp[i][k] = 0

    return max(dp[n])
