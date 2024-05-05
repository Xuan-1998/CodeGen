def solve():
    n, q = map(int, input().split())
    signs = list(map(lambda x: 1 if x == "+" else -1, input()))
    dp = [[float("inf")] * ((n + 1) // 2) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for j in range(max(-((n - 1) // 2), -i), min(((n - 1) // 2) + 1, (n - i) // 2) + 1):
            if j > 0:
                dp[i][j] = min(dp[i-1][k-1], dp[i-1][k+1]) + signs[i]
            elif j < 0:
                dp[i][j] = min(dp[i-1][k-1], dp[i-1][k+1])
    ans = float("inf")
    for j in range(max(-((n - 1) // 2), -q), min(((n - 1) // 2) + 1, (n - q) // 2) + 1):
        ans = min(ans, dp[q][j])
    print(ans)

solve()
