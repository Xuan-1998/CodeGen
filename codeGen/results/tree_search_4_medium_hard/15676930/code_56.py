def dp_hares(n):
    if n == 1:
        return max(b[0], c[0])
    else:
        dp = [0] * (n + 1)
        for i in range(2, n+1):
            dp[i] = max(dp[i-1], b[i-1] if dp[i-2] == dp[i-3] else c[i-1]) + a[i-1]
        return dp[n]
