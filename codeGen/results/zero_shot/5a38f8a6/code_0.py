def min_perfect_squares(n):
    if n ** 0.5 == int(n ** 0.5):
        return 1

    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(i ** 0.5)
        for k in range(j, 0, -1):
            if i >= k ** 2:
                dp[i] = min(dp[i], dp[i-k**2] + 1)

    return dp[n]
