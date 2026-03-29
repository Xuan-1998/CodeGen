def solve():
    t = int(input())
    MOD = 10**9 + 7
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(1 << k)]
        dp[0][0] = 1
        for i in range(n):
            x = int(input())
            and_mask = (x & ((1 << k) - 1))
            for j in range((1 << k) - 1, -1, -1):
                if (and_mask & j) == j:
                    dp[j][j ^ and_mask] += dp[and_mask][j]
        print(sum(dp[i][i] for i in range(1 << k)) % MOD)

solve()
