def max_bitwise_or(n, s):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = 0
        for k in range(1, i + 1):
            dp[i] = max(dp[i], bin(int(s[k-1:i], 2) | int(s[:k-1], 2))[2:])
    return dp[n][:-1]
