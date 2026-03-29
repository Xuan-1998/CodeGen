def solve(n, k):
    MOD = 10**9 + 7

    dp = {0: 1}
    for i in range(k-1, -1, -1):
        and_count = 0
        xor_count = 0
        for j in range(i+1):
            if (j & (1 << i)) == 0:
                and_count += dp.get(j, 0)
                xor_count += dp.get((j ^ ((1 << i) - 1)), 0)
            else:
                and_count += dp.get(j ^ (1 << i), 0)
        for j in range(2**i):
            if all(((j >> bit) & 1) == 0 for bit in range(i)):
                dp[j] = (and_count + xor_count) % MOD
    return dp[0]

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    print(solve(n, k))
