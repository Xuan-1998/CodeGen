def count_bitwise_and_or_xor(input):
    MOD = 10**9 + 7

    n, k = map(int, input().split())
    dp = [[0] * (1 << k) for _ in range(n + 1)]
    dp[0][0] = 1

    for i in range(1, n + 1):
        for s in range(1 << k):
            if s & 1:
                dp[i][s ^ (1 << (k - 1))] += dp[i - 1][s]
            else:
                dp[i][s] = dp[i - 1][s]

    return sum(dp[-1]) % MOD

t = int(input())
for _ in range(t):
    print(count_bitwise_and_or_xor(input()))
