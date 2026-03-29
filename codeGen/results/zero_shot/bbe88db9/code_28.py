def solve(n):
    p = [int(x) for x in input().split()]
    dp = [[float('inf')] * (n + 2) for _ in range(2)]
    dp[0][1] = 1
    for i in range(1, n + 1):
        if i % 2 == 0:
            dp[0][i+1] = min(dp[0][i], dp[1][p[i-1]] + 1)
            dp[1][i+1] = float('inf')
        else:
            dp[0][i+1] = float('inf')
            dp[1][i+1] = min(dp[1][i], dp[0][p[i-1]] + 1)
    return (dp[1][n+1] % (10**9 + 7))
