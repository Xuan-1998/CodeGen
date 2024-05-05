def canCross(stones):
    dp = [False] * (max(stones) + 1)
    dp[0] = True

    for stone in stones:
        if dp[stone]:
            for k in range(1, abs(stone - (stone + 2)) + 1):
                if stone + k <= max(stones):
                    dp[stone + k] = True
                if stone - k >= 0 and stone - 2*k >= 0:
                    dp[stone - k] = True
                if stone - k - 1 >= 0:
                    dp[stone - k - 1] = True

    return dp[-1]
