def solve():
    a, b = map(int, input().split())
    dp = [[[0]*64 for _ in range(64)] for _ in range(315)]

    for i in range(315):
        for a_bit in range(64):
            if (a & 1):
                dp[i][a_bit][b] = ((dp[i-1][a_bit>>1][b>>1] ^ a) + dp[i-1][a_bit>>1][b>>1]) % (10**9+7)
            else:
                dp[i][a_bit][b] = dp[i-1][a_bit>>1][b>>1] if i > 0 else 0
        a >>= 1

    return sum(dp[314159][i][b] for i in range(64)) % (10**9+7)

print(solve())
