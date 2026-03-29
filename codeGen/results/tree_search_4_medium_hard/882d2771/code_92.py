def beautycontest(t, l, r):
    MOD = 1_000_007
    dp = [[0] * (r + 1) for _ in range(l + 1)]

    for i in range(2, l + 1):
        for j in range(i, r + 1):
            if i == 2:
                dp[i][j] = min(dp[i-1][k-1] + 1 for k in range(j+1))
            else:
                dp[i][j] = min(dp[i-1][k-1] + 1 for k in range(1, j+1))

    total = 0
    for i in range(t):
        total += (l - 1) * (dp[l-1][r-1]) % MOD
    return total % MOD

t, l, r = map(int, input().split())
print(beautycontest(t, l, r))
