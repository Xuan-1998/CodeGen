def count_ones(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        if i < 2:
            dp[i] = i
        else:
            leading_zeros = int(math.log10(i))
            remaining = i - 10 ** leading_zeros
            dp[i] = dp[remaining] + (10 ** (leading_zeros + 1) - 10 ** leading_zeros)
    return sum(dp)

n = int(input())
print(count_ones(n))
