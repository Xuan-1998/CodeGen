def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i == 1:
            dp[i] = 1
        else:
            last_digit = (i // 10 ** int(math.log10(i)) % 10)
            if last_digit == 1:
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = dp[i - 1]
    return sum(dp)

import math

if __name__ == "__main__":
    n = int(input())
    print(findDigitOne(n))
