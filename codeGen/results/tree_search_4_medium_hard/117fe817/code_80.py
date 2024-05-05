def findDigitsOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        last_digit = i % 10
        if last_digit == 1:
            dp[i] = 1
        elif last_digit != 0:
            dp[i] = dp[i - 1]
        else:
            if i < 10:
                dp[i] = 1
            else:
                dp[i] = 9 * (dp[i // 10])
    return sum(dp)

n = int(input())
print(findDigitsOne(n))
