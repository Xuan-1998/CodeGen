def min_perfect_squares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = i - 1
        while j >= 0 and math.sqrt(j) % 1 != 0:
            j -= int(math.sqrt(j)) ** 2
        dp[i] = min(dp[i], dp[j] + 1)

    return dp[n]
