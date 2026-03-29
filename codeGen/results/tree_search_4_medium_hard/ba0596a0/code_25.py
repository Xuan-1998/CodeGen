def can_cross_stones(stones):
    n = len(stones)
    dp = [[False] * (n // 2 + 1) for _ in range(n)]

    # Base case: the frog starts at the first stone
    dp[0][0] = True

    for i in range(1, n):
        for j in range(min(i, n // 2), -1, -1):
            if dp[i-1][j]:
                for k in [j-1, j, j+1]:
                    if abs(stones[i] - stones[j]) in [k-1, k, k+1]:
                        dp[i][j] = True
                        break

    return dp[-1][-1]
