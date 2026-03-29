def max_profit(n, m, c0, d0):
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][0] = min(i * c0, d0)

    for j in range(1, m + 1):
        ai, bi, ci, di = [int(x) for x in input().split()]
        for i in range(n, -1, -1):
            if i >= bi:
                dp[i][j] = max(dp[max(0, i - ci)][j-1], d0 + (i - bi)//ci * di)
            else:
                dp[i][j] = max(dp[i][j-1], d0)

    return dp[n][m]

n, m, c0, d0 = [int(x) for x in input().split()]
print(max_profit(n, m, c0, d0))
