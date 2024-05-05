def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        iLastDigit = i % 10
        if iLastDigit == 0:
            dp[i] = dp[i - 1]
        elif iLastDigit == 1:
            dp[i] = dp[i - 1] + 1
        else:
            dp[i] = dp[i - 1] + (i >= 10)
    return dp[n]

n = int(input())
print(findDigitOne(n))
