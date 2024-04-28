def solve(a, b):
    MOD = 10**9 + 7

    dp = [[0] * (b.bit_length() + 1) for _ in range(315)]
    dp[0][0] = a ^ b

    for i in range(1, 316):
        for j in range(b.bit_length()):
            if (i & (1 << j)):
                dp[i][j] = dp[i - 1][j + 1] ^ ((a >> j) | (~b & ((1 << j) - 1)))
            else:
                dp[i][j] = dp[i - 1][j]

    ans = 0
    for i in range(315, -1, -1):
        if (i & (1 << b.bit_length())):
            ans ^= dp[i][b.bit_length()]
        else:
            ans += dp[i][b.bit_length()]

    return int(ans % MOD)
