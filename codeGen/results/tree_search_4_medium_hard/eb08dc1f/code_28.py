def countBlocks(n):
    MOD = 998244353

    dp = [[0] * (n+1) for _ in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, min(i+1, n)+1):
            if j == 1:
                dp[i][j] = 1
            else:
                dp[i][j] = sum(dp[i-1][k] for k in range(j, min(j+1, n))) % MOD

    return ' '.join(map(str, [sum(10**i * (dp[i][i]) % MOD for i in range(n)) % MOD for _ in range(n)]))

n = int(input())
print(countBlocks(n))
