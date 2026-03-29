def canCross(stones):
    dp = [False] * (max(stones) + 1)
    dp[0] = True

    for stone in stones:
        if dp[stone]:
            for i in range(max(0, stone - 2), stone + 3):
                if i >= 0 and not dp[i]:
                    dp[i] = True
    return dp[-1]
