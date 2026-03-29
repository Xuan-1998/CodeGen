def solve():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())
        dp = [[0] * (m + 1) for _ in range(n)]
        for i in range(n):
            if i == 0:
                dp[i][0] = 1
            else:
                for j in range(m + 1):
                    if 2 * i > n:
                        dp[i][j] = (dp[i - 1][j] + dp[i - 1][j - 1]) % (10**8 + 7)
                    elif 2 * i <= n:
                        dp[i][j] = (dp[i - 1][j] - dp[i - 1][j - 1]) % (10**8 + 7) if j > 0 else 1
        print((sum(dp[-1])) % (10**8 + 7))

solve()
