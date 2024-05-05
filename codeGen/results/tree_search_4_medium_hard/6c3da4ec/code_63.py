def max_bitwise_or(s):
    n = len(s)
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        for j in range(i - 1):
            left = int(s[:j], 2)
            right = int(s[j:i], 2)
            dp[i] = max(dp[i], left | right)

    return bin(max(dp))[2:]
