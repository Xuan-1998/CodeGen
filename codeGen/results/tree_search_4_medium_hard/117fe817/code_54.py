def findCountOfDigitOne(n):
    dp = {0: 0}

    for i in range(1, n + 1):
        if i % 10 == 1:
            dp[i] = dp.get(i // 10, 0) + 1
        else:
            dp[i] = dp.get(i - 1, 0)

    return sum(dp.values())

n = int(input())
print(findCountOfDigitOne(n))
