def solve():
    t = int(input())
    MOD = 10**8 + 7

    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (n+1) for _ in range(m+1)]

        for k in range(1, m+1):
            for j in range(min(k, n), -1, -1):
                if 2*j > n:
                    dp[k][j] = sum(dp[i][j-1] for i in range(j)) % MOD
                else:
                    dp[k][j] = sum(dp[i][j-1] for i in range(min(k, j))) % MOD

        print(sum(dp[i][n] for i in range(m+1)) % MOD)

solve()
