def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[float('inf')] * (s + 1) for _ in range(n + 1)]
        dp[0][0] = 0
        for i in range(1, n + 1):
            for j in range(s + 1):
                if a[i - 1] <= j:
                    dp[i][j] = min(dp[i - 1][j], dp[i - 1][max(0, j - a[i - 1])]) + max(0, j - a[i - 1])*a[i - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        print(dp[n][s])

solve()
