def solve():
    n, k = map(int, input().split())
    MOD = 1000000007

    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(min(i, k), -1, -1):
            for p in range(2, min(i, k - j) + 1):
                if i % p == 0:
                    dp[i][j] = (dp[i][j] + dp[i - p][k - j - 1]) % MOD

    print(dp[n][k])

if __name__ == "__main__":
    solve()
