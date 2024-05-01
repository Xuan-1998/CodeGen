def solve():
    dp = {0: 0}
    a, b = map(int, input().split())
    MOD = 10**9 + 7

    for i in range(1, 315160):
        dp[i] = (dp.get(i-1, 0) if i > 0 else 0) ^ ((b >> (i-1)) & 1)

    total_sum = 0
    for i in range(314159+1):
        total_sum ^= dp.get(i, 0)

    print(total_sum % MOD)

solve()
