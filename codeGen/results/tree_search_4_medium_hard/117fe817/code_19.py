def countOnes(n):
    dp = [0] * (n + 1)
    for i in range(1, 10):
        dp[i] += 1

    for d in range(2, n.bit_length() + 1):
        for i in range((1 << d) - 1, (1 << (d - 1)) - 1, -1):
            dp[i] += dp[i - (1 << d)] + (i // (1 << (d - 1))) >= (10 ** (d - 1)) and 9 or 0

    return sum(dp)

n = int(input())
print(countOnes(n))
