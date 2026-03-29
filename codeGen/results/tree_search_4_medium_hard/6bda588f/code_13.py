def solve():
    t = int(input())
    for _ in range(t):
        n, s = map(int, input().split())
        a = list(map(int, input().split()))
        dp = [[float('inf')] * (n - 1) for _ in range(n)]
        dp[0][0] = 0
        for i in range(1, n):
            for j in range(n - 1):
                if j < i:
                    dp[i][j] = min(dp[i][j], dp[i - 1][j - 1] + a[i] * (s - j))
                else:
                    dp[i][j] = min(dp[i][j], dp[i - 1][i - 1] + a[i] * (s - i))
        print(min(dp[-1]))

solve()
