def solution():
    a = int(input(), 2)
    b = int(input(), 2)

    MOD = 10**9 + 7

    dp = {0: (a ^ b) % MOD}

    for i in range(1, 315160):
        dp[i] = (dp[i-1] + a ^ (b << i)) % MOD

    print(sum(dp.values()) % MOD)

solution()
