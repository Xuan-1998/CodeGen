def can_cross_stones(stones, k):
    n = len(stones)
    dp = [False] * (n + 1)

    dp[0] = True

    for i in range(1, n):
        for j in range(max(0, i - k), min(i, k) + 1):
            if dp[j] and abs(i - j) in [k-1, k, k+1]:
                dp[i] = True
                break

    return dp[-1]
