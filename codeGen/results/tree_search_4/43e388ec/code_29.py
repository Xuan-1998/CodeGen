def solve(a, b):
    MOD = 1000000007

    dp = [[0] * 2 for _ in range(17)]

    # Initialize the base case
    dp[0][0] = (a - 1) % MOD
    dp[0][1] = (b - 1) % MOD

    for i in range(1, 17):
        if a & (1 << i):
            dp[i][0] = (dp[i-1][0] + (a - 2**i + 1)) % MOD
        else:
            dp[i][0] = dp[i-1][0]

        if b & (1 << i):
            dp[i][1] = (dp[i-1][1] + (b - 2**(i-1))) % MOD
        else:
            dp[i][1] = dp[i-1][1]

    return (dp[16][0] + dp[16][1]) % MOD

a, b = map(int, input().split())
print(solve(a, b))
