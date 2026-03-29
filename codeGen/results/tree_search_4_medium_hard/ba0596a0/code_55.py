def can_cross(stones):
    dp = [False] * (max(stones) + 1)
    dp[0] = True

    for i in range(1, len(stones)):
        for j in range(max(0, stones[i] - k), min(len(stones), stones[i] + k + 1)):
            if dp[j]:
                dp[stones[i]] = True
                break

    return dp[-1]
