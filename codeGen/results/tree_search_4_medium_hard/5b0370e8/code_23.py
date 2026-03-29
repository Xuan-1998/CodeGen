def solve(k):
    MOD = int(1e9) + 7

    dp = [0] * (2**k)
    dp[0] = 1
    for i in range(1, 2**k):
        prev_bit = (i - 1).bit_length() - 1
        if not (i & (1 << prev_bit)):
            for j in range(i.bit_length()):
                next_bit = (i >> j) & ((1 << (j + 1)) - 1)
                dp[i] += dp[next_bit]
                dp[i] %= MOD

    return sum(dp)

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(k))
