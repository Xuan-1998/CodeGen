def solve():
    t = int(input())
    MOD = 10**9 + 7

    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp_xor = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for s in range(k + 1):
                dp[i][s] = sum(dp[i-1][t] for t in range(s+1)) + sum(dp_xor[i-1][j] for j in range(k))
            for j in range(k + 1):
                dp_xor[i][j] = sum(dp[i-1][s] for s in range(k-j))

        print(sum(dp[n][s] for s in range(k+1)) % MOD)

solve()
