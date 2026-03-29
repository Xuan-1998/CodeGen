def solve():
    n = int(input())
    MOD = 998244353

    f = [[0] * (n+2) for _ in range(n+1)]
    f[0][0] = 1

    for i in range(1, n+1):
        for k in range(min(i+1, n+2)):
            for j in range(min(k, i)):
                f[i][k] = (f[i-1][j] * ((n+2)-(i-1)) choose (k-j)) % MOD

    return f[n][n+1]

print(solve())
