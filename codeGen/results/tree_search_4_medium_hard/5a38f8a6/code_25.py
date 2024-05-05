def numSquares(n):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        j = int(i ** 0.5)
        while j * j <= i:
            dp[i] = min(dp[i], dp[i - j * j] + 1)
            j -= 1
    return dp[n]
