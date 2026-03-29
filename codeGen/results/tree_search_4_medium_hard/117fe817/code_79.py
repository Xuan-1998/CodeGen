def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        elif i == 10:
            dp[i] = 2
        else:
            k = len(str(i))
            if str(i)[0] == '1':
                dp[i] = 1 + dp[i - 10**(k-1)]
            else:
                dp[i] = dp[i - 1]
    return sum(dp)
