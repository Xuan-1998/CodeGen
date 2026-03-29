def findDigitOne(n):
    dp = [0] * 10
    for i in range(1, 10):
        if i == 1:
            dp[i] = 1
        else:
            dp[i] = dp[i-1]
    for i in range(2, 9):
        dp[i] += dp[i-1]
    return dp[9] + n.bit_length()
