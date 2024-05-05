def maxBitwiseOrValue(n, s):
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if i % 2 == 1:
            left = dp[i - 1]
            right = int(s[i // 2:i], 2)
        else:
            left = int(s[:i // 2], 2)
            right = 0
        dp[i] = max(left | right, dp[i - 1])

    return bin(dp[n])[2:]
