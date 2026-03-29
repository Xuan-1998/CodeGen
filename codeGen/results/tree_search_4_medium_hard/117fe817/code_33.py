def count_digit_one(n):
    dp = [[0] * (n + 1) for _ in range(10)]

    for i in range(10):
        dp[i][i] = 1

    for k in range(1, 10):
        for i in range((10**k).bit_length() - 1, -1, -1):
            if (i & ((10**(k-1)) - 1)) == 0:
                break
            j = min(i + (10**k) - 1, n)
            dp[k][j] += k * (10**k) - (10**(k-1)) - i

    return sum(dp[9][:n+1])
