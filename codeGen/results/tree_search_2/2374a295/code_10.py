def solve():
    n, k = map(int, input().split())
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    for i in range(2, n + 1):
        for j in range(min(i, k), -1, -1):
            if j == 0:
                dp[i][j] = 1
            else:
                for p in range(2, min(i, k-j) + 1):
                    if i % p == 0 and (p != i or dp[i//p][j-1]):
                        dp[i][j] += dp[i//p][j-1]
    print(dp[n][k] % 10000007)

solve()
