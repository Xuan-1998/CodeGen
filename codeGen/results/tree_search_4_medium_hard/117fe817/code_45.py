def countDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < 10:
            dp[i] = 0
        else:
            dp[i] = dp[i - 1] + (int(str(i)[0]) == 1)
    return sum(dp)

n = int(input())
print(countDigitOne(n))
