def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            leading_ones = 0
            trailing_zeros = 9 * (i // 10)
            while trailing_zeros > 0 and i <= n:
                leading_ones += min(trailing_zeros, (n - i) % 10 + 1)
                trailing_zeros -= min(trailing_zeros, (n - i) % 10 + 1)
                i += 1
            dp[i] = dp[i-1] + leading_ones
    return sum(dp)

# Test your function with given input
n = int(input())
print(findDigitOne(n))
