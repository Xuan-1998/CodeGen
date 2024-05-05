def can_cross_river(stones):
    n = len(stones)
    dp = [[False] * (n + 1) for _ in range(n)]

    # Initialize base case: frog starts on the first stone
    dp[0][0] = True

    for i in range(1, n):
        for k in range(i - min(3, i), -1, -1):
            if k < 2:
                continue
            dp[i][k] = (dp[i-1].index(True) >= max(k-1, k, k+1)) or dp[i][k]

    return dp[-1][-1]
