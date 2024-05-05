def can_cross_stones(stone_positions):
    n = len(stone_positions)
    dp = [False] * (n + 1)
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if abs(i - j) in {k - 1, k, k + 1} and dp[j]:
                dp[i] = True
                break
        else:
            dp[i] = False

    return dp[-1]
