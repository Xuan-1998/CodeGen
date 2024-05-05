def can_cross_stones(stones):
    n = len(stones)
    dp = [False] * (n + 1)

    # base case: frog starts at the first stone
    dp[0] = True

    for i in range(1, n):
        if dp[i-2]:  # no stones between (i-2) and i-th stones
            dp[i] = True
        else:
            for j in range(max(0, i-3), i):  # possible jumps from (j-1)-th stone
                if abs(stones[j] - stones[i]) in [k-1, k, k+1]:
                    dp[i] = True
                    break

    return dp[n-1]
