def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(1, n + 1):
        if s[i-1] == '0':
            dp[i] = dp[i-1]
        else:
            dp[i] = max(dp[i-1], dp[i-1] | (1 << s[i-1] - '0'))

    return bin(max((x for x in dp if x), default=0))[2:]
