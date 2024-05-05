def findCountOfDigitOne(n):
    dp = [0] * (n+1)
    for i in range(1, n+1):
        if i < 10:
            dp[i] = 1
        elif i < 20:
            dp[i] = 2
        else:
            count = 1
            temp = i
            while temp > 0:
                if temp % 10 == 1:
                    count += 1
                temp //= 10
            dp[i] = count
    return sum(dp)
