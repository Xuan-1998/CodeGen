def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < 10:
            dp[i] = 1
        else:
            last_digit = int(str(i)[-1])
            if last_digit == 1:
                dp[i] = dp[i - 1] + 1
            elif last_digit > 1:
                dp[i] = dp[i - 1]
            else:  # last_digit == 0
                dp[i] = dp[i // 10] * 9 + 1
    return sum(dp)

n = int(input())  # read input from stdin
print(findDigitOne(n))  # print the result to stdout
