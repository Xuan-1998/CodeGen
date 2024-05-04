n = int(input())
mod = 998244353

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(n, -1, -1):
    for l in range(1, n + 1):
        if l == 1:
            dp[i][l] = 10 ** (i + 1)
        else:
            for d in range(10):
                if int(str(d) * l) % (10 ** n) < (10 ** i):
                    break
            for j in range(l - 1, -1, -1):
                dp[i][l] += dp[i - j][j]
            dp[i][l] %= mod

for l in range(1, n + 1):
    print(dp[n][l], end=' ')
