def findDigitOne(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i - 1]
        last_bit = (i - 1) // 10 ** ((i).bit_length() - 1)
        if i - last_bit == last_bit:
            dp[i] += 1
        else:
            dp[i] += dp[last_bit] + 1
    return sum(1 for x in dp[1:])
