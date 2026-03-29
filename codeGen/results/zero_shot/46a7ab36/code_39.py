def alien_language(n, m):
    MOD = 10**8 + 7

    dp = [[1] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(i):
            if 2 * j <= n:
                dp[i][j] *= n
            else:
                dp[i][j] *= (n + 1)
        if i > 0 and 2 * i <= n:
            dp[i][i] *= n
        elif i > 0 and 2 * i > n:
            dp[i][i] *= (n + 1)

    return sum(dp[m]) % MOD

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    print(alien_language(n, m))
