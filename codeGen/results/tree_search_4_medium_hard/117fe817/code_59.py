def countDigitOne(n):
    dp = [0] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            dp[i] = (i // 10) * dp[i - 9] + (i % 10 == 1)

    return sum(dp)
