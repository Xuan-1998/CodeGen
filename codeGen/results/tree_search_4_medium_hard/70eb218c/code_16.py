def min_operations(n, x):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        while x:
            last_digit = x % 10
            dp[i] = min(dp[i], dp[i - 1] + (last_digit != x % 10))
            x //= 10

    return dp[n] if dp[n] < float('inf') else -1
