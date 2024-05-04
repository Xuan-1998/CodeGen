def count_blocks(n):
    MOD = 998244353
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i):
            k = i - j
            same_digit = (10 ** (k - 1)) % MOD
            if k > 0:
                same_digit = ((same_digit * 10) + same_digit) % MOD
            dp[i] += dp[j]
            dp[i] %= MOD
    return ' '.join(map(str, [dp[i] for i in range(1, n + 1)]))
