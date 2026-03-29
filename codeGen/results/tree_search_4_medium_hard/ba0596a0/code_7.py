def can_cross(stones):
    n = len(stones)
    dp = [[False] * (stones[-1] + 1) for _ in range(n)]

    dp[0][0] = True

    for i in range(1, n):
        for d in range(max(0, stones[i - 1] - 2), stones[i]):
            dp[i][d] = any(dp[j][d - 1] for j in range(i) if abs(stones[j] - stones[i]) in (k - 1, k, k + 1))
        for d in range(1, min(d for d in dp[i])):
            dp[i][d] = dp[i][d]

    return dp[-1][-1]
