def maximum_bitwise_or(n, s):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if s[i - 1] == '1':
            dp[i] = max(dp[i], dp[i - 1] | (1 << (i - 1)))
        else:
            dp[i] = dp[i - 1]
    return bin(max(dp))[2:]
