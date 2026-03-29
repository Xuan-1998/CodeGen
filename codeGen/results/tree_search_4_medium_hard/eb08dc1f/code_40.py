def count_blocks(n):
    MOD = 998244353

    dp = [[0] * (n + 1) for _ in range(10 ** n + 1)]

    for i in range(10 ** n):
        num = int(str(i).zfill(n))
        for j in range(n, -1, -1):
            digit = (num // 10 ** (n - j)) % 10
            if j == n:
                dp[i][0] += 1
            else:
                dp[i][j] = (dp[i][j] + dp[(i * 10 + digit) % (10 ** n)][j - 1]) % MOD

    return ' '.join(str(x) for x in [dp[x][y] % MOD for y in range(n + 1)])
