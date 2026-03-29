def solve():
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        dp = [[0] * (1 << k) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for s in range(1 << k):
                if s & -s:
                    dp[i][s] = dp[i-1][s^1] + dp[i-1][s^(~s & -s)]
                else:
                    dp[i][s] = 2 * dp[i-1][s]
        print(sum(dp[n]) % (10**9+7))

solve()
